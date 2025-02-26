=====================
Objects or Interfaces
=====================

Objects or Interfaces
=====================

There is a need to review the NeXus base classes. They confuse people because of their unstructured representation of, in some cases, many, many fields. I see two main ways how this can be accomplished: Object orientation and Inheritance or Interfaces and Composition.

Object Orientation and Inheritance
----------------------------------

This should be pretty clear: we define an inheritance hierarchy of base classes. For example: ``NXarea_detector:NXdetector:NXbeamline_component``
would mean ``NXarea_detector`` inherits from ``NXdetector`` and from ``NXbeamline_component``. Choosing such a solution has a couple of consequences:
- We would need to define a great number of new NeXus base classes. This can be even more confusing.
- It is not clear how inheritance can be represented in a data file.
- The OO concept does not fit well:
- Normally OO means encapsulating behavior with data. NeXus has no behavior, only data.
- Some people say OO is really about message passing. There are no messages (yet) in NeXus.
- I can imagine situations when single inheritance is not enough and we need to deal with multiple inheritance, with all its ugliness.

Interfaces and Composition
--------------------------

This would imply that we define interfaces in addition to the base classes. For example, ``beamline_component``, ``detector``, ``area_detector``, etc. A base class would then get an ``implements`` field or attribute which details which interfaces the base class implements. To stay with the example above: ``NXdetector`` would have an ``implements`` field with: ``Iarea_detector:Ibeamline_component``. A base class would then be defined by the interfaces it can implement, plus mandatory data fields. Such an approach has the following consequences:
- Backwards compatibility is maintained. We add a new feature to NeXus. No need to generate new base classes.
- No issues with multiple inheritance.
- An application can inspect the ``implements`` field and from this can decide what type of detector/component it is dealing with.
- I have no clue how this can be mapped into NXDL.

NeXus Interfaces: A Possible Implementation
===========================================

This is a more detailed outline of how NeXus Interfaces might look in advance of a vote on the issue.

The Problem
-----------

Quite a number of NeXus base classes have become pretty big. This is due to the fact that NeXus base classes are dictionaries which hold field names for all sorts of data items which can be associated with a given NeXus component. A good example is ``NXdetector``: it holds data items to describe all sorts of detectors, single, area, arbitrarily shaped, with TOF or without, etc. Many users are confused by NeXus base classes because they mistakenly think that they have to implement all data items even if they do not make any sense for their application. A better structure would clearly help here.

One way to structure this better would be inheritance. This would mean introducing more NeXus base classes, for example: ``NXsingle_detector``, ``NXarea_detector``, ``NXtof_area_detector``, etc., which form a hierarchy rooted at ``NXbeamline_component``. The applicable fields for a component would then be derived by traveling the hierarchy. This comes at the expense of creating many more backwards incompatible classes. Moreover, the inheritance hierarchy cannot easily be encoded in an HDF5 file. Thus, a program looking for ``NXdetector`` would need to know about all its incarnations from an external source. This raises issues about the maintainability of the external sources.

The second option to be discussed is to use interfaces, like in Java or Go. This is a separate set of finer-grained dictionaries which are used to build up the NeXus base classes.

Examples
--------

How could the interface method look like for ``NXdetector``? To this purpose, let us define a set of interfaces to work this. I use the prefix ``NXIF`` here for interfaces but this is perfectly arbitrary.

``NXIFbeamline_component``:
   ``distance``
     ``@type=translation``
     ``@vector=0,0,1``

   ``height``
     ``@type=translation``
     ``@vector=0,1,0``

   ``x_translation``
     ``@type=translation``
     ``@vector=1,0,0``

   ``rotation_angle``
     ``@type=rotation``
     ``@vector=0,1,0``

   ``azimuthal_angle``
     ``@type=rotation``
     ``@vector=0,0,1``

   ``meridional_angle``
     ``@type=rotation``
     ``@vector=1,0,0``

is an interface meant to be implemented by all beamline components. Its
purpose is to position the component.
NXIFmeta:
``type\``
``description\``
An interface which contains general meta data about
anything
NXIFsingle:
``data\`` ``@signal=1\``
A simple interface for data from a single detector
NXIFscanned\\_single:

