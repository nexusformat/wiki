---
title: Application Program Interface
permalink: Application_Program_Interface/
layout: wiki
---

The Application Program Interface (API) has been developed to facilitate
the reading and writing of NeXus files. Those writing applications to
produce NeXus files are encouraged to use the API in order to ensure
compliance with the NeXus standard. The latest version supports the
reading and writing of HDF4, HDF5, and, in the latest CVS version, XML
files.

The core routines have been written in C but wrappers are available for
a number of other languages including Fortran 77, Fortran 90, Java, and
IDL (with Python and others under development). The API makes the
reading and writing of NeXus files transparent; the user doesn't even
need to know the underlying format when reading a file since the API
calls are the same.

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

Core API Routines
-----------------

The core API provides the basic routines for reading, writing and
navigating NeXus files. It is designed to be modal; there is a hidden
state that determines which groups and data sets are open at any given
moment, and subsequent operations are implicitly performed on these
entities. This cuts down the number of parameters to pass around in API
calls, at the cost of forcing a certain pre-approved mode d'emploi. This
mode d'emploi will be familiar to most: it is very similar to navigating
a directory hierarchy; in our case, NeXus groups are the directories,
which contain data sets and/or other directories.

The core API comprises the following functional groups:

-   General initialization and shutdown: opening and closing the file,
    creating or opening an existing group or dataset, and closing them.
-   Reading and writing data and attributes to previously opened
    datasets.
-   Routines to obtain meta-data and to iterate over component datasets
    and attributes.
-   Handling of linking and group hierarchy.

### List of NeXus Core API Routines

| General Initialization and Shutdown |
|-------------------------------------|
| NXopen                              |
| NXclose                             |
| NXmakegroup                         |
| NXopengroup                         |
| NXclosegroup                        |
| NXmakedata                          |
| NXcompmakedata                      |
| NXopendata                          |
| NXcompress                          |
| NXclosedata                         |
| Reading and Writing                 |
| NXgetdata                           |
| NXgetslab                           |
| NXgetattr                           |
| NXputdata                           |
| NXputslab                           |
| NXputattr                           |
| NXflush                             |
| Meta-Data Routines                  |
| NXgetinfo                           |
| NXgetgroupinfo                      |
| NXinitgroupdir                      |
| NXgetnextentry                      |
| NXgetattrinfo                       |
| NXinitattrdir                       |
| NXgetnextattr                       |
| Linking and Group Hierarchy         |
| NXgetgroupID                        |
| NXgetdataID                         |
| NXmakelink                          |

Although the NeXus API is considerably simpler than the underlying HDF
code, writing NeXus files still involves much repetitive code. Mark
Koennecke has therefore proposed a Data Dictionary Language to reduce
the amount of programming.

-   NXdict.tex - a LaTeX file describing the NeXus Dictionary API

### Fortran 77 Interface

Wrapper routines to interface the Fortran and C code have been developed
by Freddie Akeroyd. The routines have the same names and argument lists
as the corresponding C routines, although we have added extra routines
for the input/output of character data and attributes. Care must be
taken to ensure enough space is allocated for the input/output
operations being performed.

It is necessary to reverse the order of indices in multidimensional
arrays, compared to an equivalent C program, so that data are stored in
the same order in the NeXus file.

Any program using the F77 API needs to include the following line near
the top in order to define the required constants (NXHANDLESIZE,
NXLINKSIZE, etc.) :

    include 'NAPIF.INC'

Here is a comparison of the types used in the C and F77 interface.

<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead>
<tr class="header">
<th><p>C</p></th>
<th><p>Fortran</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>int a, int* a</p></td>
<td><p>INTEGER A</p></td>
</tr>
<tr class="even">
<td><p>char* a</p></td>
<td><p>CHARACTER*(*) A</p></td>
</tr>
<tr class="odd">
<td><p>NXhandle a, NXhandle* a</p></td>
<td><p>INTEGER A(NXHANDLESIZE)</p></td>
</tr>
<tr class="even">
<td><p>NXstatus</p></td>
<td><p>INTEGER</p></td>
</tr>
<tr class="odd">
<td><p>int[] a</p></td>
<td><p>INTEGER A(*)</p></td>
</tr>
<tr class="even">
<td><p>void* a</p></td>
<td><p>REAL A(*) or DOUBLE A(*) or INTEGER A(*)</p></td>
</tr>
<tr class="odd">
<td><p>NXlink a, NXlink* a</p></td>
<td><p>INTEGER A(NXLINKSIZE)</p></td>
</tr>
</tbody>
</table>

