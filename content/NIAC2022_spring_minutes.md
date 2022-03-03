---
title: Minutes of the NIAC2022 Spring Meeting
permalink: NIAC2022_spring_minutes.html
layout: wiki
---


Session A: March 3rd 14:00 UTC
------------------------------

NIAC members Present: Sandor Brockhaus (SB), Mark Koennecke (MK), Russ Berg (RB), Ben Watts (BW), Chen Zhang (CZ), Herbert Bernstein (HB), Pete Jemian (PJ), Freddie Akeroyd (FA), Peter Chang (PC), Aaron Brewster (AB), Stephen Cottrell (SC), Heike Gorzig (HG)

non-NIAC Present: Carola Emminger (CE), Markus Kunbach (Markus), Tamas Haraszti (TH), Tommaso Pincelli (TP)

There were several new people present, including people from the FAIRmat, so a round of introductions was done. BW mentioend that his term as chair was endiong at teh september meeting, and also FA was standing down as secretary, no ominations would be sourght. Contact BW if interested.

BW introduced the meeting format and that they should be placed on https://github.com/nexusformat/NIAC/projects/4


SB open discussion on https://github.com/nexusformat/NIAC/issues/107:
NX_COMPLEX PC mentioned be used two items with "re" and "im" prefix to store bits. HDF5 can handle a compound type, also h5py has some documention on this. Action to look at how h5py handles this.
BW: At a previous telco Quaternions were mentioend, can they be stored in a similar scheme? HB said he can help with this

How to use Symbols, defined at multiple levels. PJ explained how they coordinate array dimensions across items. Symbols should be listed in NXDL schema, near the top.
Markus: what is best practice, can you have multiple symbol tables e.g. makes it clearer when things are nested? PJ posted link to https://github.com/nexusformat/definitions/blob/61c2b2a6e9666a48c0ea3afc391b0d01d6bbd404/nxdl.xsd#L201-L209 as an example, symbol table needs to be early on and positioning enforced by schema. There is also one table at top to try and avoid name collisions. RB mentioned that his converter of definition to HDF file will also check the symbol table.

linking - can we refer to a link using a PID (Persistent identifier)? BW: how does this differ from a path in file? PID can connect to items outside of file - an external reference. BW - can already have links to external files, is this to give a url/doi to refer to things instead? MK - original nexus to have all items for data reduction in one file, links were for performance reasons with large datasets. How would PID be resolved to real items? BW: DOI and PURL so some of thsi management, but maybe not at the scale needed?  SB how do we do an external reference to e.g. an item in a database item rather than have to convert it to hdf5 and have a path? FA - you could store metadata about teh link in an NXnote, but e.g. an NXexternal_reference could store domain/facility specific items for linking?  
