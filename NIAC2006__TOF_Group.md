---
title: NIAC2006: TOF Group
permalink: NIAC2006:_TOF_Group/
layout: wiki
---

Time-of-Flight Working Group
----------------------------

-   [Freddie Akeroyd](User%3AFreddie_Akeroyd "wikilink")
-   [Franck Cecillon](User%3AFranck_Cecillon "wikilink")
-   [Ray Osborn](User%3ARay_Osborn "wikilink")
-   [Peter Peterson](User%3APeter_Peterson "wikilink")
-   [Thomas Proffen](User%3AThomas_Proffen "wikilink")
-   [Jiro Suzuki](User%3AJiro_Suzuki "wikilink")

This group was charged with discussing matters arising from the [NXTOFRW
- NeXus Time-of-Flight Raw File Format (simple sit and count
case)](TOFRaw "wikilink") proposal in preparation for a full group
discussion.

Summary of main proposals in [TOFRaw](TOFRaw "wikilink")
--------------------------------------------------------

1.  Some new meta-data names in NXentry for archiving and cataloguing of
    data
2.  Some thoughts about scans (now moved to
    [NXTOFRWSC](TOFRawScan "wikilink") and being considered by the
    [Scanning Group](Scanning_Group "wikilink"))
3.  General and Area detector specific NXdetector
4.  Additional options for specifying pixel geometry with area detectors
    (edges, corners, etc.)
5.  New NXdetector\_groups class for logically grouping and labelling
    detector elements
6.  Representing hardware ganging of detectors

General and Area detector specific NXdetector
---------------------------------------------

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
[NXgeometry](NXgeometry "wikilink") is in order. This class, through its
members [NXtranslation](NXtranslation "wikilink"),
[NXorientation](NXorientation "wikilink") and
[NXshape](NXshape "wikilink"), allows the position, orientation and
physical extent (size) of an object, or set of objects, to be specified.
Translation and orientation can be relative i.e. with respect to an
arbitrary origin whihc is just another
[NXgeometry](NXgeometry "wikilink") object which defines a point in
space and a set of default axes directions. When we write
NXgeometry\[i\] in the definitions below we do not mean an array of
NXgeometry object (which is not allowed by NeXus) - instead we are using
this as shorthand for indexing the **numobj** array dimension the
[NXtranslation](NXtranslation "wikilink"),
[NXorientation](NXorientation "wikilink") and
[NXshape](NXshape "wikilink") objects within the NXgeometry

Three types: point, linear and area

NXdetector.point
----------------

A collection of pixels **i** over some surface. Defined by:

polar\_angle\[i\] distance\[i\] solid\_angle\[i\]

If desired, additional information about pixels (shape, engineering
position) can be added via an NXgeometry\[i\]

NXdetector.linear
-----------------

NXgeometry\[i\] defines tube centre and pixel\_edge\[j+1\] defines the
edges of the pixels - if a pixel\_size\[j\] array is also present it
means the pixels have “dead space” between them

NXdetector.area
---------------

NXgeometry defines tube centre xoffet\[i+1\] and yoffset\[j+1\] defines
edges of pixels

Proposals
---------

1.  That the new data items in required in NXentry and NXuser for
    archiving be ratified. [Laurent
    Lerusse](User%3AL.lerusse "wikilink") has volunteered to produce a
    description such that any instruement definition that wishes can
    “conform to” this.
2.  That NeXus implement inheritance in definitions and classes by a
    method yet to be finalised.

