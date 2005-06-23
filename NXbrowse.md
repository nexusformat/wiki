---
title: NXbrowse
permalink: NXbrowse/
layout: wiki
---

NXbrowse is a terminal browser that provides a simple command-line
interface to view the contents of NeXus files. Datasets within the NeXus
file can be dumped to an ASCII file.

If you have any questions/comments/bug reports email Ray
Osborn&lt;ROsborn@anl.gov&gt;

Usage
-----

A simple terminal browser written in ISO C (replacing the earlier
version in Fortran 90). When compiled and linked with the NeXus API, it
can be run interactively to list the directories of each group within a
NeXus file. If used from a terminal (and installed in the default PATH
\[u\*\*x\] or defined as a symbol \[VMS\]), type

    nxbrowse <file_name>

If no file name is given, the user is prompted for the file to be
opened. NXbrowse then lists the global attributes and prompts for
further commands. The following commands may be given in upper or lower
case (although the group and data names are case sensitive) :

|                              |
|------------------------------|
|   ! |Command Definition      |
| DIR                          |
| OPEN <group>                 |
| READ &lt;data\[i,j,...\]&gt; |
| DUMP <data> <file>           |
| BYTEASCHAR                   |
| CLOSE                        |
| EXIT, QUIT                   |
| HELP                         |

On most systems, NXbrowse is compiled and linked during the standard
NeXus installation. Precompiled binary versions are available for a
limited number of operating systems (Linux, VMS, Macintosh). Please
contact Ray Osborn for more information.
