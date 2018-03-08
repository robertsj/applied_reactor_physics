# NE 620/860 - Applied Reactor Physics - Lab 3

## References

- Lectures 7, 8, 9
- CASMO-4 Manual
- EPRI document

## Software/Hardware

- Access to *eigendoit.ksu.mne.edu* via an MNE or your machine for using NJOY
  using SSH **or** an installation of NJOY on your machine (Linux or maybe OS X)

## Tasks

### Understanding PWR Lattice Design Features

Westinghouse has two basic designs for fuel, STD and OFA, and we want to 
compare the performance of each design for a 4.25% enriched assembly:

 - STD is CASE 3 described in EPRI Appendix B
 - OFA is CASE 4 described in EPRI Appendix B

At hot conditions, and as functions of burnup (up to 80 MWd/kg), produce 
plots of
 - k-infinity
 - moderator temperature coefficient in pcm/K 
 - fuel temperature coefficient in pcm/K
 - boron coefficient in pcm/ppm vs. burnup
 - Hot zero power (HZP, at T = 560 K) to hot full power (HFP at 900 K) reactivity defect
 - Xe-135 worth in pcm vs. burnup (read the manual on CNU card)
 - Sm-149 worth in pcm vs. burnup (read the manual on CNU card)
 - Plot the moderator temperature history in pcm/K vs. burnup
 - Plot the fuel temperature history in pcm/K vs. burnup
 - Plot the boron history in pcm/ppm vs. burnup
 - If core inlet coolant is at 560 K and core exit is 600K, plot the difference 
   in Pu-239 concentration for fuel depleted at inlet and exit coolant 
   conditions vs. burnup

### BWR Lattice Design Optimization

For this task, we want to optimize a typical BWR bundle for a 24-month
cycle (typical for BWRs).  Specifically, the task is to seek an 
optimal enrichment/Gd design to maximize fuel burnup (EOL defined as the
burnup at which where $k_{\infty} < 0.95$ with a minimum reactivity swing 
and a minimum linear heat generation rate (LHGR).

Designs are subject
to the following, absolute **constraints**:
 - $k_{\inf} > 1.00$ at zero burnup (for equilibrium Xe)
 - $k_{\inf} < 1.13$ at all burnups (for equilibrium Xe)
 - $\text{max pppf} < 1.35$ at all burnups (for equilibrium Xe)
 - ${}^{235}U enrichment  intervals of 0.1% from 2.0 to 4.90%
 - Gd enrichment intervals of 1.0% from 2.0 to 10.0%


Simplifications:
 - Bundle geometry is fixed as given in bwr_bundle.inp
 - Density of non-gad fuels are 10.5 g/cc
 - Density of all Gd fuels are 10.2 g/cc
 - Void=40%, TFU=900K, TMO=560K, 54 kW/L

Designs will be assessed by using the following objective function:

$$
  f(\text{EOL Burnup}) =  8(\text{EOL burnup} - 46.5) + 4(1.30 - \text{max pppf) + 2 (1.11 - \text{max } k_{\infty}) \, .
$$


