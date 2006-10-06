---
title: Design
permalink: Design/
layout: wiki
---

The structure of NeXus files is extremely flexible, allowing the storage
both of simple data sets, e.g., a single data array and its axes, and
also of highly complex data, e.g., the simulation results of an entire
multi-component instrument. This flexibility is achieved through a
hierarchical structure, with related data items collected together into
groups, making NeXus files easy to navigate, even without any
documentation. NeXus files are self-describing, and should be easy to
understand, at least by those familiar with the experimental technique.

The logical design is distinct from the underlying format used to store
the NeXus file on disk, which are written using the NeXus Application
Program Interface (API). Refer to the [ API
section](Application_Program_Interface "wikilink") for more details.

NeXus Objects
-------------

NeXus data files contain two types of elementary object: data items and
data groups. In addition, metadata required to describe a data item,
e.g. its physical units, can be attached to the data as data attributes.

### Data Items

Data items contain the essential information stored in a NeXus file.
They can be scalar values or multidimensional arrays of a variety of
sizes (1-byte, 2-byte, 4-byte, 8-byte) and types (integers, floats,
characters). The items may store both experimental results (counts,
detector angles, etc), and other information associated with the
experiment (start and end times, user names, etc). Data items are
identified by their names, which must be unique within the group in
which they are stored.

### Data Attributes

Attributes are extra (meta-)information that are associated with
particular data items. They are used to annotate the data, e.g. with
physical units or calibration offsets, and may be scalar numbers or
character strings. In addition, NeXus uses attributes to identify
plottable data and their axes, etc. Finally, NeXus files themselves have
global attributes that identify the NeXus version, file creation time,
etc.. Attributes are identified by their names, which must be unique in
each data item.

### Data Groups

NeXus files consist of data groups, which contain data items and/or
other groups to form a hierarchical structure. This hierarchy is
designed to make it easy to navigate a NeXus file by storing related
data items together. Data groups are identified both by a name, which
must be unique within a particular group, and a class. There can be
multiple groups with the same class.

NeXus Classes
-------------

Data groups often describe objects in the experiment (monitors,
detectors, monochromators, etc.), so that the contents (both data items
and/or other data groups) comprise the properties of that object. NeXus
has defined a set of standard objects, or classes, out of which a NeXus
file can be constructed. Each data group is therefore identified by a
name and a class. The group class, which always has “NX” as a prefix,
defines the type of object and the properties that it can contain,
whereas the group name defines a unique instance of that class. These
classes are defined in XML using the [NeXus MetaDTD
format](Metaformat "wikilink").

Not all classes define physical objects. Some refer to logical groupings
of experimental information, such as plottable data, sample environment
logs, beam profiles, etc.

The following table shows the hierarchy of a standard NeXus file, and
where groups of a particular class are located. There can be multiple
instances of each class. On the other hand, a typical NeXus file will
only contain a small subset of the possible classes.

Click on any of the class names below for a more detailed description
compiled from the latest XML files.

[NXroot](NXroot "wikilink"):The root level of a NeXus file.  

:;[NXentry](NXentry "wikilink"):All the data, including instrument and
sample descriptions, which logically make up a single scan or
measurement. At many facilities, this corresponds to the entity that is
defined by a single run number, which could be used to name the NXentry
group. There can be many NXentry groups in each NeXus file.

::;[NXinstrument](NXinstrument "wikilink"):The information needed to
describe the instrument. This group contains other groups that describe
instrument components e.g. choppers, collimators, detectors.

:::[NXaperture](NXaperture "wikilink")

:::[NXattenuator](NXattenuator "wikilink")

:::[NXbeam\_stop](NXbeam_stop "wikilink")

:::[NXbending\_magnet](NXbending_magnet "wikilink")

:::[NXcollimator](NXcollimator "wikilink")

:::[NXcrystal](NXcrystal "wikilink")

:::[NXdetector](NXdetector "wikilink")

:::[NXdisk\_chopper](NXdisk_chopper "wikilink")

:::[NXfermi\_chopper](NXfermi_chopper "wikilink")

:::[NXfilter](NXfilter "wikilink")

:::[NXflipper](NXflipper "wikilink")

:::[NXguide](NXguide "wikilink")

