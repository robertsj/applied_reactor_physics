# NE 620/860 - Applied Reactor Physics - Lab 5

For this laboratory, you will work in groups of two.

## References

- CASMO-4 Manual
- SIMULATE-3 Manual
- CMS-Link Manual
- Generic CMS PWR Equilibrium Model

## Software/Hardware

- Access to *eigendoit.ksu.mne.edu* via an MNE or your machine for using 
  CASMO-4, Simulate-3 and Python

## Tasks


The basic goal of this laboratory is to model a complete, 4-loop PWR using
Studsvik's CMS (core modeling system), i.e., CASMO-4 and Simulate 3.  You are
not starting from scratch.  As it turns out, provided with the software is a
very detailed document that describes the modeling of a 3-loop PWR.

The overall goal of this lab is to design the "best" possible 4-loop plant.  Here,
you'll be limited to use of 6 unique assemblies (any combination of enrichment
or IFBA burnable absorber).  In particular, you are to design a core that meets
the same criteria of Table 5-1 in the report except that the cycle length must 
be 18 Gwd/T instead of 12 (i.e., close to 18 months rather than 12 months).
Beyond those constraints, the objective is to minimize the amount of U-235
required for the equilibrium cycle.  

### Task 1 - Understand the 3-Loop Model and Describe the Extension to a 4-Loop Model

Read the documentated model carefully.  Your primary job is to describe 
differences between this model and the traditional, 4-loop design that was
outlined earlier this semester.  One notable difference: a 4-loop plant has 
a nominal thermal power of 3400 MWth and uses 193 assemblies.


### Task 2 - Develop the CASMO-4 Models

This task should be easy.  Define inputs for UO2 fuel following the 
documented model, but update the assembly specifications to be
those of the STD fuel assembly  you have previously
modeled.  In addition, the IFBA case from the EPRI report can be used as a 
burnable absorber.  The enrichment may be varied from 2 to 4.5% U-235, but the
total number of unique assemblies you use for any part of your design is 6.
That is the same number used for the 3-loop case (see Table 3.1 and Section 3.11).

Note, we are only doing the UO2 case!

### Task 3 - Produce the SIMULATE-3 Library

Set up the appropriate CMSLINK input file following the 3-loop example.

### Task 4 - Produce the SIMULATE-3 First-Cycle and Transition Models

Following the 3-loop example, set up the first-cycle Simulate model.  The 
basic core layout should place the highest enrichment toward the periphery
andlower enrichments in a checkerboard layout with burnable poisons
placed as needed.  Of course, the specific enrichment is a design criterion,
but you can use the 3-loop example as a guide.  Detail your core configurations
using tables like Table  4-1, 4-2, 5.1, and 5.2.  Also, provide a table of
assembly types used like Table 3.1

### Task 5 - Produce the Equilibrium Model

Use the 3-loop example as a guide.  Report your results in the same format 
as Table 5.2.




