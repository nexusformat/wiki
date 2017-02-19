---
title: NeXus 42 Testing
permalink: NeXus_42_Testing.html
layout: wiki
---

The provisional release notes for NeXus 4.2 [can be found
here](Nexus_42_Release_Notes.html "wikilink") The NeXus API testing procedure
is detailed at [SQA\_Process](SQA_Process.html "wikilink") and this page will
be used to record the results of testing for NeXus 4.2. The appropriate
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

Release candidates for 4.2.1
----------------------------

4.2.1 is currently in testing, 4.2rc5 being the first release candidate

### 4.2rc5 (released 25/02/2010)

The kit can be downloaded from the [NeXus download
page](http://download.nexusformat.org/kits/nx42testing.shtml). Issues
reported with this release [can be found
here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.2rc4&order=priority).

| | Operating System      | | Processor | | Tester                                                                        | | Kit Type | | HDF4 | | HDF5 | | MXML | | “make check”                                                       | | Remarks                             |
|-------------------------|-------------|---------------------------------------------------------------------------------|------------|--------|--------|--------|----------------------------------------------------------------------|---------------------------------------|
| | Linux (FC12)          | 64bit Intel | [Freddie](User%3AFreddie_Akeroyd.html "wikilink") 10:31, 25 February 2010 (UTC)      | tar        | 4.2.4  | 1.8.2  | 2.5-2  | 31 tests successful. 7 skipped (3/IDL, 3/NXsummary, and Python+HDF4) | gcc, g++, g77, f95, python            |
| | Linux SL5 == RHEL 5   | 32bit Intel | [Mark](User%3AMark_Koennecke.html "wikilink") 17:00, 25 February 2010 (UTC)          | tar        | 4.2.r2 | 1.6.6  | 2.5-2  | 32 tests successful.                                                 | gcc, g++, g77, python, IDL            |
| | Ubuntu Karmic Koala   | 32bit Intel | [Mark](User%3AMark_Koennecke.html "wikilink") 10:00, 3.3 2010 (UTC)                  | tar        | 4.1.4  | 1.6.6  | 2.5-2  | 25 tests successful.                                                 | gcc, g++, python                      |
| | Ubuntu Hardy heron    | 32bit Intel | [Mark](User%3AMark_Koennecke.html "wikilink") 10:00, 3.3 2010 (UTC)                  | tar        | 4.1.4  | 1.6.5  | 2.5-2  | 25 tests successful.                                                 | gcc, g++, python                      |
| | Mac OS X Snow Leopard | Intel       | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 16:09, 19 March 2010 (UTC) | tar        | 4.2.4  | 1.8.4  | 2.6    | 26 tests successful. 9 skipped (3/IDL, 3/FORTRAN, and 3/Python)      | gcc, g++, gfortran, java              |
| | Linux (RHEL5)         | 64bit Intel | [Stuart](User%3AStuart_Campbell.html "wikilink") 17:36, 19 March 2010 (UTC)          | tar        | 4.2.r4 | 1.6.10 | 2.5-2  | 26 tests successful. 9 skipped (3/IDL, 3/FORTRAN, and 3/Python)      | gcc, g++, g77, gfortran, java, python |

Release candidates for 4.2.0
----------------------------

4.2.0 was [officially released May 5,
2009](http://lists.nexusformat.org/pipermail/nexus/2009/000326.html))

### 4.2rc4 (released 23/02/2009)

The kit can be downloaded from the [NeXus download
page](http://download.nexusformat.org/kits/nx42testing.shtml). Issues
reported with this release [can be found
here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.2rc4&order=priority).

| | Operating System                   | | Processor | | Tester                                                                           | | Kit Type | | HDF4 | | HDF5 | | MXML | | “make check”                                                                                                        | | Remarks                                  |
|--------------------------------------|-------------|------------------------------------------------------------------------------------|------------|--------|--------|--------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| | Linux (FC10)                       | 32bit Intel | [Pete](User%3APete_Jemian.html "wikilink") 22:31, 23 February 2009 (UTC)                | tar        | 4.2.4  | 1.8.2  | 2.5-2  | 31 tests successful. 7 skipped (3/IDL, 3/NXsummary, and Python+HDF4)                                                  | gcc, g++, g77, f95, python                 |
| | Linux (RHEL4)                      | 64bit Intel | [Freddie](User%3AFreddie_Akeroyd.html "wikilink") 10:05, 24 February 2009 (UTC)         | tar        | 4.2.1  | 1.6.5  | 2.2.2  | 29 tests successful. 9 skipped (3/IDL, 3/Python, 3/Fortran)                                                           | gcc, g++                                   |
| | Windows XP (SP3)                   | 32bit Intel | [Freddie](User%3AFreddie_Akeroyd.html "wikilink") 10:05, 24 February 2009 (UTC)         | tar        | 4.2.1  | 1.6.5  | 2.2.2  | 29 tests successful. 9 skipped (3/IDL, 3/Python, 3/Fortran)                                                           | gcc, g++                                   |
| | Linux (Ubuntu Hardy Heron)         | 64bit Intel | [Cpascual](User%3ACpascual.html "wikilink") 13:34, 24 February 2009 (UTC)               | tar        | 4.1.4  | 1.6.5  | 2.4.1  | 28 tests ok , 6 failed (everything related to HDF4), 7 skipped (3 IDL, 3 NXsummary, 1 Python+HDF4)                    | gcc, g++, g77, gfortran, python, doxygen   |
| | Linux (SuSe 10.2)                  | 64bit Intel | [Cpascual](User%3ACpascual.html "wikilink") 13:34, 24 February 2009 (UTC)               | tar        | -      | 1.8.2  | -      | 8 tests were successful. 30 tests were skipped (everything involving HDF4, XML or bindings other than g++ and python) | gcc, g++, python                           |
| | Linux (SuSe 10.2)                  | 32bit Intel | [Cpascual](User%3ACpascual.html "wikilink") 13:34, 24 February 2009 (UTC)               | tar        | 4.2.1  | 1.8.2  | 2.2.2  | 31 tests were successful. 7 tests were skipped (3 Fortran, 3 IDL, 1 Python+HDF4).                                     | gcc, g++, python                           |
| | Linux SL-5                         | 31bit Intel | [Mark Koennecke](User%3AMakr_Koennecke.html "wikilink") 13:34, 24 February 2009 (UTC)   | tar        | 4.2r2  | 1.6.6  | 2.3    | 25 tests ok , 1 failed (IDL-HDF-5 because of different HDF5 version)                                                  | gcc, g++, g77, gfortran, python, idl, java |
| | Linux (Fedora 10)                  | 64bit Intel | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 22:01, 24 February 2009 (UTC) | tar        | 4.2r3  | 1.8.1  | 2.5    | 34 tests were successful , 4 tests were skipped (3 IDL, 1 Python-HDF4)                                                | gcc, g++, gfortran, python, openjdk        |
| | Linux (ubuntu 8.10 intrepid)       | 64bit Intel | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 22:07, 24 February 2009 (UTC) | tar        | 4.1r4  | 1.6.6  | 2.5    | 29 tests were successful , 7 tests were skipped (3 IDL, 1 Python-HDF4, 3 NXsummary)                                   | gcc, g++, gfortran, python                 |
| | Linux (openSUSE 11.1)              | 64bit Intel | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 22:33, 24 February 2009 (UTC) | tar        |        | 1.8.1  | 2.5    | 19 tests were successful , 19 tests were skipped (3 IDL, 3 NXsummary, 13 HDF4 related)                                | gcc, g++, gfortran, python-2.6, openjdk    |
| | Linux (ubuntu 8.10 intrepid)       | 32bit Intel | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 22:07, 24 February 2009 (UTC) | tar        | 4.1r4  | 1.6.6  | 2.5    | 34 tests were successful , 4 tests were skipped (3 IDL, 1 Python-HDF4)                                                | gcc, g++, gfortran, python, openjdk        |
| | Linux (CentOS 5.2)                 | 64bit Intel | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 15:09, 25 February 2009 (UTC) | tar        | 4.2r4  | 1.6.8  | 2.5    | 34 tests were successful , 4 tests were skipped (3 IDL, 1 Python-HDF4)                                                | gcc, g++, gfortran, python, openjdk        |
| | Linux Ubuntu Hard Heron            | 32bit Intel | [Mark Koennecke](User%3AMark_Koennecke.html "wikilink") 09:00, 26 February 2009 (UTC)   | tar        | 4.2r4  | 1.6.8  | 2.5    | Python, C, C++, F77 (after fix 166), Java, successfull, rest skipped                                                  | gcc, g++, gfortran, python,                |
| | Mac OS X Leopard                   | PowerPC     | [Mark Koennecke](User%3AMark_Koennecke.html "wikilink") 13:00, 26 February 2009 (UTC)   | tar        | 4.2r2  | 1.6.6  | 2.3    | 31 success, 7 skipped (F77, IDL)                                                                                      | gcc, g++, gfortran, python,                |
| | Linux (Ubuntu Hardy Heron 8.04LTS) | 32bit Intel | [Pete](User%3APete_Jemian.html "wikilink") 03:53, 27 February 2009 (UTC)                | tar        | 4.2.3  | 1.8.2  | 2.5-2  | 31 tests successful. 7 skipped (3/IDL, 3/NXsummary, and Python+HDF4)                                                  | gcc, g++, g77, f95, python                 |

### 4.2rc2 (released 3/12/2008)

The kit can be downloaded from the [NeXus download
page](http://download.nexusformat.org/kits/nx42testing.shtml). Issues
reported with this release [can be found
here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.2rc2&order=priority).

| | Operating System           | | Processor  | | Tester                                                                           | | Kit Type | | HDF4 | | HDF5 | | MXML | | “make check”                      | | Remarks                                |
|------------------------------|--------------|------------------------------------------------------------------------------------|------------|--------|--------|--------|-------------------------------------|------------------------------------------|
| | Linux (FC6)                | 32bit Intel  | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 18:46, 3 December 2008 (BST)  | tar        | 4.2.1  | 1.6.5  | 2.2.2  | passed                              | gcc, g77, g95, gcj, python               |
| | Linux (SL5)                | 32bit Intel  | [Mark Koennecke](User%3AMark_Koennecke.html "wikilink") 10:00, 17 December 2008         | tar        | 4.2.2  | 1.6.6  | 2.2.2  | passed                              | gcc, g77, g95, java1.6.0, Tcl, python    |
| | Linux (Ubuntu Hardy Heron) | 32bit Intel  | [Mark Koennecke](User%3AMark_Koennecke.html "wikilink") 11:00, 17 December 2008         | tar        | 4.1.4  | 1.6.5  | 2.2.2  | passed                              | gcc, g77, java1.6.0, python              |
| | Linux (Ubuntu Hardy Heron) | 64bit Intel  | [Cpascual](User%3ACpascual.html "wikilink") 14:06, 9 January 2009 (UTC)                 | tar        | 4.1.4  | 1.6.5  | 2.4.1  | 29 tests ok , 3 skipped (NXsummary) | gcc, g++, g77, gfortran, python, doxygen |
| | Mac OS X 10.5 Leopard      | Power-PC     | [Mark Koennecke](User%3AMark_Koennecke.html "wikilink") 12:00, 17 December 2008         | tar        | 4.2.2  | 1.6.6  | 2.2.2  | passed                              | gcc, java1.6.0, python                   |
| | Win XP PRO (SP3)           | Intel 32 bit | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 18:00, 17 December 2008       | tar        | 4.2.1  | 1.6.5  | 2.2.2  | passed                              | gcc                                      |
| | Linux (F10)                | Intel 32 bit | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 16:46, 26 December 2008 (UTC) | tar        | 4.2r3  | 1.8.1  | 2.5    | passed                              | gcc, gfortran, openjdk, python           |

### 4.2rc1 (released 24/10/2008)

The kit can be downloaded from the [NeXus download
page](http://download.nexusformat.org/kits/nx42testing.shtml). Issues
reported with this release [can be found
here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.2rc1&order=priority).

| | Operating System | | Processor | | Tester                                                                           | | Kit Type | | HDF4 | | HDF5 | | MXML | | “make check” | | Remarks                       |
|--------------------|-------------|------------------------------------------------------------------------------------|------------|--------|--------|--------|----------------|---------------------------------|
| | Linux (FC6)      | 32bit Intel | [Freddie Akeroyd](User%3AFreddie_Akeroyd.html "wikilink") 18:46, 29 August 2007 (BST)   | tar        | 4.2.1  | 1.6.5  | 2.2.2  | passed         | gcc, g77, g95, gcj, python      |
| | Linux (F9)       | 32bit Intel | [Stuart Campbell](User%3AStuart_Campbell.html "wikilink") 02:37, 11 November 2008 (UTC) | tar        | 4.2r3  | 1.8.1  | 2.2.2  | passed         | gcc, g77, gfortran, openjdk 1.6 |


