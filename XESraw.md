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
    Draft example of a X-Ray Experimental (Synchrotron) raw Nexus file.
    -->

    <NXroot>
        <NXentry name="Entry1">
            <title>"Example Data File"</title>
            
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
