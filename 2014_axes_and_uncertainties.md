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

We must also consider and allow for the common situation when **no
axes** are specified.

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

axes: {name}\_axes:

`   Defines the independent data fields supporting the {name} field.`  
`   If there is only one data field to be plotted (the other data field(s)`  
`   are axes), then it is acceptable to use the shorter `*`axes`*` attribute.`

`   The {name} field *must* exist.`  
`   The field(s) named as values (known as `“`axes`”`) of this attribute must exist.`  
`   The axes shapes must be compatible with {name}.`  
`   A axis slice may be specified through the use of subscripts to indicate`  
`   which indices should be used.`  
`   `  
`   When no axis is to be used for a particular index of the plottable data,`  
`   use a `“`.`”` in that position.  An example below demonstrates this.`  
`   If there are no axes at all (such as with a stack of images), the`  
`   `*`axes`*` attribute can be omitted.`  
`   `  
`   For example, if {name} has shape [10,100,512,3],`  
`   and {name}_axes is `“`thing1,`` ``thing2,`` ``thing3`”`,`  
`   with shapes [10], [100,512], [3],`  
`   then these criteria are satisfied.`

{axisname}\_indices:

`   Defines the list of integer values which are indices of the signal field array`  
`   (the field named as the value of the signal attribute)`  
`   to which this axis applies.  This attribute is necessary to resolve`  
`   ambiguity and to declare possible alternative axes for the signal field array.`  
`   `  
`   This attribute is to be used in all but the most trivial situations.`  
`   However, if the indices attributes are missing, file readers are encouraged`  
`   to make their best efforts to plot the data.  Thus the implementation`  
`   of the indices attribute is based on the model of`  
`   `“`strict`` ``writer,`` ``tolerant`` ``reader`”`.`  
`   `  
`   If the complexity of representing alternative axes creates conflicts,`  
`   then define the alternatives in additional NXdata groups and use links`  
`   to avoid replicating the data.`

`   This is a replacement for the `“`axis=`”` attribute method of identifying`  
`   the dimension scales for plotting.`

### Example data structures

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`data`”`  --> *names* the default data to be visualized`  
`       @axes=`“`x`”`  --> *names* the default independent data`  
`       data: float[100]  --> the default dependent data`  
`       x: float[100]  --> the default independent data`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`I`”  
`       @I_axes=`“`Q`”  
`       @Q_indices=`“`1,2`”`  --> use the last two indices of the `“`Q`”` field to plot the `“`I`”` field`  
`       I: float[100, 512]`  
`       Q: float[3, 100, 512]`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`detector1`”  
`       @axes=`“`Q`”  
`       @Q_indices=`“`1`”  
`       detector1: float[100*512]`  
`       Q: float[3,100*512]`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`data`”  
`       @axes=`“`time,pressure`”  
`       @pressure_indices=`“`1`”  
`       @time_indices=`“`0`”  
`       @temperature_indices=`“`1`”  
`       data: float[1000,20]`  
`       pressure: float[20]`  
`       temperature: float[20]`  
`       time: float[1000]`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`det`”  
`       @axes=`“`pressure,tof`”  
`       det: float[100,100000]`  
`       pressure: float[100]`  
`       tof: float[100000]`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`det`”  
`       @axes=`“`xy,tof`”  
`       @tof_indices=`“`2`”  
`       @xy_indices=`“`0,1`”  
`       det: float[100,512,100000]`  
`       tof: float[100000]`  
`       xy: float[100,512]`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`det1`”  
`       @det1_axes=`“`polar_angle_demand,frame_number,.`”  
`       @polar_angle_rbv_axes=`“`polar_angle_demand,.`”  
`       @frame_number_indices=`“`1`”  
`       @polar_angle_demand_indices=`“`0,.`”  
`       polar_angle_rbv: [50,5]`  
`       det1: [50,5,1024]`  
`       det2: [50,5,1024]`  
`       polar_angle_demand: [50]`  
`       frame_number: [5]`  
`       time: [50,5]`

Uncertainties
-------------

