---
title: Download
permalink: Download/
layout: wiki
---

The NeXus API is distributed under the terms of the GNU Lesser General
Public License. For information on using the NeXus API see the
[Application Program
Interface](Application_Program_Interface "wikilink") page. To report or
view problems/bugs/suggestions/enhancement requests goto our
[IssueReporting](IssueReporting "wikilink") system.

Requirements
------------

### External Libraries

Since NeXus uses HDF as the underlying binary format, it is necessary
first to install the HDF subroutine libraries and include files before
installing the NeXus API. It is not usually necessary to download the
HDF source code since precompiled object libraries exist for a variety
of operating systems including Windows, Mac OS X, Linux, and various
other flavors of Unix. Check the HDF web pages for more information:

-   <http://www.hdfgroup.org/>

Version 3.0.0 of the NeXus API allows the reading and writing of NeXus
files in XML. This uses the Mini-XML library, developed by Michael
Sweet, which is also available as a precompiled binary library for
several operating systems. Please ensure that you install version 2.2.2
or later. Check the Mini-XML web pages for more information:

-   <http://www.easysw.com/~mike/mxml/>

NeXus Source Code Distribution
------------------------------

The NeXus API may be built from source using one of the installation
kits linked below. Depending on which low-level file formats shall be
supported, one or several of the following libraries are required:

-   libhdf4g
-   libhdf5-<subversion?>
-   libmxml

The compilation uses the GNU Autotools. Download the appropriate gzipped
tar file, unpack it, and run the standard configure procedure from the
resulting nexus directory.

    % tar -zxvf nexus-3.0.0.tar.gz
    % cd nexus
    % ./configure 
    % make
    % make install

To find out how to customize the installation, *e.g.*, to choose
different installation directories, type

    % ./configure --help

To prevent trouble with unneeded drivers, specify e.g.

    % ./configure --without-java

See the README file for further instructions.

-   [Download NeXus API
    v3.0.0](http://download.nexusformat.org/kits/nexus-3.0.0.tar.gz)
-   [Download latest NeXus development
    snapshots](http://download.nexusformat.org/kits/)
-   [SubversionServer](SubversionServer "wikilink")

NeXus Binary Distributions
--------------------------

### Linux RPM Distribution Kits

To install and use NeXus you will need to install all of the binary RPMS
- these were built on a Fedora Core 2 Linux machine. Install using

    rpm -Uvh file.i386.rpm

or to change installation location from the default area (/usr/local)
use

    rpm -Uvh --prefix /alternative/directory file.i386.rpm

If the binary RPMS are not the correct architecture for you (e.g. you
need x64 rather than i386), instead download the Source RPM (.src.rpm)
and build a binary RPM for you machine using

    rpmbuild --rebuild file.src.rpm

This should then give you a binary RPM file file.something.rpm which you
can install as above. Be careful if you think about specifying an
alternative buildroot for rpmbuild by using --buildroot option as the
“buildroot” directory tree will get remove (so --buildroot / is a really
bad idea). Only change buildroot it if the default area turns out not to
be big enough to compile the package.

The following packages are required:

<table>
<colgroup>
<col width="20%" />
<col width="40%" />
<col width="40%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SZIP</p></th>
<th align="center"><p><a href="http://download.nexusformat.org/kits/rpm/szip-2.0-1.i386.rpm">i386 Binary RPM</a>|</p></th>
<th align="center"><p><a href="http://download.nexusformat.org/kits/rpm/szip-2.0-1.src.rpm">Source RPM</a></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>| HDF4</p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/hdf-4.2.1-1.i386.rpm">i386 Binary RPM</a></p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/hdf-4.2.1-1.src.rpm">Source RPM</a></p></td>
</tr>
<tr class="even">
<td><p>| HDF5</p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/hdf5-1.6.4-1.i386.rpm">i386 Binary RPM</a></p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/hdf5-1.6.4-1.src.rpm">Source RPM</a></p></td>
</tr>
<tr class="odd">
<td><p>| MXML</p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/mxml-2.2.2-1.i386.rpm">i386 Binary RPM</a></p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/mxml-2.2.2-1.src.rpm">Source RPM</a></p></td>
</tr>
<tr class="even">
<td><p>| NeXus</p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/nexus-3.0.0-1.i386.rpm">i386 Binary RPM</a></p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/nexus-3.0.0-1.src.rpm">Source RPM</a></p></td>
</tr>
</tbody>
</table>

If you are using [Fedora Core](http://fedora.redhat.com/) Linux,
pre-built hdf packages are contained in the fedora-extras repository and
can be installed with

    yum install hdf hdf-devel hdf5 hdf5-devel

-   [Download latest NeXus development snapshot as
    RPM](http://download.nexusformat.org/kits/rpm/)
-   [SubversionServer](SubversionServer "wikilink")

### Microsoft Windows Install Kit

[Windows Installer kits for
NeXus](http://download.nexusformat.org/kits/windows/)

### CYGWIN Kits

HDF4 is not supported under CYGWIN - both HDF5 and MXML are supported
and can be downloaded and built as usual. When configuring HDF5 you
should explicitly pass a prefix to the configure script to make sure the
libraries are installed in a “usual” location i.e.

    ./configure --prefix=/usr/local/hdf5

Otherwise you will have to use the **--with-hdf5=/path/to/hdf5** option
later when configuring NeXus to tell it where to look for hdf5.

After building hdf5, configure and build NeXus using the instructions
for [ source code
distribution](#NeXus_Source_Code_Distribution "wikilink") above.
