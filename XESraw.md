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


    <NXroot filename="XES_Example.nxs">
     <NXentry name="entry1"
      <title></title>
     </NXentry>
    </NXroot>
