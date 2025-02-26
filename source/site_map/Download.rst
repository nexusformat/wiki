========
Download
========

The use of the NeXus-API (NAPI) is \**not*\* mandatory in order to write
perfectly valid NeXus files. > Using a direct binding to HDF5 (like
h5py) or [NeXpy](NeXpy.html) should be a better choice for new projects.
The NeXus API is distributed under the terms of the GNU Lesser General
Public License.

-----------Requirements ------------
====================================

External Libraries
==================

Since NeXus uses HDF as the main underlying binary format, it is necessary
first to install the HDF subroutine libraries and include files before
installing the NeXus API. It is not usually necessary to download the
HDF source code since precompiled object libraries exist for a variety
of operating systems including Windows, Mac OS X, Linux, and various
other flavors of Unix. Check the HDF web pages for more information: -
The NeXus API also supports using XML as the underlying on-disk format.
This uses the Mini-XML library, developed by Michael Sweet, which is
also available as a precompiled binary library for several operating
systems. Please ensure that you install version 2.2.2 or later. Check
the Mini-XML web pages for more information:

NeXus Source Code Distribution
==============================

The source code distribution can be obtained from GitHub. One can either checkout the git
repositories to get access to the most recent development code. To clone
the definitions repository use
gitclone [https://github.com/nexusformat/definitions.git] (https://github.com/nexusformat/definitions.git) definitions or for the NAPI
gitclone [https://github.com/nexusformat/code.git] (https://github.com/nexusformat/code.git) code
For release tarballs go to the release page for the [NAPI] (https://github.com/nexusformat/code/releases) or the
[definitions] (https://github.com/nexusformat/definitions/releases). For the definitions it is recommended to work on
the current git repository as the available release is outdated.
