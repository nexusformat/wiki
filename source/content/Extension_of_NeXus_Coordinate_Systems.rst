=====================================
Extension of NeXus Coordinate Systems
=====================================

Extension of the NeXus Coordinate Systems
-----------------------------------------

This suggestion results from comparing imageCIF with NeXus. Ideally, we should be able to make a mapping from CIF to NeXus. Unfortunately, NeXus had some weaknesses in coordinate systems (addressed by this proposal) and scaled data. Please note, that this proposal extends in what we already do in NeXus and does not invalidate earlier efforts.

The CIF way of specifying axes is far more accurate than what we do with NeXus. Thus, the suggestion is to align NeXus with the well thought-out CIF scheme. This section consists first of a discussion of the CIF axis system and then of suggestions on how to use this within NeXus.

CIF uses a coordinate system which is similar to the McStas coordinate system that NeXus uses at its bottom. Just the orientation of the Z-axis differs. The description of any given axis in CIF consists of three elements:

1. **The type of the axis**. This can be translation or rotation.
2. **The axis vector**. This is the direction of a translation or the vector around which the axis rotates.
3. **The axis offset**. The offset to the base of the rotation or translation. If this is not given, 0,0,0 is assumed.

CIF also describes in which order transformations have to be applied to get a component into its final position from its zero position. In CIF, this is done by chaining axes through the `depends` attribute. This scheme is a generalization of the methods commonly used in crystallography. There, a crystal is brought into scattering position by applying a series of rotations. Please note that order is important!

### Axis Suggestions for NeXus

1. NeXus stays with the McStas coordinate system.
2. NeXus uses the vector and offset scheme to document existing NeXus axes. The base of all operations is always the component, if not specified by an offset vector. Rotations are in degrees, translations in millimeters. Some examples:
   - `rotation_angle` has a vector 0 1 0, rotation around Y
   - `azimuthal_angle` is a rotation around Z, vector = 0 0 1
   - `polar_angle` is also a rotation around Y, vector 0 1 0, but as the rotation axis is with the previous component upstream, we have an offset of 0 0 -distance

In `NXsample`, we additionally have:
   - `chi` is a rotation around Z, vector 0 0 1
   - `phi` is a rotation around Y, vector 0 1 0
   - `kappa`, for kappa the vector attribute has to be given as there are kappa goniometers with different values of kappa.

3. Each NeXus component can have an additional field with the name `transform`. This contains a comma-separated list of the operations required to place the component at its position in the instrument. The formula is:

    Xcurrent = op1*op2....*opn \* X0

with transform becoming:

    op1,op2,....,opn

Names of operations are the names of the axis to apply. Unqualified names relate to axes in the same group. In order to refer to axes outside the current group, full path names must be given. Storing this separately in a transform field gives direct access, whereas the CIF `depends` system requires a lot of searches to reconstruct the sequence of transforms. This is why I prefer `transform`.

In this description, our NeXus polar coordinate system has the transform:

    azimuthal_angle, polar_angle

This is also the default if the transform field is missing.

4. NeXus strongly prefers to use the NeXus simple coordinate system with `polar_angle` and `azimuthal_angle` as described above. This description has the advantage that `polar_angle` is always two theta.

5. With the vector/offset scheme, arbitrary axes can be stored in NeXus. The rule then is that type, vector, and offset have to be specified as attributes. Type is `NX_CHAR`, vector and offset are of dimension 3 and type `NX_FLOAT`. We need these attributes anyway, as there are angles such as `kappa`, which differ in their rotation axis between instruments.

6. NeXus is missing a rotation around the X-axis. As we have already adopted quite lyrical names for rotation axes, I suggest `aequatorial_angle` as a name for this.

7. Consequently, as NeXus does not have fields for describing translations, except in `NXgeometry`, I suggest adding `x_translation`, `y_translation`, and `z_translation` fields to each component. I choose to suggest separate fields for the translations as they frequently map to dedicated motors. Please note that all angles have to be 0 if you were to determine the operation of any given translation motor.

8. The `orientation` field in `NXgeometry` receives the same meaning as `vector` in axis descriptions, with `vector` being aligned with the main axis of the component.

9. `NXgeometry` stays as is as a means to describe shapes, engineering coordinates, and orientations of components.

Conclusion
----------

01/2015: CIF-style coordinate system descriptions have been ratified by NIAC in 2012. The ratified version differs in many details, but not in the approach, from the material on this page. Please consult a recent copy of the NeXus manual for an up-to-date description of NeXus coordinate descriptions.

