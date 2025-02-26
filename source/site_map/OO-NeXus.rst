========
OO-NeXus
========


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

### Path 1: OO Rework of the NeXus Classes

This means to perform a full object oriented analysis of the NeXus base
classes using polymorphism and inheritance. This was suggested by Darren
Kelly at the NIAC meeting 2006 at ILL. An example of a [possible class
hierarchy](media:NeXusOBJ.pdf.html "wikilink") was given by Mark Koennecke at
the NIAC meeting 2007 at HMI. There are some advantages to this
approach:

-   Different things, like different detectors, have different names and
      this makes the base classes easier to understand. It is easier to
      select NXtofareadetector rather then locate all the fields necessary
      for such a detector from a dictionary.

-   The use of inheritance makes the definitions easier to maintain
      because duplications can be avoided through inheritance.

-   Choices in the definitions, like the choice of coordinate system or
      shapes, can be made explicit by abstract classes and polymorphism.

-   Fully OO definitions can be mapped to appropriate classes in *all*
      object oriented programming languages.

But there are serious drawbacks to this approach as well:

-   We need a much extended set of classes.

-   Most importantly: we break backwards compatability: OO-NeXus files
      would have a deeper nesting structure and other classes.

### Path 2: Map the current NeXus Classes to Objects

This means that we directly map the current NeXus base classes hook,
line and sinker into objects in an OO programming language. This has the
huge advantage of backwards compatability: Old and new NeXus files look
alike. We also would not need to vote on new base classes. But there are
disadvantages to this approach, too:

- We loose the improved maintainability and clarity of the full
    OO-approach. But this can be overcome by using the full OO-classes
    plus some production rules as a tool for filling the actual NeXus
    base classes. An example: you have a TOF area detector? Then suck
    all fields for that class plus the inherited ones into your
    NXdetector class. Make decisions on choices like coordinate system
    on the way.

- The resulting API classes become ambiguous: i.e. different API
    detector classes loaded from different files will have different
    contents. This is less of a problem for dynamic object systems like
    the ones in python, CLOS and smalltalk. Dynamic object system in
    this context means that fields can be added at runtime. But there
    are many interesting OO programming languages which do not feature
    such an open type system: most notably C++ and Java. The problem
    with such languages can be solved in a number of ways:

    - NeXus base classes become catchalls: i.e. they have fields for
        all data items which may possibly be there. And throw errors
        when an access for an field without data is attempted. This is
        ugly.

    - Use some form of RunTime Type Information (RTTI). This can take
        the form of a group attribute with a possible name like subtype.
        Then the OO-API can read this attribute and create an
        appropriate class for this NeXus base class as on Path 1.
        Example: the subtype is NXtofareadetector. Then create a
        NXtofareadetector API class and fill its data fields from the
        content of the file.

### Questions?

- Where do we go? Path 1? Path 2? Or a yet to be defined Path 3?

- Do we have more options?

### Conclusion

01/2015: This discussion is obsolete. At NIAC 2014 it was decided to
accept interfaces as an experimental feature instead. But this text
still serves as valid statements about the difficulties which the NIAC
encountered when considering to implement OO in NeXus
