===========================
2014 axes and uncertainties
===========================

(written for NIAC2014_Meeting)

In developing the canSAS standard for storing multidimensional reduced small-angle scattering data, a new method for
identifying the related axes and uncertainties was devised. It is proposed that this will be a good addition to NeXus,
adding flexibility to data file writers while preserving an obvious path from data to axes and uncertainties.

Proposal to describe N-dimensional data (Axes)
----------------------------------------------

(see this from canSAS: )

NeXus needs a robust method to describe and associate the axes of data with arbitrary dimensions in files. Particularly,
the existing methods rely on the concept of HDF dimension scales to describe each of the axes. There is no capability in
NeXus to describe multi-dimensional axes associated with plottable data. The current method of identifying the default
data in NeXus files by adding attributes to datasets does not work in certain important situations. For example, with
the current specifications, a dataset with @signal=1 attribute cannot be linked into a group which already has such a
dataset. Yet, the notion of NXdata to describe the default plot implies the specifications are a property of the NXdata
group, not the component datasets. An additional concern is that the method should allow great flexibility in the naming
of fields. The new method should be backwards compatible with and not spoil existing methods in NeXus. We must also
consider and allow for the common situation when **no axes** are specified.

### Proposition

Define the specifications of the default data and any associated axes using attributes attached to the NXdata group.
Preserve the simplicity of the signal attribute but provide it at the group level. Define how to describe slices of
multi-dimensional axes associated with the default data.

### NXdata Attributes

**All attributes potentially containing multiple values (axes and _indices) are to be written as integer or string
arrays, to avoid string parsing in reading applications.**

**signal**

**signal**: Defines the name of the default dataset. A field of this name *must* exist (either dataset or link to dataset).

**axes**: String array that defines the independent data fields used in the default plot for all the dimensions of the signal field. One entry is provided for every dimension in the signal field. The fields named as values (known as `axes`) of this attribute must exist. An axis slice is specified using the `{axisname}_indices` below.

When no default axis is available for a particular dimension of the plottable data, use a `.` in that position. If there are no axes at all (such as with a stack of images), the `axes` attribute can be omitted.

**{axisname}_indices**: Integer array that defines the indices of the signal field array which need to be used in the `{axisname}` dataset to reference the corresponding axis value. This attribute is to be provided in all situations. However, if the indices attributes are missing, file readers are encouraged to make their best efforts to plot the data.

The implementation of the `{axisname}_indices` attribute is based on the model of "strict writer, liberal reader."

Example Data Structures
#######################

NXroot
  NXentry
    NXdata
      @signal="data"               --> names the default data to be visualized

      @axes="x"                   --> names the default independent data

      @x_indices=0

      data: float[100]            --> the default dependent data

      x: float[100]               --> the default independent data

NXroot
  NXentry
    NXdata
      @signal="data"

      @axes="time", "pressure"

      @pressure_indices=1

      @temperature_indices=1

      @time_indices=0

      data: float[1000, 20]

      pressure: float[20]

      temperature: float[20]

      time: float[1000]

NXroot
  NXentry
    NXdata
      @signal="det"

      @axes="pressure", "tof"

      @pressure_indices=0

      @tof_indices=1

      det: float[100, 100000]

      pressure: float[100]

      tof: float[100000]

NXroot
  NXentry
    NXdata
      @signal="det"

      @axes="x", "y", "tof"

      @tof_indices=2

      @x_indices=0, 1

      @y_indices=0, 1

      det: float[100, 512, 100000]

      tof: float[100000]

      x: float[100, 512]

      y: float[100, 512]

NXroot
  NXentry
    NXdata
      @signal="det1"

      @axes="polar_angle_demand", "frame_number", "."

      @frame_number_indices=1

      @polar_angle_rbv_indices=0, 1

      @time_indices=0, 1

      @polar_angle_demand_indices=0

      polar_angle_rbv: float[50, 5]

      det1: float[50, 5, 1024]

      polar_angle_demand: float[50]

      frame_number: float[5]

      time: float[50, 5]

 Uncertainties

