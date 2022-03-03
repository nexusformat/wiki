---
title: Minutes of the NIAC2022 Spring Meeting
permalink: NIAC2022_spring_minutes.html
layout: wiki
---


Session A: March 3rd 14:00 UTC
------------------------------

NIAC members Present: Sandor Brockhaus (SB), Mark Koennecke (MK), Russ Berg (RB), Ben Watts (BW), Chen Zhang (CZ), Herbert Bernstein (HB), Pete Jemian (PJ), Freddie Akeroyd (FA), Peter Chang (PC), Aaron Brewster (AB), Stephen Cottrell (SC), Heike Gorzig (HG), Ray Osborn (RO)

non-NIAC Present: Carola Emminger (CE), Markus Kunbach (Markus), Tamas Haraszti (TH), Tommaso Pincelli (TP)

There were several new people present, including people from the FAIRmat, so a round of introductions was done. BW mentioend that his term as chair was ending at the september meeting, and also FA was standing down as secretary, so nominations would be sought. Contact BW if interested.

BW introduced the meeting format and that issues to be discussed should be placed into the corresponding column on https://github.com/nexusformat/NIAC/projects/4


SB open discussion on https://github.com/nexusformat/NIAC/issues/107:
NX_COMPLEX PC mentioned be used two items with "re" and "im" prefix to store bits. HDF5 can handle a compound type, also h5py has some documention on this. Action to look at how h5py handles this.
BW: At a previous telco Quaternions were mentioend, can they be stored in a similar scheme? HB said he can help with this

How to use Symbols, defined at multiple levels. PJ explained how they coordinate array dimensions across items. Symbols should be listed in NXDL schema, near the top.
Markus: what is best practice, can you have multiple symbol tables e.g. makes it clearer when things are nested? PJ posted link to https://github.com/nexusformat/definitions/blob/61c2b2a6e9666a48c0ea3afc391b0d01d6bbd404/nxdl.xsd#L201-L209 as an example, symbol table needs to be early on and positioning enforced by schema. There is also one table at top to try and avoid name collisions. RB mentioned that his converter of definition to HDF file will also check the symbol table.

linking - can we refer to a link using a PID (Persistent identifier)? BW: how does this differ from a path in file? PID can connect to items outside of file - an external reference. BW - can already have links to external files, is this to give a url/doi to refer to things instead? MK - original nexus to have all items for data reduction in one file, links were for performance reasons with large datasets. How would PID be resolved to real items? BW: DOI and PURL so some of thsi management, but maybe not at the scale needed?  SB how do we do an external reference to e.g. an item in a database item rather than have to convert it to hdf5 and have a path? FA - you could store metadata about teh link in an NXnote, but e.g. an NXexternal_reference could store domain/facility specific items for linking? Agreed to discuss further and SB will create an issue

html documenmtation: SB showed slides
inheritance and documentatiion strings, required and not required attribute. also enum. MK: base class is all optional, dictionary of terms. application definition says what is required.  PJ posted link refereing to documentation https://github.com/nexusformat/NIAC/issues/119#issuecomment-1058138059 inheritance 
SB volunteers to write a proposal that the NIAC can vote on to cement single inheritance for NeXus
MK makes the point that our "base classes" are not really classes and they are not supposed to inherit from each other. We only have (single) inheritance in the application definitions.
Markus asks if he needs to state everything in the application definition because he can't rely on things being inherited from the base classes.
MK says that an object in an application definition does inherit everything in the base class.

SB proposes NX_COMPOSITE to allow composite units (e.g. meters per second) by utilising unidata.
BW wants a more detailed proposal because the minimal text presented here is not expressing the same as what you are saying.

SB wants a way to require one of a set of fields.
PJ says that NXcansas has something similar with @resolutions. This is handled by a person following the rules stated in the docstring, but a validator cannot understand this. What we need is a way to express this properly in NXDL.
BW points out that @axes in NXdata is another example of the same mechanism that isn't formally expressed in NXDL.
Discussion of [cnxvalidate](https://github.com/nexusformat/cnxvalidate) and how it could be extended.
MK mentions [features](https://github.com/nexusformat/features) that could provide a lot more freedom if we put in the work to implement it on a wider scale.

SB asks about how to link things together. PJ points out the target attribute can a class path, rather than a name path, since the application definitions tend to leave the group names unspecified. The NXDL is guidance for writing the file.
The manual states that links are given with absolute paths. The manual also uses the convention that unspecified names are written in all caps.

SB asks about @default. PJ explains that there must be a chain of @default attributes where the value of one must point to the group that has the next @default attribute in the chain. SB found a file that has absolute paths in the @default attribute, but there is consensus that the file is violating the standard. attributes generally only refer to the memebrs of the local group (the @target attribute being an exception).

SB asks if we want to always base the base classes on NXobject? Do we want to have more inheritance? NXdetector is an example where having a few specialised types of NXdetector that inherit from a basic version could make it easier to work with. PJ says that this would involve a large refactoring of NeXus rules that would affect lots of things. [NXxkappa](https://manual.nexusformat.org/classes/applications/NXxkappa.html) is already extending [NXxbase](https://manual.nexusformat.org/classes/applications/NXxbase.html), inheritance of application definitions is already demonstrated.

SB asks if an application definition can define multiple entries. BW says that this is done in NXstxm, but it can't be done formally in NXDL. The manual describes some reasonable approaches, but doesn't say anything specific. Markus says that it is influenced by how much metadata you want to be repeating. We don't want to advocate putting "too many" measurements into a single file.
RO always has multiple entries (for different rotations) in a file and then combines the data together afterwards. He always uses external links to files containing calibrations. It is a question of bookkeeping to store the data and their relationships to each other.



Session B: March 3rd 22:00 UTC
------------------------------
NIAC members Present: Ben Watts, Freddie Akeroyd, Sandor Brockhauser
Pete Jemian
Mark Koennecke
Aaron Brewster
Herbert Bernstein
Russ Berg

non-NIAC Present: Carola, Tommaso, Markus Kunbach

Not enough NIAC members present for official votes

PJ introduced NXxpcs draft https://www.jemian.org/BES-XPCS-pilot/NeXus/classes/contributed_definitions/NXxpcs.html#nxxpcs
for results of xpcs experiments. BW noticed scan_number in the definition, queried if it was a general feature? Also are both entry_identifier and scan_number needed?
PJ asked for confirmation of teh process for new definitions, do we need a NIAC vote to add a contributed definition? Answer was no, only a NIAC vote to move to full definition.
AB mentioned there are 4 new definitions, so not able to go line by line. Suggested sub committees in breakouts maybe? BW suggested telcos might also be able to do this. 
PJ was asked to summarise any discussion points. He drew attention to     `g2` which is proposing a new unit type of `NX_ARBITRARY_UNITS`

BW introdiuced #98 NXdetector_channel requested by Dectris for storing different per channel valuies e.g. gain settings
