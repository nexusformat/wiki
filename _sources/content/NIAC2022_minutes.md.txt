---
title: NIAC2022 Minutes
permalink: NIAC2022_minutes.html
layout: wiki
---
NIAC2022 Minutes
================


Session B: Sept 14th 12:30 UTC
------------------------------

NIAC members Present: Sandor Brockhaus (SB), Mark Koennecke (MK), Russ Berg (RB), Ben Watts (BW), Freddie Akeroyd (FA), Peter Chang (PC), 
Heike Gorzig (HG), Wout de Nolf (WD), Pete Jemian (PJ), Luca Geliso (LG), Takahiro Matsumoto (TM), Herbert Bernstein (HB)

non-NIAC Present: Markus Kunbach (Markus), 

-----------------

BW proposed voting via github thumbs up/down and it was agreed

-----------------

SB presented issue 24, Proposal is to allow the "recommended" property (to complement "optional" which can be true or false) to be applied to attributes. https://github.com/nexusformat/NIAC/issues/140

PJ This "recommended" property has already been approved for fields and groups, so this will just make attributes more consistent. 

PJ suggested to add "Developers" as reviewers for pull requests

The proposal was voted on and approved.

-----------------

SB preseted issue 3 (Allow NXdata dimension variables to contain a list of strings https://github.com/nexusformat/NIAC/issues/945),

SB this would be an array of strings

PC this issue was voted on and approved back at the spring NIAC

PJ the changes need to be made, will set for next release

-----------------

SB presented issue 23, Support for non-dimensional coordinates in NXdata https://github.com/nexusformat/NIAC/issues/139

MK proposal refers to issues of data processing and thus goes to far for what NEXUS is expected to provide

BW NEXUS has seen this before, NEXUS shouldnt describe how to produce plot, it should make the data accessble only

SB proposal is also to propose future axes as well, 

BW NXdata is recomended to exist for each dataset so it should be kept more general and not be too specific about how to produce plotting which is more in the realm of data processing

WD this can be handled using what already exists by just creating a virtual dataset

-----------------

SB presented issue 21, NeXus Ontology v2 https://github.com/nexusformat/NIAC/issues/136

BW commented The NIAC is pleased to see further development of the NeXus ontology and we encourage you to continue this work.

PJ asked when can this work be included in public docmentation, HG said there are some issues with email addrs? FK mentioned a registration that needed to take place for nexusformat.org

PJ can this be put onto the NEXUS home page, 

SB there are also some rendering issues, but once rendered there will be a link that can be used to link to NEXUS homepage

-----------------

SB presented issue 22, Group referencing an Application Definition https://github.com/nexusformat/NIAC/issues/138

MK proposed option D, NXsubentry was created to handle situations like these

BW clarified the use of NXsubentry, where you have a single NXentry and references to other app defs appears in individual NXsubentries of the NXentry

PJ offered that what maybe what SB is looking for is NXnote to describe the process that is planned

BW NXenry is required for each measurement in a sequence, NSsubentry refers to another app def for a simulataneous measurements

MK suggested that what SB is looking for is a workflow software tool several will be presented at NOBUGS conference next week

WD suggested a specific example for future discussion

SB agreed after looking at NXsubentry that it should address this proposal, future discussion likely to follow

-----------------


SB presented issue 19, base classes always extend NXobject. Can a base class extend another base class? https://github.com/nexusformat/NIAC/issues/135

MK said that NIAC has discussed this numerous times in the past and has reasons for not adopting inheritance for base class definitions

PJ asked what base class needs extension

SB asked if people could reread the issue and continue discussions in next session and/or next week during NOBUGS

-----------------

Session C: Sept 14th 15:00 UTC
------------------------------

NIAC members Present: Raymond Osborn (RO), Aaron Brewster (AB), Sandor Brockhaus (SB), Mark Koennecke (MK), Russ Berg (RB), Ben Watts (BW),  
Freddie Akeroyd (FA), Peter Chang (PC), Heike Gorzig (HG), Wout de Nolf (WD), Pete Jemian (PJ), Luca Geliso (LG), Herbert Bernstein (HB), CHen Zhang (CZ)

BW raised question about when we should adress issue 20, Elect Executive Officers https://github.com/orgs/nexusformat/projects/2/views/1

consensus was election to occur in third session tomorrow Sept 15, 

BW to send an email to NIAC list that that is the plan

-----------------

SB presented issue 27, symbols to be connected to Field values https://github.com/nexusformat/NIAC/issues/141

MK suggests that a specific example be proposed so that the NIAC would have an actual situation to consider 

HB suggests javascript be used to provide the required structure to do what is being asked in regards to math in documentation, hooks would just need to be added into?

AB, BW, SB, MK, RO  had discussions trying to clarify the issue,

PJ, MK reminded everyone that adding executable code into a nexus file is a security issue

AB would like a way of using math to describe how to take 2 arrays to create a third

BW there are equations that exist that would produce a denial of service attack on the computer, basically the computation would be so intense as to occupy the entire CPU

HB this is a common problem, many things can occupy the entire CPU, standard code etc, people know better, and this is a neceisity 

PC if there was a determined list of approved expressions would that give AB, HB what they need

RB suggested that there be a table called expressions similar to a symbols table, the NXentry would allow expressions to be defined by an applpication definition with the burden of security executing the expresion falling on the community that is supporting the application definition

PJ the point of NEXUS is to provide data, not data processing

AB said that at the moment the data isnt 100% useful without the processing so it would be great to find a solution to this

outcome of discusson of just that raised in issue 27 is: NIAC likes the idea of proposed SB and would like SB to produce specific example for the NIAC to review later 

-----------------


WD presented issue 102, NXdata: errors on auxiliary signals, https://github.com/nexusformat/definitions/issues/1044

BW sauggests that we should go a step further and deprecate the "errors" attrubte in favor of VARIABLE_errors

MK in 2018 NIAC decided to deprecate "errors" attribute already, it just hasnt been done yet, so this is more a documentation bug than a change of the standard required

BW adds a comment to issue : NIAC agrees that this is just a documentation bug that should be fixed. Also the errors field was already decided to be deprecated in 2018. 

WD assigned to this task

-----------------

RO issue 14, Proposal to add 'angles' attribute to NXdata groups https://github.com/nexusformat/NIAC/issues/102

RO in the last 30 minutes wanted to have a general discussion about the angles and transformations, 

WD would replace the proposal with one that all transformations could be represented by specifying a single transforma matrix

BW this isnt ready to vote on

WD will put forward a proposal as mentioned above

PC requests that there be  a human readable field added to the documentation

-----------------

AB presented Can we have a standard rule in NeXus to validate presence of one item from a list of possibles? https://github.com/nexusformat/definitions/issues/1002

AB it is dependant on another issue 1002

BW was going to do some work on this, it should be possibele to do this, XML will need some crafting, this work doesnt stand in the way of voting on issue 1002

AB will switch PR to a draft

BW issue 1002 is about making the definition available so that it can be machine readble and validated

-----------------


Session D: Sept 15th 10:00-12:00 UTC
------------------------------------

NIAC members Present: Russ Berg (RB), Ben Watts (BW), Freddie Akeroyd (FA), Peter Chang (PC), Luca Geliso (LG), Pete Jemian (PJ), Heike Gorzig (HG), Sandor Brockhaus (SB), Mark Koennecke (MK),
non-NIAC Present: Markus Kunbach (Markus), 

-----------------------------------

PJ raised XPCS discussion
PJ XPCS issue (1007 https://github.com/nexusformat/definitions/issues/1007) still need discussions in the technical committee and would like to invite those people to next telco to raise related issues.
BW issues 1004/5 and 6 also have been raised for discussion
PJ XPCS community write processed data data (which is what the NXxpcs definition covers) in 2 different ways so consensus needs to be discussed with a focus on standardizing on NEXUS
PJ,LG discussion about g2 function
PJ 2 ways the data (output of the g2 functions) are linked list of keys to g2 functions and the other is a 2D array
BW this is a feature of HDF5 and there is some resistance to becoming dependant on hdf5
BW thinks that it is fine if each community writes its own storage mode and let the community decide which is more popular
PJ what is there in NXxpcs definition is version 1 and there is a version 2 in the works
PJ invited LG to review and participate in NXxpcs technical discussions
BW asked PJ if there was a preference for when the next telco should be and PJ requested later in october.
PJ the typical data size of XPCS is on the order of Gigabytes

-----------------------------------

BW looking at items in project there are 2 that likely do not need to be here, #13 (ISSUE 101 https://github.com/nexusformat/NIAC/issues/101) it has already been discussed in spring and merged already,
PC suggested that we wait to see if AB connects to meeting to see if he agrees that this can be closed, 
BW #11 (ISSUE 88), doesn't think it needs a NIAC decision and can be left for next code camp
BW the issue author was pointing out that documentation was a bit messy so BW suggesting this be moved from NIAC repo to the DEFINITIONS repo and consensus achieved for this
BW moved issue to definitions repo and added CODECAMP label

-----------------------------------

SB inquired about item 3 issue https://github.com/nexusformat/definitions/issues/945, idendify labels for axis, of type NX_NUMBER or NX_CHAR, 
SB inquireds about crteate something like NX_ANY that could handle either NX_NUMBER or NX_CHAR
PJ has partially proposed using the type attribute using logical operators to include "or" in the type specification
PJ forsees difficulty in XML specofication unless a new type that includes both NX_CHAR and NX_NUMBER is used
SB suggests something like NX_SIMPLE which would represnt a string or a single part number, not complex or quarternian numbers
PJ/SB maybe NX_LABEL? 
BW is writing item 31 this up as an issue 142 https://github.com/nexusformat/NIAC/issues/142 that references 945
BW and PJ had intense discussion about cats
PJ the entire point of NXdata is to be able to plot the data
MK suggests NX_ALPHANUM, consensus was in favor 
BW proposaol to create NX_ALPHANUM to include NX_CHAR and NX_NUMBER

-----------------------------------

MK should NX_POSINT be renamed NX_UINT
PC NX_UINT already exists

-----------------------------------

MK/SB/Markus discussion about inheritance of base class defs, application defs and cnxvalidate, many idea's and opinions expressed faster than could be recorded accurately
there is not a consensus as to what is meant be "inheritance", 
MK there is only proper inheritcance in application definitions, when it comes to base class "inheritance" it is really a reference only
MK type= will only name a base class not an application definition, extends is used for extending an application definition
SB what is the actual restriction for not allowing "inheritance"?, there should be a way to include an application def in another without having to copy everything
SB we already (using the example of NXsubentry) have an inhreitance and the questions is why is this limited to NXsubentry inheriting NXentry only
Markus we (electro microscopy) would like some guidance on how to do this then to just create 50 sub definitions and suggesting this for in an application definition
SB the main issue is to use what he is seeing is already there (NXsubentry inherits NXentry) and use that for appl defs so that there isnt all this copied definition 
BW there is good arguments for inheritance, NXdetectoir is abn example as to why inheritance has been avoided for a long time, perhaps SB/Markus will be the motivators for getting this implimented

 
-----------------------------------



Session E: Sept 15th 12:30-14:30 UTC
------------------------------------

NIAC members Present: Russ Berg (RB), Ben Watts (BW), Peter Chang (PC), Pete Jemian (PJ), Heike Gorzig (HG), Sandor Brockhaus (SB), Mark Koennecke (MK),
			 Herbert Bernstein (HB), Aaron Brewster (AB), Heike Gorzig (HG),  Raymond Osborn (RO),
			 
			 
BW presented his proposed changes in item 30 , PR https://github.com/nexusformat/definitions/tree/1170-nxxas-documentation-improvement nxxas documentation improvement issue https://github.com/nexusformat/definitions/pull/1190
PC the documentation suggests that the links that are all in lower case imply that thay should be the actual names of the fields where the documentation should use upper case to indicate they would only be NX classes not actual names
BW will make the changes and look at it again later

-----------------------------------

MK after the break and some further contemplation MK continued inheritance discussion from previous session
MK because SB is trying to do something new with NEXUS, it needs a proposal and a discussion
SB the data he deals with doesn't really support the idea of a "single file" data is always spread across multiple files and produced by multiple vendors, so they are trying to harmonize all the sources
SB clarified the inheritance currently exists in NEXUS and what he is looking for
Seems to be consensus that the future should include a "programmers" understanding of inheritiancr to create new base classes so that base classes can be exteneded via inheritance to avoid
duplication of definition code, but the problem is how to document this class relationship a)to non programmers and b) in a way that explains why we have inheritance in one place but not in another (NXdetector copies base class propoerties)
BW suggests that maybe we should over haul it all

