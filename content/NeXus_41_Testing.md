---
title: NeXus 41 Testing
permalink: NeXus_41_Testing.html
layout: wiki
---

The provisional release notes for NeXus 4.1 [can be found
here](Nexus_41_Release_Notes.html "wikilink") The NeXus API testing procedure
is detailed at [SQA\_Process](SQA_Process.html "wikilink") and this page will
be used to record the results of testing for NeXus 4.1. The appropriate
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

### 4.1rc1 (released 29th August 2007)

The kit can be downloaded from the [NeXus download
page](http://download.nexusformat.org/kits/nx41testing.shtml). Issues
reported with this release [can be found
here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.1rc1&order=priority).

| | Operating System   | | Processor  | | Tester                                                                                     | | Kit Type | | HDF4 | | HDF5 | | MXML | | “make check” | | Remarks                                           |
|----------------------|--------------|----------------------------------------------------------------------------------------------|------------|--------|--------|--------|----------------|-----------------------------------------------------|
| | Linux (FC6)        | 32bit Intel  | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 18:46, 29 August 2007 (BST)             | tar        | 4.2.1  | 1.6.5  | 2.2.2  | passed         | gcc, g77, g95, gcj, python                          |
| | Linux (F7)         | 32bit Intel  | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 11:07, 12 September 2007 (BST)          | tar        | 4.2.1  | 1.6.5  | 2.2.2  | passed         | gcc, g77, gfortran, sun java-1.6.0\_2, python       |
| | Linux (RHEL4)      | 64bit Intel  | [Peter Peterson](User%3APeter_Peterson.html "wikilink") 14:58, 30 August 2007 (BST)               | tar        | 4.2.1  | 1.6.5  | 2.2.2  | passed         | gcc, gfortran, gfortran, sun java 1.5.0\_11, python |
| | Linux (SL3)        | 32 bit Intel | [User%3AMark Koennecke](User%3AMark_Koennecke.html "wikilink") 17:00, 08 October 2007             | tar        | 4.2.0  | 1.6.3  | 2.2.2  | passed         | gcc, g77, tcl, sun java 1.4.2                       |
| | MS Windows (MinGW) | 32bit Intel  | [User%3ANick Maliszewskyj](User%3ANick_Maliszewskyj.html "wikilink") 10:50, 31 October 2007 (EST) | tar        | 4.2.1  | 1.6.6  | 2.2.2  | passed         | gcc/java(gcj)                                       |
| | MacOS X            | 32 bit Intel | [User%3ANick Maliszewskyj](User%3ANick_Maliszewskyj.html "wikilink") 18:23, 29 October 2007 (EST) | tar        | 4.2.0  | 1.6.4  | 2.2.2  | passed         | gcc, gfortran (4.2), gcj, fink HDF                  |

