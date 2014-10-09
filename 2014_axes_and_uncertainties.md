---
title: 2014 axes and uncertainties
permalink: 2014_axes_and_uncertainties/
layout: wiki
---

(written for [NIAC2014\_Meeting](NIAC2014_Meeting "wikilink"))

In developing the [canSAS standard for storing multidimensional reduced
small-angle scattering
data](http://www.cansas.org/formats/canSAS2012/1.0/doc/), a new method
for identifying the [related
axes](http://www.cansas.org/formats/canSAS2012/1.0/doc/implementation.html#algorithm-to-identify-values-given-a-set-of-indices-on-the-i-data)
and
[uncertainties](http://www.cansas.org/formats/canSAS2012/1.0/doc/framework.html#index-5)
was devised. It is proposed that this will be a good addition to NeXus,
adding flexibility to data file writers while preserving an obvious path
from data to axes and uncertainties.

Axes
----

-tba-

Uncertainties
-------------

In a scientific data file, it is assumed that uncertainty about the
value of the data is expressed in an array of the same shape as the
data. The uncertainty of a datum may be expressed in a single value or
as derived from several components.

Examples

-   <http://www.cansas.org/formats/canSAS2012/1.0/doc/examples.html#d-image-i-q-with-uncertainty>
-   <http://www.cansas.org/formats/canSAS2012/1.0/doc/examples.html#d-sas-data-in-a-time-series-i-t-q-t-idev-t-q-t>
-   <http://www.cansas.org/formats/canSAS2012/1.0/doc/examples.html#representing-uncertainty-components>

