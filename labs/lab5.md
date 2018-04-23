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
very detailed document that describes the modeling of a 3-loop PWR.  For this
lab, your analysis will be limited to the first cycle model; you may choose
to do the equilibrium analysis for additional learning.

### Task 1 - Understand the 3-Loop Model and Describe the Extension to a 4-Loop Model

Read the documentated model carefully.  Your primary job is to describe 
differences between this model and the traditional, 4-loop design that was
outlined earlier this semester.  You may need to do a bit of searching to
nail down any missing details---use me, Dr. Bindra, and anyone else as a resource.

### Task 2 - Develop the CASMO-4 Models

This task should be easy.  Define inputs for UO2 fuel following the 
documented model, but update the assembly specifications to be
those of the OFA fuel assembly  you have previously
modeled.  Use the same enrichments as the 3-loop design.

Only do the UO2 case, but do include the control rods (adjust any
dimensions needed) and burnable absorbers (same as used for the 3-loop design).

### Task 3 - Produce the SIMULATE-3 Library

Set up the appropriate CMSLINK input file following the 3-loop example.

### Task 4 - Produce the SIMULATE-3 Models

Following the 3-loop example, set up the first-cycle simulate model.  The 
basic core layout should place the highest enrichment toward the periphery
and the two lower enrichments in a checkerboard layout with burnable poisons
placed as needed.  Your goal is to produce a core with an assembly power
peaking factor no greater than the one reported for the 3-loop core's first
cycle.

### Task 5 - Run your Models and Report Relevant Features

Use the 3-loop example as a guide, and describe how you designed your core,
and how it performs.