-----------------------------------

There was discussion about issue 1038 https://github.com/nexusformat/definitions/issues/1038
It will require more discussion and was best kept for teh next codecamp
Label changed to code camp

-----------------------------------

BW presented his changes to file(s) for item 30 https://github.com/nexusformat/definitions/pull/1190/files/758973719c5cab6843e7bc2a00a5bcd405339386..5716b3511a73ac76eb86e6e5b67d2346654e2090
MK do these changes serve the significant part of the community? BW yes, to handle non single mode folks wouls really require a new NXxas definition as this one is really inadequate.
After review the changes were voted on and accepted, code merged

-----------------------------------

AB raised Fix up NXBeam symbols and polarization https://github.com/nexusformat/NIAC/issues/101
AB this is likely closed and can be removed
BW changes were already merged and were included into last release
PJ there is nothing to do here, it has all been done
AB concurred

-----------------------------------

AB said this issue was discussed yesterday and can be reviewed now,  Flux changes for NXmx https://github.com/nexusformat/definitions/pull/1035 is done
PJ requested some changes relating to the documentation reference link
BW added a comment that in order for the optional NXmonitor that is specified to be validated it must have a name https://github.com/nexusformat/definitions/pull/1035/files/a40bdc6beabeeb3c794c1083399f38bbb46300e4
clarification was made to the docstring for the attribute flux must point to a field or link to a field with one of the 4 names listed

 
			 

