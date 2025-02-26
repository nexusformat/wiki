==========
Metaformat
==========

Metaformat
----------

*Work is currently in progress to replace Meta-DTDs with* [XML schema](Schema.html "wikilink").

The contents of NeXus files are defined using XML. The hierarchical
structure of NeXus files maps very conveniently into XML files with
NeXus groups and items as the XML entities, and data attributes as XML
attributes. NeXus utilities are being developed to help people determine
whether their files are standard-conforming. However, formal XML format
definitions (DTDs) are difficult for the non-expert to read, so we have
produced a much simpler meta-DTD format, which produces well-formed
(DTD-less) XML files that will be converted into DTD files. This page
describes the rules for producing these files - some examples are
available below and in the NeXus content section. The utility NXtoDTD
can be used to generate the skeleton of such a file from an existing
NeXus file; it outputs the XML tags without the data or any annotation.

Meta-DTD Definition
-------------------

-   Each meta-DTD file should begin with a standard XML document tag,
    i.e.

.. code-block:: xml

    <!-- -->

    <?xml version="1.0" ?>


This should be followed by a comment block giving the URL of the XML
file, the name of the editor, the keyword $Id$, which will generate a
revision number when the file is committed to the
[SubversionServer](SubversionServer.html "wikilink"), and a brief description
of the file, e.g.

.. code-block:: xml

    <!-- -->

    <!--
    URL:     http://www.neutron.anl.gov/nexus/xml/NXgroup.xml
    Editor:  Jean Dupont <JDupont@some.where>
    $Id$

    Definition of a fake but well-formed NeXus group.

    -->

-   Each NeXus group is an XML entity defined by its class, e.g. NXuser,
    NXdata, ....
-   The name of the group is given by the name attribute of the entity.



N.B. XML attributes are the name=“value” pairs located within the
opening tag of the XML entity, e.g.

.. code-block:: xml

    <!-- -->

    <NXsample name="sample">


All other data items are XML entities defined by their name, e.g.
<temperature>

-   Data attributes are stored as XML attributes. The data type is
    defined as an XML attribute although it is not defined as an HDF
    attribute in the NeXus file itself, e.g.

.. code-block:: xml

    <!-- -->

    <temperature type="NX_FLOAT32" units="K">

-   If the value of an attribute is not defined by the DTD, a short
    description is enclosed within quotes and curly braces, e.g.

.. code-block:: xml

    <!-- -->

    <NXdetector name="{Name of detector bank}">

-   Similarly, the value of a data item which is not defined by the DTD
    should be placed within curly braces between the opening and closing
    tag, e.g.

.. code-block:: xml

    <!-- -->

    <temperature>{Temperature of sample}</temperature>

-   Following the opening tag of a group entity and before the closing
    tag of a data entity, there may be one of three symbols, which have
    the same meanings that they have in regular expressions.
    -   `*` May occur 0 or more times
    -   `+` May occur one or more times (i.e. at least once)
    -   `?` May occur 0 or one times (i.e. no more than once)


e.g.

.. code-block:: xml

    <!-- -->

    <NXsample>?
       <temperature>{Temperature of sample}?</temperature>
    </NXsample>


If no symbol is given, the item is mandatory.

-   If a data item is an array, add the array dimensions in square
    brackets to the type attribute. Use a colon if the dimension length
    is not defined by the DTD, e.g.

.. code-block:: xml

    <!-- -->

    <polar_angle type="NX_FLOAT32[:]">


Replace the colon with i, j, ... if you wish to match the dimension
length to other data items within the same group.

-   If no data type is specified, it is assumed to be a character string
    (NX\_CHAR).
-   The “version” attribute of the “analysis” entity, defined in each
    NXentry group should be set to $Revision$ when the file is first
    written so that the CVS revision number is substituted when the XML
    file is committed to the CVS server, e.g.

.. code-block:: xml

    <!-- -->

    <analysis version="$Revision$">

Example
-------

The instrument definitions are being constructed out of XML files for
each of the component groups. If you are interested in defining your own
definition, please form them from these component parts (remove the XML
document type at the top of each file). See NXtofnpd.xml for a complete
example. The following is a colorized version of NXmonitor.xml.


NXmonitor.xml
#############

.. code-block:: xml

    <?xml version="1.0" ?>
    <!--
    URL: http://www.neutron.anl.gov/nexus/xml/NXmonitor.xml
    Editor: Ray Osborn <ROsborn@anl.gov>
    $Id$

    Definition of monitor data. It is similar to the NXdata groups containing
    monitor data and its associated dimension scale, e.g. time_of_flight or
    wavelength in pulsed neutron instruments. However, it may also include
    integrals, or scalar monitor counts, which are often used in both in both pulsed
    and steady-state instrumentation.

    -->
    <NXmonitor name="{Name of monitor}">
            <distance units="m" type="NX_FLOAT32"> {Distance of monitor from sample} </distance>
            <integral type="NX_FLOAT32"> {Integral over monitor spectrum}? </integral>
            <range type="NX_FLOAT32[2]"> {Time-of-flight range over which the integral was calculated}? </range>
            <type> "Fission Chamber"|"Scintillator"? </type>
            <height units="cm" type="NX_FLOAT32"> {Height of monitor}? </height>
            <width units="cm" type="NX_FLOAT32"> {Width of monitor}? </width>
            <time_of_flight units="microseconds" type="NX_FLOAT32[i]"> {Time-of-flight}? </time_of_flight>
            <efficiency type="NX_FLOAT32[i]"> {Monitor efficiency}? </efficiency>
            <data type="NX_INT32[i]"> {Monitor data}? </data>
    </NXmonitor>
