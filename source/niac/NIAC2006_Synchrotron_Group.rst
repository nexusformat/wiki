==========================
NIAC2006 Synchrotron Group
==========================

.. container:: content

   .. container:: page

      .. rubric:: NIAC2006 Synchrotron Group
         :name: NIAC2006_Synchrotron_Group_niac2006-synchrotron-group
         :class: page-title

      .. rubric:: Nexus " Synchrotron breakout group
         :name: NIAC2006_Synchrotron_Group_nexus--synchrotron-breakout-group

      These are notes from our first discussion on 2006-02-01

      present : AG (ESRF), RW (ESRF), PJ (APS), CM (Soleil), SP
      (Soleil), SC (Diamond), LL (CCLRC,RAL)

      RW " ESRF has their own format but willing to adopt

      PJ " need an international collaborative effort, EPICS low level

      SP " Soleil has adopted Nexus, need tools, developed a tango
      generic system store data in Nexus, NO DATA to store yet, need to
      start quickly to store data, do not need a complete DTD

      SC " committed to Nexus, MX beamlines will store imageCIF, prefer
      to store data in Nexus in the long term, EPICS low level
      simulators, simple classes to start with

      LL " working on catalogue information, TOF meta-data definition,
      data portal to access different type of data for modelled and
      measured data

      PJ " basic questions about which class contains which ?

      .. rubric:: PROPOSED CLASSES
         :name: proposed-classes

      -  COMMON

         -  source
         -  insertion device
         -  bending magnet

      -  INSTRUMENTS

         -  tomography
         -  pin hole saxs
         -  exafs
         -  powder diffraction
         -  single crystal diffraction
         -  protein crystallography

      -  BEAMLINE COMPONENTS

         -  bpm
         -  goniometer

      -  DETECTORS

         -  ccd
         -  psd
         -  ionisation chamber
         -  opaque data (image plates, other large data slugs)

      .. rubric:: NXsource additions
         :name: nxsource-additions

      +--------+------+-------------+---+--------------------------------------------------+
      | Name   | Type | Description |   |                                                  |
      +========+======+=============+===+==================================================+
      | mode   |      | NX_CHAR     |   | synchrotron mode e.g. single bunch, multi bunch  |
      +--------+------+-------------+---+--------------------------------------------------+
      | top_up |      | NX_BOOLEAN  |   | flag indicating top-up mode                      |
      +--------+------+-------------+---+--------------------------------------------------+

      *NXsource is more like NXfacility for us*

      .. rubric:: NXinsertion_device
         :name: nxinsertion_device

      ========= ==== =========== = =========================================
      Name      Type Description    
      ========= ==== =========== = =========================================
      name           NX_CHAR       name of insertion device (ID33, UD02)
      type           NX_CHAR       undulator, wiggler,  
      gap            NX_FLOAT      gap in mm
      taper          NX_FLOAT      taper in mm
      phase          NX_FLOAT      phase in degrees
      poles          NX_INT        number of poles
      length         NX_FLOAT      length of insertion device
      power          NX_FLOAT      total power delivered by insertion device
      energy         NX_FLOAT      energy of peak
      bandwidth      NX_FLOAT      bandwidth of peak energy
      harmonic       NX_INT        harmonic of peak
      spectrum       NXdata        spectrum of insertion device
      geometry       NXgeometry    position, orientation of insertion device
      ========= ==== =========== = =========================================

      .. rubric:: NXbending_magnet
         :name: nxbending_magnet

      +-----------------+------+-------------+---+-------------------------------------------+
      | Name            | Type | Description |   |                                           |
      +=================+======+=============+===+===========================================+
      | name            |      | NX_CHAR     |   | name of bending magnet                    |
      +-----------------+------+-------------+---+-------------------------------------------+
      | critical energy |      | NX_FLOAT    |   | critical energy                           |
      +-----------------+------+-------------+---+-------------------------------------------+
      | bending radius  |      | NX_FLOAT    |   |                                           |
      +-----------------+------+-------------+---+-------------------------------------------+
      | spectrum        |      | NXdata      |   | spectrum of insertion device              |
      +-----------------+------+-------------+---+-------------------------------------------+
      | geometry        |      | NXgeometry  |   | position, orientation of insertion device |
      +-----------------+------+-------------+---+-------------------------------------------+

      .. rubric:: Questions
         :name: questions

      #. Can we have NX_BOOLEAN ?
      #. Do we have to use microamp units for current ?
      #. Why is NXmonitor not NXdata ?

      .. rubric:: IDEAS
         :name: ideas

      NXbeam_position_monitor could be a separate class (subclass of
      NXlog) ?