Session F: Sept 15th 15:00-17:00 UTC
------------------------------------

NIAC members Present: Russ Berg (RB), Ben Watts (BW), Peter Chang (PC), Pete Jemian (PJ), Wout de Nolf (WD), Freddie Akeroyd (FA), Sandor Brockhaus (SB), 
Mark Koennecke (MK), Herbert Bernstein (HB), Aaron Brewster (AB), Luca Geliso (LG),  Raymond Osborn (RO), Heike Gorzig (HG)

-----------------------------------

BW The proposal is to accept the changes to NXmx (previous session) represented by pull request #1035, vote was unanimous to accept changes, marked approve

-----------------------------------

SB requests to vote on item 31, Clarify Data Types https://github.com/nexusformat/NIAC/issues/142
BW presents summary of changes to clarify data types in issue 142
PJ that would still open up an issue of there still being text finding its way into NX_NUMBER, so PJ is not recomending including NX_BOOL in NX_NUMBER
BW Proposal is to replace the description of NX_NUMBER in the NeXus manual with: "any of the set of non-compound number representations NX_INT, NX_UINT, NX_POSINT and NX_FLOAT." Voting was unanimous to accept proposal
BW Proposal is to define NX_CHAR_XOR_NUM which encompasses NX_NUMBER and NX_CHAR such that either type can be used exclusively for all elements of the entire dataset. Voting was unanimous to accept proposal
BW Proposal is to define NX_COMPOUND as encompassing the set of compound number types such as NX_COMPLEX, NX_CCOMPLEX, NX_PCOMPLEX and NX_QUATERNION. 
PC does not think there is a use case for this
PJ says we have talkde about this
BW proposes to vote to reject this with PC to add a comment explaining as to why there is no use case

