---
title: Coordinate Systems
permalink: Coordinate_Systems/
layout: wiki
---

The MARS experience showed me that it is easy to get confused about the
NeXus coordinate systems. I therefore suggest the following:

-   Remove coordinates from all component DTD
-   Make a documentation page describing our two coordinate systems:
    -   The simple polar\_angle, distance etc system
    -   The NXgeometry system
-   State that coordinate describing datasets can occur in any component
    group
-   State that one system must be used throughout the whole definition

The last point should prohibit to have both NXgeometry and simple
coordinates in one DTD. This can be confusing. As NXgeometry is anyway
intended to be used by the simulation community this should be OK.

NeXus Coordinate System
-----------------------

Nexus provide two coordinate system: an
[NXgeometry](NXgeometry "wikilink") based system for physical
coordinates of beamline components and a polar coordinate based system
for “neutronic” coordinates. The usage of these two system can be seen
by considering a 3He gas tube detector:

-   The [NXgeometry](NXgeometry "wikilink") system represents true
    spatial location and would describe a cylinder at a certain distance
    from the sample that never changes from one run to another
-   The polar system would describe the neutronic, rather than actual,
    geometry. For example, the “distance” coordinate would refer to the
    distance from the sample to an effective measurement point within
    the gas tube, which would depend on neutron energy; lower energy
    neutrons would tend to penetrate a smaller distance within the tube,
    and so have a shorter secondary flight path.

### Simple (Polar) Coordinate System

In this system the instrument is considered as a set of components
through which the incident beam passes. The variable **distance** is
assigned to each component and represents the effective beam flight path
length between this component and the sample. A sign convention is used
where -ve numbers represent components pre-sample and +ve numbers
components post-sample.

