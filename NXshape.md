---
title: NXshape
permalink: NXshape/
layout: wiki
---

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL:     http://www.nexus.anl.gov/classes/xml/NXshape.xml
    Editor:  NIAC
    $Id: NXshape.xml,v 1.2 2005/07/19 04:10:26 rio Exp $

    This is the description of the general shape and size of a 
    component, which may be made up of "numobj" separate elements - 
    it is used by the NXgeometry.xml class
    -->
    <NXshape name="{name of shape}">
        <shape type="NX_CHAR">
            {"nxcylinder", "nxbox", "nxsphere", ...}?
        </shape>
        <size type="NX_FLOAT[numobj,nshapepar]" units="meter">
            {physical extent of the object along its local axes (after
            NXorientation) with the center of mass at the local origin (after
            NXtranslate).}{The meaning and location of these axes will vary
            according to the value of the "shape" variable. nshapepar defines how
            many parameters. For the "nxcylinder" type the paramters are
            (diameter,height). For the "nxbox" type the parameters are
            (length,width,height). For the "nxsphere" type the parameters are
            (diameter).}?
        </size>
    </NXshape>
