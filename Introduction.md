---
title: Introduction
permalink: Introduction/
layout: wiki
---

In recent years, a number of scientists and computer programmers working
in neutron and synchrotron facilities around the world came to the
conclusion that a common data format would fulfil a valuable function in
the scattering community. As instrumentation becomes more complex and
data visualization become more challenging, individual scientists, or
even institutions, have found it difficult to keep up with new
developments. A common data format makes it easier, both to exchange
experimental results and to exchange ideas about how to analyze them. It
promotes greater cooperation in software development and stimulate the
design of more sophisticated visualization tools.

This section is designed to give a brief introduction to NeXus, the data
format that has been developed in response to these needs. It explains
what a modern data format such as NeXus is and how to write simple
programs to read and write NeXus files. More detailed descriptions are
contained in other sections. This page addresses three questions:

-   What is NeXus?
-   How do I write a NeXus file?
-   How do I read a NeXus file?

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
label “wavelength”, storing the result in the variable lambda. fileID is
a file identifier that is provided by NeXus when the file is opened.

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

Note that each data item is identified by a name, e.g., counts, but each
group is identified both by a name and, in parentheses, a class
identifier, e.g., monitor (NXmonitor). The class names, which all begin
with NX, define the sort of data items that the group should contain, in
this case, counts from a beamline monitor. The hierarchical design, with
data items nested in groups, makes it easy to identify information if
you are browsing through a file.

#### Important Classes

NXentry:The top level of any NeXus file contains one or more groups with the class NXentry. These contain all the data that is required to describe an experimental run or scan. Each NXentry typically contains a number of groups describing sample information (class NXsample), instrument details (class NXinstrument), and monitor counts (class NXmonitor).  
NXdata:Each NXentry group contains one or more groups with class NXdata. These groups contain the experimental results in a self-contained way, i.e., it should be possible to generate a sensible plot of the data from the information contained in each NXdata group. That means it should contain the axis labels and titles as well as the data.  
NXsample:A NXentry group will often contain a group with class NXsample. This group contains information pertaining to the sample, such as its chemical composition, mass, and environment variables (temperature, pressure, magnetic field, etc.).  
NXinstrument:There might also be a group with class NXinstrument. This is designed to encapsulate all the instrumental information that might be relevant to a measurement, such as flight paths, collimations, chopper frequencies, etc.  

Since an instrument can comprise several beamline components each
defined by several parameters, they are each specified by a separate
group. This hides the complexity from generic file browsers, but makes
the information available in an intuitively obvious way if it is
required.

#### Simple Example

NeXus data files do not need to be complicated. In fact, the following
diagram shows an extremely simple NeXus file that could be used to
transfer data between programs.

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
<NXentry name="{Name of entry}">  
`         `<NXdata name="{Name of data}">  
`                  `<time_of_flight units="microseconds" type="NX_FLOAT32[i]">`{Time-of-flight} `</time_of_flight>  
`                  `<data type="NX_INT32[i]" >` {Counts} `</data>  
`         `</NXdata>  
</NXentry>

If you want to define the format of a particular type of NeXus file for
your own use, e.g. as the standard output from a program, you are
encouraged to “publish” the format using this XML format.

How do I write a NeXus file?
----------------------------

The NeXus Application Program Interface (API) provides a set of
subroutines that make it easy to read and write NeXus files. These
subroutines are available in C, Fortran 77, Fortran 90, Java, and IDL.
Access from other languages, such as Python, is anticipated in the near
future. It is also possible to read NeXus files in a number of data
analysis tools, such as LAMP, ISAW, and open Genie.

The API uses a very simple “state” model to navigate through a NeXus
file. When you open a file, the API provides a file “handle”, which then
stores the current location, i.e. which group and/or data item is
currently open. Read and write operations then act on the currently open
entity. In the following, we walk through some parts of a typical NeXus
program written in C. See the API section for a more complete version.

First, it is necessary to open the file, specifying whether we want read
or write access.

1.  include “napi.h”

`int main()`  
`{`  
`  NXhandle fileID;`  
`  NXopen ('NXfile.nxs', NXACC_CREATE, &fileID);`

The file is opened with “create” access (implying write access), and the
API returns a file identifier of type NXhandle. Next, we create an
NXentry group to contain the scan using NXmakegroup and then open it for
access using NXopengroup.

` NXmakegroup (fileID, `“`Entry`”`, `“`NXentry`”`);`  
` NXopengroup (fileID, `“`Entry`”`, `“`NXentry`”`);`

The plottable data is contained within an NXdata group, which must also
be created and opened.

` NXmakegroup (fileID, `“`Data`”`, `“`NXdata`”`);`  
` NXopengroup (fileID, `“`Data`”`, `“`NXdata`”`);`

To create a data item, call NXmakedata, specifying the data name, type
(NX\_FLOAT32), rank (in this case, 1), and length of the array (n\_t).
Then, it can be opened for writing.

` NXmakedata (fileID, `“`time_of_flight`”`, NX_FLOAT32, 1, &n_t);`  
` NXopendata (fileID, `“`time_of_flight`”`)`

Then write the data using NXputdata.

` NXputdata (fileID, t);`

With data item is still open, we can also add some data attributes, such
as the data units, which are specified as a character string (type
NX\_CHAR) that is 12 bytes long.

` NXputattr (fileID, `“`units`”`, `“`microseconds`”`, 12, NX_CHAR);`

