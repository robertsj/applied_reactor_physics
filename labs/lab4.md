# NE 620/860 - Applied Reactor Physics - Lab 4

For this laboratory, you may work in groups of 5, i.e., two groups total.  
I therefore expect the reports to be pristine, well-written documents that 
go beyond what previous reports have been.

## References

- CASMO-4 Manual
- Roberts et al. paper on NRM
- Smith paper on homogenization
- Any book on reactor theory with two-group diffusion

## Software/Hardware

- Access to *eigendoit.ksu.mne.edu* via an MNE or your machine for using 
  CASMO-4 and Python

- Installation of NRM code from github.com

## Tasks

### Understanding LRM and NRM

For this task, you will adapt the CASMO-4 example included with 
the `nrm` package to analyze again the STD and OFA models from Lab 3. 
Assuming a 4.25% enrichment, and use `nrm` to compute the 
(1) cycle length,
(2) discharge burnup,
(3) cycle-averaged batch peaking factors, 
(4) cycle-averaged fuel temperature, and 
(5) cycle-averaged coolant temperature for the following:
  - STD and OFA models
  - 1-, 2-, 3-, and 4-batch cores
  - equal and unequal power sharing
These represent $2 \times 4 \times 2 = 16$ unique cases.  Explain your
observations.  Are they consistent with expectations?

### Understanding homogenization

For this problem, you will solve the two-group diffusion equations for
a piece-wise homogenous reactor subject to reflecting conditions.  The geometry
of interest is given below:


```
        |         |           |         |
reflect |    A    |  A  |  B  |    B    | reflect
        |         |           |         |
             1          2          3
```

The geometry consists of three assemblies.  Assembly 1 is a homogenous
assembly filled with material A, while Assembly 3 is homogenous and filled
with material B.  Assembly 2 is heterogeneous, with its left half filled with
material A and its right half with material B.  Each assembly is 21 cm wide.


The cross sections for materials A and B are given in the following table:


| Material  | $g$  | $D_g$  |  $\Sigma_{ag}$ | $\nu\Sigma_{fg}$  | $\Sigma_{sg\to g'}$  |
|---|---|---|---|---|---|
| A  | 1  | 1.320  | 0.009  | 0.006  | 0.017  |
|    | 2  | 0.383  | 0.080  | 0.104  | 0.000  |
| B  | 1  | 1.320  | 0.009  | 0.006  | 0.017  |
|    | 2  | 0.383  | 0.090  | 0.104  | 0.000  |

Assume $\chi_1 = 1$ and $\chi_2 = 0$, i.e., fission neutrons are born in
group 1 only.

**Your tasks**:
 1. Solve this problem "exactly" to provide a reference solution.  I suggest doing this
   *semi-analytically*, but a numerical solution using finite differences is
   acceptable if you can demonstrate you know what you are doing (recall, this
   was a topic of both ME 400 and ME 701).  For the semianalytical approach,
   I provided some hints in class.
 2. Produce flux-weighted, homogenized, two-group cross sections and diffusion
   coefficients in each region.  Do the cross sections for Assemblies 1 and 3
   change?  Here, the flux to use for weighting is the reference solution from
   part 1.
 3. Solve the homogenized problem in exactly the same way and compare the 
   solutions.  In particular, show the two-group fluxes, currents, and partial
   currents for the reference and homogenized problems.
 4. Use the original "reference" solution to compute discontinuity 
   factors based on Generalized Equivalence Theory (GET) and demonstrate how 
   the discontinuity factors change the homogenized result.  Note, your report
    should provide a sufficient description of homogenization and GET so that
   a general student of you background can understand the work.