(see this from canSAS:
<http://www.cansas.org/formats/canSAS2012/1.0/doc/examples.html#representing-uncertainty-components>)

In a scientific data file, it is assumed that uncertainty about the
value of the data is expressed in an array of the same shape as the
data. The uncertainty of a datum may be expressed in a single value or
as derived from several components.

The way that data uncertainties are described in NeXus data files is
inconsistent across the base classes and can be improved while also
being generalized. Currently, the name of these uncertainties is most
often called “errors” which is incorrect. At best, these are error
estimates but actually describe an estimate of one's uncertainty in the
data.

While uncertainties are properties of the dataset rather than the
containing group, it is difficult in some cases such as
externally-linked datasets, to attach the attributes directly to the
dataset.

### Proposition

The attribute-based scheme used to describe the axes (see above) can be
extended to describe the uncertainties. A subgroup can be created to
deposit these constituents. It seems that a new base class would be
needed for this subgroup.

It is a question for debate whether to attach the attribute to the
dataset or the NXdata group. We leave that open for now.

### NXdata Attributes

We must consider the description of uncertainty as an attribute of
either a dataset or the containing NXdata group. The value of the
attribute should be the same in either case.

Name of the uncertainty attribute depends on the context:

-   parent NXdata group: {name}\_uncertainty
-   dataset: uncertainty

Value:

`   Defines the name of the dataset with the uncertainty to be used.`  
`   This dataset must exist and have the same shape as the signal dataset.`

*Examples*

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`data`”  
`       @data_axes=`“`xy`”  
`       @data_uncertainty=`“`esd`”  
`       data: float[300, 300]`  
`       xy: float[300, 300]`  
`       esd: float[300, 300]`

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`data`”  
`       @data_axes=`“`xy`”  
`       data: float[300, 300]`  
`         @uncertainty=`“`esd`”  
`       xy: float[300, 300]`  
`       esd: float[300, 300]`

Name of the uncertainty components subgroup attribute depends on the
context:

-   parent NXdata group: “{name}\_uncertainty\_components” where {name}
    is the uncertainty dataset
    -   {name} must exist as a dataset
-   dataset: “uncertainty\_components” attached to uncertainty dataset

Value:

`   Defines the name of the NXuncertainty subgroup with the uncertainty components.`  
`   This subgroup must exist.`

*Examples*

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`data`”  
`       @data_axes=`“`xy`”  
`       @data_uncertainty=`“`esd`”  
`       @esd_uncertainty_components=`“`esd_uncertainties`”  
`       data: float[300, 300]`  
`       xy: float[300, 300]`  
`       esd: float[300, 300]`  
`       esd_uncertainties:NXuncertainty`  
`          electronic : float[300, 300]`  
`             @basis=`“`Johnson`` ``noise`”  
`          counting_statistics: float[300, 300]`  
`             @basis=`“`shot`` ``noise`”  
`          secondary_standard: float[300, 300]`  
`             @basis=`“`esd`”

` NXroot`  
`   NXentry`  
`     NXdata`  
`       @signal=`“`data`”  
`       @data_axes=`“`xy`”  
`       data: float[300, 300]`  
`         @uncertainty=`“`esd`”  
`       xy: float[300, 300]`  
`       esd: float[300, 300]`  
`         @uncertainty_components=`“`esd_uncertainties`”  
`       esd_uncertainties:NXuncertainty`  
`          electronic : float[300, 300]`  
`             @basis=`“`Johnson`` ``noise`”  
`          counting_statistics: float[300, 300]`  
`             @basis=`“`shot`` ``noise`”  
`          secondary_standard: float[300, 300]`  
`             @basis=`“`esd`”

### Topics for Discussion on this Proposal

These are some of the topics to be considered when evaluating this
proposal.

1.  . There are known advantages and disadvantages to the decision to
    store attributes on the parent group or on the field itself.
    1.  . attributes stored on the field will transfer when the field is
        copied or linked
    2.  . It may not be possible to add or modify a field attribute
        which is linked due to conflicts or write permissions
2.  . The uncertainty field (and possible complex uncertainties) need to
    be considered when copying or linking
3.  . “Uncertainty” is not a popular word to spell. Yet “errors” is not
    correct in this context.

### *NXuncertainty* Base Class

TODO: need to write this section
