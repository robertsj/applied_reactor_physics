import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# load data
E, sigma_ar, sigma_sr = np.loadtxt('u238_xs.txt', unpack=True)

# Spectrum functions
def narrow_resonance(E, sigma_ar, sigma_sr, sigma_d):
    phi = 1/((sigma_ar+sigma_sr+sigma_d)*E)
    return phi/phi[0]
def wide_resonance(E, sigma_ar, sigma_sr, sigma_d):
    phi = 1/((sigma_ar+sigma_d)*E)
    return phi/phi[0]

# group boundaries (from WIMS 69-group format.)
group_boundaries = [27.7, 15.968, 9.877, 4.0] 

# dilution cross sections
inf_dilute = 100000000
sigma_d = [inf_dilute, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]

# produce fluxes at each dilution
phi_nr = {}
phi_wr = {}
for sd in sigma_d:
    phi_nr[sd] = narrow_resonance(E, sigma_ar, sigma_sr, sd)
    phi_wr[sd] = wide_resonance(E, sigma_ar, sigma_sr, sd)

# produce cross sections
sigma_g = {}
for sd in sigma_d:
    sigma_g[sd] = [0]*(len(group_boundaries)-1)
    # define the integrands for the numerator and denominator of the
    # group cross section using linear interpolation.
    top_integrand = lambda x: np.interp(x, E, sigma_ar*phi_nr[sd])
    bot_integrand = lambda x: np.interp(x, E, phi_nr[sd])
    for g in range(len(sigma_g[sd])):
        E_high = group_boundaries[g]
        E_low = group_boundaries[g+1]
        sigma_g[sd][g] = quad(top_integrand, E_low, E_high)[0] / \
                         quad(bot_integrand, E_low, E_high)[0]

# compute self-shielding factor
self_shielding = []
for sd in sigma_d:
      self_shielding.append(sigma_g[sd][2] / sigma_g[inf_dilute][2])
             

plt.figure(1)
plt.title('NR vs WR')
plt.loglog(E, phi_nr[100], label='NR ($\sigma_d=100$ b)', color='b', ls='-')
plt.loglog(E, phi_wr[100], label='WR ($\sigma_d=100$ b)', color='r', ls='-')
plt.axis([1e0, 1e2, 1e-5, 1e-1])
plt.legend()
plt.xlabel('$E$ (eV)')
plt.ylabel('$phi(E)$')

"""
Quick Question: Which flux leads to a larger dip and why?
"""

plt.figure(2)
plt.title('Impact of Dilution')
plt.loglog(E, phi_nr[inf_dilute], label='NR ($\sigma_d=\infty$ b)', color='k', ls='-')
plt.loglog(E, phi_nr[100], label='NR ($\sigma_d=100$ b)', color='b', ls='-')
plt.loglog(E, phi_nr[10], label='NR ($\sigma_d=10$ b)', color='r', ls='-')
plt.axis([1e0, 1e2, 1e-5, 1e-1])
plt.legend()
plt.xlabel('$E$ (eV)')
plt.ylabel('$phi(E)$')


plt.figure(3)
plt.title('Group and Continuous Cross Sections')
plt.loglog(E, sigma_ar)
for sd in sigma_d:
    color = np.random.rand(3)
    E_plt, sigma_plt = [], []
    for g in range(3):
        E_plt.append(group_boundaries[g])
        E_plt.append(group_boundaries[g+1])
        sigma_plt.append(sigma_g[sd][g])
        sigma_plt.append(sigma_g[sd][g])        
    plt.plot(E_plt, sigma_plt, c=color, 
             label='$\sigma_d={}$'.format(float(sd) if sd < inf_dilute else "\infty"))
plt.axis([group_boundaries[-1], group_boundaries[0], 1e-1, 1e5])
plt.legend()
plt.xlabel('energy (eV)')
plt.ylabel('cross section (b)')

"""
Quick Question: Why does the middle cross section have no apparent dependence
on the dilution cross section?
"""

plt.figure(4)
plt.title('Self-Shielding Factor (4-9.9 eV group)')
plt.semilogx(sigma_d[1:], self_shielding[1:], '-o')

plt.show()