:::[NXinsertion\_device](NXinsertion_device "wikilink")

:::[NXmirror](NXmirror "wikilink")

:::[NXmoderator](NXmoderator "wikilink")

:::[NXmonochromator](NXmonochromator "wikilink")

:::NXpolarizer

:::[NXpositioner](NXpositioner "wikilink")

:::[NXsource](NXsource "wikilink")

:::[NXvelocity\_selector](NXvelocity_selector "wikilink")

::;[NXsample](NXsample "wikilink"):The information needed to define the
physical state of the sample during the scan <i>e.g.</i> temperature,
magnetic field, crystal mosaic.

::;[NXmonitor](NXmonitor "wikilink"):Monitor data, i.e., counts,
integrals, *etc*.

::;[NXdata](NXdata "wikilink"):The data to be plotted i.e. a single data
set comprising the measurements along with the data errors, and the
default axis scales and labels required to plot the data. There can be
more than one [NXentry](NXentry "wikilink"), e.g., if there are several
detector banks producing plottable data.

::;[NXevent\_data](NXevent_data "wikilink"):Event-based data, i.e. a
data set in which each count is recorded as a separate data event. This
form might be chosen when the data are too sparse to be stored
efficiently in histograms. Normally, such data will have to be converted
to a regular [NXdata](NXdata "wikilink") group before it can be
analyzed.

::;[NXuser](NXuser "wikilink"):Details of a user, i.e., name,
affiliation, email address, *etc*.

::;[NXprocess](NXprocess "wikilink"):Group used to store details of how
the data have been processed.

::;[NXcharacterizations](NXcharacterizations "wikilink"):Information
required for the analysis of this [NXentry](NXentry "wikilink"), *e.g.*
identification of empty can runs, vanadium runs, *etc.* In addition to
these classes, which appear in the locations shown above, the following
groups can be added to any group in a NeXus file.

:;[NXlog](NXlog "wikilink"):This group contains any logged information,
*i.e.*, information monitored during the run. It comprises the logged
values and the times at which they were measured as elapsed time since a
specified starting time.

:;[NXnote](NXnote "wikilink"):This is a generic group designed to hold
annotations or images stored in order to describe the experiment.

:;[NXbeam](NXbeam "wikilink"):This group records the state of the
neutron or X-ray beam at any location. It could be referenced by
instrument components within the NXinstrument group or by the NXsample
group. In storing the results of instrument simulations in which it is
useful to specify the beam profile, time distribution etc., at various
stages down the beamline. Otherwise, its most likely use is in the
NXsample group in which it defines the results of the neutron scattering
by the sample, *e.g.*, energy transfer, polarizations.

:;[NXgeometry](NXgeometry "wikilink"):This group contains the
geometrical information required to define the position, shape, and
orientation of a NeXus object. This is especially important if the NeXus
file contains the results of a comprehensive instrument simulation.

::;[NXtranslation](NXtranslation "wikilink"):This group defines the
position of the object in either absolute coordinates or relative to
another object.

::;[NXshape](NXshape "wikilink"):This group defines the shape of an
object.

::;[NXorientation](NXorientation "wikilink"):This group defines the
orientation of the object. The NXgeometry group defines the shape of an
object in terms of a conventional set of coordinate axes, but this group
allows it to be rotated into an arbitrary orientation.

:;[NXenvironment](NXenvironment "wikilink"):This group contains details
of the environment of a beamline component.

::;[NXsensor](NXsensor "wikilink"):This group defines an environment
sensor.

### NeXus Data

One of the aims of the NeXus design was to make it possible to separate
the measured data in a NeXus file from all the metadata that describe
how that measurement was performed. In principle, it should be possible
for a plotting utility to identify the plottable data automatically (or
to provide a list of choices if there is more than one set of data). In
order to distinguish the actual measurements from this metadata, it is
stored separately in groups with the class NXdata. These groups
encapsulate all the information required to produce a meaningful plot,
including any error arrays and axis scales, i.e. the physical values
corresponding to the data dimensions.

The NXdata groups have to be flexible enough to cope with data of
arbitrary rank and provide a mechanism for associating axis scales with
the appropriate dimension of data. We use data attributes to accomplish
this. Here are the main rules that must be followed in constructing an
NXdata group.

