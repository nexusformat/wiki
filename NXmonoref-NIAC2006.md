---
title: NXmonoref-NIAC2006
permalink: NXmonoref-NIAC2006/
layout: wiki
---

<C ?xml version="1.0" ?>  
<C !--
 Instrument Definition for Monochromatic Source Reflectometers.
 Editor: Paul Kienzle <pkienzle@nist.gov>  
`Mangled_by: Nick Maliszewskyj <nickm@nist.gov>`  
`$Id$`  
`See `[`http://www.neutron.anl.gov:8080/NeXus/5`](http://www.neutron.anl.gov:8080/NeXus/5)` for component definitions.`  
`-->`

<NXentry>

` `<definition version="1.0" URL="http://www.nexus.anl.gov/instruments/xml/monoref.xml">  
`   NXmonoref`  
` `</definition>  
` `<start_time type="ISO8601" />

` `<tag name="scan">“`intensity|background+|background-|specular|rock|area`”</tag>  
` `<tag name="polarization">“`++|+-|-+|--|+|-`”`?`</tag>  
` `<intensity_scan NAPIlink="">  
`   {Slit scans for determining incident beam intensity}*`  
` `</intensity_scan>  
` `<background_scan NAPIlink"">  
`   {Off-specular scans for determining background intensity}*`  
` `</background_scan>

` `<NXsample>  
`   `<polar_angle type="NX_FLOAT[i]" units="degrees"/>  
`   `<momentum_transfer type="NX_FLOAT[i]" />  
` `</NXsample>

` `<C !--
    *** link to spectrum measurement for intensity vs. wavelength
    *** for a given slit setting
  
    *** warning: beam profile is not regular, but this effect is 
    *** accomodated in the spectrum measurement
  -->

` `<NXinstrument>

`   `<C !-- wavelength selection -->  
`   `<NXcrystal name="monochromator">  
`     `<wavelength />  
`   `</NXcrystal>

`   `<C !-- collimation -->  
`   `<NXaperture name="pre[sample|detector]_slit#">  
`     `<NXgeometry name="geometry">`?`  
`       `<NXtranslation name="translation">  
`         `<distances type="NX_FLOAT" units="mm">  
`           { Location of slit along beamline (midway between slits `  
`             if slits are not coplanar).  This is required to compute `  
`             instrument resolution. }`  
`         `</distances>`          `  
`       `</NXtranslation>  
`       `<NXshape name="shape">  
`         `<shape />  
`         `<size type="NX_FLOAT[nshapepars,np]" units="mm" />  
`       `</NXshape>  
`     `</NXgeometry>  
`   `</NXaperture>

`   `<C !-- 
      The polarizer-flipper-guidefield combination selects polarization vectors 
      in and out of the sample.  A number of scans are required to tune the 
      instrument so that polarization is either 'up' or 'down' on the sample.  
      On correctly tuned instruments the polarization angle selected should 
      be recorded by the flipper using polar_angle relative to the surface 
      (0/180 for +/-, or with out of plane polarization, 90/270 for +/-).  
      The polarization efficiency must be determined from a spectrum scan
      and the appropriate correction applied to the data.
      Raw values from the instrument, such as time dependent field applied
      to flipper coils or current on the current sheet can be recorded for
      specialized reduction programs which know how to handle them.
      -->  
`   `<NXpolarizer name="presample_polarizer">`?`</NXpolarizer>  
`   `<NXflipper name="presample_flipper">`?`</NXflipper>

`   `<NXpolarizer name="predetector_polarizer">`?`</NXpolarizer>  
`   `<NXflipper name="predetector_flipper">`?`</NXflipper>

`   `<C !-- detector may be protected by an attenuator and/or a beam stop -->  
`   `<NXattenuator>`?`  
`     `<attenuator_transmission />  
`   `</NXattenuator>  
`   `<NXbeam_stop>`?`  
`     { Need all fields so that we can calculate shadow of beam stop on detector. }`  
`   `</NXbeam_stop>

`   `<NXdetector>  
`     `<polar_angle type="NX_FLOAT[np]/>  
`     `<azimuthal_angle type="NX_FLOAT" units="degrees">  
`       { Indicate sense of scattering: 0 is front surface of sample, `  
`         180 is back surface of sample.  If 180, change the sign of the`  
`         reflected angle in the data.  It is also possible for the beam`  
`         to enter the substrate from the side and reflect off the back `  
`         surface of a film, in which case negative angles can be `  
`         interpreted as inverting the scattering length density profile`  
`         of the film (after accounting for absorption in the substrate. }`  
`     `</azimuthal_angle>  
`   `</NXdetector>

` `</NXinstrument>

` `<NXmonitor>`?`  
`   `<data type="FLOAT32[np]" />  
` `</NXmonitor>

` `<NXlog name="timer">`?`  
`   `<time />  
`   `<value type="FLOAT32[np]" units="second" />  
` `</NXlog>

` `<NXdata>  
`   `<momentum_transfer NAPIlink="NXentry/NXsample/momentum_transfer" />  
`   `<theta NAPIlink="NXentry/NXsample/polar_angle" />  
`   `<twotheta NAPIlink="NXentry/detector/polar_angle" />  
`   `<presample_slit1 NAPIlink="NXentry/presample_slit1/opening" />  
`   `<presample_slit2 NAPIlink="NXentry/presample_slit2/opening" />  
`   `<predetector_slit1 NAPIlink="NXentry/predetector_slit1/opening" />  
`   `<predetector_slit2 NAPIlink="NXentry/predetector_slit2/opening" />  
`   `<counts NAPIlink="NXentry/detector/counts" signal=1 />  
`   `<count_start NAPIlink="NXentry/timer/time" />  
`   `<count_length NAPIlink="NXentry/timer/value" />  
`   `<count_monitor NAPIlink="NXentry/monitor/data" />  
` `</NXdata>

` `<NXlog name="??">  
`   { Various logs for temperature, field, etc. which are assumed to`  
`     be constant over the duration of the run.  The reduction program`  
`     should be able to display their values on a parallel graph.  Note`  
`     that logs are not necessarily sampled synchronously with the`  
`     data points. }*`  
` `</NXlog>

</NXentry>