-----------------------------------

BW presents issue 20 Elect Executive Officers issue https://github.com/nexusformat/NIAC/issues/137
BW Position of Executine Chair request for volunteers, AB responded affirmitively, RB seconded, voting was unanimously accepted
BW Position of executive secretary, request for volunteers, SB responded affirmitively, PJ seconded, vote was accepted
BW Position of technical manager, BW request for volunteers, MK asked to accept the role and he did, PJ seconded, voting was unanimously accepted
BW Position of defintions release manager, PC asked to continue on in the position, PJ seconded, voting was unanimously accepted 

-----------------------------------

SB items 15 -> 18 can be left until tomorrows session

-----------------------------------

AB presentented item 21 NXmx: Change entry/end_time_estimated from "required" to "recommended" issue https://github.com/nexusformat/definitions/issues/966
HB proposes to leave the rules documented as they are and let Dectris deal with not being compliant
AB making comment to respond to Dectris
BW we will mark this item as done

-----------------------------------

BW raises item 10 NXsqom: filenames -> file_name https://github.com/nexusformat/NIAC/issues/63
RB has not provided comment requested by BW back in feb 2022
BW proposes to move it to next NIAC meeting

-----------------------------------

BW raises issue 9 NXsas: review use of minOccurs on various components https://github.com/nexusformat/NIAC/issues/58
BW we need community involment in reccomendations PJ said he could
There was discussion about "fair" by MK, SB, PJ, HG

