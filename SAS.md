---
title: SAS
permalink: SAS/
layout: wiki
---

Small-Angle Scattering
----------------------

### 2006-04-19

Given the complex requirements forinitial data treatment on pulsed
source SANS instruments there has been general agreement to separate
these from the much simpler pin-hole geometry cameras used for
monochromatic X-ray and Neutron SAS studies, shown together below as
NXmonosas.

<?xml version="1.0" encoding="utf-8"?>
<NXroot  file_name="{File name of original NeXus file}"
 file_time="{Date and time of file creation}"
 file_update_time="{Date and time of last file change at close}"
 NeXus_version="{Version of NeXus API used in writing the file}"
 HDF_version="?"
 HDF5_version="?"
 creator="{facility or program where file originated}?">

<NXentry name="{entry name}">`+`</NXentry>  
<NXentry name="{Entry Name}">  
` `

<title>
{Extended title for entry}?

</title>
` `<short_title>`{20 characters max. for legends etc.}>`</short_title>  
` `<start_time type="ISO8601">`{Starting time of measurement}?`</start_time>  
` `<end_time type="ISO8601">`{Ending time of measurement}?`</end_time>  
` `<experiment_identifier type="NX_CHAR">`{}?`</experiment_identifier>  
` `<run_number type="NX_INT">`{Number of run or scan stored `  
`  in this entry}?`</run_number>  
` `<run_cycle type="NX_CHAR">`{Number of the facility cycle in which `  
`  the measurements were made}?`</run_cycle>

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
`   `<status type="NX_CHAR">`{`“`in`”`|`“`out`”`}?`</status>  
`  `</NXattenuator>

`  `<NXvelocity_selector name="selector_name">  
`   `<wavelength type="NX_FLOAT">`{wavelength}`</wavelength>  
`   `<wavelength_spread type="NX_FLOAT">`{% deviation FWHM /Wavelength}?`  
`   `</wavelength_spread>  
`  `</NXvelocity_selector>

`   `<NXguide name="">  
`   `</NXguide>

`  `<NXcrystal name="{Name of crystal monochromator or analyzer}">  
`    `<wavelength type="NX_FLOAT[i]">`{Optimum diffracted wavelength}?`  
`    `</wavelength>  
`  `</NXcrystal>

`  `<NXpolarizer name="{Name of beam polarizer}">  
`  `</NXpolarizer>

`  `<NXflipper name="{Name of flipper}">  
`  `</NXflipper>

`  `<NXaperture name="Name of beamline aperture">  
`   `<distance>`{distance  with respect to sample}`</distance>  
`   `<NXgeometry name="geometry">`{location and shape of aperture}`</NXgeometry>  
`  `</NXaperture>

`  `<NXaperture name="Name of Sample aperture">  
`    `<distance>`{distance  with respect to sample}`</distance>  
`  `</NXaperture>

`  `<NXbeam name="Beam_at_sample">` {characteristics of beam at sample}`  
`  `</NXbeam>

`  `<NXdetector name="{Name of bank of detectors, or multidetector}">  
`   `<SD_distance units = "m" type="NX_FLOAT" >`{sample to detector centre `  
`    distance}`  
`   `</SD_distance>  
`   `<data type="NX_FLOAT[i,j,...]|NX_INT[i,j,...]">`{Data values}?`</data>  
`   `<data_errors type="NX_FLOAT[i,j,...]">`{Data errors}?`</data_errors>  
`   `<detector_number type="NX_INT[i]">`{Identifier for detector}?`  
`   `</detector_number>  
`   `<x_offset type="NX_FLOAT[k+1]">`{pixel offset from the detector center `  
`    in x-direction}?`</x_offset>  
`   `<y_offset type="NX_FLOAT[l+1]">`{pixel offset from the detector center `  
`    in the y-direction}?`</y_offset>  
`   `<NXgeometry name="geometry">`{Position and orientation of detector centre`  
`    with respect to direct beam}?`  
`   `</NXgeometry>  
`    `<x_pixelsize type="NX_FLOAT[i?]">`{Size of each detector pixel. `  
`      If it is scalar all pixels are the same size}?`</x_pixelsize>  
`    `<y_pixelsize type="NX_FLOAT[i?]">`{Size of each detector pixel. `  
`      If it is scalar all pixels are the same size}?`</y_pixelsize>  
`    `<quiet_count type="NX_FLOAT[i?]">`{Detector dark current count.  `  
`      If it is scalar all pixels hav ethe same count}?`</quiet_count>  
`    `<x_pixels type="NX_INT[i]">`{Number of pixels in the x-direction}?`  
`    `</x_pixels>  
`    `<y_pixels type="NX_INT[i]">`{Number of pixels in the y-direction}?`  
`    `</y_pixels>  
`    `<x_beamcentre type="NX_FLOAT[i]">`{position of straight-through beam `  
`     on the detector in x-direction}?`</x_beamcentre>  
`    `<y_beamcentre type="NX_FLOAT[i]">`{position of straight-through beam `  
`     on the detector in y-direction}?`</y_beamcentre>  
`   `</NXdetector>  
`   `<NXbeam_stop name="Name of beam stop">  
`    `<NXgeometry name="geometry">`{shape, orientation and position of the beam stop}`  
`    `</NXgeometry>  
`     `<description type="NX_CHAR">`{ `“`circular`”`|`“`rectangular`”`}?`</description>  
`     `<distance>`{Distance of the beam stop from the sample}`</distance>  
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
`  `“`time`”`|`“`neutrons`”`|`“`charge`”`?`</counting_mode>  
`   `<prescale type="NX_FLOAT">`{Monitor prescale}?`</prescale>  
`   `<quiet_count type="NX_FLOAT">`{Monitor dark current count}?`</quiet_count>  
`   `<preset type="NX_FLOAT32">`{preset for terminating run}?`</preset>  
`   `<data type="NX_INT32">` {Monitor value}`  
`   `</data>  
`  `</NXmonitor>

` `<NXuser name="{Details of the user}">  
`  `<name type="NX_CHAR">`{Name of user responsible for this entry}?`</name>  
`  `<affiliation type="NX_CHAR">`{Affiliation of user}?`</affiliation>  
`  `

<address type="NX_CHAR">
{Address of user}?

</address>
`  `<telephone_number type="NX_CHAR">`{Telephone number of user}?`</telephone_number>  
`  `<fax_number type="NX_CHAR">`{Fax number of user}?`</fax_number>  
`  `<email type="NX_CHAR">`{Email of user}?`</email>  
`  `<facility_user_id type="NX_CHAR">`{facility based unique identifier for `  
`   this person e.g. their identification code on the facility address/contact `  
`   database}?`</facility_user_id>  
` `</NXuser>

` `<NXsample name="{Name of sample}">  
`  `<name type="NX_CHAR">`{descriptive name of sample}?`</name>  
`  `<chemical_formula>`{specified using CIF conventions}`  
`  `</chemical_formula>  
`  `<changer_position type="NX_INT">`{sample changer position}?`  
`  `</changer_position>  
`  `<temperature type="NX_FLOAT[:]" units="K">`{sample temperature ?scannable}`  
`  `</temperature>  
` `</NXsample>

` `<NXdata name="Datablock name">`+`  
`  `<data type="NX_INT32[i,j]" signal="1">` {link to detector counts`  
`   in NXdetector}`  
`  `</data>  
` `</NXdata>  
</NXentry>

</NXroot>
