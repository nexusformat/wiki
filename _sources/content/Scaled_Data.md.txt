---
title: Scaled Data
permalink: Scaled_Data.html
layout: wiki
---
Scaled Data
===========

This suggestion is one of the outcomes of the NeXus for Synchrotrons
Workshop at PSI: <http://lns00.psi.ch/nexus2010>

The Suggestion
--------------

NeXus STRONGLY suggests to store data as arrays of physical values in C
storage order. However, for cases where this is not possible or would
cause an efficiency concern when writing allow to store raw data. Such
data must be annotated with additional attributes as described below in
order to allow reading software to reconstruct the true physical value.

The Reasoning
-------------

The data rates possible at synchrotron facilities and the new pixel
detectors test current computing technology to their limits. There may
not be enough time to scale or convert data on the fly before writing to
disk. In some occasions significant space savings can be obtained by
storing data as short integers and scaling them to the desired floating
point values.

In the formulas below Vtrue denotes the true value of the data item,
Vraw the one which is stored in the data element on file. The attributes
are:

-   transform: This is the indicator that a transformation of the Vraw
    data is necessary. Transform can have one the following values:
    -   offset: Vtrue = Vraw + offset
    -   scaling: Vtrue = Vraw \* scaling
    -   scaling\_offset: both an offset and scaling is applied. Vtrue =
        Vraw\*scaling + offset
    -   sqrt\_scaled: Vtrue = (Vraw/scaling)\*(Vraw/scaling)
    -   logarithmic\_scaled: Vtrue = (Vraw/scaling)\*\*10
    -   polynomial: Vtrue = p1 + p2\*Vraw + p3\*Vraw\*Vraw +
        p4\*Vraw\*Vraw\*Vraw ....
-   offset: The offset to apply
-   scaling: The scale factor to apply
-   direction: a komma separated list of length ndim which specifies for
    each dimension if it is increasing or decreasing. If this attribute
    is missing, increasing is implied.
-   precedence: a komma separated list of length ndim which gives the
    rank order in which array indexes change with respect to other
    indexes. A precedence of 1 denotes the fastest changing index. If
    this attribute is missing, C storage order is implied.
-   coefficients, a komma separated list of the polynomial coefficients
    to use for a polynomial transform

Update 01/2015
--------------

There was some discussion on this at NIAC 2010 and 2012. IMHO, the
result was that all fixed schemes fall over in some point when people
come up with new scaling schemes. It was decided to devise a NXformula
base class to solve this problem. There was some further discussion on
scaling in 2014 in the mailing list and on the teleconferences. At NIAC
2014 it was decided to accept a NXformula base class as suggested by Ben
Watts as an experimental feature.
