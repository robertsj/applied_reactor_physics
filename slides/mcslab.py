"""
Computes group-wise fluxes and microscopic cross sections in a two
region pin cell assuming only U-238 and H-1, isotropic scattering, and 
no fission.  All neutrons are born at a fixed starting energy E0. 
"""

#%% imports
import numpy as np
rnd = np.random.rand
#np.random.seed(1234)
import matplotlib.pyplot as plt

#%% Material Definitions

# Load U-238 data processed via reconstruction of SLBW resonances
energy, sigma_fa, sigma_fs = np.loadtxt('u238_xs.txt', unpack=True)

# Use fake, constant hydrogen cross sections
sigma_ma =  0.0 + np.zeros_like(energy)
sigma_ms = 20.0 + np.zeros_like(energy)

# Define U-238 and H-1 number densities close to what true fuel has.
Nf = 10/238*6.022e23
Nm = 2/18 * 6.022e23 

# Define the macroscopic cross sections as functions of E
Sigma_fa = lambda x: np.interp(x, energy, Nf*sigma_fa*1e-24)
Sigma_fs = lambda x: np.interp(x, energy, Nf*sigma_fs*1e-24)
Sigma_ma = lambda x: np.interp(x, energy, Nm*sigma_ma*1e-24)
Sigma_ms = lambda x: np.interp(x, energy, Nm*sigma_ms*1e-24)
Sigma_ft = lambda x: Sigma_fa(x) + Sigma_fs(x)
Sigma_mt = lambda x: Sigma_ma(x) + Sigma_ms(x)
Sigma_t = [Sigma_ft, Sigma_mt]
Sigma_a = [Sigma_fa, Sigma_ma]
Sigma_s = [Sigma_fs, Sigma_ms]

# Masses and alpha for each region.
mass = [238, 1]  
alpha = [(238-1)**2/(238+1)**2, 0]


#%% Geometry
radius = 0.5 # fuel radius (cm)
hpitch = 1.3/2 # half pin pitch (cm)
V = [np.pi*radius**2,  (2*hpitch)**2 - np.pi*radius**2]
FUEL = 0
MOD = 1

#%% Control parameters

# Number of source particles to simulate
num_hist = 5000 

# Initial energy (eV) of source particles
E_0 = 1e4

# Boundary condition at outer pin-cell surface
boundary = 'reflect' 

# Use true physics (i.e., conserve energy).  If False, then isotropic
# scattering is assumed in the laboratory system but energy losses follow
# center-of-mass kinematics.  In other words, setting to False should 
# demonstrate how bad the isotropic assumption made for NR and WR is relative
# to reality.
real_physics = True

# Surface tolerances
tolerance = 1e-15

#%% Tallies

# The goal is to compute the spectrum and the spectrum- and volume-
# averaged fuel absorption cross section in each energy group.  Note, 
# no capability for uncertainty quantification is built in.  If you want
# uncertainties, run the simulation multiple times and perform statistics
# on the multiple outputs.

# Group boundaries (from WIMS 69-group format.)
group_boundaries = [27.7, 15.968, 9.877, 4.0] 


# Collision estimator for flux:
#   phi = 1/(N*V) * sum(1/Sigma_t(E))  [1/cm^2 per source particle]
# where N is the number of histories and V is the volume.  The sum is over
# all events that meet the criteria, e.g., the neutron is in the right
# region and has the right energy.  Similarly, the collision estimator
# for the cross section comes from the reaction rate:
#    R =  1/(N*V) * sum(1)   [1/cm^3 per source particle]
# i.e., we simply increment the counter if the reaction of interest occurs.
# Finally, 
#    SigmaT = R/phi [1/cm]

reactions = np.zeros((2, 3)) 
fluxes = np.zeros((2, 3))
total_leaks = 0
total_absorptions = 0
total_low_energy = 0


#%% Simulation

def surface_intersection(x, y, mu, eta, xi):
    """Returns the surface and distance to it given position and angle.
    """
    # cosine and sin of phi in the place
    c, s = mu / sin_theta, eta / sin_theta
    
    # distance to outer box (must be smaller than box diagonal!)
    d_x = hpitch-x if c > 0 else x+hpitch
    d_y = hpitch-y if s > 0 else y+hpitch
    d_x, d_y = abs(d_x/c), abs(d_y/s)
    d_box = d_x if 0 < d_x < d_y else d_y
    assert d_box <= np.sqrt(2*(2*hpitch)**2)
           
    # distance to pin
    d_pin = np.nan
    A, B, C = 1, 2*(x*c+y*s), x**2+y**2-radius**2
    if B**2 >= 4*A*C:
        root1 = (-B - np.sqrt(B**2 - 4*A*C))/(2*A)
        root2 = (-B + np.sqrt(B**2 - 4*A*C))/(2*A)
        d_pin = root1 if root1 > 0 else root2
        
    # assign surface and distance
    if d_pin > tolerance and d_pin < d_box:
        d_surf = d_pin
        surf = 0
    else :
        d_surf = d_box
        surf = 1
    assert d_surf > tolerance, 'rare event! try again.'
    
    return surf, d_surf
    

