---
title: Extension of NeXus Coordinate Systems
permalink: Extension_of_NeXus_Coordinate_Systems.html
layout: wiki
---
Extension of NeXus Coordinate Systems
=====================================

Extension of the NeXus Coordinate Systems
-----------------------------------------

This suggestion results from comparing imageCIF with NeXus. Ideally we
should be able to make a mapping from CIF to NeXus. Unfortunately, NeXus
had some weaknesses in coordinate systems (addressed by this proposal)
and scaled data. Please note, that this proposal extends in what we
already do in NeXus and does not invalidate earlier efforts.

The CIF way of specifying axis is far more accurate then what we do with
NeXus. Thus the suggestion is to align NeXus with the well thought out
CIF scheme. This section consists first of a discussion of the CIF axis
system and then of suggestions how to use this within NeXus.

CIF uses a coordinate system which is similar to the McStas coordinate
system which NeXus uses at its bottom. Just the orientation of the
Z-axis differs. The description of any given axis in CIF consists of
three elements:

-   The type of the axis. This can be translation or rotation
-   The axis vector. This is the direction of a translation or the
    vector around which the axis rotates.
-   The axis offset. The offset to the base of the rotation or
    translation. If this is not given 0,0,0 is assumed.

CIF also describes in which order transformations have to be applied to
get a component into its final position from its zero position. In CIF
this is done by chaining axis through the depends attribute.

This scheme is a generalisation of the methods used commonly in
crystallography. There a crystal is brought into scattering position by
applying a series of rotations. Please note that order is important!

### Axis Suggestions for NeXus

1) NeXus stays with the McStas coordinate system.

2) NeXus uses the vector and offset scheme to document existing NeXus
axis. The base of all operations is always the component, if not
specified by an offset vector. Rotations are in degree, translations in
milimetre.

Some examples:

-   rotation\_angle has a vector 0 1 0, rotation around Y
-   azimuthal\_angle is a rotation around Z, vector = 0 0 1
-   polar\_angle is also a rotation around Y, vector 0 1 0, but as the
    rotation axis is with the previous component upstream, we have an
    offset of 0 0 -distance

In NXsample we additionally have:

-   chi is a rotation around Z, vector 0 0 1
-   phi is a rotation around Y, vector 0 1 0
-   kappa, for kappa the vector attribute has to be given as there are
    kappa goniometres with different values of kappa.

3) Each NeXus component can have an additional field with the name
transform. This contains a komma separated list of the operations
required to place the component at its position in the instrument. The
formula is:

          Xcurrent = op1*op2....*opn * X0

with transform becoming: op1,op2,....,opn Names of operations are the
names of the axis to apply. Unqualified names relate to axis in the same
group. In order to refer axis outside the current group, full path names
must be given. Storing this separatly in a transform field gives direct
access whereas the CIF depends system requires a lot of searches to
reconstruct the sequence of transforms. This is why I like transform
better.

In this description, our NeXus polar coordinate system has the
transform:

              azimuthal_angle, polar_angle

This is also the default if the transform field is missing.

4) NeXus strongly prefers to use the NeXus simple coordinate system with
polar\_angle and azimuthal\_angle as describe above. This description
has the advantage that polar\_angle is always two theta.

5) With the vector/offset scheme arbitrary axis can be stored in NeXus.
The rule then is that type, vector and offset have to be specified as
attributes. Type is NX\_CHAR, vector and offset are of dim 3 and type
NX\_FLOAT. We need these attributes anyway as there are angles such as
kappa, which differ in their rotation axis between instruments.

6) NeXus is missing a rotation around the X axis. As we already bought
into quite lyrical names for rotation axis I suggest aequatorial\_angle
as a name for this.

7) Consequently, as NeXus does not have fields for describing
translations, except in Nxgeometry, I suggest to add x\_translation,
y\_translation and z\_translation fields to each component. I choose to
suggest separate fields for the translations as they frequently map to
dedicated motors. Please note that all angles have to be 0 if you were
to determine the operation of any given translation motor.

8) The orientation field in NXgeometry receives the same meaning as
vector in axis descriptions. With vector being aligned with the main
axis of the component.

9) NXgeometry stays as is as a means to describe shapes, engineering
coordinates of orientations of components.

Conclusion
----------

01/2015: CIF style coordinate system descriptions have been ratified by
NIAC in 2012. The ratified version differs in many details, but not in
the approach, from the material on this page. Please consult a recent
copy of the NeXus manual for an update to date description of NeXus
coordinate descriptions.