### Fortran 90 Interface

The Fortran 90 interface is a wrapper to the C interface with nearly
identical routine definitions. As with the Fortran 77 interface, it is
necessary to reverse the order of indices in multidimensional arrays,
compared to an equivalent C program, so that data are stored in the same
order in the NeXus file.

Furthermore, we have developed a set of utility functions which are
designed to make the reading and writing of NeXus data files even easier
to code. When the manpower is available, equivalent functions will be
ported back to C.

Any program using the F90 API needs to put the following line at the top
(after the PROGRAM statement) :

    use NXmodule

### Java Interface

NeXus for Java provides access to NeXus data files for programs written
in Java. This API was implemented by Java code calling the original C
language NeXus API through the Java Native Methods Interface.

-   [Description of NeXus-Java interface](Java_API "wikilink")

### IDL Interface

IDL is an interactive data evaluation environment developed by Research
Systems. It is an interpreted language for data manipulation and
visualization. Part of IDL is an HDF-interface. In order to facilitate
the import of NeXus files into this popular data manipulation package,
the NeXus-API was reimplemented in the IDL language by Mark Koennecke.
The package may be downloaded as a tar file from
&lt;<ftp://ftp.neutron.anl.gov/nexus/nidl.tar>&gt;.

-   [Description of NeXus-IDL interface](IDL_API "wikilink")

Utility API
-----------

The NeXus F90 Utility API provides a number of routines that combine the
operations of various core API routines in order to simplify the reading
and writing of NeXus files. At present, they are only available as a
Fortran 90 module but a C version is in preparation.

The utility API comprises the following functional groups:

-   Routines to read or write data.
-   Routines to find if groups, data, or attributes exist, and to find
    data with specific signal or axis attributes i.e. to identify valid
    data or axes.
-   Routines to open other groups to which NXdata items are linked, and
    to return again.

Any program using the F90 Utility API needs to put the following line
near the top of the program (N.B. do not put USE statements for both
NXmodule and NXUmodule; the former is included in the latter) :

    use NXUmodule

### List of NeXus Utility API Routines

| Reading and Writing                  |
|--------------------------------------|
| NXUwriteglobals                      |
| NXUwritegroup                        |
| NXUwritedata                         |
| NXUreaddata                          |
| NXUwritehistogram                    |
| NXUreadhistogram                     |
| NXUsetcompress                       |
| Finding Groups, Data, and Attributes |
||
| NXUfindclass                         |
| NXUfinddata                          |
| NXUfindattr                          |
| NXUfindsignal                        |
| NXUfindaxis                          |
| Finding Linked Groups                |
| NXUfindlink                          |
| NXUresumelink                        |

Currently, the F90 utility API will only write character strings, 4-byte
integers and reals, and 8-byte reals. It can read other integer sizes
into four-byte integers, but does not differentiate between signed and
unsigned integers. Here are two example programs which make heavy use of
the Utility API.

[NXbrowse.f90](NXbrowse.f90 "wikilink") provides a simple terminal
browser of any NeXus file. When compiled and linked with the NeXus API,
it can be run interactively. Type HELP to obtain a list of available
commands. (Please note that this version of the browser has now been
superceded by a version written in C. Only the C version is now included
in the Makefile distributed with the API.)

[NXlrcs.f90](NXlrcs.f90 "wikilink") is a program for converting IPNS
data from the LRMECS chopper spectrometer into NeXus format. It cannot
be run without linking to the IPNS run-file modules (not provided), but
gives an example of how to write such programs.

Example NeXus program
---------------------

The following code reads a two-dimensional set 'counts' with dimension
scales of 't' and 'phi' using local routines, and then writes a NeXus
file containing a single NXentry group and a single NXdata group. This
is the simplest data file that conforms to the NeXus standard.

