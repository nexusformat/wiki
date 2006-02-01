---
title: NIAC2006: Synchrotron Group
permalink: NIAC2006:_Synchrotron_Group/
layout: wiki
---

Nexus – Synchrotron breakout group
----------------------------------

These are notes from our first discussion on 2006-02-01

present : AG (ESRF), RW (ESRF), PJ (APS), CM (Soleil), SL (Soleil), SC
(Diamond), LL (ISIS)

RW – ESRF has their own format but willing to adopt

PJ – need an international collaborative effort, EPICS low level

SL – Soleil has adopted Nexus, need tools, developed a tango generic
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

### NXsource is more like NXfacility for us

#### NXsource additions

| Name  | Type     | Description                                        |
|-------|----------|----------------------------------------------------|
| mode  | NX\_CHAR | synchrotron mode e.g. single bunch, multi bunch... |
| topup | NX\_INT  | flag indicating topup mode (0=no, 1=yes)           |

    Name    Type    Description 
    mode    NX_CHAR synchrotron mode e.g. single bunch, multi bunch...  
    topup   NX_INT  flag indicating topup mode (0=no, 1=yes)    

#### NXinsertion\_device

    Name        Type    Description 
    name        NX_CHAR name of insertion device    
    gap     NX_FLOAT    gap in mm   
    taper       NX_FLOAT    taper in mm 
    phase       NX_FLOAT    phase in degrees    
    poles       NX_INT  number of poles 
    length      NX_FLOAT    length of insertion device  
    power       NX_FLOAT    total power delivered by insertion device   
    energy      NX_FLOAT    energy of peak  
    bandwidth   NX_FLOAT    bandwidth of peak energy    
    harmonic    NX_INT  harmonic of peak    
    spectrum    NXdata  spectrum of insertion device    

#### NXbending\_magnet

    Name        Type    Description 
    name        NX_CHAR name of bending magnet  
    critical energy NX_FLOAT    critical energy 
    bending radius  NX_FLOAT        

### Questions

1.  Can we have NX\_BOOLEAN ?
2.  Do we have to use microamp units for current ?
3.  Why is NXmonitor not NXdata ?

### IDEAS

NXbeam\_position\_monitor could be a separate class (subclass of NXlog)
?
