---
title: FAQ
permalink: FAQ.html
layout: wiki
---
FAQ
===

This is a list of commonly asked questions concerning the NeXus data
format. If you wish to suggest any more questions to include on this
page, please visit the [discussion page](FAQ.html "wikilink") and add an
entry.

How many facilities use NeXus
-----------------------------

This is continually evolving. It has been used as the instrument format
for several years on some or all instruments at a number of facilities
including PSI (Switzerland), LLB (France), LANSCE (USA), and APS (USA).
It will be used on all future instrumentation at ISIS (UK), NIST (USA),
ANSTO (Australia) and was used by instruments using the new data
acquisition system at IPNS (USA). Finally, it has been formally adopted
by major facilities under construction, the SNS (USA), JPARC (Japan) and
Diamond Light Source (UK). For more information see the
[Facilities](Facilities.html "wikilink") page.

NeXus files are only useful for archiving instrumental data, aren't they?
-------------------------------------------------------------------------

NeXus files can be used to store both extremely simple data, e.g. a
single (x,y) array, and highly complex instrument descriptions. In fact,
the original intention of the NeXus data format was to provide a way of
interchanging data between facilities and their user communities.
However, the power of NeXus hierarchical design has led to its adoption
as a standard archiving format by several major facilities, such as
ISIS, LANSCE, and the SNS.

Why aren't NXsample and NXmonitor groups stored in the NXinstrument group?
--------------------------------------------------------------------------

A NeXus file can contain a number of NXentry groups, which may represent
different scans in an experiment, or sample and calibration runs, etc.
In many cases, though by no means all, the instrument has the same
configuration so that it would be possible to save space by storing the
NXinstrument group once and using multiple links in the remaining
NXentry groups. It is assumed that the sample and monitor information
would be more likely to change from run to run, and so should be stored
at the top level.

How do I identify the plottable data?
-------------------------------------

Any program whose aim is to identify plottable data should use the
following procedure:

1.  Open the first top level NeXus group with class NXentry.
2.  Open the first NeXus group with class NXdata.
3.  Loop through NeXus data items in this group searching for the item
    with attribute “signal” =1. This is the plottable data.
4.  Check to see if this data item has an attribute called “axes”. If
    so, the names are defined as a comma-delimited string within this
    attribute in the C-order of the data array, and you can skip the
    next two steps.
5.  If the “axes” attribute is not defined, search for the
    one-dimensional NeXus data items with attribute “primary” = 1.
    \#These are the dimension scales to label the axes of each dimension
    of the data.
6.  Link each dimension scale to the respective data dimension by the
    “axis” attribute (= 1,2,...,rank of data).
7.  If necessary, close the NXdata group, open the next one and repeat
    steps 3 to 6.
8.  If necessary, close the NXentry group, open the next one and repeat
    steps 2 to 7.

Consult the NeXus API section, which describes the routines available to
program these operations. In the course of time, generic NeXus browsers
will provide this functionality automatically.

Why are the NeXus classes so complicated? I'll never store all that information
-------------------------------------------------------------------------------

The NeXus classes are essentially glossaries of terms. If you need to
store a piece of information, consult the class definitions to see if it
has been defined. If so, use it. However, it is not compulsory to
include every item that has been defined if it is not relevant to your
experiment. On the other hand, if there is an NeXus definition for your
instrument, you are recommended to include all the compulsory items if
you want to use standard software to analyze your data.

I want to produce an instrument definition. How do I go about it?
-----------------------------------------------------------------

The first thing is to check whether the instrument you are interested in
is already being defined by an instrument editor. Check the list on the
NeXus Instruments page. The [NeXus International Advisory
Committee](NIAC.html "wikilink") is responsible for appointing editors of
special interest groups that wish to become a part of the standard, so
contact the [Executive Secretary](NIAC.html "wikilink"), if a group does not
yet exist. Of course, if you want to produce your own private definition
for personal use, you are free to do so without our approval although we
encourage people to share what they are doing . If you are an editor,
the process of defining an instrument should be quite simple:

1.  Make sure that the data you wish to analyze are stored in NXdata
    groups. The rest of the definition is to supply what is necessary
    for simple analysis of the data, for example, the detector positions
    and incident wavelength for a x-ray powder diffraction measurement.
2.  Study the base classes to decide which ones are essential for your
    definition. If you believe that a new base class is needed, contact
    the NIAC with a proposal.
3.  Select those data items and groups that you consider important in
    analyzing data from your instrument.

Insert the relevant grep character, as defined in the [NeXus Meta-DTD
format](Metaformat.html "wikilink") to denote the number of occurrences. If
the item is optional (“?” or “\*”), then it does not need to be added to
your definition.

1.  If you encounter any problems because the classes are not sufficient
    to describe your configuration, please contact the NIAC Executive
    Secretary explaining the problem, and post a suggestion at the
    relevant class wiki page. The NIAC is always willing to consider
    proposals to amend the base classes. The procedures are defined in
    the NIAC constitution.

What coordinate system does NeXus use?
--------------------------------------

This is described on the
[Coordinate\_Systems] (Coordinate_Systems.html "wikilink") page
