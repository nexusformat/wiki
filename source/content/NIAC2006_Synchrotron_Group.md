---
title: NIAC2006 Synchrotron Group
permalink: NIAC2006_Synchrotron_Group.html
layout: wiki
---
NIAC2006 Synchrotron Group
==========================

Nexus – Synchrotron breakout group
----------------------------------

These are notes from our first discussion on 2006-02-01

present : AG (ESRF), RW (ESRF), PJ (APS), CM (Soleil), SP (Soleil), SC
(Diamond), LL (CCLRC,RAL)

RW – ESRF has their own format but willing to adopt

PJ – need an international collaborative effort, EPICS low level

SP – Soleil has adopted Nexus, need tools, developed a tango generic
system store data in Nexus, NO DATA to store yet, need to start quickly
to store data, do not need a complete DTD

SC – committed to Nexus, MX beamlines will store imageCIF, prefer to
store data in Nexus in the long term, EPICS low level simulators, simple
classes to start with

LL – working on catalogue information, TOF meta-data definition, data
portal to access different type of data for modelled and measured data

PJ – basic questions about which class contains which ?

### PROPOSED CLASSES

-   COMMON
    -   source
    -   insertion device
    -   bending magnet

<!-- -->

-   INSTRUMENTS
    -   tomography
    -   pin hole saxs
    -   exafs
    -   powder diffraction
    -   single crystal diffraction
    -   protein crystallography

<!-- -->

-   BEAMLINE COMPONENTS
    -   bpm
    -   goniometer

<!-- -->

-   DETECTORS
    -   ccd
    -   psd
    -   ionisation chamber
    -   opaque data (image plates, other large data slugs)

#### NXsource additions

| Name    | Type          | Description                                          |
|---------|---------------|------------------------------------------------------|
| mode    | | NX\_CHAR    | | synchrotron mode e.g. single bunch, multi bunch... |
| top\_up | | NX\_BOOLEAN | | flag indicating top-up mode                        |

<i>NXsource is more like NXfacility for us</i>

#### NXinsertion\_device

| Name      | Type        | Description                                |
|-----------|-------------|--------------------------------------------|
| name      | | NX\_CHAR  | | name of insertion device (ID33, UD02)    |
| type      | | NX\_CHAR  | | undulator, wiggler, ...                  |
| gap       | | NX\_FLOAT | | gap in mm                                |
| taper     | | NX\_FLOAT | | taper in mm                              |
| phase     | |NX\_FLOAT  | |phase in degrees                          |
| poles     | |NX\_INT    | |number of poles                           |
| length    | |NX\_FLOAT  | |length of insertion device                |
| power     | |NX\_FLOAT  | |total power delivered by insertion device |
| energy    | |NX\_FLOAT  | |energy of peak                            |
| bandwidth | |NX\_FLOAT  | |bandwidth of peak energy                  |
| harmonic  | |NX\_INT    | |harmonic of peak                          |
| spectrum  | |NXdata     | |spectrum of insertion device              |
| geometry  | |NXgeometry | |position, orientation of insertion device |

#### NXbending\_magnet

| Name            | Type        | Description                                |
|-----------------|-------------|--------------------------------------------|
| name            | | NX\_CHAR  | | name of bending magnet                   |
| critical energy | | NX\_FLOAT | | critical energy                          |
| bending radius  | | NX\_FLOAT | |                                          |
| spectrum        | |NXdata     | |spectrum of insertion device              |
| geometry        | |NXgeometry | |position, orientation of insertion device |

### Questions

1.  Can we have NX\_BOOLEAN ?
2.  Do we have to use microamp units for current ?
3.  Why is NXmonitor not NXdata ?

### IDEAS

NXbeam\_position\_monitor could be a separate class (subclass of NXlog)
?
