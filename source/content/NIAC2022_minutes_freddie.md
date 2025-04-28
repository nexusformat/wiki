---
title: NIAC2022 Minutes
permalink: NIAC2022_minutes.html
layout: wiki
---
NIAC2022 Minutes
================

## NIAC2022 Minutes

### Session A: Sept 14th 10:00-12:00 UTC

Present: BW, FA, PJ, LG, HG, SB, MK (Markus Kuhbach), RB, PC, SS (Sherjeel Shabih), AP (Allan Pinto), PM (Paolo Baraldi Mausbach)

BW began by summarising the meeting, and then there was a round of introductions as new people were present. As well as NIAC members, there were some observers from the Brazilian Synchrotron Light Laboratory (LNLS) and other facilities. AP mentioned that he had planned meeting with Diaomond and ESRF and was interested in learning more about NeXus, it was suggested that the monthly NeXus teleconferences would be good from this perspective. They are listed on the [Teleconferences]( https://www.nexusformat.org/Teleconferences.html) page and to be notified of their dates you can join the [nexus-tech](https://lists.nexusformat.org/mailman/listinfo/nexus-tech) mailing list. There is also the [nexus manual](https://manual.nexusformat.org/user_manual.html)

The list of items to discuss is kept as a [github project](https://github.com/orgs/nexusformat/projects/2) and the committee then took some time to look through the list and decide on who should represent a given issue at this or a future session.  

As there were not many members present it was decided to adjourn early and return in the afternoon to discuss matters

### Session B: Sept 14th 12:30 UTC

Present: HG, FA, WDN, SB, PJ, MarkuK, BW, PC, LG, TM, HB, CZ, MarkK

As many people were remote, voting on issues would be via thumbs up or down attached to a voting comment on a ticket

SB introduced [supporting the recommended property for Attributes](https://github.com/nexusformat/NIAC/issues/140) 
PJ asked if there was any python code to render this this change yet, SB said that was in progress but the change did not break any existing documentation generation.
It was proposed to  allow the "recommended" property (to complement "optional" which can be true or false) to be applied to attributes. This "recommended" property has already been approved for fields and groups, so this will just make attributes more consistent. VOTE: approved
 
PJ commented that in general it was good if people selected nexusformat/developers in teh reviewer of tickets/PRs as we require one review.

SB then introduced [Allow NXdata dimension variables to contain a list of strings](https://github.com/nexusformat/NIAC/issues/97) currently only NX_NUMBER data is allowed in axes, the change was to allow NX_CHAR too so e.g. channel names (i.e. an array of strings) could be used as labels along an axis for data. VOTE: approved 

SB then introduced [Support for non-dimensional coordinates in NXdata](https://github.com/nexusformat/NIAC/issues/139) which intends to introduce virtual axes, which are like the [non-dimensional coordinates of the python xarrays package](https://docs.xarray.dev/en/stable/user-guide/terminology.html?highlight=non%20dimensional#term-Non-dimension-coordinate). BW wondered if this was adding too specialist and adding too much complexity? We have discussed similar ideas previously and decided that NeXus should make data available for plotting, but should not try to describe how the plot is presented.  SB mentioned that a separate NXdata of rearranged data could be created to acheieve the same result, but that would be duplicating data. WDN suggested that this could aslo be achieved by flattening the axis data and linking via a virtual dataset, he posted an example on the ticket.     VOTE: it was decided not to propose this feature for NeXus at this time

SB introduced [NeXus Ontology v2](https://github.com/nexusformat/NIAC/issues/136) The NIAC welcomed the update and unanimously supports the initiative and continuing work. PJ asked if this could be made more visible? HG said that she would be working with Steve Collins shortly to get things hosted via PURL with the new `nexus-purl` email address as the keeper. SB says there are also some rendering issues to solve.

SB introduced [Group referencing an Application Definition](https://github.com/nexusformat/NIAC/issues/138) this listed three approaches to ther problem of a complex meaurement where you would like to apply validation to a set of entries. There was discussion about this, `NXsubentry` was mentioned but this normally applies to multiple simultaneous techniques (multi modal) as opposed to a sequence of techniques. NeXus currently treates each NXentry as validated separately, so a prescribed sequence of NXentry is not validated. WDN proposed a subentry stucture that may be appriopriate on the ticket, SB will consider this and bring back and examplefor further discussion as appropriate. HG mentioned the use of sequence_index in NXprocess that might provide some mechanism. MK suggested that what SB is looking for might be a workflow software tool and notes that several will be presented at NOBUGS conference next week. VOTE: deferred

SB introduced [base classes always extend NXobject. Can a base class extend another base class?](https://github.com/nexusformat/NIAC/issues/135) The NIAC has traditionally avoided too much interitance in base classes to limit complexity, base classes are generally dictionaries. Such a change would also require a validator to follow the relationships.  

## Session C: Sept 14th 15:00 UTC

Present: AB, FA, SB, RO, PJ, LG, BW, RB, PC, MK, PC, HB, HG, WDN, CZ

As this was a larger group with some new people, BW summariesed use of the [project board](https://github.com/orgs/nexusformat/projects/2/views/1) and people taking ownership of issues to champion. 

RO mentioned he had a PR about changes to documentation and asked if it needed a vote? BW confirmed that if it did not change how files were written (i.e. was e.g. clarification) then it did not need NIAC and could just go via normal PR approval. 

It was discussed when to have a session to elect officers, later in the day looked better for best attendance due to time zones. The third session on Thursday (session F) was agreed.

SB introduced [symbols to be connected to Field values](https://github.com/nexusformat/NIAC/issues/141) Symbols are used in definitions as placeholders for values and allow you to indicate that two arrays must have the same (or a related) size. Symbols themselves are, however, not explicitly documented and a new symbol cannot be defined in terms of existing symbols. The proposal was for a symbols table that would allow both. The NIAC likes the ideas put forward here and encourages preparatation of a more complete proposal.

As an offshoot of this, use of math within a nexus definition of file was discussed. For the general case, a machine parsable syntax would need to be chosen - HB suggested Javascript might be a good one. As this point math was only being considered for dimension attributes, and the math is contained in the NXDL. AB mentioned [math support in nexus](https://github.com/nexusformat/definitions/issues/711)    which is having math applied in the NeXus file during reading, which has potential security issues if an arbitrary equation is allowed leading to a denial of service attack. However it was pointed out that reading an extremely large dataset in an incorrect way can lead to such a thing anyway! It was discussed if a simpler set of operations rather than full equations could be used, but in this case the equation is quite complex. WDN mentioned [HDF5 UDF](https://hdf5-udf.readthedocs.io/en/latest/) which is an interesting option but this would tie nexus to HDF5. HDF5 UDF also has security issues. PC asked if there was a determined list of approved expressions would that give AB, HB what they need? SB suggested that there be a table called expressions similar to a symbols table, the NXentry would allow expressions to be defined by an applpication definition with the burden of security executing the expresion falling on the community that is supporting the application definition. PJ thinks that the point of NEXUS is to provide data, not data processing. AB said that at the moment the data isnt 100% useful without the processing so it would be great to find a solution to this.

WDN introduced [NXdata: errors on auxiliary signals](https://github.com/nexusformat/definitions/issues/1044) which was to allow use of `VARIABLE_errors` on additional signal arrays, it is currently allowed on axes and the main signal array. NIAC agrees that this is just a documentation bug that should be fixed. Also the `errors` field was already decided to be deprecated in 2018, this was just not yet actioned.

There was a rediscusison of [Support for non-dimensional coordinates in NXdata](https://github.com/nexusformat/NIAC/issues/139) introduced by SB as RO was now present. RO and WDN has been doing something similar using transformation matrices for the axes, so it will be considereded if allowing the addition of a transformatioin matrix to the dataset would be able t solve the use case. PC requests that there be a human readable field added to the documentation.

AB introduced [Flux changes for NXmx](https://github.com/nexusformat/definitions/pull/1035). The NIAC agreed that this did not need to wait for [Can we have a standard rule in NeXus to validate presence of one item from a list of possibles](https://github.com/nexusformat/definitions/issues/1002) to be resolved and could be voted on and merged. The outstanding ticket referred to being able to specify that one of: flux, total_flux, flux_integrated, total_flux_integrated being present, which is currently not a rule available in NDXL. It is not possible just to use an enum for these option as one can refer to an external arbitrary named NXmonitor. 

## Session D: Sept 15th 10:00-12:00 UTC

NIAC members Present: Russ Berg (RB), Ben Watts (BW), Freddie Akeroyd (FA), Peter Chang (PC), Luca Geliso (LG), Pete Jemian (PJ), Heike Gorzig (HG), Sandor Brockhaus (SB), Mark Koennecke (MK),
non-NIAC Present: Markus Kunbach (Markus), 

-----------------------------------

PJ raised [XPCS issue 1007 ](https://github.com/nexusformat/definitions/issues/1007) but it still needs discussions in the technical committee and would like to invite those people to next telco to discuss related issues, such as issues [1004](https://github.com/nexusformat/definitions/issues/1004), [1005](https://github.com/nexusformat/definitions/issues/1005) and [1006](https://github.com/nexusformat/definitions/issues/1006).
PJ XPCS community write processed data data (which is what the NXxpcs definition covers) in 2 different ways so consensus needs to be discussed with a focus on standardizing on NeXus.
PJ,LG discussion about g2 function.
PJ 2 ways the data (output of the g2 functions) are linked list of keys to g2 functions and the other is a 2D array.
BW this is a feature of HDF5 and there is some resistance to becoming dependant on hdf5.
BW thinks that it is fine if each community writes its own storage mode and let the community decide which is more popular.
PJ what is there in NXxpcs definition is version 1 and there is a version 2 in the works.
PJ invited LG to review and participate in NXxpcs technical discussions.
BW asked PJ if there was a preference for when the next telco should be and PJ requested later in october.
PJ the typical data size of XPCS is on the order of Gigabytes.

-----------------------------------

BW looking at items in project there are 2 that likely do not need to be here, [ISSUE 101](https://github.com/nexusformat/NIAC/issues/101) has already been discussed in spring and merged already.
PC suggested that we wait to see if AB connects to meeting to see if he agrees that this can be closed.
BW think [ISSUE 88](https://github.com/nexusformat/NIAC/issues/88) doesn't needs a NIAC decision and can be left for next code camp.
BW the issue author was pointing out that documentation was a bit messy so BW suggesting this be moved from NIAC repo to the DEFINITIONS repo and consensus was achieved for this.
BW moved issue to definitions repo and added CODECAMP label.

-----------------------------------

SB inquired about [issue 945](https://github.com/nexusformat/definitions/issues/945), identify labels for axis, of type NX_NUMBER or NX_CHAR.
SB inquireds about crteate something like NX_ANY that could handle either NX_NUMBER or NX_CHAR.
PJ has partially proposed using the type attribute using logical operators to include "or" in the type specification.
PJ forsees difficulty in XML specofication unless a new type that includes both NX_CHAR and NX_NUMBER is used.
SB suggests something like NX_SIMPLE which would represnt a string or a single part number, not complex or quarternian numbers.
PJ/SB maybe NX_LABEL? 
BW is writing this up as [issue 142](https://github.com/nexusformat/NIAC/issues/142) that references [issue 945](https://github.com/nexusformat/definitions/issues/945).
BW and PJ had intense discussion about cats.
PJ the entire point of NXdata is to be able to plot the data.
MK suggests NX_ALPHANUM, consensus was in favor.
BW prepared proposal to create NX_ALPHANUM to include NX_CHAR and NX_NUMBER, but voting is delayed until more members are present.

-----------------------------------

MK should NX_POSINT be renamed NX_UINT?
PC NX_UINT already exists.

-----------------------------------

MK/SB/Markus discussion about inheritance of base class defs, application defs and cnxvalidate, many ideas and opinions expressed faster than could be recorded accurately.
There is not a consensus as to what is meant by "inheritance".
MK there is only proper inheritcance in application definitions, when it comes to base class "inheritance" it is really a reference only.
MK `type` will only name a base class not an application definition, `extends` is used for extending an application definition.
SB what is the actual restriction for not allowing "inheritance"?, there should be a way to include an application def in another without having to copy everything.
SB we already (using the example of NXsubentry) have an inhreitance and the questions is why is this limited to NXsubentry inheriting NXentry only.
Markus we (electro microscopy) would like some guidance on how to do this then to just create 50 sub definitions and suggesting this for in an application definition.
SB the main issue is to use what he is seeing is already there (NXsubentry inherits NXentry) and use that for appl defs so that there isnt all this copied definition .
BW there are good arguments for inheritance, NXdetector is an example where inheritance could be useful, but it has been avoided for a long time. Perhaps SB/Markus will be the motivators for getting this implemented.

 

## Session E: Sept 15th 12:30-14:30 UTC

NIAC members Present: Russ Berg (RB), Ben Watts (BW), Peter Chang (PC), Pete Jemian (PJ), Heike Gorzig (HG), Sandor Brockhaus (SB), Mark Koennecke (MK),
			 Herbert Bernstein (HB), Aaron Brewster (AB), Heike Gorzig (HG),  Raymond Osborn (RO),
			 
			 
BW presented his proposed changes to the [NXxas documentation](https://github.com/nexusformat/definitions/issues/1170) in a [pull request](https://github.com/nexusformat/definitions/pull/1190).
PC the documentation suggests that the links that are all in lower case imply that thay should be the actual names of the fields where the documentation should use upper case to indicate they would only be NX classes not actual names.
BW will make the changes and we can look at it again later.

-----------------------------------

MK after the break and some further contemplation MK continued inheritance discussion from previous session.
MK because SB is trying to do something new with NeXus, it needs a proposal and a discussion.
SB the data he deals with doesn't really support the idea of a "single file" data is always spread across multiple files and produced by multiple vendors, so they are trying to harmonize all the sources.
SB clarified the inheritance currently exists in NeXus and what he is looking for.
Seems to be consensus that the future should include a "programmers" understanding of inheritance to create new base classes so that base classes can be exteneded via inheritance to avoid duplication of definition code, but the problem is how to document this class relationship a)to non programmers and b) in a way that explains why we have inheritance in one place but not in another (NXdetector copies base class propoerties).
BW suggests that maybe we should consider to overhaul the entire system at a code camp.

-----------------------------------

There was discussion about NXDL versions in [issue 1038](https://github.com/nexusformat/definitions/issues/1038).
It will require more discussion and was best kept for the next code camp.
Label changed to code camp.

-----------------------------------

BW again presented his [changes to NXxas](https://github.com/nexusformat/definitions/pull/1190/files).
MK asks if these changes serve the significant part of the community? BW answers yes, these changes are a significant improvement, but it is far from perfect still. To handle experiments doing multiple modes of measurement, it would really require a new NXxas definition as this one is really restricted to a single mode.
After review the changes were voted on and accepted, code merged.

-----------------------------------

AB raised the [Fix up NXBeam symbols and polarization](https://github.com/nexusformat/NIAC/issues/101) issue.
AB this is likely closed and can be removed.
BW changes were already merged and were included into last release.
PJ there is nothing to do here, it has all been done.
AB concurred.

-----------------------------------

AB said this issue was discussed yesterday and can be reviewed now,  [Flux changes for NXmx](https://github.com/nexusformat/definitions/pull/1035) is done.
PJ requested some changes relating to the documentation reference link.
BW added a comment that in order for the optional NXmonitor that is specified to be validated it [must have a name](https://github.com/nexusformat/definitions/pull/1035/files/a40bdc6beabeeb3c794c1083399f38bbb46300e4).
clarification was made to the docstring for the attribute flux must point to a field or link to a field with one of the 4 names listed.


## Session F: Sept 15th 15:00-17:00 UTC

NIAC members Present: Russ Berg (RB), Ben Watts (BW), Peter Chang (PC), Pete Jemian (PJ), Wout de Nolf (WD), Freddie Akeroyd (FA), Sandor Brockhaus (SB), 
Mark Koennecke (MK), Herbert Bernstein (HB), Aaron Brewster (AB), Luca Geliso (LG),  Raymond Osborn (RO), Heike Gorzig (HG)

-----------------------------------

BW The proposal is to accept the changes to NXmx (previous session) represented by [pull request #1035](https://github.com/nexusformat/definitions/pull/1035), vote was unanimous to accept changes, marked approve.

-----------------------------------

SB requests to vote on [Clarify Data Types](https://github.com/nexusformat/NIAC/issues/142).
BW presents summary of changes to clarify data types in issue 142.
PJ that would still open up an issue of there still being text finding its way into NX_NUMBER, so PJ is not recomending including NX_BOOL in NX_NUMBER.
BW [Proposal is to replace the description of NX_NUMBER in the NeXus manual with: "any of the set of non-compound number representations NX_INT, NX_UINT, NX_POSINT and NX_FLOAT."](https://github.com/nexusformat/NIAC/issues/142#issuecomment-1247957679) Voting was unanimous to accept proposal.
BW [Proposal is to define NX_CHAR_XOR_NUM which encompasses NX_NUMBER and NX_CHAR such that either type can be used exclusively for all elements of the entire dataset](https://github.com/nexusformat/NIAC/issues/142#issuecomment-1247951551). Voting was unanimous to accept proposal.
BW [Proposal is to define NX_COMPOUND as encompassing the set of compound number types such as NX_COMPLEX, NX_CCOMPLEX, NX_PCOMPLEX and NX_QUATERNION](https://github.com/nexusformat/NIAC/issues/142#issuecomment-1247961708). 
PC does not think there is a use case for this.
PJ says we have talked about this.
BW proposes to vote to reject this with PC to add a comment explaining as to why there is no valid use case.

-----------------------------------

BW presents issue to [Elect Executive Officers](https://github.com/nexusformat/NIAC/issues/137).
BW Position of Executine Chair request for volunteers, AB responded affirmitively, RB seconded, voting was unanimously accepted.
BW Position of executive secretary, request for volunteers, SB responded affirmitively, PJ seconded, vote was accepted.
BW Position of technical manager, BW request for volunteers, MK asked to accept the role and he did, PJ seconded, voting was unanimously accepted.
BW Position of defintions release manager, PC asked to continue on in the position, PJ seconded, voting was unanimously accepted .

-----------------------------------

SB items 15 -> 18 can be left until tomorrows session.

-----------------------------------

AB presentented item [NXmx: Change entry/end_time_estimated from "required" to "recommended"](https://github.com/nexusformat/definitions/issues/966). Dectris want it to be "recommended" since they find it difficult to guarantee compliance, but the MX community want it to be "required" in order to make sure it is included.
HB proposes to leave the rules documented as they are and let Dectris deal with not being compliant.
AB making [comment to respond](https://github.com/nexusformat/definitions/issues/966#issuecomment-1248323401) to Dectris agreeing that the detector manufacturer only has to provide an API to allow the metadata to be included in the file and that it is the responsibility of those operating the detector to provide the actual metadata.
BW we will mark this item as done.

-----------------------------------

BW raises item [NXsqom: filenames -> file_name](https://github.com/nexusformat/NIAC/issues/63).
RB has not provided comment requested by BW back in feb 2022.
BW proposes to move it to next NIAC meeting.

-----------------------------------

BW raises issue [NXsas: review use of minOccurs on various components](https://github.com/nexusformat/NIAC/issues/58).
BW we need community involment in reccomendations - PJ said he could.
There was discussion about "fair" data by MK, SB, PJ, HG.

-----------------------------------

BW raises issue [NXdata errors on an axis, signal or auxiliary signal](https://github.com/nexusformat/definitions/pull/1047).
WD presents the changes he made to resolve the issue as was talked about yesterday.
PC wanted some discussion to clarify what is meant by the word VARIABLE.
BW suggests changing VARIABLE to FIELDNAME in the docstring.
WD asked to make the change to the docstring, as its just documentation no vote is required.
BW added comment "Replacing "VARIABLE" with "FIELDNAME" would be more general and easier to understand."
WD made changes, BW made changes to NXdata.nxdl.xml.
Changes can be merged.

-----------------------------------

BW because of low turnout for first session of the day it was proposed to use the first session tomorrow for homework and instead meet for the second session, it was agreed.

Session G: Sept 16th 10:00-12:00 UTC 
------------------------------------

not used as agreed upon in session F.


## Session H: Sept 16th 12:30-14:30 UTC 

NIAC members Present: Russ Berg (RB), Ben Watts (BW), Peter Chang (PC), Pete Jemian (PJ), Mark Koennecke (MK), Herbert Bernstein (HB), Aaron Brewster (AB), Sandor Brockhaus (SB), CHen Zhang (CZ)

-----------------------------------

PJ presented issue  [NXsas: review minOccurs and group names](https://github.com/nexusformat/definitions/pull/1194).
PJ went through file [changes he made](https://github.com/nexusformat/definitions/pull/1194/files).
PJ received comments from BW, MK, PC, PJ will make changes and bring this up again when they are done.

-----------------------------------

SB question about item [supporting the recommended property for Attributes](https://github.com/nexusformat/NIAC/issues/140).
BW this is already finished and can be marked done.

-----------------------------------

BW asked if this was done: [NXmx: Definitions for multi-channel (thresholds) data](https://github.com/nexusformat/definitions/issues/940).
PJ, AB we need information from Dectris, so this is done from the perspective of NIAC 2022.

-----------------------------------

BW raised item [math in the \<dim\> element](https://github.com/nexusformat/definitions/issues/1084).
AB we need a pull request for this.
group discussion about math element added to the symbols table to define new symbols that are used in the definition to specify dimensions etc. 
MK raised a practical concern that because cnxvalidate is written in C that there be a library used to convert javascript to C if javascript will be
used as the essential supported math grammer that will be allowed/supported.
group discussion on possible use of javascript to evaluate math expressions in symbol definitions.
BW [Proposal is to explore the use of javascript syntax for mathematical expressions in NXDL symbol tables (and elsewhere in NeXus) and encourage the production of a technical demonstration](https://github.com/nexusformat/definitions/issues/1084#issuecomment-1249411564).
BW proposed a vote to accept, PJ seconded,proposal was unanimously accepted.

-----------------------------------

SB raised a discussion with BW about item [symbols to be connected to Field values](https://github.com/nexusformat/NIAC/issues/141).
PC about having symbols defined not only in the sybmbols table but also in a new attribute to a group as an expression.
The outcome was that the need for such a thing is not clear.
BW asked if the topic required more discussion next session SB indicated no.


  

## Session I: Sept 16th 15:00-17:00 UTC 

NIAC members Present: Russ Berg (RB), Ben Watts (BW), Peter Chang (PC), Pete Jemian (PJ), Mark Koennecke (MK), Herbert Bernstein (HB),  Sandor Brockhaus (SB), Freddie Akeroyd (FA), Aaron Brewster (AB), Raymond Osborn (RO),


PJ mentioned PR [NXsas: review minOccurs and group names](https://github.com/nexusformat/definitions/pull/1194).
PJ raised a question regarding signal indices.
Group discussion about assumptions about indices that are not specified, assumption is the first in the list is the horizontal axis but we dont believe it is stated anywhere, it is just assumed.
PJ documentation states "C storage order" which isn't really helpful, should maybe be replaced by something more immediately understandable for everyone.
MK propose change to the words "Row Major Order" instead.
PJ [Changes finalized](https://github.com/nexusformat/definitions/pull/1194/files/aaed8881ea25d49d7920fee2f557e6ecbfa40492).
BW proposes motion to [vote to accept](https://github.com/nexusformat/NIAC/issues/58#issuecomment-1249513045), RB seconded.
after Voting motion was unanimously approved.
PJ changes merged.

-----------------------------------

BW raises an old item from [NIAC2020](https://www.nexusformat.org/NIAC2020.html) with [Suggested improvements to the NXdata base class definition](https://github.com/nexusformat/NIAC/issues/48).
PC there is a change requested before a PR can be executed.
BW suggests we put this issue aside, PJ seconded, it will get a telco label to make sure it gets examined on next telco/code camp.

-----------------------------------

RB raises again [issue 322](https://github.com/nexusformat/definitions/issues/322) and how to specify list of file paths.
PC should be 1D array because we allow variable length strings.
BW suggests changing "filenames" to "file_list", PJ says this already exists in NXxpcs and that there would be no collision since the meaning is the same.
Group discussion on the question is there a statement in NEXUS to avoid plural in favor of singular field names, couldn't really find anything that states that directly.
PC proposes to reject this issue as it doesn't appear to be a problem and not worth taking the chance on disrupting things for no apparent reason.
BW commented on this issue in github that due to our conversation and the amount of time lapsed we won't change anything unless the original reporter of the issue replies to make the case for this change.
BW asked if there were any objections to closing this issue, there were none.
BW closed issue.

-----------------------------------

SB raises that [PR 1183](https://github.com/nexusformat/definitions/pull/1183) is ready for merging.
PJ merged in GH.

-----------------------------------

BW raised item [Suggested improvements to the NXdata base class definition](https://github.com/nexusformat/NIAC/issues/48) because RO was attending and we had time.
PC, RO, BW discuss Tobias' comments.
BW putting this aside for today and look at in future telco, someone needs to look at the proposed changes to NXdata to handle this.

-----------------------------------

BW again reviewing item [Proposal to add 'angles' attribute to NXdata groups](https://github.com/nexusformat/NIAC/issues/102).
BW not going to reconsider this items concerns today.
RO asked will this extra array in NXdata to handle transformations require a NIAC vote.
BW only if it is a change to the NXdata base class or the application definition.

-----------------------------------

BW raises item [AppDef for Electron Microscopy](https://github.com/nexusformat/NIAC/issues/103).

SB we can mark this as done for this meeting as they are still being worked on.

same for project items:
* [NeXus Ontology v2](https://github.com/nexusformat/NIAC/issues/136).
* [Group referencing an Application Definition](https://github.com/nexusformat/NIAC/issues/138).
* [Support for non-dimensional coordinates in NXdata](https://github.com/nexusformat/NIAC/issues/139).

-----------------------------------

BW there are no more NIAC items remaining in the project board, asked if there is anything else anyone wanted to raise for the NIAC.

RO asked PJ about PR [Add nexusformat examples](https://github.com/nexusformat/definitions/pull/1145).

PJ gave positive reply.

BW calls the meeting to a close.





