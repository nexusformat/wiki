---
title: TOFRawScan
permalink: TOFRawScan.html
layout: wiki
---
TOFRawScan
==========

NXTOFRWSC - proposed extensions to NXTOFRW to provide a NeXus
Time-Of-Flight Raw Data File Scan Format

Introduction
------------

This document defines extensions to the [single run
format](TOFRaw.html "wikilink") to deal with scans and ISIS period type
experiments; the same conventions used there apply here.

### NXentry

One question that is the subject of much debate is whether a single
NXentry should only describe a single measurement or whether it could
contain several measurements. The single measurement case is outlined in
[TOFRaw](TOFRaw.html "wikilink") and we outline here two possible methods of
storing multiple measurements.

#### Type 1: linking entries to describe scans

Often each scan point will be written as an NXentry in a separate file
e.g. the scan is controlled by some external script. In this case all
that is needed is:

1.  a way to identify which files belong together
2.  preferably, a way to quickly identify what is changing during the
    scan without having to compare all items in the file

A suggestion for (1) is to have a “scan\_id” variable so that all files
with the same value of “scan\_id” will form part of the same scan; the
element scan\_point will indicate the scan point (1, 2, 3, …). If
scan\_id is set to the “run\_number” of the first scan point, it will be
guaranteed not to conflict with any other scans or run as the run number
is unique for a given file (and often part of the file name).

| RE  | Name                                | Attribute | Type     | Value | Description                                                                                                          |
|-----|-------------------------------------|-----------|----------|-------|----------------------------------------------------------------------------------------------------------------------|
| 0/1 | <font color=red>Scan\_id</font>     |           | NX\_INT  |       | Allows Entries that are part of the same scan to be identified. This could be the run number of the first scan point |
| 0/1 | <font color=red>Scan\_point</font>  |           | NX\_INT  |       | the point within a scan. 1=first, 2=second etc                                                                       |
| 0/1 | <font color=red>Scan\_total</font>  |           | NX\_INT  |       | Number of points in this scan i.e. number of separate NXentries making up the scan                                   |
| 0/1 | <font color=red>Scan\_labels</font> |           | NX\_CHAR |       | comma separated list of titles/labels for each scan point                                                            |

For (2) above there are two choices: either tag each variable that is
being varied with an extra attribute called e.g. “scanned”, or link all
the variables that are being scanned into an “NXscan” structure. If an
NXscan structure is decided on, then scan\_id above should probably be
moved into this rather than be in NXentry.

In the case of a scan of two variables, we could set scanned=1 for the
fastest varying variable and scanned=2 for the second fastest etc. Note
that the notion of “fastest varying” depends, of course, on the order
that you read the files in - this notion tells you which is varying
fastest if the files are read in numerical run number order. Note that
the “scanned variable” is a hint to the reading program and tells you
what is being scanned over the whole measurement - if you just picked
two files at random then only one of the many marked “scanned” variables
would have changed and it is up to the reading program to work out which
one.

If several NXentry objects are written to the same file to describe scan
points, it would be useful to have a naming convention so that they
could be ordered quickly. NeXus convention is that entries are called
“entry1”, “entry2”, … maybe for scans this could be extended to
“entry1\_1”, “entry1\_2” for scan points 1 and 2 etc.

#### Type 2: containing multiple measurements

*Note: we are considering splitting “single measurement” and “scan” into
separate definitions - see the **discussion** tab for more information*

Sometimes a scan is set up and directed by the data acquisition
electronics itself. An example would be when you want to perform a very
rapid scan of e.g. temperature or to rapidly swap between two states
(e.g. laser on and laser off). What is different about this situation
compared to above is that no data is transferred from the acquisition
system (and so no file written) until the scan is complete. Such a
situation could be treated by the same mechanism as above, but has
traditionally been done by adding an extra array dimension to the data
and the varying variables rather than writing additional files.

To illustrate this rather than having “entry1.sample.temperature”,
“entry1.detector.counts\[i\]”, “entry2.sample.temperature” and
“entry2.detector.counts\[i\]” we would just have
“entry1.sample.temperature\[j\]” and “entry1.detector.counts\[i,j\]”
where j indexes the scan point. Advantages of this scheme over writing
seapare NXentries to a single file are:

-   If you have very many scan points, you don’t get a huge number of
    NXentry structures that you need to search to get the list of
    scanned values
-   Your scanned variables are already stored as arrays and so can
    easily be plotted i.e. counts\[1,j\] against temperature\[j\]
-   You don’t have a huge number of linked entries in the file - links
    can cause wasted memory if all the objects in the file are loaded
    into computer memory by a language that cannot represent the links
    internally and so must create copies.
-   you don't have to think about having multiple copies of, or how to
    split, any time dependent NXlog objects bewteen NXentries
-   you can easily load all the data for all scans into memory in one go
-   data analysis is more straightforward

You still need a mechanism to indicate scanned variables (either a
scanned attribute or an NXscan structure as described above). Several of
the above variables in NXentry will also become arrays of size (number
of scan points, scan\_total) e.g. raw\_frames, good\_frames,
scan\_point. As the counts array that appears within NXdata now depends
on the the scan index \[j\], you will need to link in additional
axis/axes to the NXdata to indicate this dependence. For this you could
link in the scan\_point\[j\] array or the individual temperature\[j\],
magnetic\_field\[j\] etc. arrays depending on how you want to plot your
data.

As as it is possible cycle rounds the scans and continue counting a
particular scan point at a later stage, the following new variable is
introduced:

|     |                                     |     |              |     |                                                                      |
|-----|-------------------------------------|-----|--------------|-----|----------------------------------------------------------------------|
| 1   | <font color=red>scan\_cycles</font> |     | NX\_INT\[j\] |     | Number of times a data acquisition was initiated for this scan point |

### NXsample

Some variables describing sample environment parameters may become
arrays with a Type 2 NXentry e.g.

| RE  | Name        | Attribute | Type               | Value | Description |
|-----|-------------|-----------|--------------------|-------|-------------|
| 0/1 | temperature |           | NX\_FLOAT\[nscan\] |       |             |

### NXdetector

If detetor angles are scanned, an extra array dimension may be present
with a Type 2 NXentry e.g.

| RE  | Name             | Attribute | Type                 | Value                | Description |
|-----|------------------|-----------|----------------------|----------------------|-------------|
| 1   | Polar\_angle     |           | NX\_FLOAT\[i,nscan\] |                      |             |
| 0/1 | Azimuthal\_angle |           | NX\_FLOAT\[i,nscan\] |                      |             |
| 0/1 | Distance         |           | NX\_FLOAT\[i,nscan\] | distance from sample |             |


