---
title: Housekeeping pre-NeXus2.0
permalink: Housekeeping_pre-NeXus2.0/
layout: wiki
---

Issue
-----

As an action item from the NIAC October 5-6, 2006 at LBL, Berkeley, CA,
USA, housekeeping of base classes and instrument definitions was
required before release of NeXus2.0

Proposal: Definition of housekeeping tasks
------------------------------------------

1.  set a release date for NeXus2.0
2.  define the task that can be achieved before the release date
    -   data entities include either a desciption or a (list of)
        value(s) but not both e.g.
        [NXdisk\_chopper](NXdisk_chopper "wikilink") type has both
        description and a list of values
    -   remove all “?” and “\*” (i.e. all elements are optional)
    -   leave all “+”
    -   fix typos and inconsistencies using a dictionary
    -   check all units against the standard [Units](Units "wikilink")

Some of these task may not be possible in the timeframe

### Proposal: Execute housekeeping tasks

It is proposed to execute these task using XSLT. We (ANSTO) have been
using regular expression in xslt to clean up the metaDTD for ANSTO use.
The tasks include:

1.  from the 'definition of housekeeping tasks', write the required xslt
    file
2.  Editors run the xslt file against the base classes and instrument
    definitions that generates a report which flag the points where the
    metaDTD diverges from the standard
3.  Editors fix the errors by hand and re-generate the reports
4.  Editor commits to nexusformat subversion repository

  
[Nick Hauser](User%3ANick_Hauser "wikilink") 05:03, 13 February 2007
(UTC)
