---
title: Minutes of the NIAC2022 Spring Meeting
permalink: NIAC2022_spring_minutes.html
layout: wiki
---
Minutes of the NIAC2022 Spring Meeting
======================================


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
NIAC members Present: Ben Watts, Freddie Akeroyd, Sandor Brockhauser, Pete Jemian, Mark Koennecke, Aaron Brewster, Herbert Bernstein, Russ Berg, Matsumoto Takahiro

non-NIAC Present: Carola, Tommaso, Markus Kunbach

Not enough NIAC members present for official votes

PJ introduced NXxpcs draft https://www.jemian.org/BES-XPCS-pilot/NeXus/classes/contributed_definitions/NXxpcs.html#nxxpcs
for results of xpcs experiments. BW noticed scan_number in the definition, queried if it was a general feature? Also are both entry_identifier and scan_number needed?
PJ asked for confirmation of teh process for new definitions, do we need a NIAC vote to add a contributed definition? Answer was no, only a NIAC vote to move to full definition.
AB mentioned there are 4 new definitions, so not able to go line by line. Suggested sub committees in breakouts maybe? BW suggested telcos might also be able to do this. 
PJ was asked to summarise any discussion points. He drew attention to     `g2` which is proposing a new unit type of `NX_ARBITRARY_UNITS`. However as it happens to be dimensionless it was suggested to use `NX_DIMENSIONLESS`. PJ also mentioned `storage_mode` as something that may need more discussion. SB asked if they could use HDF virtual data sets for this? BW  wondered if not using a 3D array was due to possible missing elements and a linked dataset routes was to avoid this. PJ suggested we had a telco with xpcs people to have a good discussion over these points. MK: sa this is processed data, we should add an NXprocess .
SB: how is the raw data stored? PJ: this is very detector dependent, collected by BlueSky, but not usually stored in HDF5 format. This data then goes to have g2 calcualated and the idea is to use nexus for sharing the processed data. So plan is to discuss at a telco.

BW introduced #98 NXdetector_channel requested by Dectris for storing different per channel valuies e.g. gain settings See https://github.com/nexusformat/definitions/issues/940#issuecomment-972672865 The detector channels are different versions of the data. Could this be doen as separate NXdetector_groups ? Decris though a single NXdetector was better as there is only one physical detector.  Tomaso: could you have nxprocess inside nxdetector to describe some of this processing? BW described this is done by chip in detector, so processing is "black box". MK: though you could use an extra array dimension to store this data, using proposed NXdetector_channel does look clearer. AB described https://github.com/nexusformat/definitions/issues/711 and that detector channel woiuld be helpful here.      

