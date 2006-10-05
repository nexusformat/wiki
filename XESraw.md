---
title: XESraw
permalink: XESraw/
layout: wiki
---

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL:      http://www.nexus.anl.gov/
    Editor:   Stuart Campbell, DLS
    $Id$
    Draft definition of a X-Ray Experimental (Synchrotron) raw Nexus file.
    -->
       <NXentry name="{Name of entry}">
       
            <!--Identification metadata -->
            <title>{Extended title for entry}?</title>
            <experiment_identifier type="NX_CHAR[]">
                {unique identifier for the experiment, defined by the facility, possibly 
                linked to the proposals}?
            </experiment_identifier>
            <run_number type="NX_INT">
                {Number of run or scan stored in this entry}?
            </run_number>
                
            
            <NXinstrument name="{Name of instrument}">
                <name type="NX_CHAR" short_name="{addreviated name of instrument}">
                    {Name of instrument}
                </name>
                <NXsource name="{Name of facility}">
                    <name type="NX_CHAR">
                        {Name of source}?
                    </name>
                    <type type="NX_CHAR">
                        "Spallation Neutron Source"|"Pulsed Reactor Neutron Source"|
                        "Reactor Neutron Source"|"Synchrotron X-ray Source"|
                        "Pulsed Muon Source"|"Rotating Anode X-ray"|Fixed Tube X-ray"
                    </type>
                    <probe type="NX_CHAR">
                        neutron|x-ray|muon|electron?
                    </probe>
                </NXsource>
                
                <!--
                    We would include a different NXpositioner entry for each 'scannable' or
                    motor/variable that we want to record the position of at each scan point.
                -->
                <NXpositioner name="{Name of scannable}">+
                    <value type="NX_FLOAT[n]" units="{}">
                        {value of scannable - need [n] as may be scanned}
                    </value>
                    <controller_record type="NX_CHAR">
                        {Hardware device record, e.g. EPICS process variable, taco/tango ...}?
                    </controller_record>
                </NXpositioner>


                <NXdetector name="{Name of detector}">1+
                    <data type="NX_FLOAT[nx?,ny?,n]|NX_INT[nx?,ny?,n]" signal="1" units="number" axes="{...}"
                          check_sum="{Integral of data as check of data integrity} (NX_INT)?" link="{absolute path to location}">
                        {Data values}
                    </data>
                    <data_error type="NX_FLOAT[i,j,k?,l?]|NX_INT[i,j,k?,l?]" units="number" link="{absolute path to location}">
                        {Data values}
                    </data_error>               
                    <description type="NX_CHAR">
                        {name/manufacturer/model/etc. information}?
                    </description>
                                
                    <type type="NX_CHAR">
                        "He3 gas cylinder"|He3 PSD"|"He3 planar multidetector"| "He3 curved multidetector"| 
                        "multi-tube He3 PSD"|"BF3 gas"|"scintillator"|"fission chamber"|"CCD"|...?
                    </type>             
                    
                    <detector_number type="NX_INT[i]" axis="2" primary="1?" long_name="{Axis label}" link="{absolute path to location}">
                        {Identifier for detector}?
                    </detector_number>
                    <x_offset axis="3" primary="1?" type="NX_FLOAT[k+1]" units="10^-3 meter|10^-2 meter" 
                                long_name="{Axis label}" link="{absolute path to location in NXdetector}">
                        {offset from the detector center in x-direction}?
                    </x_offset>
                    <y_offset axis="4" primary="1?" type="NX_FLOAT[l+1]" units="10^-3 meter|10^-2 meter" 
                                long_name="{Axis label}" link="{absolute path to location in NXdetector}">
                        {offset from the detector center in the y-direction}?
                    </y_offset>
                    <x_pixelsize type="NX_FLOAT[i?]" units="mili*metre">
                        {Size of each detector pixel. If it is scalar all pixels are the same size}?
                    </x_pixelsize>
                    <y_pixelsize type="NX_FLOAT[i?]" units="mili*metre">
                        {Size of each detector pixel. If it is scalar all pixels are the same size}?
                    </y_pixelsize>              
                    
                    
                    <distance type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?">
                        {Distance}?
                    </distance>
                    <polar_angle type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?">
                        {Polar Angle}?
                    </polar_angle>
                    <azimuthal_angle type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?">
                        {Azimuthal Angle}?
                    </azimuthal_angle>
                    <NXgeometry name="">
                        {Position and orientation of detector element}?
                    </NXgeometry>
                    <translation type="NX_FLOAT[2]" units="centimeter">
                        {translation normal to direct beam}?
                    </translation>
                    <solid_angle type="NX_FLOAT[i]" units="steradians">
                        {Solid angle subtended by the detector at the sample}?
                    </solid_angle>  
                            
                </NXdetector>
            
            </NXinstrument>

            <!--
                The data section contains links back to the actual data which is contained within the 
                NXdetector and NXmotor entries.
            -->
            <NXdata name="{Name of data block}">1+
            
                <data NAPIlink="{absolute path to location in NXdetector}" signal="1" 
                      axes="{...}" long_name="{Title of data}">
                    {Data Values}?
                </data>
                <variable type="NX_FLOAT[:]|NX_INT[:]" long_name="{Axis label}" distribution="0|1" first_good="{Index of first good value}" 
                          last_good="{Index of last good value}" NAPIlink="{absolute path to location}">
                    {Dimension scale defining an axis of the data}?
                </variable>     
                        
            </NXdata>

       </NXentry>
