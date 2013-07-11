---
title: NeXus CIF Integration
permalink: NeXus_CIF_Integration/
layout: wiki
---

NeXus CIF Merger
================

At august, 22, 2013 some members of the NIAC will meet with
representatives of the CIF community and the IUCR in order to discuss a
possible merger or collaboration between NeXus and CIF. This wiki page
is meant as a forum to discuss the NIACS position towards this merger.
The initial reaction was quite positive.

Some Issues and Differences
===========================

-   NeXus addresses a far greater range of techniques and
    instrumentation then CIF does.
-   NeXus is about hierarchical data storage and arrays
-   CIF so far prefers tables and ASCII.
-   CIF (or Herbert) are very concerned about getting data out of files
    into relational databases. The NeXus position as of now is to store
    the necessary information in a NeXus file and have databases
    populated by external scanners. Thus NeXus makes no assumptions
    about database structures.
-   Both CIF and NeXus have dictionaries of documented names. In many
    cases the dictionaries overlap.
-   NeXus is based on HDF-5 and NXDL, CIF on the star ASCII file format
    and DDL as a dictionary description language. There are many
    versions of DDL.
-   CIF's ASCII file format is hitting a limit when storing raw data
    from modern high speed detectors. Or sometimes even when storing
    atom positions for huge protein structures.
-   Herbert has demonstrated that it is possible to map CIF into NeXus.
    There are issues but no real show stoppers.

Questions
=========

-   Is CIF ready to expand towards a more general data format?
-   How are the NeXus and CIF dictionaries to be merged? Or are they to
    be merged?
-   Is the merged product still CIF or NeXus or do we need a new name?
-   How will the new joint file format be used? I assume for deposition
    of data with IUCR journals.
-   What exactly is the interest of the CIF community to collaborate
    with NeXus?
-   Which CIF concepts would need to be included into NeXus to make it
    work?

The NIACS Interest
==================

-   NeXus has always tried to be inclusive: it is no use having a
    standard if everyone has an own one!
-   Recognition by the IUCR would be a selling point for NeXus and
    helpful.

To Discuss
==========

-   Anything to add to the statements above?
-   NeXus tries to be inclusive: how far are we prepared to change?
    Presumably this can only be answered after the meeting when we can
    see more clearly what the merger means. It is also crystal clear
    that any changes to NeXus for a CIF merger need proper process:
    discussion and voting.

