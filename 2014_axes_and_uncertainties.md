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

Proposal to describe multi-dimensional data (Axes)
--------------------------------------------------

TODO: write this section

(see this from canSAS:
<http://www.cansas.org/formats/canSAS2012/1.0/doc/framework.html>)

NeXus needs a robust method to describe and associate the axes of
multi-dimensional data in data files. Particularly, the existing methods
rely on the concept of HDF dimension scales to describe each of the
axes. There is no capability in NeXus to describe multi-dimensional axes
associated with plottable data.

The current method of identifying the default data in NeXus files by
adding attributes to datasets does not work in certain important
situations. For example, with the current specifications, a dataset with
@signal=1 attribute can not be linked into a group which already has
such a dataset. Yet, the notion of NXdata to describe the default plot
implies the specifications are a property of the NXdata group, not the
component datasets.

An additional concern is that the method should allow great flexibility
in the naming of fields.

The new method should be backwards compatible with and not spoil
existing methods in NeXus.

One additional interest is that the new method be capable of describing
alternative views of data in the NXdata group, not just the default
data.

### Proposition

Define the specifications of the default data and any associated axes
using attributes attached to the NXdata group.

Preserve the simplicity of the signal attribute but provide it at the
group level.

Define how to describe slices of multi-dimensional axes associated with
the default data.

### NXdata Attributes

signal:

`   Defines the name of the default dataset.`  
`   A field of this name *must* exist.`  
`   (either dataset or link to dataset)`

{name}\_axes:

`   Defines the independent data fields supporting the {name} field.`  
`   The {name} field *must* exist.`  
`   The field(s) named as values (known as `“`axes`”`) of this attribute must exist.`  
`   The axes shapes must be compatible with {name}.`  
`   A axis slice may be specified through the use of subscripts to indicate`  
`   which indices should be used.`  
`   `  
`   For example, if {name} has shape [10,100,512,3],`  
`   and {name}_axes is `“`thing1,`` ``thing2,`` ``thing3`”`,`  
`   with shapes [10], [100,512], [3],`  
`   then these criteria are satisfied.`

### Example data structures

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`data`”`  --> *names* the default data to be visualized`  
`       @data_axes=`“`x`”`  --> *names* the default independent data`  
`       data: float[100]  --> the default dependent data`  
`       x: float[100]  --> the default independent data`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`I`”  
`       @I_axes=`“`Q[1,2]`”  
`       I: float[100, 512]`  
`       Q: float[3, 100, 512]`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`counts`”  
`       @counts_axes=`“`polar_angle[1]`”  
`       counts: float[100*512]`  
`       polar_angle: float[3,100*512]`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`det`”  
`       @det_axes=`“`tof,pressure`”  
`       det: float[100000,100]`  
`       pressure: float[100]`  
`       tof: float[100000]`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`det`”  
`       @det_axes=`“`tof,xy`”  
`       det: float[100000,100,512]`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`counts`”  
`       @counts_axes=`“`polar_angle_demand,frame_number,?`”  
`       polar_angle_rbv: [50,5]`  
`       counts[50,5,1024]`  
`       polar_angle_demand: [50]`  
`       frame_number: [5]`  
`       time: [50,5]`

Uncertainties
-------------

TODO: finish writing this section

In a scientific data file, it is assumed that uncertainty about the
value of the data is expressed in an array of the same shape as the
data. The uncertainty of a datum may be expressed in a single value or
as derived from several components.

Examples

-   <http://www.cansas.org/formats/canSAS2012/1.0/doc/examples.html#d-image-i-q-with-uncertainty>
-   <http://www.cansas.org/formats/canSAS2012/1.0/doc/examples.html#d-sas-data-in-a-time-series-i-t-q-t-idev-t-q-t>
-   <http://www.cansas.org/formats/canSAS2012/1.0/doc/examples.html#representing-uncertainty-components>

