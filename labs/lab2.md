# NE 620/860 - Applied Reactor Physics - Lab 2

## References

- Lectures 4, 5, 6
- CASMO-4 Manual

## Software/Hardware

You'll again need access to *eigendoit.ksu.mne.edu* via an MNE or your machine 
for using CASMO-4 via SSH.  To run CASMO-4, you'll need the appropriate 
paths set.  To do so, execute the following in your home directory:

```
homersimpson@eigendoit:~$ cp /share/apps/.studsvikrc .
```

## Tasks

### Four Factors

A key output of CASMO-4 is the two-group data produced for the homogenized
pin (or assembly).  Consider a UO$_2$ fuel pin having the following properties:

  - $\rho = 10$ g/cm$^3$
  - 4 w/o enriched (w/o enriched means "percent of U 
    that is ${}^{235}$U by mass")
  - fuel pellet radius is 0.4096 cm
  - cladding inner radius is 0.4180 cm
  - cladding outer radius is 0.4750 cm
  - pin pitch (distance between pin centers) is 1.2598 cm
  - hot PWR conditions (fuel temperature of 900 K, coolant temperature
    of 300 K)

Use CASMO-4 to produce two group cross sections.  Derive the two-group, 
four-factor formula for the homogenized pin cell, and define what each
term represents.  Substitute the cross sections computed by CASMO-4 into
the four-factor formula and compare to the computed eigenvalue.  Are 
they identical? close?  Why or why not?

### Geometry

Start with the same model used in the previous task.  Then use CASMO-4 to
produce a curve of the four factors versus the P/D ratio, where $P$ is the 
pin pitch and $D$ is the fuel diameter.  Vary the P/D ratio by modifying
the fuel radius (i.e., keep the pitch constant).  What P/D ratio does the 
original model have and why?  (*Hint*: consider what happens if the water
density suddenly increases or decreases, which would have the same effect
as the P/D going up or down.)



### Cladding Options

Zirconium-based alloys (e.g., Zr-4) are currently used for PWR
fuel cladding, but owing to their behavior under accident conditions, 
alternative, "accident-tolerant" cladding materials are being studied by
numerous groups.  Two options under consideration are:
  - FeCrAl (21% Cr, 5.8% Al, 0.7% Si, 0.4% Mn, and 0.08% C by mass)
    with $\rho = 7.25$ g/cm$^3$
  - SiC with $\rho = 3.21$ g/cm$^3$
Each material is being studied as a thin, protective layer over traditional
cladding.

To understand the impact of these materials, assume that the original model
cladding is reduced in thickness by 150 $\mu$m and replaced by the FeCrAl
alloy or SiC.  What is the impact on reactivity?  How much would the enrichment
need to be increased or decreased to compensate?

### Depletion

Consider the original model.  Deplete it to 40 MWd/kg.  How does the 
reactivity change as a function of time?  What fraction of the pin power
comes from ${}^{235}$U as function of time?  From ${}^{239}$Pu? 

### Temperature

Consider the original model.  Compute the fuel temperature and coolant 
temperature coefficients as a function of $P/D$.  Explain the trends using
the four factors.  *Hint*: Recall that $\alpha = d\rho/dT$ and that 
$\ln(fp\epsilon \eta) = \ln(f) + \ln(p) + \ln(\epsilon) + \ln(\eta)$.
