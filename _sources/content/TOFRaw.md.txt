---
title: TOFRaw
permalink: TOFRaw.html
layout: wiki
---
TOFRaw
======

NXTOFRAW - A proposal for a NeXus Time-of-Flight Raw Data File Format

Introduction
------------

[NeXus](http://www.nexusformat.org/) is moving onto the idea of
inherited incremental definitions as discussed at the last meeting of
the [NeXus International Advisory Committee (NIAC)](NIAC.html "wikilink") –
for example with powder diffractometers there is a definition for both
time focussing and total scattering with one being a subset of the
other; a file can conform to one or both. The initial work on this
definition comes from discussions between [SNS](https://neutrons.ornl.gov/sns/),
[J-PARC](http://j-parc.jp/index-e.html) and
[ISIS](https://www.isis.stfc.ac.uk/) - the three facilities are interested
in having a unified base for all instruments to allow for low level
instrument debugging tools to be used, without change, in a given
facility. Further discussions occured in the [TOF Breakout Group at NIAC
2006](NIAC2006_TOF_Group.html "wikilink")

An example file is available in [HDF4
(2MB)](http://download.nexusformat.org/TOFRAW/examples/hrp08639.nx4),
[HDF5
(2MB)](http://download.nexusformat.org/TOFRAW/examples/hrp08639.nx5) and
[XML(16MB)](http://download.nexusformat.org/TOFRAW/examples/hrp08639.xml)
format as well as a [basic
DTD](http://download.nexusformat.org/TOFRAW/examples/TOFRAW.xml).

For historical information see the [draft proposal for an ISIS NeXus
based RAW data file format](../pdfs/Isis_nexus_016.pdf "wikilink").

Goal of the Definition
----------------------

The definition/format should:

-   Be general i.e. not specific to any particular instrument type and
    so can be used as a common root/parent format across all instruments
    at a facility
-   allow the sharing of diagnostic and “first look” data/detector
    display programs between the facilities.
-   provide a common input format to metadata capture programs (such as
    the ISIS ICAT search interface)

With the above in mind the instrument components of most importance are
the ones related to the detector, data, user, sample and sample
conditions; other instrument components are, of course, needed for
analysis but will be covered by specific NeXus instrument definitions.
The NeXus classes we will ultimately consider are then:

    NXroot
    NXdata
    NXdetector
    NXentry
    NXgeometry
    NXinstrument
    NXlog
    NXmoderator
    NXmonitor
    NXsample
    NXuser
    NXevent_data 
    NXsource
    NXdetector_group (proposed)

Some of these classes, such as NXgeometry, are taken directly from what
was ratified by the [NIAC](NIAC.html "wikilink").

Conventions Used in this Document
---------------------------------

A tabular format is used for ease of viewing and printing rather than
the [NeXus XML meta-DTD format](Metaformat.html "wikilink"). The Name column
in a table identifies an item in an instance of a NeXus class. Items can
have extra “meta data” associated with them, which are called attributes
– these, if any, are listed in the next few lines in the attributes
column. Any variables in the attributes column are always attached to
the previous variable in the Name column above them; if the Name of the
variable is the same as the class (e.g. NXfile), then the attributes are
associated with an instance of that class (global) and not to any of its
specific members.

### Identifying Mandatory and Optional Components

The following convention will be used:

-   Variables in **bold** in the Name column of tables are mandatory –
    they must be present in ALL NeXus files; otherwise they are optional
    and their inclusion will depend on the instrument, experiment or
    presence of other items in the class (see the class description of
    usage)
-   Variables in *{italics}* in the Name column are examples of names
    and any variable name can in fact be used; variable names in normal
    type mean that exact name must be used
-   Anything in <font color=red>red</font> is currently an extension to
    NeXus

This information is also included in a RE column (the name derives from
the fact that a “Regular Expression” is used here in the [XML DTD
format](Metaformat.html "wikilink")). Thus:

| Font/style in Name Column | RE Column | Meaning                                                                                                | XML DTD symbol |
|---------------------------|-----------|--------------------------------------------------------------------------------------------------------|----------------|
| Something                 | 0/1       | A single instance of this variable may be present (optional) – if it is, it must be called “something” | ?              |
| **Something**             | 1         | A single instance of this variable must be present (mandatory) and called “something”                  |                |
| *{Something}*             | 0+        | Zero or more variables of this type/class may be present (optional) and can have any unique name(s)    | -              |
| **{Something}**           | 1+        | One or more variables of this type/class must be present (mandatory), but can have any name(s)         | +              |

The above convention dictates that the name for any item that occurs
only 0 or 1 times is fixed; this is not required by the current NeXus
standard, but would add clarity and ease of location if followed.

### Naming

We will try and name logged variables (type NXlog) such that they end in
the \_log suffix

NeXus Classes
-------------

### NXroot

The root is not a real class in the NeXus file, it is a convenient name
under which to group the global attributes of the file. This is taken
directly from the NeXus technical reference without change.

| RE  | Name    | Attribute                              | Type     | Value | Description                                                                                                                                                                                          |
|-----|---------|----------------------------------------|----------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   |         | NeXus\_version                         | NX\_CHAR |       |                                                                                                                                                                                                      |
| 0/1 |         | HDF\_version                           | NX\_CHAR |       |                                                                                                                                                                                                      |
| 0/1 |         | HDF5\_version                          | NX\_CHAR |       |                                                                                                                                                                                                      |
| 0/1 |         | XML\_version                           | NX\_CHAR |       |                                                                                                                                                                                                      |
| 1   |         | creator                                | NX\_CHAR |       |                                                                                                                                                                                                      |
| 1   |         | file\_name                             | NX\_CHAR |       | Original file name                                                                                                                                                                                   |
| 1   |         | file\_time                             | NX\_CHAR |       | Original creation time of file                                                                                                                                                                       |
| 1   |         | file\_update\_time                     | NX\_CHAR |       | Last time file contents were changed                                                                                                                                                                 |
| 1   |         | <font color=red>initial\_format</font> | NX\_CHAR |       | Initial format file was created in (HDF4,HDF5 or XML)                                                                                                                                                |
| 1+  | {entry} |                                        | NXentry  |       |                                                                                                                                                                                                      |
| 0/1 |         | unique\_id                             | NX\_CHAR |       | UUID to uniquely identify file (even if name changes .etc). Maybe useful to have it in the NXentry instead so that you can indentify where an entry comes from even if it is copied into a new file? |

### NXentry

This is the top level group in a file that contains a complete set of
information (e.g. a “run”) - raw, reduced, and analyzed data can occur
in the same file, each as a separate NXentry . The definition below is
taken from the NeXus technical reference changing some elements to be
required rather an optional. Additional items are highlighted in
<font color=red>red</font>.

This definition covers a single run experiment - extensions are proposed
for [scan type experiments](TOFRawScan.html "wikilink")

#### NXentry

| RE   | Name                                          | Attribute                         | Type                          | Value          | Description                                                                                                                      |
|------|-----------------------------------------------|-----------------------------------|-------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| 0/1  | title                                         |                                   | NX\_CHAR                      |                | run title                                                                                                                        |
| 1    | definition                                    |                                   | NX\_CHAR                      |                | Official NeXus definitions this file conforms to                                                                                 |
| 1    |                                               | URL                               | NX\_CHAR                      |                |                                                                                                                                  |
| 1    |                                               | version                           | NX\_CHAR                      |                |                                                                                                                                  |
| 0/1  | <font color=red>definition\_local</font>      |                                   | NX\_CHAR                      |                | Local definition this file also conforms to – this will describe the meaning of any additional local data items etc.             |
| 1    |                                               | url                               | NX\_CHAR                      |                |                                                                                                                                  |
| 1    |                                               | version                           | NX\_CHAR                      |                | This would correspond to the ISIS Muon IDF\_Version                                                                              |
| 1    | start\_time                                   |                                   | ISO8601                       |                | Time data collection started                                                                                                     |
| 1    | end\_time                                     |                                   | ISO8601                       |                | Time data collection ended                                                                                                       |
| 1    | duration                                      |                                   | NX\_FLOAT                     |                | wall clock time transpired (end – start)                                                                                         |
| 1    |                                               | units                             | NX\_CHAR                      | second         |                                                                                                                                  |
| 1    | <font color=red>collection\_time</font>       |                                   | NX\_FLOAT                     |                | Time transpired actually collecting data i.e. taking out time when collection was suspended due to e.g. temperature out of range |
| 1    |                                               | units                             | NX\_CHAR                      | second         |                                                                                                                                  |
| 0/1  | proton\_charge                                |                                   | NX\_FLOAT                     |                |                                                                                                                                  |
| 1    |                                               | units                             | NX\_CHAR                      | microAmp\*hour |                                                                                                                                  |
| 0/1  | raw\_frames                                   |                                   | NX\_INT                       |                | number of proton pulses on target                                                                                                |
| 0/1  | good\_frames                                  |                                   | NX\_INT                       |                | number of proton pulses used (i.e. not vetoed)                                                                                   |
| 0/1  | <font color=red>total\_counts</font>          |                                   | NX\_INT                       |                | Total number of detector counts (events)                                                                                         |
| 1    | experiment\_identifier                        |                                   | NX\_CHAR                      |                | proposal number                                                                                                                  |
| 0/1  | <font color=red>discipline </font>            |                                   | NX\_CHAR                      |                | Keyword domain (e.g. chemistry, astronomy, ecology, … )                                                                          |
| 1    |                                               | <font color=red>info\_src</font>  | NX\_CHAR                      | propsal        | Source of the information (proposal, updated during experiment, after, ...)                                                      |
| 0/1  | <font color=red>keyword </font>               |                                   | NX\_CHAR                      |                | Keywords defined for this study.                                                                                                 |
| 1    |                                               | <font color=red>info\_src</font>  | NX\_CHAR                      | propsal        | Source of the information                                                                                                        |
| 0/1  | <font color=red>keyword\_source</font>        |                                   | NX\_CHAR                      |                | A pointer to a reference work providing the definition of the restricted vocabulary of which the keyword list is a subset.       |
| 1    |                                               | <font color=red>info\_src </font> | NX\_CHAR                      | propsal        | Source of the information                                                                                                        |
| 0/1  | <font color=red>subject </font>               |                                   | NX\_CHAR                      |                | Subject categorisations for this study                                                                                           |
| 1    |                                               | <font color=red>info\_src</font>  | NX\_CHAR                      | propsal        | Source of the information                                                                                                        |
| 0/1  | <font color=red>description\_summary</font>   |                                   | NX\_CHAR                      |                | Brief summary of the experiment, including key objectives                                                                        |
| 1    |                                               | <font color=red>info\_src</font>  | NX\_CHAR                      | propsal        | Source of the information                                                                                                        |
| 0/1  | <font color=red>description</font>            |                                   | NXnote                        |                | Description of the full experiment (document in pdf, latex, …)                                                                   |
| 1    |                                               | <font color=red>info\_src </font> | NX\_CHAR                      | propsal        | Source of the information                                                                                                        |
| 0/1  | <font color=red>requirement</font>            |                                   | NX\_CHAR                      |                | Special requirements of instrument                                                                                               |
| 1    |                                               | <font color=red>info\_src </font> | NX\_CHAR                      | propsal        | Source of the information                                                                                                        |
| 0/1  | <font color=red>publications</font>           |                                   | NX\_CHAR                      |                | List of publication related to the proposal                                                                                      |
| 1    |                                               | <font color=red>info\_src</font>  | NX\_CHAR                      | propsal        | Source of the information                                                                                                        |
| 0/1  | <font color=red>facility\_access\_type</font> |                                   | NX\_CHAR                      |                | Facility access type (normal, rapid access, programme access …)                                                                  |
| 1    |                                               | <font color=red>info\_src</font>  | NX\_CHAR                      | propsal        | Source of the information                                                                                                        |
| 0/1  | <font color=red>grant\_id </font>             |                                   | NX\_CHAR                      |                | Identifier of the funding grant.                                                                                                 |
| 1    |                                               | <font color=red>info\_src</font>  | NX\_CHAR                      | propsal        | Source of the information                                                                                                        |
| 1    | run\_number                                   |                                   | NX\_INT                       |                | Unique number identifying this data collection                                                                                   |
| 0 /1 | run\_cycle                                    |                                   | NX\_CHAR                      |                |                                                                                                                                  |
| 0/1  | program\_name                                 |                                   | NX\_CHAR                      |                |                                                                                                                                  |
| 1    |                                               | version                           | NX\_CHAR                      |                |                                                                                                                                  |
| 0/1  |                                               | command\_line                     | NX\_CHAR                      |                |                                                                                                                                  |
| 0/1  | <font color=red>release\_date</font>          |                                   | NX\_CHAR                      |                | Date of the public release of the data. (file\_time + X years)                                                                   |
| 0/1  | <font color=red>revision</font>               |                                   | NX\_CHAR                      |                | Revision id of the file due to re-calibration, reprocessing, new analysis, new instrument definition format, ...                 |
| 0/1  | notes                                         |                                   | <font color=red>NXnote</font> |                | User notes                                                                                                                       |
| 0/1  | thumbnail                                     |                                   | NXnote                        |                |                                                                                                                                  |
| 1    |                                               | mime\_type                        | NX\_CHAR                      | image/\*       |                                                                                                                                  |
| 0+   | {characterisation}                            |                                   | NXcharacterization            |                |                                                                                                                                  |
| 1+   | {user1,user2,…}                               |                                   | NXuser                        |                |                                                                                                                                  |
| 1    | {sample}                                      |                                   | NXsample                      |                |                                                                                                                                  |
| 1    | {instrument}                                  |                                   | NXinstrument                  |                |                                                                                                                                  |
| 1+   | {monitor}                                     |                                   | NXmonitor                     |                |                                                                                                                                  |
| 1+   | {data}                                        |                                   | NXdata                        |                |                                                                                                                                  |
| 0/1  | {process}                                     |                                   | NXprocess                     |                |                                                                                                                                  |

### NXuser

As denoted in NXentry, there can be multiple NXuser, one for each person
involved with an experiment. This definition of user requires only a
name and a facility identifier and this is taken directly from the NeXus
technical reference changing some elements to be required rather an
optional.

| RE  | Name                                     | Attribute                           | Type     | Value                                         | Description               |
|-----|------------------------------------------|-------------------------------------|----------|-----------------------------------------------|---------------------------|
| 1   | name                                     |                                     | NX\_CHAR |                                               |                           |
| 0/1 |                                          | <font  color="red">info\_src</font> | NX\_CHAR | “proposal”, “updated”, “corrected”, “logging” | Source of the information |
| 0/1 | role                                     |                                     | NX\_CHAR | “local\_contact”,”Principle Investigator”, …  |                           |
| 0/1 | affiliation                              |                                     | NX\_CHAR |                                               |                           |
| 0/1 | address                                  |                                     | NX\_CHAR |                                               |                           |
| 0/1 | telephone\_number                        |                                     | NX\_CHAR |                                               |                           |
| 0/1 | fax\_number                              |                                     | NX\_CHAR |                                               |                           |
| 0/1 | email                                    |                                     | NX\_CHAR |                                               |                           |
| 1   | facility\_user\_id                       |                                     | NX\_CHAR |                                               |                           |
| 0/1 | <font color="red">affiliation\_id</font> |                                     | NX\_CHAR |                                               |                           |

### NXsample

This list is limited to items that were desired by the group. See the
NeXus technical reference for a full list of possible items.

| RE  | Name                                     | Attribute | Type       | Value                                    | Description                                                                                 |
|-----|------------------------------------------|-----------|------------|------------------------------------------|---------------------------------------------------------------------------------------------|
| 1   | Name                                     |           | NX\_CHAR   |                                          |                                                                                             |
| 1   | identifier                               |           | NX\_CHAR   |                                          | Identity given to the sample by health physics or sample environment. (Could be a bar code) |
| 0/1 |                                          | Type      | NX\_CHAR   | e.g.“barcode                             |                                                                                             |
| 0/1 | chemical\_formula                        |           | NX\_CHAR   |                                          |                                                                                             |
| 0/1 | mass                                     |           | NX\_FLOAT  |                                          |                                                                                             |
| 1   |                                          | units     | NX\_CHAR   |                                          |                                                                                             |
| 0/1 | volume                                   |           | NX\_FLOAT  |                                          |                                                                                             |
| 1   |                                          | units     | NX\_CHAR   |                                          |                                                                                             |
| 0/1 | geometry                                 |           | NXgeometry |                                          |                                                                                             |
| 1   | nature                                   |           | NX\_CHAR   | solid | powder | liquid | single crystal |                                                                                             |
| 0/1 | preparation                              |           | NX\_CHAR   |                                          | Sample handling/preparation prior to experiment                                             |
| 0/1 | changer\_position                        |           | NX\_INT    |                                          | Sample changer position                                                                     |
| 0/1 | <font color=red>sample\_holder</font>    |           | NX\_CHAR   |                                          |                                                                                             |
| 0/1 | <font color=red>preparation\_date</font> |           | ISO8601    |                                          |                                                                                             |
| 0/1 | thickness                                |           | NX\_FLOAT  |                                          |                                                                                             |
| 0/1 | temperature                              |           | NX\_FLOAT  |                                          |                                                                                             |

#### Sample environment parameters

By these we mean “temperature”, “magnetic\_field” etc. which may be
considered to be outside of the remit of this document, but we will just
add a reminder that if the file represents a scan then these values will
be annotated as described in the NXentry section.

### NXinstrument

This is the class that contains all information about instrument
components except the monitors and sample (which are just inside the
NXentry). This is taken directly from the NeXus technical reference
changing some elements to be required rather an optional.

| RE  | Name     | Attribute   | Type                                       | Value | Description                        |
|-----|----------|-------------|--------------------------------------------|-------|------------------------------------|
| 1   | name     |             | NX\_CHAR                                   |       |                                    |
| 1   |          | short\_name | NX\_CHAR                                   |       |                                    |
| 1   | beamline |             | NX\_CHAR                                   |       | Beamline instrument is attached to |
| 0/1 |          |             | NXsource                                   |       |                                    |
| 0+  |          |             | NXdisk\_chopper                            |       |                                    |
| 0+  |          |             | NXfermi\_chopper                           |       |                                    |
| 0+  |          |             | NXvelocity\_selector                       |       |                                    |
| 0+  |          |             | NXguide                                    |       |                                    |
| 0+  |          |             | NXcrystal                                  |       |                                    |
| 0+  |          |             | NXaperature                                |       |                                    |
| 0+  |          |             | NXfilter                                   |       |                                    |
| 0+  |          |             | NXcollimator                               |       |                                    |
| 0+  |          |             | NXattenuator                               |       |                                    |
| 0+  |          |             | NXpolarizer                                |       |                                    |
| 0+  |          |             | NXflipper                                  |       |                                    |
| 0+  |          |             | NXmirror                                   |       |                                    |
| 1+  |          |             | NXdetector                                 |       |                                    |
| 0+  |          |             | <font color="red">NXdetector\_group</font> |       |                                    |
| 0+  |          |             | NXbeam\_stop                               |       |                                    |

### NXmonitor

| RE  | Name                                    | Attribute | Type             | Value           | Description                                           |
|-----|-----------------------------------------|-----------|------------------|-----------------|-------------------------------------------------------|
| 0/1 | mode                                    |           | NX\_CHAR         | monitor | timer |                                                       |
| 0/1 | preset                                  |           | NX\_FLOAT        |                 |                                                       |
| 0/1 | distance                                |           | NX\_FLOAT        |                 |                                                       |
| 0/1 |                                         | units     | NX\_CHAR         | metre           |                                                       |
| 0/1 | range                                   |           | NX\_FLOAT\[2\]   |                 |                                                       |
| 1   |                                         | units     | NX\_CHAR         |                 |                                                       |
| 0/1 | integral                                |           | NX\_FLOAT        |                 |                                                       |
| 1   |                                         | units     | NX\_CHAR         |                 |                                                       |
| 0/1 | integral\_log                           |           | NXlog            |                 | Time log of monitor integrals                         |
| 0/1 | type                                    |           | NX\_CHAR         |                 |                                                       |
| 1   | time\_of\_flight                        |           | NX\_FLOAT\[i+1\] |                 |                                                       |
| 1   |                                         | units     | NX\_CHAR         | microsecond     |                                                       |
| 0/1 | efficiency                              |           | NX\_FLOAT\[i\]   |                 |                                                       |
| 1   | data                                    |           | NX\_FLOAT\[i\]   |                 |                                                       |
| 1   |                                         | units     | NX\_CHAR         |                 |                                                       |
| 1   |                                         | signal    | NX\_INT          |                 |                                                       |
| 1   |                                         | axes      | NX\_CHAR         |                 |                                                       |
| 0/1 | sampled\_fraction                       |           | NX\_FLOAT        |                 |                                                       |
| 1   |                                         | units     | NX\_CHAR         | unitless        |                                                       |
| 0/1 | geometry                                |           | NXgeometry       |                 |                                                       |
| 0/1 | <font color=red>monitor\_number</font>  |           | NX\_INT          |                 | If monitors are numbered, this is what it is known as |
| 0/1 | <font color=red>detector\_number</font> |           | NX\_INT          |                 | Detector/spectrum number for this monitor             |

Note that for a position sensitive monitor detector\_number etc. will
need to be an array and NXmonitor will have other fields and look more
like NXdetector.

### NXdetector

We will now look at possible representations of the detector – we will
start with a general one and then consider the special case of an area
detector. Though the general (point) detector representation would cover
all cases, if the detector is physically “rectangular” in nature there
are advantages in using this symmetry in the representation. Which
representation is used is recorded in the <font color=red>layout</font>
attribute

#### Point Detector

The general representation is to consider a detector as just a group of
pixels arranged in no particular order. Each pixel will be identified by
a unique single index i and then the following information will be
stored:

| RE  | Name                                | Attribute | Type             | Value                | Description                                                  |
|-----|-------------------------------------|-----------|------------------|----------------------|--------------------------------------------------------------|
| 1   | <font color=red>layout</font>       |           | NX\_CHAR         | point                | How detector is represented                                  |
| 1   | detector\_number                    |           | NX\_INT\[i\]     |                      |                                                              |
| 0/1 | polar\_angle                        |           | NX\_FLOAT\[i\]   |                      |                                                              |
| 0/1 | azimuthal\_angle                    |           | NX\_FLOAT\[i\]   |                      |                                                              |
| 0/1 | solid\_angle                        |           | NX\_FLOAT\[i\]   |                      |                                                              |
| 0/1 | distance                            |           | NX\_FLOAT\[i\]   | distance from sample |                                                              |
| 1   | time\_of\_flight                    |           | NX\_FLOAT\[j+1\] |                      | Bin boundaries                                               |
| 0/1 |                                     | units     | NX\_CHAR         | Micro.second         |                                                              |
| 0/1 | time\_of\_flight\_raw               |           | NX\_INT\[j+1\]   |                      | in DAQ clock pulses                                          |
| 0/1 |                                     | units     | NX\_CHAR         | Clock\_pulses        |                                                              |
| 0/1 |                                     | frequency | NX\_FLOAT        |                      | Clock frequency of acquisition system (Hz)                   |
| 1   | data                                |           | NX\_FLOAT\[i,j\] |                      |                                                              |
| 0/1 | geometry                            |           | NXgeometry\[i\]  |                      | These will be relative to “Origin” below                     |
| 0/1 | <font color=red>group\_index</font> |           | NX\_INT\[i\]     |                      | Detector grouping information – see NXdetector\_groups class |

The detector data would be plotted with axes (detector number, tof) by
any program. An NXgeometry object included in the detector contains
arrays that store the position and orientation of each pixel. As this
detector representation imposes no constraint on the relationship
between pixels, a single NXdetector could represent the entire
instrument (so long as all detectors have the same time\_of\_flight) –
however in practice an NXdetector and NXdata would be created for each
bank. The “origin” object provides a reference point for the pixel
geometries – the “shape” part of origin is the bounding box of the
entire detector/detector bank.

#### Linear Detector

Here we mean a collection of linear straight strips e.g. tubes. We have
two indicies: **j** will label the strip/tube and **i** the position
along the tube. All tubes must have the same number of pixels; if not,
you must use the point detector representation above. The tubes do not
need to be parallel - they just need to be straight. Thus:

| RE  | Name                          | Attribute | Type               | Value           | Description                              |
|-----|-------------------------------|-----------|--------------------|-----------------|------------------------------------------|
| 1   | <font color=red>layout</font> |           | NX\_CHAR           | linear          | How detector is represented              |
| 1   | detector\_number              |           | NX\_INT\[i,j\]     |                 |                                          |
| 1   | polar\_angle                  |           | NX\_FLOAT\[i,j\]   |                 |                                          |
| 1   | azimuthal\_angle              |           | NX\_FLOAT\[i,j\]   |                 |                                          |
| 1   | distance                      |           | NX\_FLOAT\[i,j\]   |                 |                                          |
| 1   | time\_of\_flight              |           | NX\_FLOAT\[k+1\]   |                 | Bin boundaries                           |
| 0/1 |                               | Units     | NX\_CHAR           | Micro.second    |                                          |
| 1   | raw\_time\_of\_flight         |           | NX\_INT\[k+1\]     |                 | in DAQ clock pulses                      |
| 0/1 |                               | Units     | NX\_CHAR           | Clock\_pulses   |                                          |
| 0/1 |                               | Frequency | NX\_FLOAT          | Clock frequency |                                          |
| 1   | data                          |           | NX\_FLOAT\[i,j,k\] |                 |                                          |
| 0/1 | geometry                      |           | NXgeometry\[i\]    |                 | These will be relative to “Origin” below |
| 0/1 | pixel\_offset                 |           | NX\_FLOAT\[j\]     |                 | 0 at origin                              |
| 0/1 | pixel\_size                   |           | NX\_FLOAT\[j\]     |                 |                                          |
||

By specifying both size and offset “dead space” between pixels can be
accounted for.

This looks similar to a point detector, but with two array indices
rather than one. However note the geometry information is different - as
the tubes are straight we need only specify a location of the tube
centre and an offset along the tube. Thus:

-   NXgeometry geometry\[i\] \# defines tube/strip centre; each NXshape
    member give the tube size and shape; each NXorientation member
    rotates the axes such that **x** points along each tube.
-   pixel\_offset\[j\] \# offset from tube centre of each pixel centre
-   pixel\_size\[j\] \# size of each pixel

#### Area Detector

A flat rectangular area detector could be described by the “general”
representation above, but taking account of the two dimensional symmetry
of the detector allows several potential savings in the calculation of
angles and in plotting time of the data. An area detector will have
indices (i,j) indexing each pixel with i along the local detector “x”
axis and j along the local detector “y”. In the case of curved detectors
the offsets and sizes are to be considered as arc lengths along the face
of the detector. An offset of “0” is the origin of the detector and the
NXgeometry named “origin” describes the geometry of the entire detector:
the NXtranslation part describes the position of the detector, the
NXorientation part defines the local coordinates (local x and y axes)
with respect to the global position, and the NXshape describe the size
(bounding box) and topology of the detector as a whole. The NXgeometry
named “geometry” describes the pixels and their shape (assuming that
they are uniform). The necessary shapes are: rectangular prism,
cylindrical slice, and spherical slice.

Below are the three cases for describing the pixels on a detector.

| RE  | Name                             | Attribute | Type               | Value           | Description                                                                            |
|-----|----------------------------------|-----------|--------------------|-----------------|----------------------------------------------------------------------------------------|
| 1   | <font color=red>layout</font>    |           | NX\_CHAR           | area            | How detector is represented                                                            |
| 1   | detector\_number                 |           | NX\_INT\[i,j\]     |                 |                                                                                        |
| 1   | polar\_angle                     |           | NX\_FLOAT\[i,j\]   |                 |                                                                                        |
| 1   | azimuthal\_angle                 |           | NX\_FLOAT\[i,j\]   |                 |                                                                                        |
| 1   | distance                         |           | NX\_FLOAT\[i,j\]   |                 |                                                                                        |
| 1   | time\_of\_flight                 |           | NX\_FLOAT\[k+1\]   |                 | Bin boundaries                                                                         |
| 0/1 |                                  | Units     | NX\_CHAR           | Micro.second    |                                                                                        |
| 1   | raw\_time\_of\_flight            |           | NX\_INT\[k+1\]     |                 | in DAQ clock pulses                                                                    |
| 0/1 |                                  | Units     | NX\_CHAR           | Clock\_pulses   |                                                                                        |
| 0/1 |                                  | Frequency | NX\_FLOAT          | Clock frequency |                                                                                        |
| 1   | data                             |           | NX\_FLOAT\[i,j,k\] |                 |                                                                                        |
| 0/1 | geometry                         |           | NXgeometry\[i,j\]  |                 | These will be relative to “Origin” below                                               |
| 0/1 | x\_pixel\_offset                 |           | NX\_FLOAT\[i\]     |                 | 0 at origin                                                                            |
| 0/1 | x\_pixel\_size                   |           | NX\_FLOAT\[i\]     |                 |                                                                                        |
| 0/1 | y\_pixel\_offset                 |           | NX\_FLOAT\[j\]     |                 | 0 at origin                                                                            |
| 0/1 | y\_pixel\_size                   |           | NX\_FLOAT\[j\]     |                 |                                                                                        |
| 0/1 | <font color=red>x\_radius</font> |           | NX\_FLOAT          |                 | If we are curved, the radius of curvature ( \*\_offset above will then be arc lengths) |
| 0/1 | <font color=red>y\_radius</font> |           | NX\_FLOAT          |                 | If we are curved, the radius of curvature ( \*\_offset above will then be arc lengths) |

You can either specify an NXgeometry\[i,j\] for the pixels or instead
use the x\_pixel\_\* arrays. By specifying both size and offset “dead
space” between pixels can be accounted for.

azimuthal\_angle, polar\_angle and distance can be left out of
NXdetector as they can be calculated from the detector geometry

**Hardware ganging of detector elements**

In some cases individual detector elements are ganged together by the
acquisition system for symmetry reasons or to create a smaller data
files. In these cases the above formalisms can still be used, but the
“detector number” does not correspond to a real physical detector and so
the values of “polar\_angle”, “distance”, “azimuthal\_angle” are some
sort of average over the ganged elements. When analysis and simulation
of the data is performed, it is sometimes necessary to know the details
of the individual detectors that have been ganged together. An initial
proposal was that these additional arrays would be stored with the
“\_unganged” suffix e.g. “Polar\_angle\_unganged”, “distance\_unganged”,
“detector\_number\_unganged”. However after discussions of [TOF
Group] (TOF_Group.html "wikilink") if was decided to move these arrays into a
substructure of NXdetector so we would have NXdetector.polar\_angle and
NXdetector.distance for the ganed values;
NXdetector.unganged.polar\_angle and NXdetector.unganged.distance for
the raw values.

To relate the ganged and unganged arrays, a simple grouping scheme can
usually be used: detector.unganged.grouping\[j\] give the value \[i\]
detector.polar\_angle\[i\] that this detector contributes to. This
covers most cases, except for when a detector may have its signal fed
into more than one place; in which case a more complex mapping scheme is
needed.

To cover the general case the “unganged” arrays are arranged so that
elements that are ganged together appear sequentially and information to
relate these arrays to the hardware ganged “polar\_angle” etc arrays are
provided by

| RE  | Name                               | Attribute | Type         | Value                                                 | Description |
|-----|------------------------------------|-----------|--------------|-------------------------------------------------------|-------------|
| 0/1 | <font color=red>gang\_count</font> |           | NX\_INT\[i\] | Number of physical detectors elements ganged together |             |
| 0/1 | <font color=red>gang\_index</font> |           | NX\_INT\[i\] | Index of first ganged element                         |             |

Detector\_number\[i\] is ganged from gang\_count\[i\] elements. The
values of polar\_angle\[i\] was obtained by average the gang\_count\[i\]
values of polar\_angle\_unganged\[gang\_index\[i\]\],
polar\_angle\_unganged\[gang\_index\[i\]+1\], … ,
polar\_angle\[gang\_index\[i\]+gang\_count\[i\]-1\]

### NXdata

| RE  | Name             | Attribute  | Type                 | Value | Description   |
|-----|------------------|------------|----------------------|-------|---------------|
| 0/1 |                  |            | NXdata               |       |               |
| 1   | data             |            | NX\_FLOAT\[i,j,k,m\] |       |               |
| 1   |                  | units      | NX\_CHAR             |       |               |
| 1   |                  | long\_name | NX\_CHAR             |       | Title of data |
| 1   | time\_of\_flight |            | NX\_FLOAT\[k+1\]     |       |               |
| 0/1 | x\_pixel\_offset |            | NX\_FLOAT\[i\]       |       |               |
| 0/1 | y\_pixel\_offset |            | NX\_FLOAT\[j\]       |       |               |
||

The exact format of this will depend on the NXdetector definition used.

### NXmoderator

The moderator is the effective source for all time-of-flight
instruments. This is taken directly from the NeXus technical reference
changing some elements to be required rather an optional. Additional
items are in red.

| RE  | Name             | Attribute | Type        | Value  | Description            |
|-----|------------------|-----------|-------------|--------|------------------------|
| 1   | distance         |           | NX\_FLOAT   |        |                        |
| 1   |                  | units     | NX\_CHAR    |        |                        |
| 1   | type             |           | NX\_CHAR    |        | The moderator material |
| 0/1 | poison\_depth    |           | NX\_FLOAT   |        |                        |
| 1   |                  | units     | NX\_CHAR    |        |                        |
| 0/1 | coupled          |           | NX\_BOOLEAN |        |                        |
| 0/1 | poison\_material |           | NX\_CHAR    |        |                        |
| 0/1 | temperature      |           | NX\_FLOAT   |        |                        |
| 1   |                  | units     | NX\_CHAR    | Kelvin |                        |
| 0/1 | temperature\_log |           | NXlog       |        |                        |
| 0/1 | pulse\_shape     |           | NXdata      |        |                        |
| 0/1 | geometry         |           | NXgeometry  |        |                        |

### NXgeometry

This group describes the shape, position, and orientation of a
component. Almost all of the information is actually stored in
subgroups. This is taken directly from the NeXus technical reference
without change.

| RE  | Name             | Attribute | Type          | Value | Description                                |
|-----|------------------|-----------|---------------|-------|--------------------------------------------|
| 0/1 |                  |           | NXshape       |       |                                            |
| 0/1 |                  |           | NXtranslation |       |                                            |
| 0/1 |                  |           | NXorientation |       |                                            |
| 0/1 | description      |           | NX\_CHAR      |       |                                            |
| 0/1 | component\_index |           | NX\_INT       |       | Position of component along the beam path. |

The sample has a component\_index of 0, components upstream have
negative component\_index.

### NXlog

Contains log information monitored during the run in a timed fashion.
This can contain the time-stamped values, or the average (with standard
deviation), minimum, maximum and total time log was taken. This is taken
directly from the NeXus technical reference without change.

| RE  | Name                                 | Attribute | Type                | Value | Description                                  |
|-----|--------------------------------------|-----------|---------------------|-------|----------------------------------------------|
| 0/1 | time                                 |           | NX\_FLOAT           |       | relative to “start”                          |
| 1   |                                      | units     | NX\_CHAR            |       |                                              |
| 1   |                                      | start     | ISO8601             |       | start time of logging                        |
| 0/1 | value                                |           | NX\_FLOAT / NX\_INT |       |                                              |
| 1   |                                      | units     | NX\_CHAR            |       |                                              |
| 0/1 | raw\_value                           |           | NX\_FLOAT / NX\_INT |       | e.g. voltage from thermocouple               |
| 1   |                                      | units     | NX\_CHAR            |       |                                              |
| 0/1 | description                          |           | NX\_CHAR            |       |                                              |
| 0/1 | average\_value                       |           | NX\_FLOAT           |       |                                              |
| 1   |                                      | units     | NX\_CHAR            |       |                                              |
| 0/1 | average\_value\_error                |           | NX\_FLOAT           |       |                                              |
| 1   |                                      | units     | NX\_CHAR            |       |                                              |
| 0/1 | minimum\_value                       |           | NX\_FLOAT           |       |                                              |
| 1   |                                      | units     | NX\_CHAR            |       |                                              |
| 0/1 | maximum\_value                       |           | NX\_FLOAT           |       |                                              |
| 1   |                                      | units     | NX\_CHAR            |       |                                              |
| 0/1 | duration                             |           | NX\_FLOAT           |       |                                              |
| 1   |                                      | units     | NX\_CHAR            |       |                                              |
| 0/1 | <font color=red>display\_name</font> |           | NX\_CHAR            |       | short name displayed on instrument dashboard |
| 0/1 | <font color=red>software</font>      |           | NX\_CHAR            |       | program or software used to measure value    |
| 0/1 | <font color=red>hardware</font>      |           | NX\_CHAR            |       | hardware used to measure value               |

### NXorientation

| RE  | Name  | Attribute | Type                  | Value | Description                                                                  |
|-----|-------|-----------|-----------------------|-------|------------------------------------------------------------------------------|
| 0/1 |       |           | NXgeometry            |       | Link to another object for relative positioning                              |
| 0/1 | value |           | NX\_FLOAT\[numobj,6\] |       | The orientation information is stored as 6 direction cosines for each object |

### NXshape

| RE  | Name  | Attribute | Type                           | Value                     | Description |
|-----|-------|-----------|--------------------------------|---------------------------|-------------|
| 0/1 | shape |           | NX\_CHAR                       | nxcylinder|nxbox|nxsphere |             |
| 0/1 | size  |           | NX\_FLOAT\[numobj, nshapepar\] |                           |             |
| 1   |       | units     | NX\_CHAR                       | metre                     |             |

The interpretation of the “shapepar” depends on the “shape”

### NXtranslation

| RE  | Name     | Attribute | Type                  | Value | Description                                     |
|-----|----------|-----------|-----------------------|-------|-------------------------------------------------|
| 0/1 |          |           | NXgeometry            |       | Link to another object for relative positioning |
| 0/1 | distance |           | NX\_FLOAT\[numobj,3\] |       |                                                 |
| 1   |          | Units     | NX\_CHAR              | metre |                                                 |

### NXevent\_data

This requires that a Pixel\_number field is provided in the NXdetector
for determining geometry information. While normally this takes the
place of the NXdata in a NXentry, there is no reason that the two cannot
coexist. The index I runs over events - the index j runs counts pulses.

| RE  | Name               | Attribute | Type              | Value        | Description                                                                                                                                                                                                                                         |
|-----|--------------------|-----------|-------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0/1 | time\_of\_flight   |           | NX\_INT\[i\]      |              | A list of time of flight for each event as it comes in. This list is for all pulses with information to attach to a particular pulse located in events\_per\_pulse                                                                                  |
| 1   |                    | units     | NX\_CHAR          | Micro.second |                                                                                                                                                                                                                                                     |
| 0/1 | pixel\_number      |           | NX\_INT\[i\]      |              | There will be extra information in the NXdetector to convert pixel\_number to detector\_number. This list is for all pulses with information to attach to a particular pulse located in events\_per\_pulse                                          |
| 0/1 | pulse\_time        |           | NX\_INT\[j\]      |              | The time that each pulse started with respect to the offset                                                                                                                                                                                         |
| 1   |                    | Units     | NX\_CHAR          |              |                                                                                                                                                                                                                                                     |
| 1   |                    | Offset    | ISO8601           |              |                                                                                                                                                                                                                                                     |
| 0/1 | events\_per\_pulse |           | NX\_INT\[j\]      |              | This connects the index “i” to the index “j”. The jth element is the number of events in “i” that occured during the jth pulse                                                                                                                      |
| 0/1 | pulse\_height      |           | NX\_FLOAT\[I,k?\] |              | If voltages from the ends of the detector are read out this is where they go. This list is for all events with information to attach to a particular pulse height. The information to attach to a particular pulse is located in events\_per\_pulse |

### NXsource

| RE  | Name      | Attribute | Type        | Value                                                                                                         | Description                                                                                                                                       |
|-----|-----------|-----------|-------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|     | NXsource  |           |             | Name of source                                                                                                |                                                                                                                                                   |
| 1   | name      |           | NX\_CHAR    |                                                                                                               | Facility name                                                                                                                                     |
| 1   | type      |           | NX\_CHAR    | “Spallation Neutron Source” | ”Pulsed Reactor Source” | ”Reactor Neutron Source” | “Synchrotron X-ray Source” |                                                                                                                                                   |
| 1   | probe     |           | NX\_CHAR    | “neutrons” | “muons” | “x-rays”                                                                               |                                                                                                                                                   |
| 1   | frequency |           | NX\_FLOAT32 |                                                                                                               | Frequency of pulsed source at the target “at target” allows for the main proton beam being split with.g. 1 in 5 pulses diverted to another target |
| 1   |           | units     | NX\_CHAR    | Hertz                                                                                                         |                                                                                                                                                   |
| 0/1 | period    |           | NX\_FLOAT   |                                                                                                               |                                                                                                                                                   |
| 0/1 |           | units     | NX\_CHAR    | microseconds                                                                                                  | Length of an acquisition frame                                                                                                                    |
| 0/1 | notes     |           | NX\_TEXT    | Source/facility related messages or announcements during the experiment                                       | At ISIS, the MCR beam messages                                                                                                                    |

### NXdetector\_groups

This class is used to allow a logical grouping of detector elements
(e.g. which tube, bank or group of banks) to be recorded in the file. As
well as allowing you to e.g just select the “left” or “east” detectors,
it may also be useful for determining which elements belong to the same
PSD tube and hence have e.g. the same dead time.

| RE  | Name          | Attribute | Type         | Value                                  | Description                               |
|-----|---------------|-----------|--------------|----------------------------------------|-------------------------------------------|
| RE  | Name          | Attribute | Type         | Value                                  | Description                               |
| 1   | group\_names  |           | NX\_CHAR     |                                        | Comma separated list of name              |
| 1   | group\_index  |           | NX\_INT\[i\] |                                        | Unique ID for group                       |
| 1   | group\_parent |           | NX\_INT\[i\] | Index of group parent in the hierarchy | -1 means no parent i.e. a top level group |
| 1   | group\_type   |           | NX\_INT\[i\] | Code number for group type             | e.g. bank=1, tube=2 etc.                  |

For example of we had “bank1” composed of “tube1”, “tube2” and “tube3”
then Group\_names would be the string “bank1, bank1/tube1,
bank1/tube2,bank1/tube3” Group\_index would be {1,2,3,4} Group\_parent
would be {-1,1,1,1}

The mapping array is interpreted as group 1 is a top level group
containing groups 2, 3 and 4

A group\_index array in NXdetector give the base group for a detector
element.
