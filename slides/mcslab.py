"""
Computes group-wise fluxes and microscopic cross sections in a two
region pin cell assuming only U-238 and H-1, isotropic scattering, and 
no fission.  All neutrons are born at a fixed starting energy E0.
"""

#%% imports
import numpy as np
import matplotlib.pyplot as plt

#%% cross section data
# load u238 data
E, sigma_fa, sigma_fs = np.loadtxt('u238_xs.txt', unpack=True)

# hydrogen cross section
sigma_ma =  0.0 + np.zeros_like(E)
sigma_ms = 20.0 + np.zeros_like(E)

# number densities
Nf = 10/238*6.022e23
Nm = 0.8 * 6.022e23

# macroscopic cross sections 
Sigma_fa = lambda x: np.interp(x, E, Nf*sigma_fa*1e-24)
Sigma_fs = lambda x: np.interp(x, E, Nf*sigma_fs*1e-24)
Sigma_ma = lambda x: np.interp(x, E, Nm*sigma_ma*1e-24)
Sigma_ms = lambda x: np.interp(x, E, Nm*sigma_ms*1e-24)
Sigma_ft = lambda x: Sigma_fa(x) + Sigma_fs(x)
Sigma_mt = lambda x: Sigma_ma(x) + Sigma_ms(x)

# 

#%% control parameters
num_hist = 10 # number of histories
boundary = 'reflect' #


for h in range(num_hist) :
    
    # initial energy (eV)
    E0 = 1e6 

    # initial location
    #x, y





