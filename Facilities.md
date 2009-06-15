---
title: Facilities
permalink: Facilities/
layout: wiki
---

Facilities currently using the NeXus data format
------------------------------------------------

### Neutron Scattering Facilities

ISIS Neutron Facility, STFC Rutherford Appleton Laboratory, UK: Instruments on the [ISIS second target station](http://ts-2.isis.rl.ac.uk/) are now generating NeXus files as per the [TOFRaw](TOFRaw "wikilink") definition in parallel with old ISIS RAW format files. Currently most data analysis is carried out using the ISIS RAW files, but the new [Mantid data analysis framework](http://www.mantidproject.org/) supports [TOFRaw](TOFRaw "wikilink") NeXus files and is being increasingly used. The long term goal is to entirely replace the old ISIS RAW file format on both the first and second target stations with NeXus files; the rate determining step for this is the updating of data analysis code to read NeXus files.  

<!-- -->

Lujan Neutron Scattering Center, [Los Alamos National Laboratory](http://lansce.lanl.gov/lujan), USA: The Lujan Center is generating NeXus files on all instruments. We are in the process of making the files consistent with the emerging standards, especially [TOFRaw](TOFRaw "wikilink"). The facility hosts about 65,000 NeXus files and the number is growing.  

<!-- -->

Materials and Life Science Facility [1](http://www.j-parc.jp/index-e.html), J-PARC, Japan: In FY2008, we have successfully received first proton beam and produced pulsed neutron and muon beam at Materials and Life Science Facility (MLF) in J-PARC (http://www.j-parc.jp/index-e.html). Histogrammed data converted from event-format data and analyzed data are stored in NeXus data format with metadata, and NeXus is common and shared data format among neutron scattering instruments and scientists in MLF. NeXus C-API is utilized through Manyo-Library which is the data analysis framework for neutron scattering experiments. Data analysis softwares for each instrument have been developed with C++ and python on Manyo-Library.  

<!-- -->

Bragg Institute, [Australian Nuclear Science and Technology Organisation](http://www.ansto.gov.au/research/bragg_institute), Australia: We are currently writing NeXus files in HDF5 on 5 out of 7 instruments, including Small Angle, Reflectometer, Powder Diffaction and Residual Stress. NeXus is not being used on Triple Axis and Single Crystal Diffraction. The next wave of instruments will be predominantly NeXus.  

<!-- -->

Institut Laue Langevin [ILL](http://www.ill.eu), Grenoble France: As of 2008-2009, the ILL has 2 instruments that generate NeXus/HDF5 files as base format: the Disk chopper time-of-flight cold neutrons spectrometer IN5 [IN5](http://www.ill.fr/in5) and Time of Flight Neutron Spectrometer for Small Angle Inelastic themal neutron Scattering BRISP [BRISP](http://www.ill.fr/brisp). Volume of data (Gb's) is substantially higher than what we used to have at the ILL before - because of large PSD detectors - and NeXus was then the only sensible choice for storage. We then use [LAMP](http://www.ill.eu/instruments-support/computing-for-science/cs-software/all-software/lamp/), and Matlab tools (incl. Mslice from Oxford/ISIS) to read and convert data sets. [McStas](http://www.mcstas.org) is also used to model these instruments, and may also generate NeXus files.  

<!-- -->

Spallation Neutron Source [SNS](http://neutrons.ornl.gov/), Oak Ridge, TN, USA: SNS is using [TOFRaw](TOFRaw "wikilink") for storing histogram based data from all instruments. We are working towards storing the raw event data in NeXus instead as the data acquisition saves data in that form already.  

### Pulsed Muon Facilities

ISIS Muon Facility, STFC Rutherford Appleton Laboratory, UK: The [ISIS facility](http://www.isis.rl.ac.uk/) has been producing and using NeXus files on its [muon spectrometers](http://www.isis.rl.ac.uk/muons/) for many years now (see [Muon\_Time\_Differential](Muon_Time_Differential "wikilink") definition). The current definition is in the process of being updated to allow it to store more complex experiments and also to make it more similar to the [TOFRaw](TOFRaw "wikilink") definition used on the ISIS neutron instruments.  

### X-ray Facilities

Advanced Photon Source, Argonne National Laboratory, US: For many years now, NeXus-compliant (HDF4) are one of the file format options in the [CCD Image Server software](http://www.aps.anl.gov/bcda/dataAcq/) developed and used at the APS. The [X-ray microtomography](http://www.aps.anl.gov/Xray_Science_Division/Xray_Microscopy_and_Imaging/Science_and_Research/Techniques/Tomography) instrument is a major user of this software and records some *O*(10<sup>5</sup>) images per month of operation. Data reduction of the Tomo files proceeds from the HDF4 files. Use of the NeXus-compatible format is discretionary for other users of the `CCDImageServer` software (the alternative choice is TIFF with metadata stored external to the TIFF files). As APS replaces `CCDImageServer` with newer EPICS software (`areaDetector` and a GUI), it is expected to retain and improve the support for the NeXus format, as required by and best serves the APS user community. The microdiffraction instrument at [34ID-E](http://www.aps.anl.gov/Sectors/33_34/microdiff/) is considering HDF5 files written through the NeXus API for the storage of their experimental results including metadata. This may prove a challenge as the instrument expects to stream 5 MB images at 20 frames/second on a continuous basis; it may not be practical to store and retain all the raw data.  

Facilities planning to support the NeXus data format
----------------------------------------------------

### Neutron Scattering Facilities

### X-ray Facilities

European Synchrotron Radiation Facility, ESRF, FRANCE: The [ESRF](http://www.esrf.eu) is planning on moving to use Nexus/HDF5 for storing all raw data as part of the ambitious [ESRF upgrade program](http://www.esrf.eu/Upgrade). The adoption of Nexus/HDF5 is planned over the time period 2009 to 2012. Currently (2009) the ESRF is actively exploring Nexus and HDF5 to see what the technical implications are for data acquisition and analysis programs. The plan is to where possible adapt data analysis to directly read data generated by data acquisition programs in Nexus/HDF5 format. The current experience shows that Nexus alone is not sufficient and extensions to the standard are required. The extensions are being implemented directly in HDF5.  

<!-- -->

ALBA/CELLS Synchrotron Light Facility, Spain: [ALBA](http://www.cells.es) is currently (2009) in commissioning stage and therefore not yet producing significant amounts of data. During this stage a variety of data formats are in use, but the adoption of NeXus as the main data format for the data acquisition in beam lines and machine is being planned. The first steps are being taken in using NeXus for all the scans in the beam lines (following the GenericScan definition). Whether pure nexus is sufficient or a HDF5 extension like the one in ESRF needs to be adopted is not yet decided. Given that most of the data analysis programs do not support NeXus yet, we foresee that the use of NeXus will be mostly limited to data acquisition and pre-processing and that translators/extractors will be needed for further data analysis for the short-medium term.  