For angular information, the quantities *polar\_angle* and
*azimuthal\_angle* are used and these quantities correspond exactly to
the usual [spherical polar
coordinate](http://en.wikipedia.org/wiki/Spherical_coordinate_system)
definitions i.e. the polar\_angle is the *zenith angle* and measured
with respect to a *z* axis and the azimuthal\_angle to the *x* axis in
the xy plane. The direction of these local axes may be different for
each component: *z* is the incident beam direction for the **previous**
component and we then follow [McStas](http://mcstas.risoe.dk/) for *x*
and *y* i.e. the *x* axis is perpendicular to the beam in the horizontal
plane pointing left as seen from the source, and the y axis points
upwards (see diagram below). The *z* axis thus represents the direction
of the beam if it was un-deviated by the previous component, and so the
polar\_angle and azimuthal\_angle for a component indicate how much the
beam was bent/scattered by the previous component.

If we consider an [NXdetector](NXdetector "wikilink") element placed
directly after an [NXsample](NXsample "wikilink"), the *z* axis would be
in the direction of the beam incident on
[NXsample](NXsample "wikilink"). The polar\_angle for the
[NXdetector](NXdetector "wikilink") would be the angle between the
scattering vector and this *z* axis and so correspond to the *Bragg
angle* or *two theta* even for out-of-plane scattering. The
azimuthal\_angle would be the angle between the positive x-axis and the
scattering vector projected onto the xy-plane - scattering to the left
as seen from the source would have azimuthal\_angle=0 and scattering to
the right azimuthal\_angle=pi. The distance would correspond to what is
often called the *secondary flight path length* or *L2*.

### NXgeometry based system

This coordinate system is based on more fully on the [McStas coordinate
system](http://mcstas.risoe.dk/). The instrument is given a global,
absolute coordinate system where the z axis points in the direction of
the incident beam, the x axis is perpendicular to the beam in the
horizontal plane pointing left as seen from the source, and the y axis
points upwards. Each beamline component also has a local coordinate
system, which is defined by the [NXgeometry](NXgeometry "wikilink")
object. The local z direction for a component is taken as the incident
beam direction, with x and y defined as before i.e. the x axis is
perpendicular to the beam in the horizontal plane pointing left as seen
from the source, and the y axis points upwards. Information about these
coordinate systems and the placement of components is described by the
[NXgeometry](NXgeometry "wikilink") class via its
[NXtranslation](NXtranslation "wikilink") and
[NXorientation](NXorientation "wikilink") members.

![](Coordinates.png "Coordinates.png")

When computing a transformation, NXtranslation is applied before
NXorientation. All of our axes are right handed and orthogonal.
Orientation information is stored as direction cosines. The direction
cosines will be between the local coordinate directions and the
reference directions (to origin or relative NXgeometry). Calling the
local unit vectors (x',y',z') and the reference unit vectors (x,y,z) the
six numbers will be \[x' dot x, x' dot y, x' dot z, y' dot x, y' dot y,
y' dot z\] where “dot” is the scalar dot product (cosine of the angle
between the unit vectors). The unit vectors in both the local and
reference coordinates are right-handed and orthonormal: with this
restriction we only ned to store 6 rather than 9 direction cosines as
the z' axis can be obtained by the vector cross product of x' and y'.

The origin of coordinates is arbitrary, but all components in the file
must either agree on its absolute location or use relative positioning.
To allow for this generality, an origin member can be defined in
[NXentry](NXentry "wikilink"); its use will be detailed shortly.

We choose as our absolute the origin the scattering center, which is
where a perfectly aligned sample would be. Note that the centre of the
sample itself may not always be at this point if the sample is being
scanned across the beam. With an origin at the “scattering centre” the
spherical polar coordinate specifications of the detector positions
conveniently relates to scattering angles and lengths for direct
geometry instruments.

Individual components of the instrument (e.g. jaws) will have their own
set of local axes (x,y,z) which will be fixed to their body in a way
defined by their shape. These local axes will probably not coincide with
the global instrument axes and so a set of rotation angles will also
need to be stored. For this an [NXgeometry](NXgeometry "wikilink") class
is defined, along with [NXtranslation](NXtranslation "wikilink") and
[NXorientation](NXorientation "wikilink"); the hope is to provide a
general enough method for relating the location of any object with
respect to another object. The mechanism also allows for specifying one
position relative to another component: a NeXus file link is made in one
instance of an [NXgeometry](NXgeometry "wikilink") object to another
[NXgeometry](NXgeometry "wikilink") object and a program can then
traverse the chain of links to calculate an absolute position.

NeXus does not need to define absolutely where to place the “origin”.
All components can instead be declared with a relative position that
ultimately follows a chain back to one object; this will be named
“origin1”, be of class [NXgeometry](NXgeometry "wikilink") and a member
of [NXentry](NXentry "wikilink"). The real space location of this origin
is chosen for convenience and should be mentioned in the description
attached to “origin1”. If the origin is taken at the sample, then
“sample.geometry.distance” will always be (0,0,0) relative to “origin1”;
if the origin is taken elsewhere this will not be so, but everything
will still work. It may be convenient to define extra origins (similar
to “arms” in [McStas](http://mcstas.risoe.dk/)) at other parts of the
instrument. For example, defining one at the centre of a circular array
of detectors would allow their positions to be conveniently specified in
spherical polar coordinates. Another possibility would be to define the
sample relative to “origin1” and the detectors to “origin2”; the
detectors could then be rotated by a rotation of “origin2” without
modifying [NXdetector](NXdetector "wikilink").

As well as specifying the component location, it is also necessary to
specify the beam direction. Unless otherwise given in an
[NXbeam](NXbeam "wikilink") member of the component, the incident beam
is assumed to be travelling along (0,0,+z) in the coordinate system of
the object (or origin) our position was defined relative to. Thus, for a
component with absolute positioning the beam will always be in the
incident beam direction unless specified by an
[NXbeam](NXbeam "wikilink") member.

**Size and Shape** ([NXshape](NXshape "wikilink"))

Many instrument components define “height” and “width” variables to
specify their size when rectangular, a “radius” variable for when
circular etc. Rather than all these different names, an alternative
scheme is proposed based on the “shape” of the object and the local
coordinate axes this shape defines. All object would just need to
specify a shape (“cuboid”, “cylinder” etc.) and a size array. Specifying
size\[3\] would give the dimensions of the object along its local
(±x,±y,±z) axes; specifying size\[6\] would give the extent along
(+x,+y,+z,-x,-y,-z) and allow for e.g. asymmetric jaws where the
reference point may not be the centre of the rectangle. For example take
shape=“cylinder”: the [NXtranslation](NXtranslation "wikilink") variable
of position would define the location of the reference point for the
origin of the local axes: z in the direction of the cylinder axis, x and
y in plane. With no rotation the object would be oriented with its local
axes pointing in the direction of axes of the object it was defined
relative to, but this can be altered with the
[NXorientation](NXorientation "wikilink") variable within position. If a
size\[3\] array variable was specified, the reference point must be the
centre of the cylinder and the dimension are size\[0\]=size\[1\]=radius,
size\[2\]=length/2). If size\[6\] was specified then the reference point
would be elsewhere in the object, with its distance from the cylinder
edges along the various axes given by elements of the size\[6\] array.
