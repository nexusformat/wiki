---
title: Nexus 4 Release Notes
permalink: Nexus_4_Release_Notes.html
layout: wiki
---
Nexus 4 Release Notes
=====================

System Requirements
-------------------

**MXML XML Parsing Library**

Version 2.2.2 of mxml is required. Earlier versions have a bug and the
XML API will not work. This package can be downloded in [both source and
binary rpm form](http://www.easysw.com/~mike/mxml/software.php) and is
also available as part of [Fedora
Extras](http://fedoraproject.org/wiki/Extras/UsingExtras). IMPORTANT
NOTE: Debian also provides the mxml package, but it based on 2.0 and
will not work properly.

Building Notes
--------------

### NAG F90/F95 Compiler

The NAG compiler needs the **-mismatch** flag to be specified or else it
will not compile NXmodule.f90 This is achieve by running configure with
the **FCFLAGS** environment variable set to contain the flag e.g.

    env FCFLAGS="-mismatch" ./configure --with-f90=f95

New Features
------------

The following items are features added to the NeXus API to provide new
functionality to the core library or to assist in the build process.

-   Extended XML-API to handle unlimited dimensions
-   Add building of Doxygen documentation
-   Add support for two dimensional character arrays (HDF4 and HDF5
    only)
-   Added group attribute support to HDF4 (2006/05/02). Requires HDF4
    version (???)
-   Add NXmakenamedlink (2007/01/09) to all three file formats (external
    linking)
-   Add NXprintlink
-   Improved link testing in test suite
-   API can now read generic HDF5 files, such as those produced by
    matlab
-   Add facility to enable/disable error reporting
-   New NXsummary tool for summarising contentes of a NeXus file
-   Fortran 90 API now works with gfortran 4.2 and above as well as with
    G95
-   PYTHON and TCL bindings provided via a [SWIG
    interface](http://www.swig.org/)
-   Additional NXtranslate translators: SPEC, ESRF-EDF

Changed Features
----------------

The following aspects of the API have changed in a potentially
non-backward compatible way

-   The JAVA API now uses org.nexusformat rather than
    gov.anl.neutron.nexus

Known Issues
------------

The main problems are summarised here - for a complete list see [all
reported 4.0.0
issues](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.0.0&order=priority)

-   The Fortran 90 part of testsuite fails with the Absoft compiler on
    MacOSX (it passes with g95 and gfortran (4.2)) [details
    here](http://trac.nexusformat.org/code/ticket/68)
-   NXputattr assumes NULL termination of NX\_CHAR attributes, which is
    usually the case in C but not true for JAVA. A workaround is to add
    '\\0' manually. This error has been fixed in the code and will be
    available in the next release. More information is available in the
    [bug report](http://trac.nexusformat.org/code/ticket/83)

Miscellaneous bug fixes
-----------------------

The following items are bugs reported in the 3.x releases and resolved
for the 4.0 release.

-   Leading and trailing whitespace is stripped from char data on a
    read; this can be disabled by passing the NXACC\_NOSTRIP option to
    NXopen
-   Fix problems with MXML (what problems?)
-   Improve test procedures when not all libraries are present
-   Correct sourcepath for javadoc
-   Updated makefiles for swig bindings (python, tcl)

Upcoming Features
-----------------

Work on these features is still in progress. They are expected to be
part of the NeXus 4.1 release.

-   Add skeletal utility functions (NXU) to API (2005/04/26)