# We loop over all simulated source particles.  The only physics included
# are elastic scattering and radiative capture.  A source particle's history
# is terminated if (1) it is absorbed, (2) its energy falls below the 
# minimum energy tallied, or (3) it escapes the system (i.e., vacuum boundary).
flag = False
#%%
for h in range(num_hist) :
    if flag:
        break
    # initial energy (eV)
    E = E_0

    # Sample the initial location
    r = np.sqrt(rnd()*radius**2)
    phi = 2*np.pi*rnd()
    x, y = r*np.cos(phi), r*np.sin(phi)

    # I'm born in fuel
    region = FUEL 
    
    # Sample the initial direction.  Here. mu, eta, and xi are the 
    # directional cosines with respect to the x, y, and z axes.  The pin
    # is oriented along the z axis.
    xi = rnd() 
    phi = 2*np.pi*rnd() 
    sin_theta = np.sqrt(1 - xi**2) 
    mu = np.cos(phi)*sin_theta
    eta = np.sin(phi)*sin_theta
    
    if h % 10 == 0:
        tmpl = "h={}, absorptions={}, low_energy_kills={}, leaks={}"
        print(tmpl.format(h, total_absorptions, total_low_energy, total_leaks))
    
    counter = 0
 
    while True:
       
        assert abs(mu**2 + eta**2 + xi**2 - 1) < 1e-14
        assert abs(xi**2 + sin_theta**2 - 1)  < 1e-14
        
        # distance to collision (cm) *in the plane*
        SigT = Sigma_t[region](E)
        d_coll = -np.log(rnd()) / SigT * sin_theta
        
        # distance to surface (cm) *in the plane*
        surf, d_surf = surface_intersection(x, y, mu, eta, xi)
        
        if d_coll < d_surf:
            
            # We have a collision.  First, move to the collision site.
            x, y = x+d_coll*mu/sin_theta, y+d_coll*eta/sin_theta
            
            for g in range(3):
                if group_boundaries[g] > E >= group_boundaries[g+1]:
                    fluxes[region][g] += 1.0 / Sigma_t[region](E)
            
            if rnd() < Sigma_s[region](E)/Sigma_t[region](E): 
                # We scattered!  Assume isotropic scattering the the 
                # center-of-mass system.  The corresponding outgoing 
                # energy is given directly (see, e.g., )
                mu_c = 2*rnd()-1 # COM scattering cosine
                A = mass[region] # mass number in this region
                E = E * (A**2 + 2*mu_c*A + 1)/(A+1)**2 # new energy
                
                if E < group_boundaries[-1] :
                    # No upscatter, so we're done with this history.
                    total_low_energy += 1
                    break 
                    
                if real_physics:
                    #  Scattering cosine and azimuth in the laboratory frame
                    mu_lab = (1+A*mu_c)/np.sqrt(A**2+2*A*mu_c+1)
                    phi_lab = 2*np.pi*rnd()
                    
                    # update (see Brown notes, slide 5-15)                 
                    mu_new = mu_lab*mu + \
                             (np.sqrt(1-mu_lab**2)/sin_theta) * \
                                (mu*xi*np.cos(phi_lab)-eta*np.sin(phi_lab))
                    eta_new = mu_lab*eta + \
                              (np.sqrt(1-mu_lab**2)/sin_theta) * \
                                (eta*xi*np.cos(phi_lab)+mu*np.sin(phi_lab))   
                    # There is a formula for xi, but use the trig identity.
                    xi_new = np.sqrt(1-mu_new**2-eta_new**2)
                    
                    xi, mu, eta = xi_new, mu_new, eta_new
                    
                else:
                    # just sample new direction randomly
                    xi = 2*rnd()-1
                    phi = 2*np.pi*rnd()
                    mu = np.cos(phi)*np.sqrt(1-xi**2)
                    eta = np.sin(phi)*np.sqrt(1-xi**2)
                    
                # Ensure we have a sane angle.
                sin_theta = np.sqrt(1-xi**2)
                
            else:
                # we're absorbed!
                total_absorptions += 1
                # Then, increment the collision counter if we're in the right 
                # energy range.
                for g in range(3):
                    if group_boundaries[g] > E >= group_boundaries[g+1]:
                        reactions[region][g] += 1.0
                break
        else:
            # Move to the surface
            if surf == 1 and boundary != 'reflect':
                total_leaks += 1
                break
            else:
                c, s = mu/np.sqrt(1-xi**2), eta/np.sqrt(1-xi**2)
                
                assert(abs(xi**2 + mu**2 + eta**2 - 1) < tolerance)
                assert(abs(xi**2 + sin_theta**2 - 1)  < tolerance)
                x = x + d_surf*c
                y = y + d_surf*s 

                if surf == 1:
                    # reflecting off east or west changes the x component only
                    if abs(x - hpitch) < 1e-14 or abs(x + hpitch) < 1e-14:
                        mu *= -1
                    # reflecting off north or south changes the y component only 
                    else:
                        eta *= -1
                elif surf == 0:
                    if region == 0:
                        region = 1
                    else:
                        region = 0

#%% Final output
                        
siga = reactions / fluxes
siga[FUEL] /= (Nf * 1e-24)
print(siga[FUEL])