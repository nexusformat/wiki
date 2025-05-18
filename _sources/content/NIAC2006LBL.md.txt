---
title: NIAC2006LBL
permalink: NIAC2006LBL.html
layout: wiki
---

NIAC Meeting - October 2006
===========================

The next meeting of the [ NeXus International Advisory
Committee](NIAC.html "wikilink") will be held at the [Lawrence Berkeley
National Laboratory](http://www.lbl.gov) near San Francisco, California,
USA. The meeting will be held from October 5 to 6, 2006, immediately
following [NOBUGS 2006](http://nobugs2006.lbl.gov/).

### List of Attendees

If you are interested in attending (and are not already on the [list of
attendees](NIAC2006LBL_attendees.html "wikilink")), contact [Andrew
Götz] (Andy_Gotz.html "wikilink").

### Start of the Meeting

-   You are responsible for your own breakfast and travel to the lab. In
    theory there are many people staying at the DoubleTree and the
    Durant so carpooling is encouraged.
-   Arrive at the badging office and they will give you a visitor badge
    and a “blue triangle” parking pass. For those of you without a car
    there is a lab shuttle bus that will take you from there to building
    two (2).
-   We will be starting at 8:30 am (pacific time) in building two (2)
    room 100B. This is the biggest room and will be where refreshments
    are served.

### Agenda

#### Proposed Agenda Items

-   Discuss NeXus collaborating with imgCIF. see [MEDSBIO
    proposal](http://www.medsbio.org/)
-   Request institutes from the NeXus community sponsor a full-time
    technical secretary for next 12-24 months.
-   Institutes that write NeXus files are **data providers.**. NeXus
    provides an interface between **data providers** and **data
    requirers**. Discuss if the NIAC constitution should be change to
    allow data requirers e.g. DANSE to have representation on the NIAC
    as a stakeholder that requires NeXus.
-   SCAN definition similar to TOFRAW definition
-   NXcharacterization needs to be formalized
-   Finalize [archive definition](Archive_Definition.html "wikilink")

#### Tabled Until Next Time

-   Moving from [Meta-DTDs](Metaformat.html "wikilink") to XML Schema. see
    [NeXML proposal](http://www.webel.com.au/nexml)

#### October 5

-   08:30 Welcome and Introduction
-   First buisiness
    -   Review of NIAC'2006ILL minutes
    -   [Renew members](Membership_Dates.html "wikilink")
    -   Add new members
        -   Jens-Uwe Hoffmann - Hahn-Meitner-Institut Berlin
        -   Paul Kienzle - DANSE
-   Triage
    -   Define missing agenda items
    -   Vote on things already ready for voting
    -   Define working groups and divide items
-   09:30 break
-   09:45 Ratify instrument definitions
-   12:00 break for lunch
-   13:00 Ratify instrument definitions
-   15:00 break
-   15:30 split into groups

#### October 6

-   08:30 Small items (see [Roadmap](NIAC2006LBL_RoadMap.html "wikilink"))
    -   Examine classes for ratification
        -   [ X-ray Experimental (Synchrotron) raw NeXus
            data](XESraw.html "wikilink")
        -   [Archive\_Definition](Archive_Definition.html "wikilink")

<!-- -->

-   -   Examine instruments for ratification
        -   [ Monochromatic Neutron and X-ray Small-Angle
            Scattering](SAS.html "wikilink")
        -   Reflectometry
        -   [Time-of-Flight\_Neutron\_Indirect\_Geometry\_Spectrometer] (Time-of-Flight_Neutron_Indirect_Geometry_Spectrometer.html "wikilink")
        -   [Monochromatic\_Neutron\_and\_X-ray\_Triple-Axis\_Spectrometer] (Monochromatic_Neutron_and_X-ray_Triple-Axis_Spectrometer.html "wikilink")
        -   [Time-of-Flight\_Neutron\_Powder\_Diffraction](Time-of-Flight_Neutron_Powder_Diffraction.html "wikilink")
        -   [Muon\_Time\_Differential](Muon_Time_Differential.html "wikilink")
        -   [MonoXPSD](MonoXPSD.html "wikilink") Monochromatic Single Crystal
            Diffractometer with Position Sensitive Detector
        -   [MonoXSingle](MonoXSingle.html "wikilink") Monochromatic Single
            Crystal Diffractometer with Single Detector

<!-- -->

-   ??:?? Triage

### General Information

**Accomodations**

LBL has a list of housing in the area:
[<http://www.lbl.gov/Workplace/near-our-shuttle.html>](http://www.lbl.gov/Workplace/near-our-shuttle.html)

The NOBUGS 2006 conference suggests two hotels:
[<http://nobugs2006.lbl.gov/index.php?content=Lodging>](http://nobugs2006.lbl.gov/index.php?content=Lodging)

#### Room Reservations

For help in locating the buildings with the meeting rooms, please refer
to the [http://www.lbl.gov/Workplace/lab-site-map.html LBL campus
map](http://www.lbl.gov/Workplace/lab-site-map.html_LBL_campus_map.html "wikilink").

| Room        | Session   | Network   | Projector? | 10/5               | 10/6               |
|-------------|-----------|-----------|------------|--------------------|--------------------|
| Bldg. 2-100B| Plenary   | wireless  | no         | 7:00 AM to 6:30 PM | 7:00 AM to 6:30 PM |
| Bldg. 6-2202| Breakout  | wired     | yes        | 12:00 - 6:30 PM    | 7:00 AM - 6:30 PM  |
| Bldg. 7-211 | Breakout  | wired     | no         | 12:00 - 6:30 PM    | 7:00 AM - 6:30 PM  |

### Working Groups

#### API/Technical Issues

-   Improving NeXus internal code documention on private structures and
    functions. Only API developer needs to know about these, but at the
    moment the knowledge is restricted to a few people. The existing
    in-code documentation needs to be tidied up and it would be a good
    idea if programs such as
    [Doxygen](http://www.stack.nl/~dimitri/doxygen/index.html) could
    parse it.
-   Move from the current [CVS](http://www.nongnu.org/cvs/) (for version
    control) / [Bugzilla](http://www.bugzilla.org/) (for bugs/issues)
    system to using [Subversion](http://subversion.tigris.org/) /
    [TRAC](http://trac.edgewall.org/). Freddie has set up two sites at
    [<http://svn.nexusformat.org/code>](http://svn.nexusformat.org/code)
    and [<http://trac.nexusformat.org>](http://trac.nexusformat.org) for
    testing
-   Move mailing list to nexusformat.org
-   Determine location to store definitions
-   Design and implement a way to deal with having approved definitions
    and a way to modify a working copy on the website
-   It would be useful if NeXus could support arrays of strings
-   Source and target of a link must have same name
-   Java package name should be org.nexusformat

Minutes
-------

Here are the minutes in [pdf
format](../pdfs/NIAC2006LBL_minutes.pdf "wikilink") or [MS-Word
format](../pdfs/NIAC2006LBL_minutes.doc "wikilink").

Photos
------

-   [ Group photos](NIAC2006LBL_photos.html "wikilink")
-   [ other photos] (NIAC2006LBL_photos_other.html "wikilink")

