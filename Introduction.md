---
title: Introduction
permalink: Introduction/
layout: wiki
---

What is NeXus?
--------------

The NeXus data format has three components:

A set of subroutines:to make it easy to read and write NeXus files.  
A set of design principles:to help people understand what is in them.  
A set of instrument definitions:to allow the development of more portable analysis software.  

### A Set of Subroutines

In the past, a data format was defined by a document describing the
precise location of every item in the data file, either as row and
column numbers in an ASCII file, or as record and byte numbers in a
binary file. In modern data formats, such as NeXus, the user does not
need to know where the data are stored, just what they are called. It is
the job of the subroutine library to retrieve the data.

For example, in NeXus, a program to read in the wavelength of an
experiment would contain lines similar to the following:

`NXopendata (fileID, `“`wavelength`”`);`  
`NXgetdata (fileID, lambda);`  
`NXclosedata (fileID);`

In this example, the program requests the value of the data that has the
label `wavelength`, storing the result in the variable lambda. `fileID`
is a file identifier that is provided by NeXus when the file is opened.

We shall provide a more complete example when we have discussed the
contents of the NeXus files.

### A Set of Design Principles

NeXus data files contain two types of entity: data items and data
groups.

Data Items:These can be scalar values or multidimensional arrays of a variety of sizes (1-byte, 2-byte, 4-byte, 8-byte) and types (characters, integers, floats). Extra information required to describe a particular data item, such as the data units, can be stored as a data attribute.  
Data Groups:These are like folders that can contain a number of data items and/or other groups.  

In fact, a NeXus file can be viewed as a computer file system. Just as
files are stored in folders (or subdirectories) to make them easy to
locate, so NeXus data items are stored in groups. The group hierarchy is
designed to make it easy to navigate a NeXus file.

#### Example of a NeXus File

The following diagram shows an example of a NeXus file represented as a
tree structure.

![](Hierarchy.gif "Hierarchy.gif")

Note that each data item is identified by a name, e.g., counts, but each
group is identified both by a name and, in parentheses, a class
identifier, e.g., monitor (NXmonitor). The class names, which all begin
with NX, define the sort of data items that the group should contain, in
this case, counts from a beamline monitor. The hierarchical design, with
data items nested in groups, makes it easy to identify information if
you are browsing through a file.

#### Important Classes

Here are some of the important classes found in nearly all NeXus files.
A complete list can be found in the [NeXus Design
page](Design "wikilink").

NXentry:The top level of any NeXus file contains one or more groups with the class NXentry. These contain all the data that is required to describe an experimental run or scan. Each NXentry typically contains a number of groups describing sample information (class NXsample), instrument details (class NXinstrument), and monitor counts (class NXmonitor).  
NXdata:Each NXentry group contains one or more groups with class NXdata. These groups contain the experimental results in a self-contained way, i.e., it should be possible to generate a sensible plot of the data from the information contained in each NXdata group. That means it should contain the axis labels and titles as well as the data.  
NXsample:A NXentry group will often contain a group with class NXsample. This group contains information pertaining to the sample, such as its chemical composition, mass, and environment variables (temperature, pressure, magnetic field, etc.).  
NXinstrument:There might also be a group with class NXinstrument. This is designed to encapsulate all the instrumental information that might be relevant to a measurement, such as flight paths, collimations, chopper frequencies, etc.  

<center>
![](NXinstrument.gif "NXinstrument.gif")

</center>
Since an instrument can comprise several beamline components each
defined by several parameters, they are each specified by a separate
group. This hides the complexity from generic file browsers, but makes
the information available in an intuitively obvious way if it is
required.

#### Simple Example

NeXus data files do not need to be complicated. In fact, the following
diagram shows an extremely simple NeXus file that could be used to
transfer data between programs.

![](simple.gif "simple.gif")

This illustrates the fact that the structure of NeXus files is extremely
flexible. It can accommodate very complex instrumental information, if
required, but it can also be used to store very simple data sets.

### A Set of Instrument Definitions

If the design principles are followed, it will be easy for anyone
browsing a NeXus file to understand what it contains, without any prior
information. However, if you are writing visualization or analysis
software, you will need to know precisely what information is contained
in advance. For that reason, NeXus provides a way of defining the format
for particular instrument types, e.g., time-of-flight small angle
neutron scattering. This requires some agreement by the relevant
communities, but would allow the development of much more portable
software.

These instrument definitions are being formalized as XML files, using a
specially devised syntax that specifies the names of data items, and
whether they are optional or required. The following is an example of
such a file for the simple NeXus file shown above.

    <?xml version="1.0" ?> 
    <!--
    URL: http://www.neutron.anl.gov/nexus/xml/simple.xml
    Editor: Ray Osborn <ROsborn@anl.gov>
    $Id$

    A very simple NeXus file

    -->
    <NXentry name="{Name of entry}">
       <NXdata name="{Name of data}">
         <time_of_flight units="microseconds" type="NX_FLOAT32[i]">{Time-of-flight}</time_of_flight>
         <data type="NX_INT32[i]" axes="time_of_flight"> {Counts} </data>
       </NXdata>
    </NXentry>

If you want to define the format of a particular type of NeXus file for
your own use, e.g. as the standard output from a program, you are
encouraged to “publish” the format using this XML format.
