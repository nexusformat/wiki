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

Inheritance
-----------

We would use a . in a class name to denote inheritance and so define
classes called NXdetector.area and NXdetector.point which would imply
they inherited from NXdetector. The API would need a minor change so
that is you asked for **getnext(“NXdetector”)** it swould not look for
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

NXgeometry\[i\] defines tube centre offet\[j+1\] or offset\[i,j+1\]
defines edges of tube pixels

NXdetector.area
---------------

NXgeometry defines tube centre xoffet\[i+1\] and yoffset\[j+1\] defines
edges of pixels
