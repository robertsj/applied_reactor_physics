import numpy as np
import matplotlib.pyplot as plt

# potential cross section
sigma_p = 11.2934
# radius, from sigma_p = 4*pi*R^2
R = np.sqrt(sigma_p*1e-24/4/np.pi)

I = 0 # s wave
E0, J, GN, GG, _, _ = np.loadtxt('u238.txt', unpack=True)
G = GN+GG
A = 238.0
E = np.logspace(-1, 3, 10000)
sigma_g = np.zeros_like(E)
sigma_n = np.zeros_like(E)
sigma_n[:] = sigma_p

for i in range(len(E0)):
    # statistical spin factor, where I=nuclear spint, J=total spin
    g = (2*J[i]+1)/(2*(2*I+1))

    # reduced wavelength at resonance (in cm)
    lambda_0 = 2.86e-9/np.sqrt(E0[i])/np.pi/2
    
    # total cross section at resonance energy (DH 2-36)
    sigma_0 = 2.608e6 * (A+1)**2/(A**2 * E0[i]) * (GN[i]/G[i]) * g
     
    # capture cross section (DH 2-35)
    y = (2/G[i])*(E - E0[i])
    sigma_g += sigma_0 * (GG[i]/G[i]) * np.sqrt(E0[i]/E) * (1/(1+y**2))
    
    # scattering cross section (DH 2-3?)
    sigma_n += sigma_0 * (GN[i]/G[i]) * np.sqrt(E0[i]/E) * (1/(1+y**2)) \
             + sigma_0 * 2*R/lambda_0 * (y/(1+y**2)) 

# add potential after other terms
sigma_n += sigma_p

plt.figure(1)
plt.loglog(E, sigma_g, E, sigma_n)
plt.legend(['capture', 'elastic'])
plt.xlabel('energy (eV)')
plt.ylabel('cross section (b)')            
plt.show()

# Save the data for collapsing demo
np.savetxt('u238_xs.txt', np.transpose(np.array([E, sigma_g, sigma_n])))
