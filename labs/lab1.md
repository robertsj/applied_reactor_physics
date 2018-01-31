# NE 620/860 - Applied Reactor Physics - Lab 1

## References

- Lectures 1, 2, and 3
- NJOY Reference Manual
- Understanding NJOY (http://t2.lanl.gov/nis/njoy/)

## Software/Hardware

- Access to *eigendoit.ksu.mne.edu* via an MNE or your machine for using NJOY
  using SSH **or** an installation of NJOY on your machine (Linux or maybe OS X)

## Tasks

### Acquiring the Data

Throughout these laboratory exercises, we'll focus exclusively on the
materials used in traditional, light-water reactor fuel (UO$_2$) and
its surrounding moderator (H$_2$O).

Head to https://t2.lanl.gov/nis/data/endf/endfvii-n.html and acquire the
*neutron* data for the following nuclides:
 - U-235
 - U-238
 - H-1
 - O-16

Save these files as u235, u238, h1, and o16, respectively.

Note, these are text files and quite large.  Make sure to place these in a
folder that you can access later on and in which you can execute NJOY.

Then head to https://t2.lanl.gov/nis/data/endf/endfvii-thermal.html and 
acquire the *thermal data* for H in H$_2$O.  Save this file as h_in_h20 in the
same directory as the other files.

### Simple Cross Sections

(Adapted from http://t2.lanl.gov/nis/njoy/exer01.html)

Use your text editor to open the H-1 ENDF file you downloaded.  Search for
the beginning of the elastic cross section tabulation by looking for 
MAT=125, MF=3, and MT=2.  Answer the following:
  - What is the elastic cross section at 0.0253 eV?
  - What is the mathematical shape of this cross section at low energies?
  - Where does the cross section begin to deviate from its low-energy shape?
  - What interpolation law is specified for elastic scattering?
  - What is the elastic scattering cross section at .0015 eV?

Now, search for the beginning of the radiative capture cross section (MT=102)
and answer the following:
  - What is the capture cross section at 0.0253 eV?
  - What is the mathematical shape of this cross section at low energies?
  - Where does the cross section begin to deviate from its low-energy shape?
  - What interpolation law is specified for capture? 
  - What is the capture cross section at .0015 eV?

Finally, search for the beginning of the total cross section (MT=1):
  - Does the total cross section at 0.0253 eV match the sum of the elastic,
    and capture cross sections?
  - Compute the total cross section at .0015 eV using linear interpolation. 
    What is the percent error with respect to the sum of the elastic and 
    capture cross sections at that energy?
  - Does the more complicated interpolation law given for MT=1 really solve 
    the problem?

### Plotting Cross Sections

(Adapted from http://t2.lanl.gov/nis/njoy/exer02.html)

NJOY runs data through its various modules by using files called "tapes" to
communicate between the modules. Therefore, NJOY input files give the module
name to use, then the input and output units for that module, and then the
characteristic input for that module. This is repeated for each module to
be used, and then terminated with the module name "stop". 

Navigate to your directory containing the ENDF data files, and copy `h1` to 
tape 20 (i.e., `cp h1 tape20`). Produce the following input file *but leave off
the comments to the right of the slash symbol*.

```
reconr
20 21
'exercise 2'/       new tape ID title
125 1/              material 125 (H-1)
.001/               tolerance
'1-H-1'/            descriptive card for new tape
0/
plotr
22/
/
1/                  first plot on new axis
'1-H-1'/            title line 1
/                   title line 2 (here, it's empty!)
4 0 0 1/            log-log, no second axis, no grid lines/ticks, use legend
1e-4 1e6/           energy range
/                   xlabel
1e-4 1e2/           cross-section range
/                   ylabel
7 21 125 3 1/       endf type, data tape, material (3 is sigma vs E), file, and reaction
0 0 0 0/            line with no symbols, square (not used), solid, black
'total'/
2/                  second plot on same axis, so skip a bunch of other cards.
7 21 125 3 2/       endf type, data tape, material (3 is sigma vs E), file, and reaction
0 0 0 1/            line with no symbols, square (not used), solid, black
'elastic'/
3/                  third plot on same axis, so skip a bunch of other cards.
7 21 125 3 102/     endf type, data tape, material (3 is sigma vs E), file, and reaction
0 0 0 2/            line with no symbols, square (not used), solid, black
'capture'/
99/                 finished (99 indicates no more curves will be read)
viewr
22 23/
stop
```

This file says to run RECONR on MAT125 with a reconstruction tolerance
of .001 (.1%). Take the output on tape21 into PLOTR and extract the data
for MAT125, MF3, MT102 onto tape22. A title is provided for the graph,
and special scales are specified for the axes. The default axis labels and
line type will be used. Finally, a Postscript version of the graph is produced
on tape23 using VIEWR. 

Run NJOY with this input file to produce the image file.  Include this image,
in your report and answer the following:
  - What shape does the *elastic scattering* cross section have?
  - What shape does the *capture* cross section have?  Is there a physical
    reason for that shape?  (You may find that Lamarsh offers some insight!)

### Reconstructing Resonances with Doppler Broadening

(Adapted from http://t2.lanl.gov/nis/njoy/exer04.html)

Copy u238 to tape 20. Create an input file containing the following lines,
again leaving off the comments after the slashes: 

```
           reconr
           20 21
           'exercise 4'/    new tape ID title
           9237 1/          MAT
           .01/             fractional tolerance
           '92-U-238'/      descriptive card for new tape
           0/
           broadr
           20 21 22
           9237 1/          MAT, one temperature
           .01/             tolerance
           900/             temperature is 900 K
           0/
           plotr
           23/              output file
           /                default page style
           1/               new axes, new curve
           '92-U-238'/      title line 1
           /                no line 2 for titles
           2/               lin x - log y
           2 4 .5/          x-axis range and step
           /                default label
           .1 1000/         y-axis range
           /                default label
           4 21 9237 3 102 0./ data source for curve
           1 3 0/           crosses with solid line
           2/               second curve on axes
           4 22 9237 3 102 10000./ data source for curve
           0 0 1/           crosses with dashed curve
           99/              finished
           viewr
           23 24/
           stop
```

Run this input to produce the image on tape24.  Include this image in your
report and answer the following:
  - How did the shape of the resonances change between 0K and 900K?
  - What impact does this resonance shape change have on reactors?
  - Does the overall "area under the curve" appear to change for a given
    resonance?  (You may wish to repeat this calculation over a smaller
    energy range to answer this.)

### Multigroup Cross Sections


NJOY is most often used to produce data for downstream applications.  For 
example, NJOY can turn ENDF data into ACE files suitable for MCNP.  Here,
we'll use it to produce multigroup cross sections suitable for *deterministic*
codes like CASMO-4 (which we'll use later on in the course).

Specifically, we'll produce a multigroup "library" for 
U-238 for several different "background" cross sections and 
temperatures.


```
moder  / Convert data on 20 to binary to 21, id is 9237
20 -21
reconr / Reconstruct cross sections onto 22
-21 -22
'PENDF TAPE FOR U-238'/
9237 0/
0.001  0.  0.005/ Reconstruction 0.1% (0.5% max) with 0K temp
0 /
broadr
-21 -22 -23
9237 3/
.001/
300.0 600.0 900.0/
0/
unresr
-21 -23 -24
9237 3 7 1
300.0 600.0 900.0
1.e10 1.e5 1.e4 1000. 100. 10. 1
0/
groupr
-21 -24 0 -25
9237 9 0 5 0 3 7 1
'92-U-238'/
300. 600. 900.
1.e10 1.e5 1.e4 1000. 100. 10. 1
3 1 'total'/
3 2 'elastic'/
3 18 'fission'/
3 102 'capture'/
6 2 'elastic'/
6 18 'fission'/
0/
3 1 'total'/
3 2 'elastic'/
3 18 'fission'/
3 102 'capture'/
6 2 'elastic'/
6 18 'fission'/
0/
3 1 'total'/
3 2 'elastic'/
3 18 'fission'/
3 102 'capture'/
6 2 'elastic'/
6 18 'fission'/
0/
0/
stop
```
Now, you should

- Modify this input to produce plots of the continuous 
  and  multigroup *capture* cross section between 0 and
  50 eV using a linear scale for the horizontal axis and 
  a log scale for the vertical axis.  Include the multigroup
  cross sections for  background cross 
  sections of 10, 100, 1000, and 10$^{10}$  barns.  The latter is very
  large and represents the infinite-dilution case.  All data should be for
  the 900 K case.

- See if you can read the the output of GROUPR to pick out the multigroup
  values shown in your plot.  See if you can pick out the same values for
  300 K and 600 K.  The ratio $f = \sigma/\sigma_0$ is the self-shielding
  factor.  How does $f$ depend on the background cross section?  On
  temperature?