AB presents discussion of [fixing symbols of NXbeam](https://github.com/nexusformat/definitions/pull/858) (this is the version of NXbeam in NXmx). Here it is using the symbol nP for the number of scan points, while the base class doesn't use any symbols and doesn't really consider multiple scan points.
Divergence has 3 components, X, Y, and XY. This is documented in CIFS and is also called "crossfire" and we should copy from their definitions.
AB will change the size of the array corresponding to the divergence components to "c" and explain the concept of "crossfire" where there can be many moments of divergence. 
Questions of whether nP symbols is normally used in the first dimension? MK says nP would be the "scan dimension" that is usually first. This is not what NXbeam currently states (we messed up) and we should change it to match the standard order of nP first. BW suggests that we shouldn't specify the size of the second dimension (components of the divergence) since we don't want to enforce it. 

Tommaso says we should state that the "extent" is measured according to the FWHM. There should be a shape description (string). SB says that at ESRF they gave the choice of a few basic shapes, together with the option of a profile. HB suggests a working group.

The meaning of some symbols (in the old version) is not clear. We can port most of the NXmx version of NXbeam back to the base class.
"fixing" the spelling of "polarization" should involve deprecating "polarisation".

Tobias has gone through the base classes and deprecated NXgeometry and added in NXtransformations and depends_on. It looks fairly safe and repetitive with the exception of the images that have been added. We can mark it as ready to vote on with a note to discuss the images.

SB has [written down some details regarding inheritance](https://github.com/nexusformat/NIAC/issues/119#issuecomment-1058508119) in order to explain the way NeXus currently operates with formal language. Feedback and comments are welcome (please post to the issue).

SB presents the [documentation for the FAIRMAT proposed application definitions](https://fairmat-experimental.github.io/nexus-fairmat-proposal/d122a69ce0c953805e60a662e9580ee2c4a6fae7/index.html) that includes the feature allowing the community to annotate the docs to make comments and suggest improvements. Carola walks us through the proposed ellipsometry application definition. PJ points out that the new files should go to the `contributed_definitions` folder, which SB has already implemented in the pull request.

Close session.

Session C: March 4th 14:00 UTC
------------------------------
NIAC members Present: Ben Watts, Sandor Brockhauser, Pete Jemian, Aaron Brewster, Chen Zhang, Heike Goerzig, Herbert Bernstein, Ray Osborn, Stephen Cottrell, Wout de Nolf, Peter Chang, Mark Koennecke, Russ Berg, Takahiro Matsumoto

non-NIAC Present: Markus Kuehbach, Tommaso Pincelli

With 14 NIAC members attending we have a quorum to make decisions by a small margin.

Votes are on github. Links are provided. The voting period is one week. 

Publishing the NeXus ontology on PURL. Automatically generated from NXDL. PURL provides persistent identifiers for NeXus and persists it. Quality checking the NeXus ontology is on us.  Motion to publish the NeXus ontology on PURL: Voting at https://github.com/nexusformat/NIAC/issues/95#issuecomment-1059210877. 12 agreed 
Thus the motion is approved.

Changing gain_setting in NXdetector to be free form and not an enum. Votes at https://github.com/nexusformat/NIAC/issues/100, 9 agreed so far. Consensus was this should be revised with a suggestion for a controlled vocabulary for the gain settings. And the addition of numeric gain setting and offset fields. 

Reserve the private prefix DECTRIS for the company DECTRIS. Issue: https://github.com/nexusformat/NIAC/issues/110. This raised the suggestion that prefix owners store the documentation for their private fields with NeXus in NXDL. This will be a new issue. Voted for the DECTRIS prefix: 11 during the session. This is approved. 

Next issue: allowing arrays of strings as axis dimensions, https://github.com/nexusformat/NIAC/issues/97, This drifted off into a discussion if we allow date time strings here. This was deferred to another proposal. We vote on allowing NX_CHAR or NX_NUMBER arrays as axis in NXdata. 11 votes in agreement so far.

Allow NXdetector_channel for storing detector channel specific parameters. https://github.com/nexusformat/definitions/issues/940#issuecomment-972672865. The consensus is that we encourage further development of this until we have a pull request for a NXdetector_channel base class. This is not ready for a NIAC vote yet. 
This also raised questions about how to link data together in NXdata. 

Next topic is the virtual_pixel_correction_applied field, https://github.com/nexusformat/NIAC/issues/94, The vote is for accepting it. 12 votes in favour, accepted. 

The NIAC decided in 2012 to deprecate NXgeometry and introduce NXtransformations and depends_on fields in any positionable NeXus base classes. The issues is https://github.com/nexusformat/NIAC/issues/109, This vote is to confirm that the changes sugegsted reflect the NIAC vote of 2012. Approved with 12 votes. 

The next issue is to protect the main branch of the github repository in order to prevent abuse. The github link is: https://github.com/nexusformat/NIAC/issues/113#issuecomment-1059291945 Accepted with 12 votes.

Next issue is to add image_key to NXdetector. It is already used in NXtomo. The issue is https://github.com/nexusformat/NIAC/issues/111. Approved with 11 votes. 

With the votes out of the way we started discussing NXmpes. Which improves NXmpes.  This is a processed data application definition. The approach is to agree on  a processed data standard and when people got used to the standard push for a raw data format. The field is dominated by vendors. In some cases, data files provided by commercial instruments can be encrypted. In many other cases, the data is obfuscated with undocumented calibrations and processing. FAIRMAT aims to provide the community with exchange formats (processed data) with the hope of increasing demand for more open formats for raw data files.

Discuss application definitions for electron microscopy. Lenses are an integral part of microscopes and we can build a detailed model of the instrument via description of a set of lenses. Can see value in having base classes for all types of lenses - still want to find good names for the classes. BW encourages FAIRMAT to develop a very general lens base class that covers all cases - NXxraylens could be deprecated if a suitable replacement is available.
Current situation for atom probe microscopy of scraping data out of commercial file formats with limited knowledge. Atom probe data needs high precision that is difficult to get from commercial data files. Published methods tend to be incomplete and the community is wanting to not accept this in future. They are trying to include as many details as possible.
Current situation in electron microscopy is also heavily reliant on commercial suppliers, so incentive for open protocols is very low. Vendors provide all-in-one gui-based software to make customers happy, but results in lack of openness in the data and lots of undefined processing. The sample stage can be very complex with lots of versatile capabilities. This lead to NXstage_lab therefore contains some fields, but more importantly can act as a container for including lots of further base classes describing further capabilities.

Discussion of tracking the history of a sample or session. lab books versus large files or a master-file or a database. Sample synthesis is an example where collecting an entire history together is valuable. Connecting the data and actions together with ontologies is something that FAIRMAT would like to ework towards.

BW suggests bringing up these application definitions in future telcos. Announcing the intention beforehand can give people time to do some homework reading and we can focus on each part in detail over many meetings.


Close session.

Session D: March 4th 22:00 UTC
------------------------------
NIAC members Present: Russ Berg, Peter Jemian, Freddie Akeroyd, Mark Koennecke, Sandor Brockhauser, Ben Watts, Wout de Nolf, Aaron Brewster (AB), Takahiro Matsumoto, Ray Osborn 

non-NIAC Present: 

* Leave "Fix up NXBeam symbols and polarization" https://github.com/nexusformat/NIAC/issues/101 as need Aaron
* NXmx total_flux https://github.com/nexusformat/NIAC/issues/96 need way to specify one of a set of fields is present in NXDL. There is "flux" and "total_flux" currently, discussion was around whether NXmonitor could be used for this and also whether flux and total_flux could be merged into a single flux field. NXstxm has a NXmonitor called control. AB will consult MX community and discuss if NXmonitor would work here. There was a discussion about units for NX_FLUX and whether it was possible to have unit options that were dimensionly different e.g. per area or not per area. No other NX units currently do this. There is also an integral log in NXmonitor that may be useful for total flux.

Deprecate incr attribute in dimensionsType https://github.com/nexusformat/NIAC/issues/112 a field was accidentally left in. ref and refindex were deprecated but https://manual.nexusformat.org/nxdl_desc.html#incr depends on them. These were deprecated in a telco, they have not been removed that needs a niac, so it was agreed they can be deprecated here. VOTE: unanimous

NXregion https://github.com/nexusformat/NIAC/issues/118.   MK: what does imgCIF do for region of interest?   AB: it doesn't seem to describe it exactly, but could create a detector object that describes it. Whhat does EPICS Area Detector do? https://areadetector.github.io/master/ADCore/NDPluginROI.html Also ESRF https://bliss.gitlab-pages.esrf.fr/bliss/master/flint/flint_roi_counters.html There seems to be a branch https://github.com/nexusformat/definitions/compare/944-add-NXregion but not a PR at the moment. RO: this seems to define the data but not how to use it? Would it be clearer as a child of NXdata rather than NXdetector? Could we see an example file of usage? SB mentioened that the category element of contributed definitions wasn't always clear whether it was a base or application definition, this needs to be tidied up.  

AB presented updates to https://github.com/nexusformat/definitions/pull/858 There was discussion around "energy_transfer" field as to whether it made sense in NXbeam. Was it there for MCstas simulations? There was also discussion about the dimensionality of the variuous quantities, it looked better to not specify this directly but to add the various options in a description at the top. Various suggestions were added as review comments to the PR. 

Add geometry information to NXbeam https://github.com/nexusformat/NIAC/issues/115 and https://github.com/nexusformat/definitions/compare/925-nxbeam-geometry After discussion, looks good and would like to see PR from PC

https://github.com/nexusformat/NIAC/issues/99 , https://github.com/nexusformat/definitions/pull/913 - this looks like a bugfix so OK to merge.

Question about choice of fields - seems there is a choice of groups in https://github.com/nexusformat/definitions/blob/1af5f99cbfe0741c50cba3936bc793127390c410/base_classes/NXdetector.nxdl.xml#L779-L792 and this could potentially be extended to fields?

BW will create page of votes and send out doodle for choice of final meeting date


Session E: March, 15, 14:00 UTC
-------------------------------

Pete Jemian brought up the topic of holding a code camp for implementing the decisions from NIAC. After some discussions we 
agreed to hold this in may. A doodle poll will be held in order to find a suitable date. BW clarified that we do not vote on code camps.

A discussion about the default attribute. There is some confusuion about if the default attribute is a path to the default plot item or 
a chain. The consensus was that it is a chain and the documentation ought to be clarified. 

Then there is the problem that now many base classes like NXcapillary have the default group attribute without there being a NXdata 
group foreseen in the group. BW linked this issue to the problem about the inheritance model of NeXus. This is to be discussed at 
the next code camp. MK reminded the group that the Interfaces proposal which suggested some inheritance in base classes was shot
down at NIAC 2018.

We agreed that there are no further discussions required on the voting items from session C. 

AB brought up #896, clarifying the NXdetector gain_setting for discussion. The list of known gain settings was amended. The group made 
suggestions how to improve the text even more. AB suggested to vote on the proposed and amended changes in #896. The vote is at https://github.com/nexusformat/NIAC/issues/100#issuecomment-1068071881

AB brought up NXmx_total_flux, #986. There is some discussion about using NXmonitor instead of the flux fields. The MX community uses flux for 
a use case for which NeXus has invented NXmonitor. There is also discussion about the dimensionality of flux. Apparently, some beam lines 
give a single number here as the beam line is very stable or the normalisation is done before writing the file. Others store a value per image in 
order to allow for later normalisation. HB points out that for crystallography you have to be descriptive. If you are prescriptive as NeXus tries 
to be, wou will be ignored. Various suggestions to improve the wording of AB's proposal were made and applied.  It was felt that this needs further 
discussion and the discussion was adjourned. 

The next issue is the clarification of NXbeam espcially the polarisation parameters. THis is issue #858. The proposal was reviewed. There is some discussion 
about the meaning of the stokes parameters. Peter Chang agreed to clarify this. RO brought up that this has to be discussed with neutron and light scattering people. A solution is not to deprecate the old fields but rather add the new proposed new fields. With neutrons many bespoke devices are used for polarisation analysis. Thus no standard can be proposed.

Meeting closed with one open vote. Next steps will be Doodles for the code camp and a NeXus telco.

