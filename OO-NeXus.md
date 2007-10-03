---
title: OO-NeXus
permalink: OO-NeXus/
layout: wiki
---

Object Oriented NeXus
---------------------

This is a page to discuss the various options we have for defining both
object oriented instrument definitions and an object oriented NeXus-API.
The initial content of this page results from discussions at the NIAC
meeting 2007 at HMI, Berlin and between Mark Koennecke and Nick Hauser
later on.

### Summary of OO Discussions at the NIAC Meeting 2007 at HMI

-   People seem to be happy to use a NeXusFile object with methods like
    nf.makegroup(..), nf.opengroup(..) etc. as a low level object
    oriented API for NeXus files. This approach only encapsulates the
    file object and has already been implemented in the Java NeXus API.
-   A higher level NeXus OO-API should give access to the NeXus classes
    as defined in the instrument definitions.

### Current State of the NeXus Base Classes

The current NeXus base classes used for instrument definitions are not
really base classes. They are rather dictionaries or templates which
define names for data items which may be present in a NeXus base class
depending on the actual configuration of the instrument. As such these
NeXus base classes contain lots of fields and concepts which often
confuse both the initiated and the uninitiated.

### OO-NeXus: Two Paths into the Future

As things are we have two ways how to proceed with an object oriented
NeXus-API and object oriented definitions:

-   Rework the NeXus base classes in a fully object oriented way using
    polymorphism and inheritance.
-   A direct mapping of current neXus base classes to objects.

