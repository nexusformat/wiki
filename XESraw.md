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
                </NXpositioner>

                <NXdetector name="{Name of detector}">1+
                    <data type="NX_FLOAT[nx?,ny?,n]|NX_INT[nx?,ny?,n]" signal="1" units="number" axes="{...}"
                          check_sum="{Integral of data as check of data integrity} (NX_INT)?" link="{absolute path to location}">
                        {Data values}
                    </data>
                    <description type="NX_CHAR">
                        {name/manufacturer/model/etc. information}?
                    </description>
                                
                    <type type="NX_CHAR">
                        "He3 gas cylinder"|He3 PSD"|"He3 planar multidetector"| "He3 curved multidetector"| 
                        "multi-tube He3 PSD"|"BF3 gas"|"scintillator"|"fission chamber"|"CCD"|...?
                    </type>                 
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
                          last_good="{Index of last good value}" NAPIlink="{absolute path to location in NXpositioner}">
                    {Dimension scale defining an axis of the data}?
                </variable>     
                        
            </NXdata>

       </NXentry>

Example:


    <NXroot>
        <NXentry name="{Entry name}">
            <title>{Extended title for entry}</title>
            
            <NXinstrument name="I18">
                    <name>"I18"</name>
                    <NXsource name="source">
                        <name>"Diamond Light Source"</name>
                        <type>"Synchrotron X-ray Source"</type>
                        <probe>"x-ray"</probe>
                    </NXsource>
                    <NXpositioner name="energy">
                        <energy>[3001.0, 3002.0, 3003.0]</energy>
                    </NXpositioner>
                    <NXpositioner name="time">
                        <time>[1.22, 2.34, 3.53]</time>
                    </NXpositioner>
                    <NXdetector name="detector1">
                        <description>"Ortec C-TRAIN"</description>
                        <type>"Counter Timer"</type>
                        <data>[203.0, 245.0, 233.0]</data>
                    </NXdetector>
                    <NXdetector name="detector2">
                        <description>"Quantum 315"</description>
                        <type>"CCD"</type>
                        <data>{a data array with dimensions[3, nx, ny]}</data>
                    </NXdetector>
            </NXinstrument>
            
            <NXdata name="detector1">
                <data>{Link to detector1 counts}</data>
                <energy axis=1 primary=1>{Link to values in NXpositioner}</energy>
                <time axis=1 primary=2>{Link to values in NXpositioner}</time>
            </NXdata>
                    <NXdata name="detector2">
                <data>{Link to detector2 counts}</data>
                <energy axis=1 primary=1>{Link to values in NXpositioner}</energy>
                <time axis=1 primary=2>{Link to values in NXpositioner}</time>
            </NXdata>
            
        </NXentry>
    </NXroot>
