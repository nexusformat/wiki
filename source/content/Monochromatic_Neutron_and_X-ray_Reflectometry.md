---
title: Monochromatic Neutron and X-ray Reflectometry
permalink: Monochromatic_Neutron_and_X-ray_Reflectometry.html
layout: wiki
---
Monochromatic Neutron and X-ray Reflectometry
=============================================

**Please add comments to the discussion tab of this page and [sign
them]((Contents#Signatures.html "wikilink")**

This proposed instrument definition adds a new class (NXspin) and also
incorporates a few additions to existing base classes.

Additions
---------

### New background [NXcharacterization] (NXcharacterization.html "wikilink") type:

`     specular_offset_background`

The two existing backgrounds are isotropic\_scatter and
empty\_container. Physically we are moving the detector/sample slightly
away from the specular reflection condition and measuring the strength
of the signal rather than putting an isotropic scatter at the sample
position or leaving it empty.

Note: this simply identifies the location of the background scan, but
does not specify how the background was measured.

### Need to know the sample angle.

Propose adding the following to [NXsample] (NXsample.html "wikilink"):

       <polar_angle units="degrees" type="NX_FLOAT[np]">
       {Polar angle of the sample with respect to the beam incident on
        the monochromator}
       </polar_angle>
       <azimuthal_angle units="degress" type="NX_FLOAT[np]">
       {Azimuthal angle of the sample with respect to the beam incident on
        the monochromator}
       </azimuthal_angle>
       <rotation_angle units="degrees" type="NX_FLOAT[np]">
       {Rotation angle of the sample}
       </rotation_angle>

These fields are already used in the ratified
[NXmonotas] (Monochromatic_Neutron_and_X-ray_Triple-Axis_Spectrometer.html "wikilink"),
so there should be no problem ratifying them in the base class.

### Record Spin State

For polarized neutron reflectometry the control software allows the user
to select and tune a particular spin state. Expressed in terms of the
individual filters and flipper currents, it is difficult to determine
which spin state is desired. Instead the instrument component should
record the target spin state.

Propose NXspin class to record the target spin at the sample or at the
detector:

       
    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL:    http://definitions.nexusformat.org/NXspin.xml
    Editor: NIAC
    $Id$
        
    This is a description of the neutron spin state at a point in the
    beam path, as set by the combination of filters and flippers.
    -->
    <NXspin name="{presample_spin|predetector_spin}">
            <azimuthal_angle type="NX_FLOAT[np]" units="degrees">
            {90 for spin up, -90 for spin down}
            </azimuthal_angle>
            <polar_angle type="NX_FLOAT[np]" units="degrees">
            {Constant usually ignored. 0 in the direction of the beam path.}
            </polar_angle>
    </NXspin>

### Accurate record of the start and stop of every scan

We need an accurate record of the start and stop of every measurement in
a scan (e.g., to normalize by measurement time, and to correct for He3
polarizer efficiency decay).

[NXmonitor] (NXmonitor.html "wikilink") already stores count duration. Propose
adding count start\_time as well:

         <start_time type="NX_FLOAT[n]" units="seconds">
            {Start time for each scan point}
         </start_time>

The alternative is to use [NXlog] (NXlog.html "wikilink") and assume a
particularly named log corresponds to the
[NXmonitor] (NXmonitor.html "wikilink"), with the same length as the measured
points:

            
       <NXlog name="count_time">
          <time start="{ISO8601}" type="NX_FLOAT[np]" units="seconds">
            {Start of the measurement of point np}
          </time>
          <value type="NX_FLOAT[np]" units="seconds">
            {Durations of the measurement point np}
           </value>
       </NXlog>

The first solution is cleaner.

Full Definition
---------------

<nxformat file="NXmonoref.xml" tree="yes"></nxformat>
