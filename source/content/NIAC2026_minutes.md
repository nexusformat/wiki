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
  - Florin Boariu - Uni Potsdam


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
  - bottleneck: efficient support from NIAC can  

Session B: Sept 25th 11:30 UTC
------------------------------
- EMcP (SLAC):
  - data compression in NXmx (compression level and read is good, but not ideal)
  - question: any better and standardised way?
  - saprse data: could HDF5 lib cover it? what about looking at it as event data? or as data processing/reduction result?
- LP (FAIRmat):
  - NeXus in NOMAD
  - NeXus Ontology to place NeXus Metadata into semantic ontology world
  - plan: more flexible experiment description, incl. multi-model experiments
  - need:
    - improve and clarify NXDL to describe semantics better
    - use of PIDs
    - link NeXus to external knowledge (e.g. ontologies)
    - multimodel experiments
    - how wide NeXus coverage shall be in terms of experiment techniques 
- IL (FRM II):
  - zoo of data formats
  - plan:
    - move to NeXus (and use it with Mantid, Miezepy, OpenHKL, Steca, Ufit, BerSANS...)
    - use NXtransofmration for complex geometry detector description
    - store simulation data in NeXus, too
    - also processed/reduced data should go to NeXus (like NX in Mantid)
  - questions:
    - how to best create new application definitinos
    - shall we propose new defintion or rather (miss)use not 100% fitting base classes
    - where to put unnecessary Nicos (DAQ) parameters? may be difficult to decide what is needed what is not.
    - shall we use master-file and original raw data to separate files
    - multi-modal experiments
    - how to use PIDs
    - new definitinos shall have only proper description , or name must also be  descriptive?
    - needs of the TAS (Triple Axis Spectroscopy) community? will name harmonisation needed?
    - next to new AppDefs, new base classes are also needed
- PB (HZB):
  - SECoP (Sample Environment) -> NeXus, and now more generic needs for Operando (measured during operation) experiments
  - needs:
    - multi-modal experiments
    - hardware setup description
    - link to external knowledge
    - supporting 'identifier's for fields, too, not only for groups
  - questions/comments:
    - measurements may go parallel or subsequential or overalpping
    - shall we have an NXmass_spectrometry or just describe things in NXenvironment? or somewhere else in the NeXus tree?
    - global timestamps for all subexperiments
    - global view (during the full experiment) for sensors/stages (not only in a subtechnique)
    - instead of AppDefs, maybe base classes with runtime annotation with ontology links
    - how to link a definition (and not a data item) to an ontology concept?
    - what about chemical formula which also changes during operando
- discussion:
  - what is a blocker with NeXus
    - availability of tools
    - how to use NeXus at all?
    - what to do when an application (architecture/structure) misses information
      - archiver format? interchange format?
      - sematic definition being independent from actual binary representation?
      - how to deal with only partial data?
    - how to extend the schema?
    - NXDL is a blocker; NYAML helps, but still uncomfortable unconvential rules e.g. PARTIAL names
  - what is the role of NIAC:
    - stear the definitions
    - also tutorials and facilitaion (better documentation) of working with NeXus? 

Session C: Sept 25th 14:00 UTC
------------------------------
- HO (HZB):
- YM (RWTH):
- MY (MaxIV):
- MR (ESRF):

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

