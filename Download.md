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

The source code distribution can be obtained from GitHub. One can either
checkout the git repositories to get access to the most recent
development code. To clone the definitions repository use

`$git clone `[`https://github.com/nexusformat/definitions.git`](https://github.com/nexusformat/definitions.git)` definitions`

or for the NAPI

`$git clone `[`https://github.com/nexusformat/code.git`](https://github.com/nexusformat/code.git)` code`

For release tarballs go to the release page for the
[NAPI](https://github.com/nexusformat/code/releases) or the
[definitions](https://github.com/nexusformat/definitions/releases). For
the definitions it is recommended to work on the current git repository
as the available release is outdated.

NeXus Binary Distributions
--------------------------

### Linux RPM Distribution Kits

<http://download.nexusformat.org/kits/rpm/>

### Linux DEB Distribution Kits

Nexus packages are available for Debian as a standard package. Many
dependent distributions will have them included as well.

### Microsoft Windows Install Kit

currently not up to date

### Apple Mac (OS-X) Install Kit

currently not up to date
