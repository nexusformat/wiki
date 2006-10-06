---
title: SAS
permalink: SAS/
layout: wiki
---

Small-Angle Scattering
----------------------

### 2006-04-19

Given the complex requirements for initial data treatment on pulsed
source SANS instruments there has been general agreement to separate
these from the much simpler pin-hole geometry cameras used for
monochromatic X-ray and Neutron SAS studies, shown together below as
NXmonosas.

### 2006-10-05

Effort was made to simplify the definition below, correct errors (such
as removed fields that did not exist in base classes), and remove
unnecessary information.

<?xml version="1.0" encoding="utf-8"?>
<NXroot>

<NXentry name="{Entry Name}">  
` `

<title>
{Extended title for entry}?

</title>
` `<short_title>`{20 characters max. for legends etc.}>`</short_title>  
` `<start_time type="ISO8601">`{Starting time of measurement}?`</start_time>  
` `<end_time type="ISO8601">`{Ending time of measurement}?`</end_time>  
` `<experiment_identifier type="NX_CHAR">`{}?`</experiment_identifier>  
` `<run_number type="NX_INT">`{Number of run or scan stored in this entry}?`</run_number>  
` `<run_cycle type="NX_CHAR">`{Number of the facility cycle in which the measurements were made}?`</run_cycle>

` `<NXinstrument name="{Name of instrument}">  
`  `<name short_name="{short name of instrument}">`{Name of instrument}?`  
`  `</name>

`  `<NXsource name="{Name of facility}">  
`   `<name type="NX_CHAR">`{Name of source}?`</name>  
`   `<type type="NX_CHAR">  
`    `“`Spallation`` ``Neutron`` ``Source`”`|`  
`    `“`Reactor`` ``Neutron`` ``Source`”`|`“`Synchrotron`` ``X-ray`` ``Source`”`|`  
`    `“`Rotating`` ``Anode`` ``X-ray`”`|`“`Fixed`` ``Tube`` ``X-ray`”`?`  
`   `</type>  
`   `<probe type="NX_CHAR">“`neutron`”`|`“`x-ray`”`?`</probe>  
`   `<bunch_mode type="NX_CHAR">“`Single`` ``Bunch`”`|`“`Multi`` ``Bunch`”`?`</bunch_mode>  
`   `<power type="NX_FLOAT">“`nominal`` ``power`”</power>  
`  `</NXsource>

`  `<NXattenuator name="{Name of beam attenuator}">  
`   `<attenuator_transmission type="NX_FLOAT">  
`    {The nominal fraction of the beam transmitted by the attenuator}`  
`   `</attenuator_transmission>  
`  `</NXattenuator>

`  `<NXaperture name="Name of beamline aperture">  
`   `<NXgeometry name="geometry">`{location and shape of aperture}`</NXgeometry>  
`  `</NXaperture>

`  `<NXbeam name="Beam_at_sample">` {characteristics of beam at sample}`  
`  `</NXbeam>

`  `<NXdetector name="{Name of bank of detectors, or multidetector}">  
`   `<data type="NX_FLOAT[i,j,...]|NX_INT[i,j,...]">`{Data values}?`</data>  
`   `<data_errors type="NX_FLOAT[i,j,...]">`{Data errors}?`</data_errors>  
`   `<detector_number type="NX_INT[i]">`{Identifier for detector}?`  
`   `</detector_number>  
`   `<x_offset type="NX_FLOAT[k+1]">`{pixel offset from the detector center `  
`    in x-direction}?`</x_offset>  
`   `<y_offset type="NX_FLOAT[l+1]">`{pixel offset from the detector center `  
`    in the y-direction}?`</y_offset>  
`   `<NXgeometry name="SD_Distance">`{Position and orientation of detector centre`  
`    with respect to direct beam}?`  
`   `</NXgeometry>  
`    `<x_pixelsize type="NX_FLOAT[i?]">`{Size of each detector pixel. `  
`      If it is scalar all pixels are the same size}?`</x_pixelsize>  
`    `<y_pixelsize type="NX_FLOAT[i?]">`{Size of each detector pixel. `  
`      If it is scalar all pixels are the same size}?`</y_pixelsize>  
`    `<quiet_count type="NX_FLOAT[i?]">`{Detector dark current count.  `  
`      If it is scalar all pixels hav ethe same count}?`</quiet_count>  
`    `<NXgeometry name="beam_center">`{x,y position of straight-through beam on the detector}?`</NXgeometry>  
`  `</NXdetector>  
`   `<NXbeam_stop name="Name of beam stop">  
`    `<NXgeometry name="geometry">`{shape, orientation and position of the beam stop}`  
`    `</NXgeometry>  
`     `<description type="NX_CHAR">`{ `“`circular`”`|`“`rectangular`”`}?`</description>  
`     `<size type="NX_FLOAT">`{size of beamstop}`</size>  
`     `<x type="NX_FLOAT">  
`      {x position of the beamstop in relation to the detector}?`</x>  
`     `<y type="NX_FLOAT">  
`      {y position of the beamstop in relation to the detector}?`</y>  
`     `<status type="NX_CHAR">`{`“`in`”`|`“`out`”`}`</status>  
`   `</NXbeam_stop>  
` `</NXinstrument>

` `<NXmonitor name="control {Name of the monitor}">  
`   `<counting_mode type="NX_CHAR">  
`  `“`time`”`|`“`neutrons`”`|`“`charge`”`?`  
`   `</counting_mode>  
`   `<quiet_count type="NX_FLOAT">`{Monitor dark current count}?`</quiet_count>  
`   `<preset type="NX_FLOAT32">`{preset for terminating run}?`</preset>  
`   `<data type="NX_INT32">` {Monitor value}`  
`   `</data>  
`   `<NXcharacterization name="quiet_count">`{to be defined}?`</NXcharacterization></NXmonitor>

` `<NXsample name="{Name of sample}">  
` `</NXsample>

` `<NXdata name="Datablock name">`+`  
`  `<data type="NX_INT[...] | NX_FLOAT[...]" signal="1">`{link to detector counts in NXdetector}`</data>  
` `</NXdata>  
</NXentry>

</NXroot>
