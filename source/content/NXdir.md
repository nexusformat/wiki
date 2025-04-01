---
title: NXdir
permalink: NXdir.html
layout: wiki
---
NXdir
=====

NXdir is a console based tool that allows inspecting the contents of a
NeXusfile. It allows for directory like listing of contents as well as
printing out data.

If you have any questions/comments/bug reports email Peter Peterson
&lt;petersonpf@ornl.gov&gt;

News
----

May 7, 2004:New version of NXdir is v0.2.5. This version now supports NX\_INT8 and NX\_UINT8 as well as fixes some bugs with reading integers from a nexus file.  
Apr 15, 2004:New version of NXdir is v0.2.4. The added feature is writing out an NXdata to file (1D and 2D only for now). Let me know if the format should be changed.  
Mar 17, 2004:New version of NXdir is v0.2.3. This version provides more consistency between abolsute and relative paths. It also allows for anchoring the path at both ends using a “/”.  
Mar 01, 2004:First public release of NXdir is v0.2.2 with linux binary here.  

Usage
-----

NXdir runs on the command line with a variety of arguments. Below is the
online help information (note that defaults can be changed during
compilation).

| About NXdir              |
|--------------------------|
| -h|--help                |
| --version                |
| Node Selection           |
| -p                       |
| Output Control           |
| -o/+o                    |
| -l|--max-array \[value\] |
| -t|--tree-mode <value>   |
| --path-mode <value>      |
| --data-mode <value>      |
| --printline <value>      |
| --write-data <filename>  |

Some common usages are:

-   Print the online (
        nxdir --help

-   List the everything at the root level of the file:
        nxdir lrcs3000.nxs

-   Find the user names in all of the files in the directory:
        nxdir *.nxs -p NXuser/name -o

-   Find all the data in a file:
        nxdir NPDF_E2_R0003000.nx.hdf -p NXdata

-   Print out how the entire file is organized
        nxdir trics058582002.hdf -p "*"

    (The asterix is in quotes so it is not expanded by the shell)

Downloads
---------

-   [NXdir-v0.2.5.tar.gz](ftp://ftp.neutron.anl.gov/nexus/NXdir/NXdir-0.2.5.tar.gz)
-   [NXdir-v0.2.4.tar.gz](ftp://ftp.neutron.anl.gov/nexus/NXdir/NXdir-0.2.5.tar.gz)
-   [NXdir-v0.2.3.tar.gz](ftp://ftp.neutron.anl.gov/nexus/NXdir/NXdir-0.2.5.tar.gz)
-   [NXdir-v0.2.2.tar.gz](ftp://ftp.neutron.anl.gov/nexus/NXdir/NXdir-0.2.5.tar.gz)
-   [CHANGES](ftp://ftp.neutron.anl.gov/nexus/NXdir/CHANGES)

Prerequisites
-------------

-   C++ compiler
-   NeXus libraries

or

-   Precompiled binary

Installation
------------

Binary:Some binaries can be found above. Download, rename to something you will remember (like nxdir) and move into your path.  
Unix/Linux/Irix/MacOSX:Unpack the tarball, enter the directory and type make. Copy the resulting binary nxdir into your path.  

Un-installing
-------------

Remove the file `nxdir`.

The installation process did not modify the registry or other system
settings in any way.

Frequently Asked Questions (FAQ)
--------------------------------

What is NXdir?:NXdir is a console tool used for inspection the contents of a NeXus file, it can print out the organization of the file as well as any data enclosed. It is intended to be a cross between the unix tools ls and grep. It should help people writing scripts access to NeXus files without having to compile in the NeXus API.  
The way NXdir prints arrays is hard to read, could you please change it?:No, but a format easier for you to read can be added. Please send <petersonpf@ornl.gov> an example of a two dimensional array in a format you like.  
