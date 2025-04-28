---
title: NIAC2006 TOF Group
permalink: NIAC2006_TOF_Group.html
layout: wiki
---
NIAC2006 TOF Group
==================

Time-of-Flight Working Group
----------------------------

-   [Freddie Akeroyd] (Freddie_Akeroyd.html "wikilink")
-   [Franck Cecillon] (Franck_Cecillon.html "wikilink")
-   [Ray Osborn] (Ray_Osborn.html "wikilink")
-   [Peter Peterson] (Peter_Peterson.html "wikilink")
-   [Thomas Proffen] (Thomas_Proffen.html "wikilink")
-   [Jiro Suzuki] (Jiro_Suzuki.html "wikilink")

This group was charged with discussing matters arising from the [NXTOFRW
- NeXus Time-of-Flight Raw File Format (simple sit and count
case)](TOFRaw.html "wikilink") proposal in preparation for a full group
discussion.

Summary of main proposals in [TOFRaw](TOFRaw.html "wikilink")
--------------------------------------------------------

1.  Some new meta-data names in NXentry for archiving and cataloguing of
    data
2.  Some thoughts about scans (now moved to
    [NXTOFRWSC](TOFRawScan.html "wikilink") and being considered by the
    [Scanning Group] (Scanning_Group.html "wikilink"))
3.  General and Area detector specific NXdetector
4.  Additional options for specifying pixel geometry with area detectors
    (edges, corners, etc.)
5.  New NXdetector\_groups class for logically grouping and labelling
    detector elements
6.  Representing hardware ganging of detectors

General, linear and Area detector specific NXdetector
-----------------------------------------------------

In all the definitions below we will leave out the Time-of-flight array
index as what we are discussing is equally valid for non time-of-flight
instruments. One new member of type NXgeometry called **origin** is
introduced into all NXdetectors - this member is used to define a
logical centre of the detector and its [NXshape] (NXshape.html "wikilink")
member defines a bounding box for the whole detector bank/array. If the
[NXgeometry] (NXgeometry.html "wikilink") instance **geometry** within
NXdetector is used to specify pixel locations, it should be define
positions relative to this detector origin.

### Inheritance of definitions

To aid with making definitions clearer we spent some time considereing
an inheritance system for NeXus. One method would be to use a period (.)
in a class name to denote inheritance and so define classes called
NXdetector.area and NXdetector.point which would imply they inherited
from NXdetector. The API would need a minor change so that is you asked
for **getnext(“NXdetector”)** it would not look for an exact match of
this string, but look for any NeXus class that started with the prefix
“detector” and so would return either an NXdetector.area or
NXdetector.point etc. By using this (.) method the reading API does not
need to know about separately about the inheritance structure as it is
encoded in the name of the item when it is written by the API.

Though we would not introduce such inheritance into the API at thois
instance, it is something that is needed. For the moment we will just
have an NXdetector with the **layout** variable indicating the type
(area, point or linear)

### NXgeometry revisited

Before giving the definitions a quick recap of
[NXgeometry](NXgeometry_and_NXshape_-_documentation_and_review.html "wikilink") is in order. This class, through its
members [NXtranslation] (NXtranslation.html "wikilink"),
[NXorientation] (NXorientation.html "wikilink") and
[NXshape](NXgeometry_and_NXshape_-_documentation_and_review.html "wikilink"), allows the position, orientation and
physical extent (size) of an object, or set of objects, to be specified.
Translation and orientation can be relative i.e. with respect to an
arbitrary origin whihc is just another
[NXgeometry](NXgeometry_and_NXshape_-_documentation_and_review.html "wikilink") object which defines a point in
space and a set of default axes directions. When we write
**NXgeometry\[i\]** in the definitions below we do not mean an array of
NXgeometry object (which is not allowed by NeXus) - instead we are using
this as shorthand for indexing the **numobj** array dimension the
[NXtranslation] (NXtranslation.html "wikilink"),
[NXorientation] (NXorientation.html "wikilink") and
[NXshape] (NXgeometry_and_NXshape_-_documentation_and_review.html "wikilink") objects within the
[NXgeometry] (NXgeometry_and_NXshape_-_documentation_and_review.html "wikilink")

### Type 1: Point Detector

