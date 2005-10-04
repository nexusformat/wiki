---
title: Introduction
permalink: Introduction/
layout: wiki
---

### A Set of Subroutines

In the past, a data format was defined by a document describing the
precise location of every item in the data file, either as row and
column numbers in an ASCII file, or as record and byte numbers in a
binary file. In modern data formats, such as NeXus, the user does not
need to know where the data are stored, just what they are called. It is
the job of the subroutine library to retrieve the data.

For example, in NeXus, a program to read in the wavelength of an
experiment would contain lines similar to the following:

`NXopendata (fileID, `“`wavelength`”`);`  
`NXgetdata (fileID, lambda);`  
`NXclosedata (fileID);`

In this example, the program requests the value of the data that has the
label `wavelength`, storing the result in the variable lambda. `fileID`
is a file identifier that is provided by NeXus when the file is opened.

We shall provide a more complete example when we have discussed the
contents of the NeXus files.