-----------------------------------

BW raises issue 1  NXdata errors on an axis, signal or auxiliary signal PR https://github.com/nexusformat/definitions/pull/1047
WD presents the changes he made to resolve the issue as was talked about yesterday
PC wanted some discussion to clarify what is meant by the word VARIABLE, 
BW suggests changing VARIABLE to FIELDNAME in the docstring, 
WD asked to make the change to the docstring, as its just documentation no vote is required
BW added comment "Replacing "VARIABLE" with "FIELDNAME" would be more general and easier to understand."
WD made changes, BW made changes to NXdata.nxdl.xml
Changes can be merged

-----------------------------------

BW because of low turnout for first session of the day it was proposed to use the first session for homework and instead meet for the second session, it was agreed

Session G: Sept 16th 10:00-12:00 UTC 
------------------------------------

not used as aggreed upon in session F


Session H: Sept 16th 12:30-14:30 UTC 
------------------------------------

NIAC members Present: Russ Berg (RB), Ben Watts (BW), Peter Chang (PC), Pete Jemian (PJ), Mark Koennecke (MK), Herbert Bernstein (HB), Aaron Brewster (AB), Sandor Brockhaus (SB), CHen Zhang (CZ)

-----------------------------------

PJ presented issue  NXsas: review minOccurs and group names https://github.com/nexusformat/definitions/pull/1194
PJ went through file changes he made https://github.com/nexusformat/definitions/pull/1194/files
PJ received comments from BW, MK, PC, PJ will make changes and bring this up again when they are done

-----------------------------------

SB question about project item 25 supporting the recommended property for Attributes https://github.com/nexusformat/NIAC/issues/140
BW this is finished and can be marked done

-----------------------------------

BW asked if this was done: NXmx: Definitions for multi-channel (thresholds) data https://github.com/nexusformat/definitions/issues/940
PJ, AB we need information from Dectris, so from perspective of NAIC 2022 this is done

-----------------------------------

BW raised project item 7 math in the <dim> element https://github.com/nexusformat/definitions/issues/1084
AB we need a pull request for this
group discussion about math element added to the symbols table to define new symbols that are used in the definition to specify dimensions etc. 
MK raised a practical concern that because cnxvalidate is written in C that there be a library used to convert javascript to C if javascript will be
used as the  essential supported math grammer that will be allowed/supported
group discussion on possible use of javascript to exavulate math expressions in symbol definitions
BW Proposal is to explore the use of javascript syntax for mathematical expressions in NXDL symbol tables (and elsewhere in NeXus) and encourage the production of a technical demonstration.
BW proposed a vote to accept, PJ seconded,proposal was unanimously accepted

