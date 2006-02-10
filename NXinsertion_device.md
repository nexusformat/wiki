---
title: NXinsertion device
permalink: NXinsertion_device/
layout: wiki
---

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL:     http://www.nexus.anl.gov/classes/xml/NXinsertion_device.xml
    Editor:  NIAC
    $Id: NXinsertion_device.xml,v 1.1 2006/02/10 14:01:58 sic78 Exp $

    This is the description for an insertion device.
    -->
    <NXinsertion_device name="{Name of insertion device}">
        <type type="NX_CHAR">
            {"undulator"|"wiggler"|...}?
        </type>
        <gap type="NX_FLOAT" units="milimetre">
            {gap}?
        </gap>
        <taper type="NX_FLOAT" units="milimetre">
            {taper}?
        </taper>
        <phase type="NX_FLOAT" units="degrees">
            {phase}?
        </phase>
        <poles type="NX_INT">
            {number of poles}?
        </poles>
        <length type="NX_FLOAT" units="mili*metre">
            {length of insertion device}?
        </length>
        <power type="NX_FLOAT">
            {total power delivered by insertion device}?
        </power>
        <energy type="NX_FLOAT">
            {energy of peak}?
        </energy>
        <bandwidth type="NX_FLOAT">
            {bandwidth of peak energy}?
        </bandwidth>
        <harmonic type="NX_INT">
            {harmonic of peak}?
        </harmonic>
        <spectrum type="NXdata">
            {spectrum of insertion device}?
        </spectrum>
        <NXgeometry name="">
            {"Engineering" position of insertion device}?
        </NXgeometry>
    </NXinsertion_device>