-   Each NXdata group will consist of only one data set containing
    plottable data and their standard deviations.
-   The data set will be identified by an attribute of “signal” given a
    value 1.
-   This data set may be of arbitrary rank.

  
If available, the standard deviations of the data are to be stored in a
data set of the same rank and dimensions, with the name “errors”.

-   For each data dimension, there should be a one-dimensional array of
    the same length.
-   These one-dimensional arrays are the “dimension scales” of the data
    i.e. the values of the independent variables at which the data is
    measured e.g. scattering angle or energy transfer.

There are two methods of linking each data dimension to its respective
dimension scale.

1.  The first method is to define an attribute of each dimension scale
    called “axis”. It is an integer whose value is the number of the
    dimension, in order of fastest varying dimension. i.e. if the array
    being stored is data, with elements `data[j][i]` in C and
    `data(i,j)` in Fortran, where `i` is the time-of-flight index and
    `j` is the polar angle index, the NXdata group would contain :

<!-- -->

    <NXdata name=" data " > 
             <time_of_flight axis= 1 primary= 1 > 1500.0 1502.0 1504.0 … </time_of_flight> 
             <polar_angle axis= 2 primary= 1 > 15.0 15.6 16.2 … </polar_angle> 
             <data > 5 7 14 … </data> 
    </NXdata>

  
This attribute must be defined for each dimension scale.

1.  The second method is to define an attribute of the data itself
    called “axes”. It contains the names of each dimensions scale as a
    comma- or colon-delimited list in the order they appear in C.
    Optionally, the list can be enclosed in brackets, but should not
    contain any spaces, e.g.

<!-- -->

    <NXdata name=" data " > 
             <time_of_flight > 1500.0 1502.0 1504.0 … </time_of_flight> 
             <polar_angle > 15.0 15.6 16.2 … </polar_angle> 
             <data axes="polar_angle:time_of_flight" > 5 7 14 … </data> 
    </NXdata>

  
The second method is required when the dimension scale is used in more
than one NXdata group in a different context, e.g. it is used as the
x-axis in one group and the y-axis in another.

The first method was historically the first to be used, but the second
is now recommended for future applications. However, both will be
supported in NeXus utilities that identify dimension scales, e.g.
NXUfindaxis.

There are limited circumstances in which more than one dimension scale
for the same data dimension can be included in the same NXdata group.
The most common is when they are the three components of an (hkl) scan.
In order to handle this case, we have defined another attribute of type
integer called “primary” whose value determines the order in which the
scale is expected to be chosen for plotting, i.e. 1st choice: primary =
1 2nd choice: primary = 2 etc. If there is more than one scale with the
same value of the “axis” attribute, one of them must have the “primary”
attribute set to 1. Defining the “primary” attribute for the other
scales is optional.

  
N.B. The “primary” attribute can only be used with the first method of
defining dimension scales discussed above. In addition to the signal
data, this group could contain a data set of the same rank and
dimensions called “errors” containing the standard deviations of the
data.

It is often (usually) necessary to associate the data and/or axis scales
with other metadata stored in other groups, e.g. the NXsample group or
components of the NXinstrument group. For example, it may be necessary
to perform corrections for the detector efficiency using information
stored in the associated NXdetector group. In this case, it is
recommended that the relevant arrays are initially stored in those
groups, and then linked to the NXdata group. The API will provide a
mechanism for identifying the parent group so that the relevant metadata
can be accessed.

Here is a simple example to illustrate the concept:

    <NXsample>
             <magnetic_field link=" entry/sample " >
    </NXsample>
    <NXinstrument>
             <NXdetector>
                     <data axes=" time_of_flight:magnetic_field " link=" /entry/instrument/detector " >
                     <time_of_flight link=" entry/instrument/detector " >
             </NXdetector>
    </NXinstrument>
    <NXdata>
             <data axes=" time_of_flight:magnetic_field " link=" /entry/instrument/detector " >
             <time_of_flight link=" entry/instrument/detector " >
             <magnetic_field link=" entry/sample " >
    </NXdata>

In this example, there are two axis scales, “magnetic\_field” and
“time\_of\_flight”, which are stored in NXsample and NXdetector groups
respectively. A program is able to use the link information in order to
locate the respective groups. One corollary of this is that there will
should be one NXdetector group for each NXdata group, e.g. one for each
detector bank in a multi-bank instrument.