-----------------------------------

SB raised a discussion with BW about item 27 symbols to be connected to Field values https://github.com/nexusformat/NIAC/issues/141
PC about having symbols definied not only in the sybmbols table but also in a new attribute to a group as an expression
The outcome was that the need for such a thing is not clear
BW asked if the topic required more discussion next session SB indicated no


  

Session I: Sept 16th 15:00-17:00 UTC 
------------------------------------

NIAC members Present: Russ Berg (RB), Ben Watts (BW), Peter Chang (PC), Pete Jemian (PJ), Mark Koennecke (MK), Herbert Bernstein (HB),  Sandor Brockhaus (SB), Freddie Akeroyd (FA), Aaron Brewster (AB), Raymond Osborn (RO),


PJ mentioned PR NXsas: review minOccurs and group names https://github.com/nexusformat/definitions/pull/1194
PJ raised a question regarding signal indices
Group discussion about assumptions about indices that are not specified, assumption is the first in the list is the horizontal axis but we dont believe it is stated anywhere, it is just assumed
PJ documentation states "C storage order" which isn't really helpful, should maybe be replaced by something more immediately understandable for everyone.
MK propose change to the words "Row Major Order" instead
PJ CHanges finalized https://github.com/nexusformat/definitions/pull/1194/files/aaed8881ea25d49d7920fee2f557e6ecbfa40492
BW proposes motion to vote to accept, RB seconded https://github.com/nexusformat/NIAC/issues/58
after Voting motion was unanimously approved
PJ changes merged

-----------------------------------

BW raises [NIAC2020] Suggested improvements to the NXdata base class definition https://github.com/nexusformat/NIAC/issues/48
PC there is a change requested before a PR can be executed
BW suggests we put this issue aside, PJ seconded, it will get a telco label to make sure it gets examined on next telco/code camp

-----------------------------------

RB issue 322
how to specify list of file paths
PC shoudl be 1D array because we allow variable length strings
BW suggests changing filenames to file_list, PJ says this already exists in NXxpcs and that there would be no collision and that the meaning is the same
Group discussion on the question is there a statement in NEXUS to avoid plural in favor of singular field names, could really find anything that states that
PC proposes to reject this issue as it doesn't appear to be a problem and not worth taking the chance on disrupting things for no apparent reason
BW commented on this issue in GH that due to our conversation and the amount of time lapsed we wont change anything unless he comes back to make the case for this change
BW asked if there were any objections to closing this issue, there were none,
BW closed issue

-----------------------------------

SB raises that PR https://github.com/nexusformat/definitions/pull/1183 is ready for merging
PJ merged in GH

-----------------------------------

BW raised project item 8 because RO was attending and we had time [NIAC2020] Suggested improvements to the NXdata base class definition https://github.com/nexusformat/NIAC/issues/48
PC, RO, BW discuss Tobias comments
BW putting this aside for today and look at in future telco, someone needs to look at teh proposed changes to NXdata to handle this

-----------------------------------

BW reviewing item 14 again, Proposal to add 'angles' attribute to NXdata groups https://github.com/nexusformat/NIAC/issues/102
BW not going to reconsider this items concerns today
RO asked will this extra array in NXdata to handle transformations require a NIAC vote
BW only if itis a change to the NXdata base class and not the application definition

-----------------------------------

BW item 15 AppDef for Electron Microscopy https://github.com/nexusformat/NIAC/issues/103
SB we can mark this as done for this meeting as they are still being worked on

-----------------------------------

same for project items:
22 NeXus Ontology v2 https://github.com/nexusformat/NIAC/issues/136
23 Group referencing an Application Definition https://github.com/nexusformat/NIAC/issues/138
24 Support for non-dimensional coordinates in NXdata https://github.com/nexusformat/NIAC/issues/139

-----------------------------------

BW there are no more NIAC items in project board left, asked if there is anything else anyone wanted to raise for the NIAC

RO asked PJ about PR https://github.com/nexusformat/definitions/pull/1145 Add nexusformat examples 



## NIAC2022 Minutes
