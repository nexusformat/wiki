---
title: NIAC2006LBL RoadMap
permalink: NIAC2006LBL_RoadMap/
layout: wiki
---

**ALL** neutron definitions **done**
------------------------------------

-   priority 1
    -   Monochromatic Neutron and X-ray Reflectometry
    -   Time-of-Flight Neutron Reflectometery
    -   Monochromatic Neutron and X-ray Single Crystal Diffractometer
    -   Monochromatic Neutron and X-ray Triple-Axis Spectrometer
    -   Archive Definition
-   priority 2
    -   Monochromatic Neutron Triple-Axis
    -   Time-of-Flight Neutron Powder Diffraction
    -   Monochromatic Neutron and X-ray Small Angle Scattering
    -   Time-of-Flight Small Angle Scattering
-   priority 3
    -   Time-of-Flight Neutron Indirect Geometry Spectrometer
    -   Time-of-Flight Neutron Direct Geometry Spectrometer
-   priority 4
    -   Time-of-Flight Neutron Single-Crystal Diffractometer
    -   Time-of-Flight Neutron Spin Echo Editor

Small Items
===========

Axis attributes on fields
-------------------------

The current documentation describes that the fastest varying dimension
is annotated with “axis=1”. In practice the slowest varying dimension is
“axis=1”.

Detector dimensions and array dimensions
----------------------------------------

Geometry order of operations
----------------------------

When looking at a geometry is the orientation applied before the
translation or the other way around.

[XESraw](XESraw "wikilink")
---------------------------

modify NXmonitor
----------------

Add “current” (units: mA) to NXmonitor “mode” field to represent a
normalization against the X-ray storage ring current or X-ray tube
operating current.

Later
=====

-   sequencing entries and measurements
-   counting time for each data point
    -   Does this belong to some base class?
    -   Which one?
-   implement a versioning system
    -   switch to subversion
    -   use SVN tagging system

Proposed Agenda Items
=====================

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
    definition](Archive_Definition "wikilink")