``data[NP]``
  ``@signal=1``
  A single detector scanned. NP is the number of scan points.

NXIFarea_detector:

``data[xdim, ydim]``
  ``@signal=1``
  ``@axes=x_pixel_offset, y_pixel_offset``

``x_pixel_offset[xdim]``
  ``@type=translation``
  ``@vector=1,0,0``

``x_pixel_size[xdim]``

``y_pixel_offset[ydim]``
  ``@type=translation``
  ``@vector=0,1,0``

``y_pixel_size[ydim]``

An interface for an area detector.
x\\_pixel\\_offset and y\\_pixel\\_offset describe the grid of the
detector in the detector coordinate system. The origin is the mechanical
center of the area detector. If the pixel sizes cannot be determined
from the grid span by x\\_pixel\\_offset and y\\_pixel\\_offset, they
are given in x,y\\_pixel\\_size. NXIFscanned\\_area\\_detector:

``data[xdim, ydim]``
  ``@signal=1``
  ``@axes=x_pixel_offset, y_pixel_offset``

``x_pixel_offset[xdim]``
  ``@type=translation``
  ``@vector=1,0,0``

``x_pixel_size[xdim]``

``y_pixel_offset[ydim]``
  ``@type=translation``
  ``@vector=0,1,0``

``y_pixel_size[ydim]``

An interface for a
scanned area detector. The meaning of x,y\\_pixel\\_offset etc are the
same as above. One might consider to allow inheritance for Interfaces.
NXIFtof\\_area\\_detector:

``data[xdim, ydim, ntbin]``
  ``@signal=1``
  ``@axes=x_pixel_offset, y_pixel_offset, time_binning``

``x_pixel_offset[xdim]``
  ``@type=translation``
  ``@vector=1,0,0``

``x_pixel_size[xdim]``

``y_pixel_offset[ydim]``
  ``@type=translation``
  ``@vector=0,1,0``

``y_pixel_size[ydim]``

``time_binning[ntbin]``

An interface for an area detector used in time
of flight mode. NXIF\\_arbitrary\\_detector:

``data[ndet]``
  ``@signal=1``

``distance[ndet]``
  ``@type=translation``
  ``@vector=0,0,1``

``height[ndet]``
  ``@type=translation``
  ``@vector=0,1,0``

``x_translation[ndet]``
  ``@type=translation``
  ``@vector=1,0,0``

``rotation_angle[ndet]``
  ``@type=rotation``
  ``@vector=0,1,0``

``azimuthal_angle[ndet]``
  ``@type=rotation``
  ``@vector=0,0,1``

``meridional_angle[ndet]``
  ``@type=rotation``
  ``@vector=1,0,0``

This is an interface to describe a highly
irregular detector. A detector which can only be described by giving
full positional and rotational coordinates for each detector element.
ISIS has this kind of detectors. NXIFtof\\_arbitrary\\_detector:

``data[ndet, ntbin]``
  ``@signal=1``

``distance[ndet]``
  ``@type=translation``
  ``@vector=0,0,1``

``height[ndet]``
  ``@type=translation``
  ``@vector=0,1,0``

``x_translation[ndet]``
  ``@type=translation``
  ``@vector=1,0,0``

``rotation_angle[ndet]``
  ``@type=rotation``
  ``@vector=0,1,0``

``azimuthal_angle[ndet]``
  ``@type=rotation``
  ``@vector=0,0,1``

``meridional_angle[ndet]``
  ``@type=rotation``
  ``@vector=1,0,0``

``time_binning[ntbin]``

This is an interface to describe a highly irregular detector used in time of flight mode. The rest is shared with above.

To be continued...

How to use such Interfaces
--------------------------

Of course, there have to be rules on how to use NeXus Interfaces. The rule set is simple:
1. A group attribute ``implements`` is added, which is a comma-separated list of the interfaces implemented by the component.
2. The software can then expect the fields defined by the interfaces to appear in the component class. Whether this is mandatory or optional is to be discussed.
3. A given NeXus base class can only implement a sensible set of interfaces. It would be dubious if ``NXdetector`` implements ``NXIFspallation_neutron_source``.