### C Version

    #include "napi.h"

    int main()
    {
        int counts[50][1000], n_t, n_p, dims[2], i;
        float t[1000], phi[50];
        NXhandle file_id;
    /* Read in data using local routines */
        getdata (n_t, t, n_p, phi, counts);
    /* Open output file and output global attributes */
        NXopen ('NXfile.nxs', NXACC_CREATE, &file_id);
          NXputattr (file_id, "user_name", "Joe Bloggs", 10, NX_CHAR);
    /* Open top-level NXentry group */
          NXmakegroup (file_id, "Entry1", "NXentry");
          NXopengroup (file_id, "Entry1", "NXentry");
    /* Open NXdata group within NXentry group */
            NXmakegroup (file_id, "Data1", "NXdata");
            NXopengroup (file_id, "Data1", "NXdata");
    /* Output time channels */
              NXmakedata (file_id, "time_of_flight", NX_FLOAT32, 1, &n_t);
              NXopendata (file_id, "time_of_flight")
                NXputdata (file_id, t);
                NXputattr (file_id, "units", "microseconds", 12, NX_CHAR);
                i = 1;
                NXputattr (file_id, "axis", &i, 1, NX_INT32);
              NXclosedata (file_id);
    /* Output detector angles */
              NXmakedata (file_id, "phi", NX_FLOAT32, 1, &n_p);
              NXopendata (file_id, "phi")
                NXputdata (file_id, phi);
                NXputattr (file_id, "units", "degrees", 7, NX_CHAR);
                i = 2;
                NXputattr (file_id, "axis", &i, 1, NX_INT32);
              NXclosedata (file_id);
    /* Output data */
              dims[0] = n_t;
              dims[1] = n_p;
              NXmakedata (file_id, "counts", NX_INT32, 2, dims);
              NXopendata (file_id, "counts")
                NXputdata (file_id, counts);
                i = 1;
                NXputattr (file_id, "signal", &i, 1, NX_INT32);
              NXclosedata (file_id);
    /* Close NXentry and NXdata groups and close file */
            NXclosegroup (file_id);
          NXclosegroup (file_id);
        NXclose (&file_id);
        return;
    }

### Fortran 77 Version

          program WRITEDATA
          
          include 'NAPIF.INC'
          integer*4 status, file_id(NXHANDLESIZE), counts(1000,50), n_p, n_t, dims(2)
          real*4 t(1000), phi(50)

    !Read in data using local routines
          call getdata (n_t, t, n_p, phi, counts)
    !Open output file
          status = NXopen ('NXFILE.NXS', NXACC_CREATE, file_id)
            status = NXputcharattr 
         +         (file_id, 'user', 'Joe Bloggs', 10, NX_CHAR)
    !Open top-level NXentry group
            status = NXmakegroup (file_id, 'Entry1', 'NXentry')
            status = NXopengroup (file_id, 'Entry1', 'NXentry')
    !Open NXdata group within NXentry group
              status = NXmakegroup (file_id, 'Data1', 'NXdata')
              status = NXopengroup (file_id, 'Data1', 'NXdata')
    !Output time channels
                status = NXmakedata 
         +         (file_id, 'time_of_flight', NX_FLOAT32, 1, n_t)
                status = NXopendata (file_id, 'time_of_flight')
                  status = NXputdata (file_id, t)
                  status = NXputcharattr 
         +         (file_id, 'units', 'microseconds', 12, NX_CHAR)
                  status = NXputattr (file_id, 'axis', 1, 1, NX_INT32)
                status = NXclosedata (file_id)
    !Output detector angles
                status = NXmakedata (file_id, 'phi', NX_FLOAT32, 1, n_p)
                status = NXopendata (file_id, 'phi')
                  status = NXputdata (file_id, phi)
                  status = NXputcharattr (file_id, 'units', 'degrees', 7, NX_CHAR)
                  status = NXputattr (file_id, 'axis', 2, 1, NX_INT32)
                status = NXclosedata (file_id)
    !Output data
                dims(1) = n_t
                dims(2) = n_p
                status = NXmakedata (file_id, 'counts', NX_INT32, 2, dims)
                status = NXopendata (file_id, 'counts')
                  status = NXputdata (file_id, counts)
                  status = NXputattr (file_id, 'signal', 1, 1, NX_INT32)
                status = NXclosedata (file_id)
    !Close NXdata and NXentry groups and close file
              status = NXclosegroup (file_id)
            status = NXclosegroup (file_id)
          status = NXclose (file_id)

          stop
          end

