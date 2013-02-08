---
title: Objects or Interfaces
permalink: Objects_or_Interfaces/
layout: wiki
---

Objects or Interfaces
=====================

There is a need to review the NeXus base classes. They confuse people
because of their unstructured representation of in some cases many, many
fields. I see two main ways how this can be accomplished: Object
orientation and Inheritance or Interfaces and Composition.

Object Orientation and Inheritance
----------------------------------

This should be pretty clear: we define an inheritance hierarchy of base
classes. For example:

    NXarea_detector:NXdetector:NXbeamline_component

would mean NXarea\_detector inherits from NXdetector and from
NXbeamline\_component.

Choosing such a solution has a couple of consequences:

-   We would need to define a great number of new NeXus base classes.
    This can be even more confusing.
-   It is not clear how inheritance can be represented in a data file.
-   The OO concept does not fit well:
    -   Normally OO means encapsulating behaviour with data. NeXus has
        no behaviour, only data
    -   Some people say OO is really about message passing. There are no
        messages (yet) in NeXus
-   I can imagine situations when single inheritance is not enough and
    we need to deal with multiple inheritance. With all its ugliness.

Interfaces and Composition
--------------------------

This would imply that we define interfaces in addition to the base
classes. For example beamline\_component, detector, area\_detector etc.
A base class would then get an implements field or attribute which
details which interfaces the base class implements. To stay with the
example above: NXdetector would have an implements field with:
Iarea\_detector:Ibeamline\_component. A base class would then be defined
by the interfaces it can implement, plus mandatory data fields.

Such an approach has the following consequences:

-   Backwards compatability is maintained. We add a new feature to
    NeXus. No need to generate no new base classes.
-   No issues with multiple inheritance
-   An application can inspect the implements field and from this can
    decide what type of detector/ component it is dealing with.
-   I have no clue how this can be mapped into NXDL

I hope this description has been clear enough. Anyway, this needs a
thorough discussion, may be even on a face to face meeting, and a vote.