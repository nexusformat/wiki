======================
Nexus 42 Release Notes
======================


4.2.1
-----
The following new featues have been added:

- NXbrowse now has readline support (i.e. previous command line recall and TAB completion of entry names)

- new API functions NXgetpath() and NXgetversion() added

- NXgetnextentry() now uses less stack space 4.2.0

System Requirements
-------------------

\**MXML XML Parsing Library*\* Version 2.2.2 or higher of mxml is required. Earlier versions
have a bug and the XML API will not work. This package can be downloded
in [both source and binary rpm form](http://www.easysw.com/~mike/mxml/software.php) and is also
available as part of [Fedora Extras](http://fedoraproject.org/wiki/Extras/UsingExtras).

IMPORTANT NOTE: Debian also provides the mxml package, but it based on 2.0 and
will not work properly. \**Python Interface*\* You will need both the
numpy and ctypes modules to be available. These are provided in both the
Fedora and EPEL repositories.

Building Notes
--------------

NAG F90/F95 Compiler
====================

The NAG compiler needs the \*\*-mismatch*\* flag to be
specified or else it will not compile NXmodule.f90 This is achieve by
running configure with the \**FCFLAGS*\* environment variable set to
contain the flag e.g. env FCFLAGS="-mismatch" ./configure --with-f90=f95
### HDF4 on Intel Macs There is a problem with the include file, hdfi.h
(normally in /usr/local/include). See for details of the modifications
necessary to fix it.

New Features
------------

C++ Interface
=============

(provided by [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink")
and [Peter Peterson](User%3APeter_Peterson.html "wikilink")) See the
[doxygen documentation](http://download.nexusformat.org/doxygen/html/classNeXus_1_1File.html)
and [NeXus API test program](http://svn.nexusformat.org/code/branches/4.2/test/napi_test_cpp.cxx).
A C++ Stream Like interface is also supported

- the idea is to provide an IOSteam like interface and allow you to type // create an entry and a data item File nf(fname, NXACC_CREATE); nf << Group("entry1", "NXentry")

.. code-block:: cpp

    << Data("dat1", w, "int_attr", 3); nf.close();
    File nf1(fname, NXACC_RDWR); // add a double_attr to an existing setup
    nf1 >>

    Group("entry1", "NXentry") >> Data("dat1") << Attr("double_attr", 6.0);
    nf1.close();

    // read back data items
    File nf2(fname, NXACC_READ); nf2 >>
    Group("entry1", "NXentry") >> Data("dat1", w1, "int_attr", i, "double_attr", d);

    // alternative way to read d1
    nf2 >> Data("dat1") >> Attr("double_attr", d1);


See also the [NeXus API test program](http://svn.nexusformat.org/code/branches/4.2/test/napi_test_cpp.cxx)

IDL Interface
=============

(provided by Jussi Kauppila and [Mark Koennecke](User%3AMark_Koennecke.html "wikilink")) There is a new
interface to RSI's Interactive Data Language, IDL for NeXus. This
interface has to be considered beta. Nevertheless it is working most of
the time. Known issues include:

- Compressed reading and writing do not work for HDF-4 files, probably because of a library version conflict on libz.

Python Interface
================

There is now, thanks to [Paul Kienzle](User%3APaul_Kienzle.html "wikilink"), a supported interface for
the python scripting language. Arrays are stored in numpy arrays and
thus allow for efficient data manipulations.

Changed Features
----------------

Known Issues
------------
See the comments on the IDL interface.

Miscellaneous bug fixes
-----------------------
The following items are bugs reported in previous releases and resolved in the 4.2 release.

Upcoming Features
-----------------
