"""
Pin-cell geometry.  Test that we can sample neutron origins and directions and
then transport from one region to another.
"""

#%% imports
import numpy as np
rnd = np.random.rand
#np.random.seed(4)
import matplotlib.pyplot as plt


#%% Geometry
radius = 0.5 # fuel radius (cm)
hpitch = 1.3/2 # half pin pitch (cm)



FUEL = 0
MOD = 1

#%% Control parameters

# Number of source particles to simulate
num_hist = 100 
# Boundary condition at outer pin-cell surface
boundary = 'reflect' 
# Surface tolerances
tolerance = 1e-15

#%% Tallies
total_leaks = 0
total_absorptions = 0
total_low_energy = 0


#%% Simulation



# We loop over all simulated source particles.  The only physics included
# are elastic scattering and radiative capture.  A source particle's history
# is terminated if (1) it is absorbed, (2) its energy falls below the 
# minimum energy tallied, or (3) it escapes the system (i.e., vacuum boundary).
flag = False
#%%
for h in range(10) :

    plt.figure(h)
    #plt.clf()
    plt.plot([-hpitch, -hpitch], [-hpitch, hpitch], 'k')
    plt.plot([-hpitch,  hpitch], [-hpitch, -hpitch], 'k')
    plt.plot([ hpitch,  hpitch], [-hpitch, hpitch], 'k')
    plt.plot([-hpitch,  hpitch], [ hpitch, hpitch], 'k')
    
    phi = np.linspace(0, 2*np.pi)
    x = radius * np.cos(phi)
    y = radius * np.sin(phi)
    
    plt.plot(x, y, 'k')
    plt.axis('equal')
    plt.grid(True)
    plt.title('history {}'.format(h))
    
    # Sample the initial location
    r = np.sqrt(rnd()*radius**2)
    phi = 2*np.pi*rnd()
    x, y = r*np.cos(phi), r*np.sin(phi)

    region = FUEL # I'm born in fuel
    E = 1e6
    # Sample the initial direction.  Here. mu, eta, and xi are the 
    # directional cosines with respect to the x, y, and z axes.  The pin
    # is oriented along the z axis.
    xi = 0.0 #rnd() # cos(theta) w/r to z axis
    sin_theta = np.sqrt(1 - xi**2) # 
    phi = 2*np.pi*rnd() # aximuthal (in xy plane)
    mu = np.cos(phi)*np.sqrt(1-xi**2)
    eta= np.sin(phi)*np.sqrt(1-xi**2)
    
 
    plt.plot(x, y, 'g*')
    
    print("")
    counter = 0
   # plt.figure(2)
    while True:
        counter += 1
        if counter==21:
            flag=True
            break        
        ss = "\nh={}, c={}\n".format(h, counter)
        print(ss)
        assert abs(mu**2 + eta**2 + xi**2 - 1) < 1e-14
        assert abs(xi**2 + sin_theta**2 - 1)  < 1e-14

        # distance to surfaces
        surf, d_surf = surface_intersection(x, y, mu, eta, xi)
        
  

        # Move the surface
        ss="moving from...{:.3f}, {:.3f}...to surf={} at...".format(x, y, surf)
        if surf == 1 and boundary != 'reflect':
                c, s = mu/np.sqrt(1-xi**2), eta/np.sqrt(1-xi**2)
                x0, y0 = x, y
                assert(abs(xi**2 + mu**2 + eta**2 - 1) < 1e-14)
                assert(abs(xi**2 + sin_theta**2 - 1)  < 1e-14)
                x = x + d_surf*c
                y = y + d_surf*s    
                total_leaks += 1
                leak = True
        else:
                leak = False
                c, s = mu/np.sqrt(1-xi**2), eta/np.sqrt(1-xi**2)
                x0, y0 = x, y
                assert(abs(xi**2 + mu**2 + eta**2 - 1) < tolerance)
                assert(abs(xi**2 + sin_theta**2 - 1)  < tolerance)
                x = x + d_surf*c
                y = y + d_surf*s 

                    
                
                assert abs(x) - hpitch < tolerance, 'x out of bounds!'
                assert abs(y) - hpitch < tolerance, 'y out of bounds!'
                
                ss+="x={:.3f} y={:.3f} c={:.3f} s={:.3f}".format(x, y, c, s)
                if surf == 1:
                    # reflecting off east or west changes the x component only
                    if abs(x - hpitch) < 1e-14 or abs(x + hpitch) < 1e-14:
                        mu *= -1
                    # reflecting off north or south changes the y component only 
                    else:
                        eta *= -1
                    ss+="\n  -->ref=c={:.3f} s={:.3f} to c={:.3f} s={:.3f}".format(
                        c, s, mu/np.sqrt(1-xi**2), eta/np.sqrt(1-xi**2))
    
                elif surf == 0:
                    if region == 0:
                        region = 1
                    else:
                        region = 0
        print(ss)
        print ('-----')
        marker = 'x' if region == 0 else 'o'
        color = 'r' if surf == 0 else 'b'
        plt.plot([x0, x], [y0, y] , color='gray')
        plt.plot(x, y, color=color, marker=marker)
        plt.text(x, y, "{}".format(counter))
        if leak :
            break