Then we close the data item before opening another. In fact, the API
will do this automatically if you attempt to open another data item, but
it is better style to close it yourself.

` NXclosedata (fileID);`

The remaining data items in this group are added in a similar fashion.
Note that the indentation whenever a new data item or group are opened
is just intended to make the structure of the NeXus file more
transparent.

`    NXmakedata (fileID, `“`phi`”`, NX_FLOAT32, 1, &n_p);`  
`      NXopendata (fileID, `“`phi`”`);`  
`        NXputdata (fileID, phi);`  
`        NXputattr (fileID, `“`units`”`, `“`degrees`”`, 7, NX_CHAR);`  
`      NXclosedata (fileID);`  
`      dims[0] = n_t;`  
`      dims[1] = n_p;`  
`      NXmakedata (fileID, `“`counts`”`, NX_INT32, 2, dims);`  
`      NXopendata (fileID, `“`counts`”`);`  
`        NXputdata (fileID, counts);`  
`      NXclosedata (fileID);`

Finally, close the groups (NXdata and NXentry) before closing the file
itself.

`  NXclosegroup (fileID);`  
`  NXclosegroup (fileID);`  
`  NXclose (&fileID);`  
`  return;`

}

How do I read a NeXus file?
---------------------------

Reading a NeXus file is almost identical to writing one. Obviously, it
is not necessary to call NXmakedata since the item already exists, but
it is necessary to call one of the query routines to find out the rank
and length of the data before allocating an array to store it.

Here is part of a program to read the time-of-flight array from the file
created by the example above.

`NXopen ('NXfile.nxs', NXACC_READ, &fileID);`  
`  NXopengroup (fileID, `“`Entry`”`, `“`NXentry`”`);`  
`    NXopengroup (fileID, `“`Data`”`, `“`NXdata`”`);`  
`      NXopendata (fileID, `“`time_of_flight`”`);`  
`        NXgetinfo (fileID, &rank, dims, &datatype);`  
`        NXmalloc ((void **) &tof, rank, dims, datatype);`  
`        NXgetdata (fileID, tof);`  
`      NXclosedata (fileID);`  
`    NXclosegroup (fileID);`  
`  NXclosegroup (fileID);`  
`NXclose (fileID);`

NeXus files can also be viewed by a command-line browser, NXbrowse,
which is included with the NeXus API. The following is an example
session of using NXbrowse to view a data file from the LRMECS
spectrometer at IPNS. The following commands are used (see the NXbrowse
web page ):

### Command Description

dir:List the contents of the current group  
open Histogram1:Open the NeXus group “Histogram1”  
read title:Print the contents of the NeXus data labelled “title”  
close:Close the current group  
quit:Quit the browser  

`%> NXbrowse lrcs3701.nxs`

`NXBrowse 2.0.0. Copyright (C) 2000 R. Osborn, M. Koennecke, P. Klosowski`  
`   NeXus_version = 1.3.3`  
`   file_name = lrcs3701.nxs`  
`   file_time = 2001-02-11 00:02:35-0600`  
`   user = EAG/RO`  
`NX> dir`  
` NX Group : Histogram1 (NXentry)`  
` NX Group : Histogram2 (NXentry)`  
`NX> open Histogram1`  
`NX/Histogram1> dir`  
` NX Data  : title[44] (NX_CHAR)`  
` NX Data  : analysis[7] (NX_CHAR)`  
` NX Data  : start_time[24] (NX_CHAR)`  
` NX Data  : end_time[24] (NX_CHAR)`  
` NX Data  : run_number (NX_INT32)`  
` NX Group : sample (NXsample)`  
` NX Group : LRMECS (NXinstrument)`  
` NX Group : monitor1 (NXmonitor)`  
` NX Group : monitor2 (NXmonitor)`  
` NX Group : data (NXdata)`  
`NX/Histogram1> read title`  
` title[44] (NX_CHAR) = MgB2 PDOS 43.37g 8K 120meV E0@240Hz T0@120Hz`  
`NX/Histogram1> open data`  
`NX/Histogram1/data> dir`  
` NX Data  : title[44] (NX_CHAR)`  
` NX Data  : data[148,750] (NX_INT32)`  
` NX Data  : time_of_flight[751] (NX_FLOAT32)`  
` NX Data  : polar_angle[148] (NX_FLOAT32)`  
`NX/Histogram1/data> read time_of_flight`  
` time_of_flight[751] (NX_FLOAT32) = [ 1900.000000 1902.000000 1904.000000 ...]`  
`   units = microseconds`  
`   long_name = Time-of-Flight [microseconds]`  
`NX/Histogram1/data> read data`  
` data[148,750] (NX_INT32) = [ 1 1 0 ...]`  
`   units = counts`  
`   signal = 1 `  
`   long_name = Neutron Counts`  
`   axes = [polar_angle,time_of_flight]`  
`NX/Histogram1/data> close`  
`NX/Histogram1> close`  
`NX> quit`

The source code provides an example of how to write a NeXus reader. The
test programs included in the NeXus API may also be useful to study.

### Where to go from here?

The other sections of this web site give much more detailed descriptions
of the NeXus data format.

NeXus Design:This describes NeXus' hierarchical design, and gives more information on how to construct valid groups.  
NeXus API:This describes the NeXus programming interface, with lists of all the subroutines and supported languages.  
