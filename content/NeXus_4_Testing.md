---
title: NeXus 4 Testing
permalink: NeXus_4_Testing.html
layout: wiki
---

The provisional release notes for NeXus 4.0 [can be found
here](Nexus_4_Release_Notes.html "wikilink") The NeXus API testing procedure
is detailed at [SQA\_Process](SQA_Process.html "wikilink") and this page will
be used to record the results of testing for NeXus 4.0. The appropriate
kit should be downloaded and then the results of the tests recorded
here. The table should record:

-   The operating system version tested
-   The name of the tester. If you write ~~~~ in this space your Wiki
    name will be inserted when the page is saved.
-   The kit type used: **tar** / **src** / **bin** for *.tar.gz* /
    *Source RPM (.src.rpm)* / *Binary RPM (.i386.rpm)*
-   The file formats picked up and tested by configure (HDF4/HDF5/XML)
    and the programs used for compiling the API (e.g. gcc/gfortran/java
    1.5.0\_11)
-   The result of a “make check”
-   Any remarks that are neither bugs nor build/test failures

If the build or check fails, please file a bug report into the
[IssueReporting](IssueReporting.html "wikilink") system and choose the **rc**
number of the kit being tested from the version menu. Please also
include/attach:

-   A copy of any error messages displayed on your screen
-   For a “make check” failure, the file *test/testsuite.log*
-   The versions of the HDF4/HDF5/XML libraries used
-   Where these HDF4/HDF5/XML libraries were obtained e.g. built locally
    from source, installed by <whatever> package management tool.

### 4.0rc1 (released 16th March 2007)

The kit can be downloaded from the [NeXus download
page](http://download.nexusformat.org/kits). Issues reported with this
release [can be found
here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.0rc1&order=priority).

| | Operating System    | | Tester                                                                        | | Kit Type | | File Formats | | “make check” | | Remarks                                |
|-----------------------|---------------------------------------------------------------------------------|------------|----------------|----------------|------------------------------------------|
| | Linux (FC6)         | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 15:04, 16 March 2007 (GMT) | tar        | HDF4/HDF5/XML  | passed         |                                          |
| | MacOS-X             | Jean Bilheux                                                                    | tar        | HDF4/HDF5/XML  | failed         | HDF4 and HDF5 failed                     |
| | Linux (RHEL4)       | Stuart Campbell                                                                 | tar        | HDF4/HDF5/XML  | passed         | g77, gfortran and Sun Java 5 (update 11) |
| | Linux (RHEL4 64bit) | Peter Peterson                                                                  | tar        | HDF4/HDF5/XML  | passed         | gfortran compiler and java 1.5.0\_11     |
| | MacOS-X (PowerPC)   | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 19:51, 28 March 2007 (BST) | tar        | HDF4/HDF5/XML  | passed         | gcc, g77, g95, gcj, fink HDF             |
| | MacOS-X (Intel)     | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 19:51, 28 March 2007 (BST) | tar        | HDF5/XML       | passed         | gcc, gfortran (4.2), gcj, fink HDF       |

### 4.0rc2 (released 30th March 2007)

The kit can be downloaded from the [NeXus download
page](http://download.nexusformat.org/kits). Issues reported with this
release [can be found
here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.0rc2&order=priority).

| | Operating System   | | Processor | | Tester                                                                        | | Kit Type | | HDF4 | | HDF5 | | MXML | | “make check” | | Remarks                          |
|----------------------|-------------|---------------------------------------------------------------------------------|------------|--------|--------|--------|----------------|------------------------------------|
| | Linux (FC6)        | 32bit Intel | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 18:27, 30 March 2007 (BST) | tar        | 4.2.1  | 1.6.5  | 2.2.2  | passed         | gcc/g95/java(gcj)/python           |
| | Linux (RHEL4)      | 32bit Intel | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 16:21, 2 April 2007 (BST)  | tar        | 4.2.1  | 1.6.4  | 2.2.2  | passed         | gcc/gfortran/java 1.5.0\_11        |
| | Linux (RHEL4)      | 64bit Intel | [Peter Peterson](User%3APeter_Peterson.html "wikilink") 2007-04-02T14:54:34-0400     | tar        | 4.2.1  | 1.6.4  | 2.2.2  | passed         | gcc/gfortran/java 1.5.0\_11/python |
| | MS Windows (MinGW) | 32bit Intel | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 11:40, 11 April 2007 (BST) | tar        | 4.2.1  | 1.6.5  | 2.2.2  | passed         | gcc/java(gcj)                      |
| | MacOS-X            | Intel       | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 14:45, 16 May 2007 (BST)   | tar        | N/A    | 1.6.4  | 2.2.2  | passed         | gcc, gfortran (4.2), gcj, fink HDF |
| | MacOS-X            | PowerPC     | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 16:54, 16 May 2007 (BST)   | tar        | 4.2.0  | 1.6.4  | 2.2.2  | passed         | gcc, g77, g95, gcj, fink HDF       |

### 4.0rc3 (released 16th May 2007)

The kit can be downloaded from the [NeXus download
page](http://download.nexusformat.org/kits). Issues reported with this
release [can be found
here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.0rc3&order=priority).

| | Operating System      | | Processor | | Tester                                                                      | | Kit Type | | HDF4 | | HDF5 | | MXML | | “make check”    | | Remarks                                           |
|-------------------------|-------------|-------------------------------------------------------------------------------|------------|--------|--------|--------|-------------------|-----------------------------------------------------|
| | Mac OS X (10.4.9)     | Intel       | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 20:19, 16 May 2007 (BST) | tar        | N/A    | 1.6.4  | 2.2.2  | passed            | gcc, gfortran (4.3), sun java 1.5.0\_07, Fink HDF   |
| | Linux (RHEL4)         | 32bit Intel | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 20:37, 16 May 2007 (BST) | tar        | 4.2.1  | 1.6.4  | 2.2.2  | passed            | gcc, g77, gfortran, sun java 1.6.0                  |
| | Linux (SL3)           | 32bit Intel | [Mark Koennecke](User%3AMark_Koennecke.html "wikilink") 10:50, 21 May 2007 (EST)   | tar        | 4.2.1  | 1.6.4  | 2.2.2  | failed            | gcc, g77, Tcl, java-1.4.2                           |
| | Linux (openSUSE 10.2) | 32bit Intel | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 20:57, 16 May 2007 (BST) | tar        | 4.2.1  | 1.6.4  | 2.2.2  | passed            | gcc, g77, gfortran                                  |
| | Linux (RHEL4)         | 64bit Intel | --[Peter Peterson](User%3APeter_Peterson.html "wikilink") 21:19, 21 May 2007 (BST) | tar        | 4.2.1  | 1.6.5  | 2.2.2  | failed - f90 test | gcc, gfortran, gfortran, sun java 1.5.0\_11, python |
| | MS Windows (MinGW)    | 32bit Intel | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 20:17, 23 May 2007 (BST) | tar        | 4.2.1  | 1.6.5  | 2.2.2  | passed            | gcc/java(gcj)                                       |
| | MacOS-X               | PowerPC     | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 20:17, 23 May 2007 (BST) | tar        | 4.2.0  | 1.6.4  | 2.2.2  | passed            | gcc, g77, g95, gcj, fink HDF                        |

### NeXus 4.1 Release Candidates

These are available from [NeXus 41 Testing](NeXus_41_Testing.html "wikilink")
