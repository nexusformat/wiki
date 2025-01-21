===================
NIAC2006LBL RoadMap
===================

.. container:: content

   .. container:: page

      .. rubric:: NIAC2006LBL RoadMap
         :name: NIAC2006LBL_RoadMap_niac2006lbl-roadmap
         :class: page-title

      .. rubric:: **ALL** neutron definitions **done**
         :name: all-neutron-definitions-done

      -  priority 1

         -  Monochromatic Neutron and X-ray Reflectometry
         -  Time-of-Flight Neutron Reflectometery
         -  Monochromatic Neutron and X-ray Single Crystal
            Diffractometers

            -  `MonoXPSD <../content/MonoXPSD.html>`__ Monochromatic Single Crystal
               Diffractometer with Position Sensitive Detector
            -  `MonoXSingle <../content/MonoXSingle.html>`__ Monochromatic Single
               Crystal Diffractometer with Single Detector

         -  Monochromatic_Neutron_and_X-ray_Triple-Axis_Spectrometer <Monochromatic_Neutron_and_X-ray_Triple-Axis_Spectrometer.html>
         -  `Archive_Definition <../content/Archive_Definition.html>`__

      -  priority 2

         -  `Time-of-Flight_Neutron_Powder_Diffraction <../content/Time-of-Flight_Neutron_Powder_Diffraction.html>`__
         -  `Monochromatic Neutron and X-ray Small Angle Scattering <../content/SAS.html>`__
         -  Time-of-Flight Small Angle Scattering

      -  priority 3

         -  Time-of-Flight_Neutron_Indirect_Geometry_Spectrometer <Time-of-Flight_Neutron_Indirect_Geometry_Spectrometer.html>
         -  Time-of-Flight Neutron Direct Geometry Spectrometer

      -  priority 4

         -  Time-of-Flight Neutron Single-Crystal Diffractometer
         -  Time-of-Flight Neutron Spin Echo Editor

      .. rubric:: Small Items
         :name: small-items

      .. rubric:: Axis attributes on fields
         :name: axis-attributes-on-fields

      The current documentation describes that the fastest varying
      dimension is annotated with "axis=1". In practice the slowest
      varying dimension is "axis=1".

      .. rubric:: Geometry order of operations
         :name: geometry-order-of-operations

      When looking at a geometry is the orientation applied before the
      translation or the other way around.

      .. rubric:: `XESraw <../content//XESraw.html>`__

      .. rubric:: scanning environment variables
         :name: scanning-environment-variables

      -  Make sure we have an example of scanning an environment
         variable in scanraw
      -  Consider how parametric scans will be represented (within and
         between entries)

      .. rubric:: Later
         :name: later

      -  sequencing entries and measurements
      -  counting time for each data point

         -  Does this belong to some base class?
         -  Which one?

      -  implement a versioning system

         -  switch to subversion
         -  use SVN tagging system

      .. rubric:: Proposed Agenda Items
         :name: NIAC2006LBL_RoadMap_proposed-agenda-items

      -  Discuss NeXus collaborating with imgCIF. see `MEDSBIO
         proposal <http://www.medsbio.org/>`__
      -  Request institutes from the NeXus community sponsor a full-time
         technical secretary for next 12-24 months.
      -  (*completed*) Institutes that write NeXus files are **data
         providers.**. NeXus provides an interface between **data
         providers** and **data requirers**. Discuss if the NIAC
         constitution should be change to allow data requirers e.g.
         DANSE to have representation on the NIAC as a stakeholder that
         requires NeXus.
      -  (*working*) SCAN definition similar to TOFRAW definition
      -  (*working*) NXcharacterization needs to be formalized
      -  (*working*) Finalize `archive
         definition <../content/Archive_Definition.html>`__
