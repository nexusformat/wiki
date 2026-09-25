---
title: NIAC2026 Minutes
permalink: NIAC2026_minutes.html
layout: wiki
---

NIAC2026 Minutes
================

Participants:
-------------
- NIAC in person: AB, SB, FdA, RB, HG, WdN, PM, MW, ZM, PC, RO, BB, HG, MO, (TM) 
- NIAC online: HB, BW, BB, GT
- other participants:
  - Aaron Finke
  - Andre Costa
  - Renee Helfert
  - Christopher Philip Schleisinger
  - Erika McPhillips - SLAC
  - Mustafa Alzubi - SESAME
  - Marius Retegan - ESRF
  - George O'Neill - ESS
  - Mridul Sath - ESS
  - Diego Gaemperle - DECTRIS
  - Jonas Fortmann - ZBT
  - Iryna Lypova - FRM II / TUM
  - Jan Kotanski - DESY
  - Loas Kron-Batenburg - RDL IUCrData
  - Markus Kuehbach - FAIRmat
  - Rubel Mozumder - FAIRmat
  - Lukas Pilsticker - FAIRmat
  - Oleksii Turkot - EuXFEL
  - Paulo Mausbach - SIRIUS
  - Eva Lott - HZB
  - Peter Braun - HZB
  - Hector Perez Ponce - HZB
  - Sonal Patel - HZB
  - Sarah Foxley - ISIS
  - Yannick Meinerzhagen - RWTH Aachen
  - Meghdad Yazdi - MAX IV
  - Clemens Vonrhein - Global Phasing
  - Patrick Pereira - SOLEIL
  - Daniel Eriksson - Australian Synchrotron
  - Abhjeet Gaur - KIT


## NIAC2026 Minutes

Session A: Sept 25th 08:00 UTC
------------------------------
- GON (ESS):
  - Status
    - JSON on top of NeXus;
    - only base classes;
    - users not understand the sandard details;
    - JSON walk & SCIPP: NXtransformation viewer;
    - most used: NXevent_data, NXdata, NXlog, NXtextlog
  - plan:
    - NeXus in the center;
    - easy XML definition extensions;
    - smoother acquistion/writer,
    - better visualisation,
    - more NX contribution,
    - integration with McStas;
    - improvments for geometries
- JK (DESY):
  - h5cpp, pninexus, pythin-pninexus writer
  - NeXpy viewer
  - AppDefs started to be used (NXmpes)
  - Need:
    - not all required fields are available, but it is now better because requirements are more relaxed
    - hdf5 performance issue with simultanious write and read 
- EL (HZB):
  - bluesky - NeXus (to NOMAD)
  - device definitions to NeXus
  - needs
    - mapping to App defs (pydentic model from NXDL)
    - referencing external asset documents
    - Tile integration
    - NXcollection -> NXbag?
- MA (SESAME):
  - no NeXus yet, but hdf5 writer is accepting template which could be NeXus
  - aim: uniform data format (e.g. NeXus: NXxas, NXmonopd, NXtomo,...)
  - bottlneck: efficient support from NIAC can  

Session B: Sept 25th 11:30 UTC
------------------------------
- EMcP (SLAC):
- LP (FAIRmat):
- IL (FRM II):
- PB (HZB):

Session C: Sept 25th 14:00 UTC
------------------------------


Session D: Sept 26th 18:00 UTC
------------------------------


Session E: Sept 26th 11:30 UTC
------------------------------


Session F: Sept 26th 14:00 UTC
------------------------------


Session G: Sept 27th 08:00 UTC
------------------------------


Session H: Sept 27th 11:30 UTC
------------------------------


Session I: Sept 27th 14:00 UTC
------------------------------

