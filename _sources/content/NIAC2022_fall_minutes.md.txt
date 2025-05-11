---
title: Minutes of the NIAC2022 Fall Meeting
permalink: NIAC2022_fall_minutes.html
layout: wiki
---
Minutes of the NIAC2022 Fall Meeting
====================================


Session B: Sept 14th 12:30 UTC
------------------------------

NIAC members Present: Sandor Brockhaus (SB), Mark Koennecke (MK), Russ Berg (RB), Ben Watts (BW), Freddie Akeroyd (FA), Peter Chang (PC), 
Heike Gorzig (HG), Wout de Nolf (WD), Pete Jemian (PJ), Luca Geliso (LG), Takahiro Matsumoto (TM), Herbert Bernstein (HB)

non-NIAC Present: Markus Kunbach (Markus), 

BW proposed voting via github thumbs up/down and it was agreed

SB presented issue 24, Proposal is to allow the "recommended" property (to complement "optional" which can be true or false) to be applied to attributes. https://github.com/nexusformat/NIAC/issues/140
PJ This "recommended" property has already been approved for fields and groups, so this will just make attributes more consistent. 
PJ suggested to add "Developers" as reviewers for pull requests
The proposal was voted on and approved.

SB preseted issue 3 (Allow NXdata dimension variables to contain a list of strings https://github.com/nexusformat/NIAC/issues/945),
SB this would be an array of strings
PC this issue was voted on and approved back at the spring NIAC
PJ the changes need to be made, will set for next release

SB presented issue 23, Support for non-dimensional coordinates in NXdata https://github.com/nexusformat/NIAC/issues/139
MK proposal refers to issues of data processing and thus goes to far for what NEXUS is expected to provide
BW NEXUS has seen this before, NEXUS shouldnt describe how to produce plot, it should make the data accessble only
SB proposal is also to propose future axes as well, 
MK this still seems to require more data specializations which 
BW NXdata is recomended to exist for each dataset so it should be kept more general and not be too specific about how to produce plotting which is more in teh realm of data processing
WD this can be handled using what already exists by just creating a virtual dataset

SB presented issue 21, NeXus Ontology v2 https://github.com/nexusformat/NIAC/issues/136
BW commented The NIAC is pleased to see further development of the NeXus ontology and we encourage you to continue this work.
PJ asked when can this work be included in public docmentation, HG said there are some issues with email addrs? FK mentioned a registration that needed to take place for nexusformat.org
PJ can this be put onto the NEXUS home page, 
SB there are also some rendering issues, but once rendered there will be a link that can be used to link to NEXUS homepage

SB presented issue 22, Group referencing an Application Definition https://github.com/nexusformat/NIAC/issues/138
MK proposed option D, NXsubentry was created to handle situations like these
BW clarified the use of NXsubentry, where you have a single NXentry and references to other app defs appears in individual NXsubentries of the NXentry
PJ offered that what maybe what SB is looking for is NXnote to describe the process that is planned
BW NXenry is required for each measurement in a sequence, NSsubentry refers to another app def for a simulataneous measurements
MK suggested that what SB is looking for is a workflow software tool several will be presented at NOBUGS conference next week
WD suggested a specific example for future discussion
SB agreed after looking at NXsubentry that it should address this proposal, future discussion likely to follow


SB presented issue 19, base classes always extend NXobject. Can a base class extend another base class? https://github.com/nexusformat/NIAC/issues/135
MK said that NIAC has discussed this numerous times in the past and has reasons for not adopting inheritance for base class definitions
PJ asked what base class needs extension
SB asked if people could reread the issue and continue discussions in next session and/or next week during NOBUGS
BW closed session



Session C: Sept 14th 15:00 UTC
------------------------------

NIAC members Present: Raymond Osborn (RO), Aaron Brewster (AB), Sandor Brockhaus (SB), Mark Koennecke (MK), Russ Berg (RB), Ben Watts (BW),  
Freddie Akeroyd (FA), Peter Chang (PC), Heike Gorzig (HG), Wout de Nolf (WD), Pete Jemian (PJ), Luca Geliso (LG), Herbert Bernstein (HB), CHen Zhang (CZ)

BW raised question about when we should adress issue 20, Elect Executive Officers https://github.com/orgs/nexusformat/projects/2/views/1
consensus was election to occur in third session tomorrow Sept 15, 
BW to send an email to NIAC list that that is the plan


SB presented issue 27, symbols to be connected to Field values https://github.com/nexusformat/NIAC/issues/141
MK suggests that a specific example be proposed so that the NIAC would have an actual situation to consider 
HB suggests javascript be used to provide the required structure to do what is being asked in regards to math in documentation, hooks would just need to be added into?
AB, BW, SB, MK, RO  had discussions trying to clarify the issue,
PJ, MK reminded everyone that adding executable code into a nexus file is a security issue
AB would like a way of using math to describe how to take 2 arrays to create a third
BW there are equations that exist that would produce a denial of service attack on the computer, basically the computation would be so intense as to occupy the entire CPU
HB this is a common problem, many things can occupy the entire CPU, standard code etc, people know better, and this is a neceisity 
PC if there was a determined list of approved expressions would that give AB, HB what they need
RB suggested that there be a table called expressions similar to a symbols table, the NXentry would allow expressions to be defined by an applpication definition
the burden of security of executing the expresion is on the community that is backing the application definition
PJ the point of NEXUS is to provide data, not data processing
AB said that at the moment the data isnt 100% useful without the processing so it would be great to find a solution to this
outcome of discusson of just that raised in issue 27 is: NIAC likes the idea of proposed SB and would like SB to produce specific example for the NIAC to review later 


WD presented issue 102, NXdata: errors on auxiliary signals, https://github.com/nexusformat/definitions/issues/1044
BW sauggests that we should go a step further and deprecate the "errors" attrubte in favor of VARIABLE_errors
MK in 2018 NIAC decided to deprecate "errors" attribute already, it just hasnt been done yet, so this is more a documentation bug than a change of the standard required
BW adds a comment to issue : NIAC agrees that this is just a documentation bug that should be fixed. Also the errors field was already decided to be deprecated in 2018. 
WD assigned to this task


RO issue 14, Proposal to add 'angles' attribute to NXdata groups https://github.com/nexusformat/NIAC/issues/102
RO in the last 30 minutes wanted to have a general discussion about the angles and transformations, 
WD would replace the proposal with one that all transformations could be represented by specifying a single transforma matrix
BW this isnt ready to vote on
WD will put forward a proposal as mentioned above
PC requests that there be  a human readable field added to the documentation

AB presented Can we have a standard rule in NeXus to validate presence of one item from a list of possibles? https://github.com/nexusformat/definitions/issues/1002
AB it is dependant on another issue 1002
BW was going to do some work on this, it should be possibele to do this, XML will need some crafting, this work doesnt stand in the way of voting on issue 1002
AB will switch PR to a draft
BW issue 1002 is about making the definition available so that it can be machine readble and validated








