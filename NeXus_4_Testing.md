---
title: NeXus 4 Testing
permalink: NeXus_4_Testing/
layout: wiki
---

The provisional release notes for NeXus 4.0 [can be found
here](Nexus_4_Release_Notes "wikilink") The NeXus API testing procedure
is detailed at [SQA\_Process](SQA_Process "wikilink") and this page will
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
[IssueReporting](IssueReporting "wikilink") system and choose the **rc**
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
| | Linux (FC6)         | [Freddie Akeroyd](User%3AFreddie_Akeroyd "wikilink") 15:04, 16 March 2007 (GMT) | tar        | HDF4/HDF5/XML  | passed         |                                          |
| | MacOS-X             | Jean Bilheux                                                                    | tar        | HDF4/HDF5/XML  | failed         | HDF4 and HDF5 failed                     |
| | Linux (RHEL4)       | Stuart Campbell                                                                 | tar        | HDF4/HDF5/XML  | passed         | g77, gfortran and Sun Java 5 (update 11) |
| | Linux (RHEL4 64bit) | Peter Peterson                                                                  | tar        | HDF4/HDF5/XML  | passed         | gfortran compiler and java 1.5.0\_11     |
| | MacOS-X (PowerPC)   | [Freddie Akeroyd](User%3AFreddie_Akeroyd "wikilink") 19:51, 28 March 2007 (BST) | tar        | HDF4/HDF5/XML  | passed         | gcc, g77, g95, gcj, fink HDF             |
| | MacOS-X (Intel)     | [Freddie Akeroyd](User%3AFreddie_Akeroyd "wikilink") 19:51, 28 March 2007 (BST) | tar        | HDF5/XML       | passed         | gcc, gfortran (4.2), gcj, fink HDF       |

### 4.0rc2 (released 30th March 2007)

The kit can be downloaded from the [NeXus download
page](http://download.nexusformat.org/kits). Issues reported with this
release [can be found
here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.0rc2&order=priority).

| | Operating System | | Processor                                                                     | | Tester | | Kit Type | | File Formats | | “make check” | | Remarks                   |
|--------------------|---------------------------------------------------------------------------------|----------|------------|----------------|----------------|-----------------------------|
| | Linux (FC6)      | [Freddie Akeroyd](User%3AFreddie_Akeroyd "wikilink") 18:27, 30 March 2007 (BST) |          | tar        | HDF4/HDF5/XML  | passed         | gcc/g95/gcj/python          |
| | Linux (RHEL4)    | [Stuart Campbell](User%3AStuart_Campbell "wikilink") 16:21, 2 April 2007 (BST)  |          | tar        | HDF4/HDF5/XML  | passed         | gcc/gfortran/java 1.5.0\_11 |