NeXus Attributes
----------------

### Global Attributes

| Name               | Type                                                     | Description                                                                                        |
|--------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| file\_name         | NX\_CHAR                                                 | File name of original NeXus file to assist in identification if the external name has been changed |
| file\_time         | [ISO 8601](http://www.cl.cam.ac.uk/~mgk25/iso-time.html) | Date and time of file creation                                                                     |
| file\_update\_time | [ISO 8601](http://www.cl.cam.ac.uk/~mgk25/iso-time.html) | Date and time of last file change at close                                                         |
| NeXus\_version     | NX\_CHAR                                                 | Version of NeXus API used in writing the file                                                      |
| creator            | NX\_CHAR                                                 | Facility or program where the file originated                                                      |

### Data Attributes

| Name                | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| units               | NX\_CHAR    | Units of data which must conform to the standard defined by the [Unidata UDunits utility](http://my.unidata.ucar.edu/content/software/udunits/) (in particular, see [udunits.dat](http://www.unidata.ucar.edu/content/software/udunits/udunits.txt))                                                                                                                                                                                                                  |
| signal              | NX\_INT32   | Defines which data set contains the signal to be plotted - set to 1 for main signal                                                                                                                                                                                                                                                                                                                                                                                   |
| axes                | NX\_CHAR    | Defines the names of the dimension scales for this data set as a comma-delimited array, optionally surrounded by brackets (see a longer discussion in the section on [NXdata structure](NXdata_structure "wikilink")) *i.e.* if the array being stored is `data`, with elements `data[j][i]` in C and `data(i,j)` in Fortran, with dimension scales `time_of_flight[i]` and `polar_angle[j]`, `data` would have an attribute called “axes” with the following value : 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
   > `[polar_angle,time_of_flight]`                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| axis                | NX\_INT32   | As an alternative to using the “axes” attribute, this defines the rank of the signal data for which this data set is a dimension scale in order of the fastest varying index (see a longer discussion in the section on <a href="NeXus_structure.html#Data">NXdata structure</a>) <i>i.e.</i> if the array being stored is `data`, with elements `data[j][i]` in C and `data(i,j)` in Fortran, “axis” would have the following values :                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
   -   <i>i</i>th dimension: axis = 1                                                                                                                                                                                                                                                                                                                                                                                                                                     
   -   <i>j</i>th dimension: axis = 2                                                                                                                                                                                                                                                                                                                                                                                                                                     
   -   <i>etc.</i>                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| primary             | NX\_INT32   | Defines the order of preference for dimension scales which apply to the same rank of signal data - set to 1 for preferred dimension scale                                                                                                                                                                                                                                                                                                                             |
| long\_name          | NX\_CHAR    | Defines title of signal data or axis label of dimension scale                                                                                                                                                                                                                                                                                                                                                                                                         |
| calibration\_status | NX\_CHAR    | Defines status of data value - set to “Nominal” or “Measured”                                                                                                                                                                                                                                                                                                                                                                                                         |
| histogram\_offset   | NX\_FLOAT32 | Defines the offset from the first data point to its bin boundary.                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
   <center>                                                                                                                                                                                                                                                                                                                                                                                                                                                               
   <i>i.e.</i> left\_bin = data\[1\] - histogram\_offset                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
   </center>                                                                                                                                                                                                                                                                                                                                                                                                                                                              
   - set to 0 if the data are not histograms. The points themselves should be set to the bin centers. For reasoning behind this design, see note on [histograms](Histograms "wikilink").                                                                                                                                                                                                                                                                                  |
| checksum            | NX\_INT32   | Sum of data array acting as a check on data integrity                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version             | NX\_CHAR    | Version of XML DTD file or schema on which the NeXus file is based. Should only be used with the “analysis” data item in an [NXentry](NXentry "wikilink") group.                                                                                                                                                                                                                                                                                                      |
| URL                 | NX\_CHAR    | The URL of the XML DTD file or schema on which the NeXus file is based. Should only be used with the “analysis” data item in an [NXentry](NXentry "wikilink") group.                                                                                                                                                                                                                                                                                                  |


