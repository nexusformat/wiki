---
title: Detector Geometry
permalink: Detector_Geometry.html
layout: wiki
---
Detector Geometry
=================

Issue
-----

Defining the location of a detector, or any generic object, is
potentially challenging. It needs to be agreed upon how to define the
location of an object, specifically detectors, and their phsyical
extent. Proposals should be able to define a position unambigiously in a
way that is easily interpreted by analysis and plotting software.

Proposal: McStas
----------------

Taken from the McStas manual p45:

The instrument is given a global, absolute coordinate system. In
addition, every component in the instrument has its own local coordinate
system that can be given any desired position and orientation (though
the position and orientatino must remain fixed for the duration of a
single simulation). By convention, the z axis points in the direction of
the beam, the x axis is perpendicular to the beam in the horizontal
plane pointing left as seen from the source, and the y axis points
upwards (see figure 5.1). Nothin in McStas enforces this convention, but
if every component used different conventions the user would be faced
with a severe headacha! It is therefore recommended that this convention
is followed by users implementing new components.

Proposal: Vitess
----------------

### Determined from a figure on p6

The x axis points in the direction of the beam, the z axis up, and the y
axis to the left while facing down-stream to complete the right handed
coordinate system.

### Determined from a figure on p22

Orientation is given by two angles which define a component's normal
direction. phi is the angle between the x axis and the normal, projected
onto the xy plane. theta is the angle between the xy plane and the
normal. This does assume that a normal direction is well defined.

[Peter Peterson] (Pfpeterson.html "wikilink") Thursday, 28 August 2003,
12:04:51 pm

Conclusion
----------

01/2015 This got nowhere. It is also now obsolete as NIAC is under the
impression that the CIF-style coordinate description allows us to define
the position and orientation of detector elements in space in an
adequate and exact way.