An example is in order. Consider:
``NXdetector``
``@implements=NXIFbeamline_component, NXIFarea_detector``

Then the following fields go into ``NXdetector``:

``@implements=NXIFbeamline_component, NXIFarea_detector``

``distance``
  ``@type=translation``
  ``@vector=0,0,1``

``height``
  ``@type=translation``
  ``@vector=0,1,0``

``x_translation``
  ``@type=translation``
  ``@vector=1,0,0``

``rotation_angle``
  ``@type=rotation``
  ``@vector=0,1,0``

``azimuthal_angle``
  ``@type=rotation``
  ``@vector=0,0,1``

``meridional_angle``
  ``@type=rotation``
  ``@vector=1,0,0``

``data[NP, xdim, ydim]``
  ``@signal=1``
  ``@axes=scan_axis, x_pixel_offset, y_pixel_offset``

``x_pixel_offset[xdim]``
  ``@type=translation``
  ``@vector=1,0,0``

``x_pixel_size[xdim]``

``y_pixel_offset[ydim]``
  ``@type=translation``
  ``@vector=0,1,0``

``y_pixel_size[ydim]``

Another example: a
scanned single detector \``NXdetector\``

``@implements=NXIFbeamline_component, NXIFscanned_single_detector``

``distance``
  ``@type=translation``
  ``@vector=0,0,1``

``height``
  ``@type=translation``
  ``@vector=0,1,0``

``x_translation``
  ``@type=translation``
  ``@vector=1,0,0``

``rotation_angle``
  ``@type=rotation``
  ``@vector=0,1,0``

``azimuthal_angle``
  ``@type=rotation``
  ``@vector=0,0,1``

``meridional_angle``
  ``@type=rotation``
  ``@vector=1,0,0``

``data[NP]``
  ``@signal=1``

Advantages and Disadvantages
----------------------------

### Advantages

What would be the advantages of the NeXus interface approach:
- We can be far more specific about what goes into a base class for a use case than with the current base class description.
- We can do so without cluttering the namespace with even more base classes.
- User confusion is reduced.
- The approach is easily extended to new use cases by defining a new interface for the new use case.
- The interface approach is backwards compatible. We add to NeXus rather than defining something entirely new. Old files can be updated to the way of the interface by adding required fields and the interface group attribute.

### Disadvantages

- It is yet another concept and set of rules to teach and learn.

NeXus Interfaces and Mapping to CIF
-----------------------------------

When mapping between NeXus and CIF there is a major difficulty: the way multiples are handled in CIF and NeXus. Consider an instrument with two detectors. In NeXus, this would map to two ``NXdetector`` classes and two ``NXdata`` classes with different names within the hierarchy. In CIF, one would loop over detector name and all the fields of the base class. A loop is basically a table. The above example would thus map to a table with ``detector_name`` and all the fields of the base class as columns and two rows indexed by detector name. With the current size of the NeXus base classes, this would make for unwieldy and sparsely populated tables. With NeXus Interfaces, this becomes much more workable. Each NeXus interface would map to a CIF category (table) and there would be other categories (tables) which detail the list of components of the instrument and which interfaces are implemented by each component. Herbert solved the problem in his concordance document by appending the NeXus base class name and the component name together. But this makes for long and unpredictable CIF category (table) names.

Where To Go From Here?
----------------------

1. All the confusion generated by this document must be resolved.
2. The big thing is: do we want NeXus Interfaces? This requires a vote.
3. Which rules do we use to write NeXus Interfaces? I made something up for this example. But, of course, this could be different.
4. How do we document NeXus interfaces? NXDL would be the first call, but...
5. Polishing up NeXus interfaces most likely requires a code camp.

------------------------------------------------------------------------

More on Interfaces
------------------

There is a branch, interfaces, on the NeXus definitions GitHub area which generates a version of the NeXus manual with Interfaces fully worked out. Well, how it should look like in my humble opinion.

Update: 01/2015
---------------

At NIAC 2014 it was decided to accept NeXus Interfaces as an experimental feature. This means that a special section of the manual will be written which uses interfaces. This section will be clearly labeled as experimental.
