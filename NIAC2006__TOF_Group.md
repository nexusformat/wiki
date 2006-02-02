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

This group was charged with discussing the proposed
[TOFRaw](TOFRaw "wikilink") in preparation for a full group discussion.

Inheritance
-----------

We would use a period (.) in a class name to denote inheritance and so
define classes called NXdetector.area and NXdetector.point which would
imply they inherited from NXdetector. The API would need a minor change
so that is you asked for **getnext(“NXdetector”)** it would not look for
an exact match of this string, but look for any NeXus class that started
with the prefix “detector” and so would return either an
NXarea\_detector or NXpoint\_detector etc.

Following an inheritance system would allow for clearer definitions

NXdetector
----------

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
