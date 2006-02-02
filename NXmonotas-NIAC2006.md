---
title: NXmonotas-NIAC2006
permalink: NXmonotas-NIAC2006/
layout: wiki
---

<COMMENT !--
 URL:     http://www.nexus.anl.gov/classes/xml/NXmonotas.xml
 Editor:  NIAC
 NIAC Version: 0.1
 $Id: monotas.docbook,v 1.1 2005/06/14 16:50:35 pfp Exp $
 Template of a generic NeXus file containing neutron or x-ray triple-axis data.-->  
<NXentry name="{Name of entry}">  
` `

<title />
` `<definition URL="http://www.nexus.anl.gov/instruments/xml/NXmonotas.xml"
      version="1.0">  
`   NXmonotas`  
` `</definition>  
` `<start_time />  
` `<NXsample name="sample">  
`   `<name />  
`   `<unit_cell />  
`   `<orientation_matrix />  
`   `<sample_orientation />  
`   `<plane_vector_0 type="NX_FLOAT32[3]">  
`     {Reciprocal space vector of primary reflection in the scattering plane}`  
`   `</plane_vector_0>  
`   `<plane_vector_1 type="NX_FLOAT32[3]">  
`     {Reciprocal space vector of secondary reflection in the scattering plane}`  
`   `</plane_vector_1>  
`   `<polar_angle units="degree" type="NX_FLOAT32[:,np]">  
`     {Polar angle of the sample with respect to the beam incident on the monochromator}`  
`   `</polar_angle>  
`   `<azimuthal_angle units="degree" type="NX_FLOAT32">  
`     {Azimuthal angle of the sample with respect to the beam incident on the`  
`     monochromator}`  
`   `</azimuthal_angle>  
`   `<rotation_angle units="degree" type="NX_FLOAT32[:,np]">  
`     {Rotation angle of the sample}`  
`   `</rotation_angle>  
`   `<Q type="NX_Float32[nd,np]">  
`    {Magnitude of momemtum transfer vector}?`  
`    `</Q>  
`   `<Qh type="NX_FLOAT32[nd,np]">  
`     {Reciprocal space component of scan}?`  
`   `</Qh>  
`   `<Qk type="NX_FLOAT32[nd,np]">  
`     {Reciprocal space component of scan}?`  
`   `</Qk>  
`   `<Ql type="NX_FLOAT32[nd,np]">  
`     {Reciprocal space component of scan}?`  
`   `</Ql>  
`   `<energy_transfer units="meV" type="NX_FLOAT32[nd,np]">  
`     {Energy transfer of scan}`  
`   `</energy_transfer>  
` `</NXsample>  
` `<NXinstrument name="{Name of instrument}">  
`   `<NXcollimator name="premonochromator_collimator">  
`     `<type />  
`     `<soller_angle />  
`   ?`</NXcollimator>  
`   `<NXfilter name="premonochromator_filter">  
`     `<description />  
`   ?`</NXfilter>  
`   `<NXcrystal name="monochromator">  
`     `<type />  
`     `<energy units="meV" type="NX_FLOAT32[np]">  
`       {Optimum diffracted energy}`  
`     `</energy>  
`     `<d_spacing units="Angstrom" type="NX_FLOAT32">  
`       {The planar spacing of the nominal reflection}`  
`     `</d_spacing>  
`     `<rotation_angle units="degree" type="NX_FLOAT32[np]">  
`       {Rotation angle of the monochromator}`  
`     `</rotation_angle>  
`   `</NXcrystal>  
`   `<NXcollimator name="presample_collimator">`?`</NXcollimator>  
`   `<NXfilter name="presample_filter">`?`</NXfilter>  
`   `<NXcollimator name="preanalyzer_collimator">`?`</NXcollimator>  
`   `<NXfilter name="preanalyzer_filter">`?`</NXfilter>  
`   `<NXcrystal name="analyzer">  
`     `<type />  
`     `<energy type="NX_FLOAT32[nd,np]" />  
`       {Optimum diffracted energy for each analyzer}`  
`     `</energy>  
`     `<d_spacing />  
`     `<rotation_angle type="NX_FLOAT32[nd,np]" />  
`   `</NXcrystal>  
`   `<NXcollimator name="predetector_collimator">`?`</NXcollimator>  
`   `<NXdetector name="detector">  
`     `<counts signal="1" axes="energy_transfer|Qh|Qk|Ql" type="NX_INT32[:]">  
`       {Integer counts}`  
`     `</counts>  
`     `<polar_angle units="degree" type="NX_FLOAT32[:]">  
`       {Polar angle of the detector with respect to the beam incident on the`  
`       monochromator}`  
`     `</polar_angle>  
`     `<azimuthal_angle units="degree" type="NX_FLOAT32">  
`       {Azimuthal angle of the detector with respect to the beam incident on`  
`       the analyzer}`  
`     `</azimuthal_angle>  
`   `</NXdetector>  
` `</NXinstrument>  
` `<NXmonitor name="monitor">  
`   `<mode />  
`   `<preset />  
`   `<data />  
` `</NXmonitor>  
` `<NXdata name="data">  
`   `<Qh NAPIlink="NXentry/NXsample/Qh" />  
`   `<Qk NAPIlink="NXentry/NXsample/Qk" />  
`   `<Ql NAPIlink="NXentry/NXsample/Ql" />  
`   `<energy_transfer NAPIlink="NXentry/NXsample/energy_transfer" />  
`   `<counts NAPIlink="NXentry/NXinstrument/detector/counts" />  
`   `<energy NAPIlink="NXentry/NXinstrument/analyzer/energy" />  
` `</NXdata>  
</NXentry>
