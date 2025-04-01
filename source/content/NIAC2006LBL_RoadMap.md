---
title: NIAC2006LBL RoadMap
permalink: NIAC2006LBL_RoadMap.html
layout: wiki
---

NIAC2006LBL RoadMap
===================

**ALL** neutron definitions **done**
------------------------------------

-   priority 1
    -   Monochromatic Neutron and X-ray Reflectometry
    -   Time-of-Flight Neutron Reflectometery
    -   Monochromatic Neutron and X-ray Single Crystal Diffractometers
        -   [MonoXPSD](MonoXPSD.html "wikilink") Monochromatic Single Crystal
            Diffractometer with Position Sensitive Detector
        -   [MonoXSingle](MonoXSingle.html "wikilink") Monochromatic Single
            Crystal Diffractometer with Single Detector
    -   [Monochromatic\_Neutron\_and\_X-ray\_Triple-Axis\_Spectrometer] (Monochromatic_Neutron_and_X-ray_Triple-Axis_Spectrometer.html "wikilink")
    -   [Archive\_Definition](Archive_Definition.html "wikilink")

<!-- -->

-   priority 2
    -   [Time-of-Flight\_Neutron\_Powder\_Diffraction](Time-of-Flight_Neutron_Powder_Diffraction.html "wikilink")
    -   [ Monochromatic Neutron and X-ray Small Angle
        Scattering](SAS.html "wikilink")
    -   Time-of-Flight Small Angle Scattering

<!-- -->

-   priority 3
    -   [Time-of-Flight\_Neutron\_Indirect\_Geometry\_Spectrometer] (Time-of-Flight_Neutron_Indirect_Geometry_Spectrometer.html "wikilink")
    -   Time-of-Flight Neutron Direct Geometry Spectrometer

<!-- -->

-   priority 4
    -   Time-of-Flight Neutron Single-Crystal Diffractometer
    -   Time-of-Flight Neutron Spin Echo Editor

Small Items
-----------

Axis attributes on fields
-------------------------

The current documentation describes that the fastest varying dimension
is annotated with “axis=1”. In practice the slowest varying dimension is
“axis=1”.

Geometry order of operations
----------------------------

When looking at a geometry is the orientation applied before the
translation or the other way around.

[XESraw](XESraw.html "wikilink")
---------------------------

scanning environment variables
------------------------------

-   Make sure we have an example of scanning an environment variable in
    scanraw
-   Consider how parametric scans will be represented (within and
    between entries)

Later
-----

-   sequencing entries and measurements
-   counting time for each data point
    -   Does this belong to some base class?
    -   Which one?
-   implement a versioning system
    -   switch to subversion
    -   use SVN tagging system

Proposed Agenda Items
---------------------

-   Discuss NeXus collaborating with imgCIF. see [MEDSBIO
    proposal](http://www.medsbio.org/)
-   Request institutes from the NeXus community sponsor a full-time
    technical secretary for next 12-24 months.
-   (*completed*) Institutes that write NeXus files are **data
    providers.**. NeXus provides an interface between **data providers**
    and **data requirers**. Discuss if the NIAC constitution should be
    change to allow data requirers e.g. DANSE to have representation on
    the NIAC as a stakeholder that requires NeXus.
-   (*working*) SCAN definition similar to TOFRAW definition
-   (*working*) NXcharacterization needs to be formalized
-   (*working*) Finalize [archive
    definition](Archive_Definition.html "wikilink")

