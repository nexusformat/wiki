=================
NIACDesign
=================

.. container:: content

   .. container:: page

      .. rubric:: NIACDesign
         :name: NIACDesign_niacdesign
         :class: page-title

      .. rubric:: NIAC Decisions regarding NeXus Design Questions
         :name: NIACDesign_niac-decisions-regarding-nexus-design-questions

      This section records NIAC decisions regarding the design of NeXus.
      With design meaning all more general topics reagrding the layout
      of files, how things are done in NeXus, general rules and such.

      .. rubric:: General Rules
         :name: general-rules

      NIAC 2003: Recommendation: use nxs extension for files nut h5,
      hdf, xml and others are prmitted

      NIAC 2003: Physical units will be stored in accordance with the
      udunits utility. Dates and times will be specified in ISO8601
      format.

      NIAC 2003: Positions will be stored as effective (physical)
      positions. Motor offsets will be stored as attribute to the data.

      NIAC 2007: When a scan is stored, the scan variable sould be the
      slowest varying variable.

      NIAC 2010: offset/stride mechanism for describing data not in C
      storage order

      NIAC 2014: By default values are readback values. If a set value
      is required, store it with the values name with \_set appended.

      

      .. rubric:: Base classes and application definition general Rules
         :name: base-classes-and-application-definition-general-rules

      NIAC 2003: Neither instrument definitions nor base classes will be
      subclassed

      NIAC 2003: When NXdetector is included in a file, there will be a
      one-to-one correspondence between NXdata and NXdetector.

      NIAC 2004: It is a violation of the NeXus standard to use NX in
      class names or fields unless authorized by NIAC

      NIAC 2004: Keep a NIAC version number aligned with the cvs-ID in
      the the header of each base class

      NIAC 2004: When linking, add a source attribute to the data item
      to indicate where it is linked too.

      NIAC 2004: Allow dimension scales to have arbitary dimensions in
      order to cope with non linear coordinate schemes

      NIAC 2005: Inheritance will be done in metaDTD only. This will be
      annotated with a tag conforms_to which contains a list of
      definitions this definitions also conforms too.

      NIAC 2005: characterisation measurements are to referenced by
      linking in another complete NXentry from another file through the
      external linking mechanism.

      NIAC 2008: ratified NXprocess for processed data. File structure
      plus associated groups and fields

      NIAC 2010: NXsubentry was agreed upon

      NIAC 2012: We allow application definitions to be flat and simple

      NIAC 2012: optional fields in application definitions endorsed.

      NIAC 2014: Optional fields in application definitions again
      ratified.

      

      .. rubric:: Coordinate Systems
         :name: coordinate-systems

      NIAC 2003: A right handed coordinate system is designed with the
      positive z-axis along the beam when facing downstream.

      NIAC 2003: If a simplifed position is needed the entries will be
      polar_angle, azimuthal_angle and distance.

      NIAC 2004: Allow cylindrical and polar coordinates in
      NXtranslation

      NIAC 2004: every instrument component is to have a distance and
      NXgeometry group. Comment in 2015: this was decided but never
      implemented.

      NIAC 2007: axes follow McStas conventions.

      NIAC 2010: Added meridional_angle axis

      NIAC 2012: accepted CIF style coordinate descriptions with
      depends_on fields and depends_on, vector, transformation_type etc
      attributes

      NIAC 2014: NXgeometry marked as deprecated. CIF style coordinate
      descriptions are the preferred method.

      

      .. rubric:: Errors
         :name: errors

      NIAC 2004: Errors to a dataset will be named dataset_error.
      Alterntaively, the dataset can have an attribute, error_formula,
      which specifies how the error is calulated.

      NIAC 2010: Add an uncertainties attribute to any numeric array to
      describe errors

      

      .. rubric:: Axes
         :name: axes

      NIAC 2003: Two axes schemes: via the axes attribute on the data
      and via the axis=n and primary=n on the dimension scales

      NIAC 2003: Histograms can be specified either by having an extra
      element in the dimension scale or by a histogram_offset attribute
      on the dimension scale

      NIAC 2012: Move axes and signal attribute as attributes of the
      enclosing group

      NIAC 2014: Accepted axes and {axis}_indices group attributes for
      the description of axes in NXdata and other groups.
