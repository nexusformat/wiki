---
title: Instruments
permalink: Instruments.html
layout: wiki
---
Instruments
===========

The NeXus Design page lists the group classes from which a NeXus file is
constructed. They provide the glossary of items that could, in
principle, be stored in a standard-conforming NeXus file (other items
may be inserted into the file if the author wishes, but they won't be
part of the standard). If you are going to include a particular piece of
metadata, consult the [class definitions] (Design.html "wikilink") to find out
what to call it. However, to assist those writing data analysis
software, it is useful to provide more than a glossary; it is important
to define the required contents of NeXus files that contain data from
particular classes of neutron, x-ray, or muon instrument.

As part of the NeXus standard, we have identified a number of generic
instruments that describe an appreciable number of existing instruments
around the world. Although not identical in every detail, they share
enough common characteristics, and more importantly, they require
sufficiently similar modes of data analysis, to make a standard
description useful. They are in the process of being defined for the
NeXus standard. The definitions will be in XML using the NXDL (NeXus
Definition Language) format.

Instrument Definitions List
---------------------------

### TRAC

[Pete] (Pete_Jemian.html "wikilink") 15:49, 14 December 2009 (UTC):
[NeXus definitions TRAC ticket
\#3](http://trac.nexusformat.org/definitions/ticket/3) was created to
describe the items on this page. Classes that were not already described
in NXDL have TRAC tickets created. The status of each of these classes
is described in the comments on that page. All new propositions for
classes should be described with a [new TRAC
ticket](http://trac.nexusformat.org/definitions/newticket).

### Ratified

These have been voted on by the [NIAC](NIAC.html "wikilink") and so are
official NeXus definitions

-   [NXTOFRaw: Time-of-Flight Raw Data](TOFRaw.html "wikilink") Editors:
    [Freddie Akeroyd] (Freddie_Akeroyd.html "wikilink"), [Peter
    Peterson] (Peter_Peterson.html "wikilink")
-   [Monochromatic Neutron and X-ray Powder
    Diffraction](Monochromatic_Neutron_and_X-ray_Powder_Diffraction.html "wikilink")
    Editor: [Mark Könnecke] (Mark_Koennecke.html "wikilink"), PSI
-   [Generic Scanning Instrument](GenericScan.html "wikilink") Editor: [Mark
    Könnecke] (Mark_Koennecke.html "wikilink"), PSI
-   [Monochromatic Neutron and X-ray Triple-Axis
    Spectrometer] (Monochromatic_Neutron_and_X-ray_Triple-Axis_Spectrometer.html "wikilink")
    Editor: [Nicholas Maliszewskyj] (Nickm.html "wikilink") (NIST
    Center for Neutron Research, USA).

### Proposed

In this case the need for a particular definition has been identified,
an editor has been assigned and some detailed discussions have taken
place; however the definition has not yet been voted on by the
[NIAC](NIAC.html "wikilink") and so could still undergo modification.

-   [Monochromatic Neutron and X-ray Single Crystal
    Diffractometer](Monochromatic_Neutron_and_X-ray_Single_Crystal_Diffractometer.html "wikilink")
    Editor: [Mark Könnecke] (Mark_Koennecke.html "wikilink"), PSI
-   [Archive Definition](Archive_Definition.html "wikilink") Editor: [Laurent
    Lerusse] (L.lerusse.html "wikilink") (CCLRC - Rutherford Appleton
    Laboratory, e-Science, UK)
-   [Monochromatic Neutron and X-ray Small Angle
    Scattering](SAS.html "wikilink") Editor: Ron Ghosh (Institut Laue
    Langevin, France).
-   [Processed Data] (Processed_Data.html "wikilink") Editor: [Ray
    Osborn] (Ray_Osborn.html "wikilink") (Argonne National Laboratory,
    USA)
-   [X-Ray Synchrotron Raw](XESraw.html "wikilink") Editor: [Stuart
    Campbell] (Stuart_Campbell.html "wikilink") (Diamond Light Source,
    UK)
-   [Muon Time Differential](Muon_Time_Differential.html "wikilink") Editor:
    [Steve Cottrell] (Steve_Cottrell.html "wikilink") (ISIS, UK)

### Planned

These definitions are currently being worked on and so could still
undergo major revisions. When they near completion they will be moved
into the *Proposed* category above.

-   Diffraction
    -   Protein Crystallography
    -   [Time-of-Flight Neutron Powder
        Diffraction](Time-of-Flight_Neutron_Powder_Diffraction.html "wikilink"),
        Editor: [Peter Peterson] (Pfpeterson.html "wikilink")
        (Spallation Neutron Source, USA).
    -   [Time-of-Flight Neutron Single Crystal
        Diffractometer] (Time-of-Flight_Neutron_Single_Crystal_Diffractometer.html "wikilink"),
        Editor: TBA
-   Reflectometry
    -   [Time-of-Flight Neutron
        Reflectometry] (Time-of-Flight_Neutron_Reflectometry.html "wikilink"),
        Editor: Robert Dalgliesh (ISIS Pulsed Neutron and Muon Source,
        UK)
    -   [Monochromatic Neutron and X-ray
        Reflectometry](Monochromatic_Neutron_and_X-ray_Reflectometry.html "wikilink"),
        Editor: Paul Kienzle (NIST Center for Neutron Research, USA)
-   Imaging
    -   X-ray Tomography
-   Small-Angle Scattering
    -   Grazing Incidence Small-Angle X-ray Scattering, Editor: TBA
    -   [Time-of-Flight Small Angle
        Scattering] (Time-of-Flight_Small_Angle_Scattering.html "wikilink"),
        Editor: Stephen King (ISIS Pulsed Neutron and Muon Source, UK)
    -   Ultra-Small-Angle Neutron Scattering, Editor: TBA
    -   Ultra-Small-Angle X-ray Scattering, Editor: [User%3APete
        Jemian] (Pete_Jemian.html "wikilink") (Advanced Photon Source,
        USA)
-   Spectrometers
    -   [Time-of-Flight Neutron Direct Geometry
        Spectrometer] (Time-of-Flight_Neutron_Direct_Geometry_Spectrometer.html "wikilink"),
        Editor: Toby Perring (ISIS Pulsed Neutron and Muon Source, UK)
    -   [Time-of-Flight Neutron Indirect Geometry
        Spectrometer] (Time-of-Flight_Neutron_Indirect_Geometry_Spectrometer.html "wikilink"),
        Editor: Martyn Bull (ISIS Pulsed Neutron and Muon Source, UK)
    -   XAS: X-ray Absorption Spectroscopy
    -   XPCS: X-ray Photon Correlation Spectroscopy
-   Spin-Echo
    -   [Neutron Spin Echo] (Neutron_Spin_Echo.html "wikilink"), Editor:
        Robert Georgii (FRM-II, Germany)
    -   [Time-of-Flight Neutron Spin
        Echo] (Time-of-Flight_Neutron_Spin_Echo.html "wikilink"), Editor: TBA

