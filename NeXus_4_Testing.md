---
title: NeXus 4 Testing
permalink: NeXus_4_Testing/
layout: wiki
---

The NeXus API testing procedure is detailed at
[SQA\_Process](SQA_Process "wikilink") and this page will be used to
record the results of testing for NeXus 4.0. The appropriate kit should
be downloaded and then the results of the tests recorded here. The table
should record:

-   The operating system version tested
-   The name of the tester
-   The kit type used: **tar** / **src** / **bin** for *.tar.gz* /
    *Source RPM (.src.rpm)* / *Binary RPM (.i386.rpm)*
-   The file formats picked up and tested by configure (HDF4/HDF5/XML)
-   The result of a “make check”
-   Any remarks that are not bugs/failures

Please file bug reports for build/test failures into the
[IssueReporting](IssueReporting "wikilink") system and choose the **rc**
number of the kit being tested from the version menu.

### 4.0rc1

The kit can be downloaded from [NeXus download
page](http://download.nexusformat.org/kits)

| | Operating System | | Tester        | | Kit Type | | File Formats | | “make check” | | Remarks |
|--------------------|-----------------|------------|----------------|----------------|-----------|
| | Linux (FC6)      | Freddie Akeroyd | tar        | HDF4/HDF5/XML  | passed         |           |
| | MacOS-X          |                 |            |                |


