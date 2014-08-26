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

Downloads for documentation are available separately at
<http://download.nexusformat.org/kits/definitions/>.

Requirements
------------

### External Libraries

Since NeXus uses HDF as the main underlying binary format, it is
necessary first to install the HDF subroutine libraries and include
files before installing the NeXus API. It is not usually necessary to
download the HDF source code since precompiled object libraries exist
for a variety of operating systems including Windows, Mac OS X, Linux,
and various other flavors of Unix. Check the HDF web pages for more
information:

-   <http://www.hdfgroup.org/>

The NeXus API also supports using XML as the underlying on-disk format.
This uses the Mini-XML library, developed by Michael Sweet, which is
also available as a precompiled binary library for several operating
systems. Please ensure that you install version 2.2.2 or later. Check
the Mini-XML web pages for more information:

-   <http://www.minixml.org/>

NeXus Source Code Distribution
------------------------------

The NeXus API may be built from source using one of the installation
kits linked below. Depending on which low-level file formats shall be
supported, one or several of the following libraries are required:

-   HDF4: packages **hdf** and **hdf-devel** on Fedora Core,
    **libhdf4g** on Debian
-   HDF5: packages **hdf5** and **hdf5-devel** on Fedora Core,
    **libhdf5** on Debian
-   MXML: packages **libmxml1** and **libmxml-devel** on Debian,
    **mxml** and **mxml-devel** on Fedora Core. Note that libmxml1 on
    Debian is curently version 2.0 and will not work; until this is
    updated you need to download version 2.2.2 from either
    <http://www.minixml.org/> (or
    <http://cilibrar.com/~cilibrar/projsup/nex4>).

The compilation uses the GNU Autotools. Download the appropriate gzipped
tar file, unpack it, and run the standard configure procedure from the
resulting nexus directory. For example, for version 3.0.0

    % tar -zxvf nexus-3.0.0.tar.gz
    % cd nexus-3.0.0
    % ./configure 
    % make
    % make install

To find out how to customize the installation, *e.g.*, to choose
different installation directories, type

    % ./configure --help

To prevent trouble with unneeded drivers, specify e.g.

    % ./configure --without-java

See the README file for further instructions.

-   [Download the NeXus API Source
    Code](http://download.nexusformat.org/kits/)
-   Information on the NeXus Code
    [SubversionServer](SubversionServer "wikilink")

NeXus Binary Distributions
--------------------------

### Linux RPM Distribution Kits

A NeXus binary RPM (nexus-\*.i386.rpm) contains ready compiled NeXus
libraries whereas a source RPM (nexus-\*.src.rpm) needs to be compiled
into a binary RPM before it can be installed. In general, a binary RPM
is installed using the command

    rpm -Uvh file.i386.rpm

or, to change installation location from the default (/usr/local) area,
using

    rpm -Uvh --prefix /alternative/directory file.i386.rpm

If the binary RPMS are not the correct architecture for you (e.g. you
need x86\_64 rather than i386) or the binary RPM requires libraries
(e.g. HDF4) that you do not have, you can instead rebuild a source RPM
(.src.rpm) to generate the correct binary RPM for you machine. Download
the source RPM file and then run

    rpmbuild --rebuild file.src.rpm

This should generate a binary RPM file which you can install as above.
Be careful if you think about specifying an alternative buildroot for
rpmbuild by using --buildroot option as the “buildroot” directory tree
will get remove (so --buildroot / is a really bad idea). Only change
buildroot it if the default area turns out not to be big enough to
compile the package.

The nexus binary RPM requires hdf4, hdf5 and mxml to already be
installed. Some or all of the following packages may be required in
addition to the NeXus binary RPM:

<table>
<colgroup>
<col width="20%" />
<col width="40%" />
<col width="40%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SZIP</p></th>
<th align="center"><p>Binary RPM <a href="http://download.nexusformat.org/kits/rpm/szip-2.0-1.i386.rpm">i386</a></p></th>
<th align="center"><p><a href="http://download.nexusformat.org/kits/rpm/szip-2.0-1.src.rpm">Source RPM</a></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>| HDF4</p></td>
<td align="center"><p>Binary RPM <a href="http://download.nexusformat.org/kits/rpm/hdf-4.2.1-1.i386.rpm">i386</a></p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/hdf-4.2.1-1.src.rpm">Source RPM</a></p></td>
</tr>
<tr class="even">
<td><p>| HDF5</p></td>
<td align="center"><p>Binary RPM <a href="http://download.nexusformat.org/kits/rpm/hdf5-1.6.4-1.i386.rpm">i386</a></p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/hdf5-1.6.4-1.src.rpm">Source RPM</a></p></td>
</tr>
<tr class="odd">
<td><p>| MXML</p></td>
<td align="center"><p>Binary RPM <a href="http://download.nexusformat.org/kits/rpm/mxml-2.2.2-1.i386.rpm">i386</a> <a href="http://download.nexusformat.org/kits/rpm/mxml-2.2.2-1.x86_64.rpm">x86_64</a></p></td>
<td align="center"><p><a href="http://download.nexusformat.org/kits/rpm/mxml-2.2.2-1.src.rpm">Source RPM</a></p></td>
</tr>
</tbody>
</table>

If you are using [Fedora Core](http://fedora.redhat.com/) Linux,
pre-built hdf packages are contained in the fedora-extras repository and
can be installed with

    yum install hdf hdf-devel hdf5 hdf5-devel mxml mxml-devel

-   [Download NeXus API in RPM (binary and/or source)
    format](http://download.nexusformat.org/kits/)
-   Information on the NeXus Code
    [SubversionServer](SubversionServer "wikilink")

### Linux DEB Distribution Kits

Nexus packages are available for Debian unstable and testing [out of the
box](http://packages.debian.org/source/sid/nexus). Therefore many
dependent distributions will pick up that package in due course. In the
mean time there is a [NeXus Personal Package Archive (PPA) for recent
Ubuntu versions](https://launchpad.net/~tsr-ubuntu/+archive/nexus)
available.

### Microsoft Windows Install Kit

[Windows Installer kits for
NeXus](http://download.nexusformat.org/kits/windows/)

### Apple Mac (OS-X) Install Kit

[MAC OSX Installer kits for
NeXus](http://download.nexusformat.org/kits/macosx/)

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
