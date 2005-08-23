---
title: Application Program Interface
permalink: Application_Program_Interface/
layout: wiki
---

Purpose of API
--------------

The NeXus Application Program Interface is a suite of subroutines,
written in C but with wrappers in Fortran 77 and 90. The subroutines
call HDF routines to read and write the NeXus files with the correct
structure. An API serves a number of useful purposes:

1.  It simplifies the reading and writing of NeXus files.
2.  It ensures a certain degree of compliance with the NeXus standard.
3.  It allows the development of sophisticated input/output features
    such as automatic unit conversion. This has not been implemented
    yet.
4.  It hides the implementation details of the format. In particular,
    the API can read and write HDF4, HDF5 (and shortly XML) files using
    the same routines.

For these reasons, we request that all NeXus files are written using the
supplied API. We cannot be sure that anything written using the
underlying HDF API will be recognized by NeXus-aware utilities.
