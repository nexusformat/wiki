---
title: NXmirror
permalink: NXmirror/
layout: wiki
---

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL:     http://www.nexus.anl.gov/classes/xml/NXmirror.xml
    Editor:  
    $Id: NXmirror.xml,v 1.2 2005/07/19 04:10:26 rio Exp $

    Template of a beamline supermirror.

    -->
    <NXmirror name="{Name of supermirror}">
        <NXgeometry name="">
            {}
        </NXgeometry>
        <description type="NX_CHAR">
            {}
        </description>
        <incident_angle type="NX_FLOAT">
            {}
        </incident_angle>
        <reflectivity type="NXdata">
            {Reflectivity as function of wavelength}
        </reflectivity>
        <bend_angle_x type="NX_FLOAT">
            {}
        </bend_angle_x>
        <bend_angle_y type="NX_FLOAT">
            {}
        </bend_angle_y>
        <interior_atmosphere type="NX_CHAR">
            "vacuum"|"helium"|"argon"
        </interior_atmosphere>
        <external_material type="NX_CHAR">
            {external material outside substrate}
        </external_material>
        <m_value type="NX_FLOAT">
            {}
        </m_value>
        <substrate_material type="NX_CHAR">
            {}
        </substrate_material>
        <substrate_thickness type="NX_FLOAT">
            {}
        </substrate_thickness>
        <coating_material type="NX_CHAR">
            {}
        </coating_material>
        <substrate_roughness type="NX_FLOAT">
            {}
        </substrate_roughness>
        <coating_roughness type="NX_FLOAT">
            {}
        </coating_roughness>
    </NXmirror>