A point detector is the most general case and represents a collection of
pixels **i** over some surface. Within the NXdetector all pixels
properties would be indxed by **i** e.g.:

-   NX\_CHAR layout = “point” (Really an Enum)
-   NX\_INT counts\[i\]
-   NX\_FLOAT polar\_angle\[i\]
-   NX\_FLOAT distance\[i\]
-   NX\_FLOAT solid\_angle\[i\]

If desired, additional information about each pixel (shape, engineering
position) can be added via an

-   NXgeometry geometry\[i\] \# for each pixel

instance **geometry**. Any detector can be represented by this general
case, though in the case of e.g. flat rectangualar detectors it is
useful to make use of simplifications introduced by this topology (see
below).

### Type 2: linear Detector

Here we mean a collection of linear straight strips e.g. tubes. We have
two indicies: **j** will label the strip/tube and **i** the position
along the tube. All tubes must have the same number of pixels; if not,
you must use the point detector representation above. The tubes do not
need to be parallel - they just need to be straight. Thus:

-   NX\_CHAR layout = “linear” (Really an Enum)
-   NX\_INT counts\[j,i\]
-   NX\_FLOAT polar\_angle\[j,i\]
-   NX\_FLOAT distance\[j,i\]
-   NX\_FLOAT solid\_angle\[j,i\]

So far this just looks like the point detector, but with two array
indices rather than one. However when we start adding geometry
information the differences become more clear. As the tubes are straight
we need only specify a location of the tube centre and an offset along
the tube. Thus:

-   NXgeometry geometry\[j\] \# defines tube/strip centre; each NXshape
    member give the tube size and shape; each NXorientation member
    rotates the axes such that **x** points along each tube.
-   pixel\_offset\[i\] \# offset from tube centre of each pixel centre
-   pixel\_size\[i\] \# size of each pixel

### Type 3: Area Detector

Here we have a rectangle for which each position can be defined by two
indices: **i** will label the pixel along the local detector **x** axis
and **j** the pixel along the local y axis. Using a third index **k**
allows us to represent a group of such detectors so:

-   NX\_CHAR layout = “area” (Really an Enum)
-   NX\_INT counts\[k,j,i\]
-   NX\_FLOAT polar\_angle\[k,j,i\]
-   NX\_FLOAT distance\[k,j,i\]
-   NX\_FLOAT solid\_angle\[k,j,i\]

As the detector is a rectangle we just need to specdify x and y offsets
from the centre to indicate each pixel. Thus:

-   NXgeometry geometry\[k\] defines each detector centre and extent
-   pixel\_offset\_x\[k,i\] \# offset from detector centre of each
    pixel's x centre
-   pixel\_offset\_y\[k,j\] \# offset from detector centre of each
    pixel's y centre
-   pixel\_size\_x\[k,i\] \# x extent of pixel
-   pixel\_size\_y\[k,j\] \# y extent of pixel

Hardware detector ganging
-------------------------

[TOFRaw](TOFRaw.html "wikilink") originally suggested using an **\_unganged**
suffix on the ungrouped elements e.g. polar\_angle\_unganged. It was
decided that creating a substructure within the NXdetector and putting
the information there was better so we will now have e.g.

-   detector.counts\[i\] - grouped values
-   detector.polar\_angle\[i\] - grouped values
-   detector.detector\_number\[i\] - identifier for each grouped
    detector
-   detector.gang.polar\_angle\[j\] - raw values
-   detector.gang.detector\_number\[j\] - identifier for each raw
    detector

As for showing the mapping scheme, a simple scheme would be

-   detector.gang.grouping\[j\] - gives the grouped value **i**
    appropriate for each detector element **j** (only allows 1-&gt;1
    mapping)

<!-- -->

-   An alternative is the gang\_count and gang\_index method in
    [TOFRaw](TOFRaw.html "wikilink"), but this does require sorting of the
    polar\_angle etc. arrays prior to writing to the file

Proposals
---------

1.  That the new data items in required in NXentry and NXuser for
    archiving be ratified. [Laurent
    Lerusse] (L.lerusse.html "wikilink") has volunteered to produce a
    description such that any instruement definition that wishes can
    “conform to” this.
2.  That NeXus implement inheritance in definitions and classes by a
    method yet to be finalised.
3.  That the three types of detector representation are accepted