### Fortran 90 Version

    program WRITEDATA
          
       use NXUmodule

       type(NXhandle) :: file_id
       integer, pointer :: counts(:,:)
       real, pointer :: t(:), phi(:)

    !Use local routines to allocate pointers and fill in data
       call getlocaldata (t, phi, counts)
    !Open output file
       if (NXopen ("NXfile.nxs", NXACC_CREATE, file_id) /= NX_OK) stop
       if (NXUwriteglobals (file_id, user="Joe Bloggs") /= NX_OK) stop
    !Set compression parameters
       if (NXUsetcompress (file_id, NX_COMP_LZW, 1000) /= NX_OK) stop
    !Open top-level NXentry group
       if (NXUwritegroup (file_id, "Entry1", "NXentry") /= NX_OK) stop
       !Open NXdata group within NXentry group
          if (NXUwritegroup (file_id, "Data1", "NXdata") /= NX_OK) stop
       !Output time channels
             if (NXUwritedata (file_id, "time_of_flight", t, "microseconds") /= NX_OK) stop
                if (NXputattr (file_id, "axis", 1) /= NX_OK) stop
       !Output detector angles
             if (NXUwritedata (file_id, "phi", phi, "degrees") /= NX_OK) stop
                if (NXputattr (file_id, "axis", 2) /= NX_OK) stop
       !Output data
             if (NXUwritedata (file_id, "counts", counts, "counts") /= NX_OK) stop
                if (NXputattr (file_id, "signal", 1) /= NX_OK) stop
       !Close NXdata group
          if (NXclosegroup (file_id) /= NX_OK) stop
    !Close NXentry group
       if (NXclosegroup (file_id) /= NX_OK) stop
    !Close NeXus file
       if (NXclose (file_id) /= NX_OK) stop

    end program WRITEDATA

Downloading the API
-------------------

The NeXus API is distributed under the terms of the GNU Lesser General
Public License.

### External Libraries

Since NeXus uses HDF as the underlying binary format, it is necessary
first to install the HDF subroutine libraries and include files before
installing the NeXus API. It is not usually necessary to download the
HDF source code since precompiled object libraries exist for a variety
of operating systems including Windows, Mac OS X, Linux, and various
other flavors of Unix. Check the HDF web pages for more information:

-   <http://hdf.ncsa.uiuc.edu/>

The latest beta version of the NeXus API allows the reading and writing
of NeXus files in XML. This uses the Mini-XML library, developed by
Michael Sweet, which is also available as a precompiled binary library
for several operating systems. Please ensure that you install version
2.2.2 or later. Check the Mini-XML web pages for more information:

-   <http://www.easysw.com/~mike/mxml/>

### Source Code Distribution

The NeXus API may be built from source by downloading one of the
installation kits from the NeXus CVS server. The compilation uses the
GNU Autotools. Download the appropriate gzipped tar file, unpack it, and
run the standard configure procedure from the resulting nexus directory

    % tar -zxvf nexus-3.0.0.tar.gz
    % cd nexus
    % ./configure
    % make
    % make install

See the README file for further instructions.

-   [Download NeXus API
    v2.0.0](http://nexus.isis.rl.ac.uk/cgi-bin/viewcvs.cgi/cvs_root.tar.gz?tarball=1&only_with_tag=NEXUS_2_0_0)
-   [Download latest CVS
    version](http://nexus.isis.rl.ac.uk/kits/nexus-latest.tar.gz)

### NeXus RPM Distribution Kits

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

| | SZIP  |  [i386 Binary RPM](http://www.nexus.anl.gov/szip-2.0-1.i386.rpm)|  |   [Source RPM](http://www.nexus.anl.gov/szip-2.0-1.src.rpm)  |
|---------|:------------------------------------------------------------------:|:------------------------------------------------------------:|
| | HDF4  |  [i386 Binary RPM](http://www.nexus.anl.gov/hdf-4.2.1-1.i386.rpm)  |  [Source RPM](http://www.nexus.anl.gov/hdf-4.2.1-1.src.rpm)  |
| | HDF5  |  [i386 Binary RPM](http://www.nexus.anl.gov/hdf5-1.6.4-1.i386.rpm) |  [Source RPM](http://www.nexus.anl.gov/hdf5-1.6.4-1.src.rpm) |
| | MXML  |  [i386 Binary RPM](http://www.nexus.anl.gov/mxml-2.2.2-1.i386.rpm) |  [Source RPM](http://www.nexus.anl.gov/mxml-2.2.2-1.src.rpm) |
| | NeXus | [i386 Binary RPM](http://www.nexus.anl.gov/nexus-3.0.0-1.i386.rpm) | [Source RPM](http://www.nexus.anl.gov/nexus-3.0.0-1.src.rpm) |

Reporting Bugs in the NeXus API
-------------------------------

If you encounter any bugs in the installation or running of the NeXus
API, please report them online using the ISIS Bugzilla reporting system.

-   \[<http://bugs.isis.rl.ac.uk/buglist.cgi?query_format=specific&order=relevance+desc&bug_status=__open__&product=NeXus&content>=
    List current NeXus bug reports\]
-   [Enter a new NeXus bug
    report](http://bugs.isis.rl.ac.uk/enter_bug.cgi?product=NeXus)

