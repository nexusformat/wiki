---
title: NeXus 43 Testing
permalink: NeXus_43_Testing/
layout: wiki
---

The provisional release notes for NeXus 4.3 [can be found
here](Nexus_43_Release_Notes "wikilink") The NeXus API testing procedure
is detailed at [SQA\_Process](SQA_Process "wikilink") and this page will
be used to record the results of testing for NeXus 4.3. The appropriate
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

Release candidates for 4.3.0
----------------------------

4.3.0 is currently in testing, 4.3rc1 being the first release candidate

### 4.3rc1 (released 30/11/2011)

The kit can be downloaded from the [NeXus download
page](http://download.nexusformat.org/kits/nx43testing.shtml). Issues
reported with this release [can be found
here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.3.0-rc1&order=priority).

| | Operating System     | | Processor | | Tester                                                                   | | Kit Type | | HDF4 | | HDF5       | | MXML | | “make check”                                                                                                                                                                                            | | Remarks        |
|------------------------|-------------|----------------------------------------------------------------------------|------------|--------|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| | Linux (FC15)         | 64bit Intel | [Freddie](User%3AFreddie_Akeroyd "wikilink") 10:31, 30 November 2011 (UTC) | tar        | 4.2.5  | 1.8.5-patch1 | 2.5-6  | 28 tests successful. 7 skipped (3/IDL, 3/FORTRAN, and Python+HDF4)                                                                                                                                        | gcc, g++, python |
| | Linux (Ubuntu 11.10) | 64bit Intel | [Stuart](User%3AStuart_Campbell "wikilink") 21:22, 30 November 2011 (UTC)  | tar        | 4.2.4  | 1.8.4-patch1 | 2.6-2  | 28 tests successful. 7 skipped (3/IDL, 3/FORTRAN, and Python+HDF4)                                                                                                                                        | gcc, g++, python |
| | Linux (RHEL 6.1)     | 64bit Intel | [Stuart](User%3AStuart_Campbell "wikilink") 22:02, 30 November 2011 (UTC)  | tar        | 4.2.5  | 1.8.5-patch1 | 2.5-5  | 28 tests successful. 7 skipped (3/IDL, 3/FORTRAN, and Python+HDF4)                                                                                                                                        | gcc, g++, python |
| | Linux (Ubuntu 10.04) | 32bit Intel | [Mark](User%3AMark_Koennecke "wikilink") 22:02, 5 December 2011 (UTC)      | tar        | 4.2.4  | 1.8.4        | 2.5-5  | 28 tests successful. 3 failed 7 skipped (3/IDL, 3/FORTRAN, and Python+HDF4)                                                                                                                               | gcc, g++, python |
| | Linux (FC16)         | 32bit Intel | [Freddie](User%3AFreddie_Akeroyd "wikilink") 10:31, 8 December 2011 (UTC)  | tar        | 4.2.6  | 1.8.7        | 2.5-6  | With optimisation enabled, 28 tests run. 7 skipped (3/IDL, 3/FORTRAN, and Python+HDF4) With optimisation disabled, 28 tests run. 3 failed (HDF5 C and C++). 7 skipped (3/IDL, 3/FORTRAN, and Python+HDF4) | gcc, g++, python |
| | Mac OSX 10.6.8       | 64bit Intel | \[\[User%3AMark Koennecke|Mark\] 11:36, 15 December 2011 (UTC)             | tar        | 4.2.4  | 1.8.8        | 2.6    | With optimisation enabled, 28 tests run. 7 skipped (3/IDL, 3/FORTRAN, and Python+HDF4) With optimisation disabled, 28 tests run. 6 failed (HDF4 C and C++). 7 skipped (3/IDL, 3/FORTRAN, and Python+HDF4) | gcc, g++, python |
| | Mac OSX 10.6.8       | 64bit Intel | \[\[User%3AMark Koennecke|Mark\] 11:36, 15 December 2011 (UTC)             | tar        | 4.2.6  | 1.8.8        | 2.6    | 28 tests run. 7 skipped (3/IDL, 3/FORTRAN, and Python+HDF4)                                                                                                                                               | gcc, g++, python |


