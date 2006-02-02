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

e.g. define NXarea\_detector and NXpoint\_detector as inheriting from
NXdetector; the API would need to have knowledge of the inheritance
hierarchy so that the function **getnext(“NXdetector”)** would return
either an NXarea\_detector or NXpoint\_detector etc.

Following an inheritance system would allow for clearer definitions

Implementation would be via a group attribute that would be written at
object creation by the NeXus API. The API would come with a description
of the current inheritance hierarchy and all parents of a class would be
written to the new attribute, which would then be used by e.g. the
**getnext** function

NXdetector
----------

Three types: NXpoint\_detector, NXlinear\_detector and NXarea\_detector

NXpoint\_detector
-----------------

A collection of pixels **i** over some surface. Defined by:

polar\_angle\[i\] distance\[i\] solid\_angle\[i\]

If desired, additional information about pixels (shape, engineering
position) can be added via an NXgeometry\[i\]
