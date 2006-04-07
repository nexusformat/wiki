---
title: NXpositioner
permalink: NXpositioner/
layout: wiki
---

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL:     http://www.nexus.anl.gov/classes/xml/NXpositioner.xml
    Editor:  NIAC

    This is the description for a generic positioner.
    -->
    <NXpositioner name="{Name of positioner}">
            <value type="NX_FLOAT[n]" units="{}">
                    {value of positioner - need [n] as may be scanned}
            </value>
            <controller_record type="NX_CHAR">
                    {Hardware device record, e.g. EPICS process variable, taco/tango ...}
            </controller_record>
    </NXpositioner>