**NOTE:** At NIAC2014, this proposal on uncertainties was not accepted.
*NIAC will see a proposal when experience has been gained with all variations.*
(See this from canSAS.)

In a scientific data file, it is assumed that uncertainty about the value of the data is expressed in an array of the same shape as the data. The uncertainty of a datum may be expressed as a single value or derived from several components.

The way that data uncertainties are described in NeXus data files is inconsistent across the base classes and can be improved while also being generalized. Currently, the name of these uncertainties is most often called "errors," which is incorrect. At best, these are error estimates but actually describe an estimate of one's uncertainty in the data.

While uncertainties are properties of the dataset rather than the containing group, it is difficult in some cases, such as with externally-linked datasets, to attach the attributes directly to the dataset.

### Proposition

The attribute-based scheme used to describe the axes (see above) can be extended to describe the uncertainties. A subgroup can be created to deposit these constituents. It seems that a new base class would be needed for this subgroup.

It is a question for debate whether to attach the attribute to the dataset or the NXdata group. For now, this remains an open question.

### NXdata Attributes

We must consider the description of uncertainty as an attribute of either a dataset or the containing NXdata group. The value of the attribute should be the same in either case.

The name of the uncertainty attribute depends on the context:

- **Parent NXdata group:** `{name}_uncertainty`
- **Dataset:** `uncertainty`

Value:
Defines the name of the dataset with the uncertainty to be used.
This dataset must exist and have the same shape as the signal dataset.

**Examples:**

NXroot
  NXentry
    NXdata
      @signal="data"
      @data_axes="xy"
      @data_uncertainty="esd"
      data: float[300, 300]
      xy: float[300, 300]
      esd: float[300, 300]

NXroot
  NXentry
    NXdata
      @signal="data"
      @data_axes="xy"
      @uncertainty="esd"
      data: float[300, 300]
      xy: float[300, 300]
      esd: float[300, 300]

**Name of the Uncertainty Components Subgroup Attribute:**
The naming of the uncertainty components subgroup attribute depends on the context:

- **Parent NXdata group:**
  `{name}_uncertainty_components`
  - `{name}` is the uncertainty dataset name.
  - `{name}` must exist as a dataset.

- **Dataset:**
  `uncertainty_components` (attached to the uncertainty dataset).

**Value:**
Defines the name of the NXuncertainty subgroup with the uncertainty components.
This subgroup must exist.

**Examples:**

NXroot
  NXentry
    NXdata
      @signal="data"

      @data_axes="xy"

      @data_uncertainty="esd"

      @esd_uncertainty_components="esd_uncertainties"

      data: float[300, 300]

      xy: float[300, 300]

      esd: float[300, 300]

      esd_uncertainties: NXuncertainty

        electronic: float[300, 300]

          @basis="Johnson noise"

        counting_statistics: float[300, 300]

          @basis="shot noise"

        secondary_standard: float[300, 300]

          @basis="esd"

NXroot
  NXentry
    NXdata
      @signal="data"

      @data_axes="xy"

      data: float[300, 300]

      xy: float[300, 300]

      esd: float[300, 300]

      @uncertainty="esd"

      @uncertainty_components="esd_uncertainties"

      esd_uncertainties: NXuncertainty

        electronic: float[300, 300]

          @basis="Johnson noise"

        counting_statistics: float[300, 300]

          @basis="shot noise"

        secondary_standard: float[300, 300]

          @basis="esd"


Topics for Discussion on this
#############################
Proposal These are some of the topics to be considered when evaluating
this proposal.

1. There are known advantages and disadvantages to the decision to store attributes on the parent group or on the field itself.

2. Attributes stored on the field will transfer when the field is copied or linked.

3. It may not be possible to add or modify a field attribute which is linked due to conflicts or write permissions.

4. The uncertainty field (and possible complex uncertainties) need to be considered when copying or linking.

5. Uncertainty is not a popular word to spell. Yet errors is not correct in this context.

### \*NXuncertainty\* Base Class TODO: need to write this section

