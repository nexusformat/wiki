======================
Nexus 41 Release Notes
======================


System Requirements
-------------------
\**MXML XML Parsing Library*\* Version 2.2.2 or higher of mxml is required. Earlier
versions have a bug and the XML API will not work. This package can be
downloded in [both source and binary rpm form](http://www.easysw.com/~mike/mxml/software.php) and is also
available as part of [Fedora Extras](http://fedoraproject.org/wiki/Extras/UsingExtras).

IMPORTANT
---------

NOTE: Debian also provides the mxml package, but it based on 2.0 and
will not work properly.

Building Notes
--------------

NAG F90/F95
============
### Compiler
The NAG compiler needs the **-mismatch** flag to be specified or else it will not compile `NXmodule.f90`. This is achieved by running configure with the **FCFLAGS** environment variable set to contain the flag, e.g.:

.. code-block:: text

    env FCFLAGS="-mismatch" ./configure --with-f90=f95

HDF4 on Intel Macs
==================

There is a problem with the include file, `hdfi.h` (normally in `/usr/local/include`). See for details of the modifications necessary to fix it.


New Features
------------

- New types NX\\_INT64 and NX\\_UINT64 to suppport 64 bit integers (only available in HDF5 and XML) [details](http://trac.nexusformat.org/code/ticket/87).

- Python bindings are now included in the Windows install kit [details](http://trac.nexusformat.org/code/ticket/86)

Changed Features
----------------

Known Issues
------------

Miscellaneous bug fixes
-----------------------

The following items are bugs reported in
previous releases and resolved in the 4.1 release.

- The Fortran 90 part of testsuite failed with the Absoft compiler on MacOSX (it passed with g95 and gfortran (4.2)) [details here](http://trac.nexusformat.org/code/ticket/68)

- NXputattr assumed NULL termination of NX\\_CHAR attributes, which is usually the case in C but not true for JAVA. A workaround is to add '\\\\0' manually [bug report](http://trac.nexusformat.org/code/ticket/83)

- pkgconfig issue [bug report](http://trac.nexusformat.org/code/ticket/84)

- Build issuewith MXML-2.3 [bug report](http://trac.nexusformat.org/code/ticket/91)

- XML buffer resizing performance issue [bug report](http://trac.nexusformat.org/code/ticket/92)

- Documentation is now installed to datadir (/usr/share) [bug report](http://trac.nexusformat.org/code/ticket/93)

Upcoming Features
-----------------
