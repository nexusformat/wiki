---
title: NIAC 2020 Concluding Session Minutes
permalink: NIAC2020minutes_concluding.html
layout: wiki
---
NIAC 2020 Concluding Session Minutes
====================================

The following [NIAC](https://www.nexusformat.org/NIAC.html) members were present: SC, FA, HB, RB, PJ, AB, PC, BW, WG, AS, TM, MJ, RO, MK, HG

Matthew Jones (MJ) was standing in for Tobias Richter.

This was the concluding session of [NIAC2020](https://www.nexusformat.org/NIAC2020.html) and was planned to summarise the NIAC and code camp results and move onto discussions and start voting on the matters arising. Items discussed and voted on at this meeting will be left open for a final week for NIAC members who were not able to be present to add their votes or raise further questions. Minutes of the previous sessions [are available](https://www.nexusformat.org/NIAC2020minutes.html)

The items to be discussed at this meeting were [listed at github](https://github.com/nexusformat/NIAC/projects/1#column-11377920)

BW summarised the recent [CodeCamp 2020-2](https://www.nexusformat.org/CodeCamp2020-2.html) Achievements

- Fixed issues in [documentation](https://github.com/nexusformat/definitions/issues?q=is%3Aissue+closed%3A%3E2020-10-18+)
- exampledata repository
  - [generate example files](https://github.com/nexusformat/exampledata/pull/18)
  - [better listing of file contents](https://github.com/nexusformat/exampledata/pull/22)
- [Clarify naming convention](https://github.com/nexusformat/definitions/pull/671#issuecomment-713166746) ([vote](https://github.com/nexusformat/definitions/pull/671#issuecomment-715476138))
- [Bug fixes for NAPI](https://github.com/nexusformat/code/pull/474)

There was a discussion over what rules were governing the current NIAC meeting. The constitution discusses regular 
NIAC meetings and teleconferences, it did not mention a virtual NIAC as such. The teleconference (TC) rules say that 2/3 of a NIAC 
need to be present for adequate discussion to take place before decisions are voted on, but any decision is passed to the email list 
for final votes of non present members to be added. There were 15 / 22 members present at this meeting, which did constitute 2/3 of the 
NIAC. It was decided to follow teleconference rules for this NIAC and leave a final week of online voting in order to ensure legality.

There was some further discussion of 2/3 quorum rule for teleconferences and whether this might prove to be restrictive in future 
for progressing decisions. Final decisions are not made at a teleconference even with more than 2/3 of the NIAC present, but 
unless 2/3 of the NIAC are present then the motion is not considered to have been adequately discussed and so does not get 
passed onto further consideration and voting. It was generally agreed that larger voting participation was desirable, but 
the mechanism may need to be enhanced. Different timezones can make finding an optimal meeting time difficult. Maybe 2/3 of NIAC member 
had been involved in the discussion over several (TC) meetings 
then it could move forward to wider email/list vote, but at the moment there is no indication that any changes are needed. 

The number of votes cast by the emoji based voting so far was not large, it was wondered if some abstentions had not been recorded and 
maybe instructions to indicate an abstention (by any not already mentioned emoji) were not originally clear enough. There will be a 
final email conclusion to voting, so people will be asked to register a choice. We should also draw people's attention to the process 
in the constitution for a NIAC member raising concern on a matter.

As discussed at the earlier sessions, a [survey has been sent out to the NeXus community](
https://lists.nexusformat.org/pipermail/nexus/2020/001140.html) by MK & FA as to their current use of ther old NeXus API (NAPI), 
with a view to determining future support options. It had been agreed that a bugfix release of NAPI would be done after merging 
current outstanding pull requests.

## Clarify naming conventions for groups and field

This was to clarify recommended NeXus names (lowercase letters with underscore plus trailing number, basically a valid variable name in most programming languages) verses generally allowed names in common usage (mixed case alphanumeric plus _ and . , except disallowing starting or ending with .) A regular expression was proposed for these combinations and is shown on the link and these expressions could be used by validation tools. HDF5 allows a wider range of characters in names than we currently use. AB asked about the current position on support and use of Unicode in NeXus. MK indicated the position was that unicode (via UTF8) was allowed for content by NeXus (HDF5 has a mechanism to indicate encoding), but not for field/dataset names which should be in standard/non-extended ASCII. This does mean that though NeXus does not specify a name for an NXentry for example, it is saying that a restricted character set should be used for it. After some discussion it was decided that though there are some technical issues in widening support the matter should be revisited at a later stage with input from members who may be interested in using a wider range of characters in field/dataset names. For info, [HDF5 support is described here](https://support.hdfgroup.org/HDF5/doc/Advanced/UsingUnicode/index.html) The NIAC proposed the statement "The NIAC recognises that the majority of the world uses characters outside of the basic latin (7-bit ASCII) set currently included in the allowed names. The restriction given here reflects current technical issues and we expect to revisit the issue and relax such restrictions in future."  [link](https://github.com/nexusformat/definitions/pull/671#issuecomment-715476138)

## NXmx application definition

The next discussion concerned [NXmx](https://github.com/nexusformat/NIAC/issues/45#issuecomment-707254127) The members present were happy with the current draft and it will be passed to the NIAC list for final email voting.

## @creator_version attribute

This is described [here](https://github.com/nexusformat/NIAC/issues/51#issuecomment-707349309) and was the addition of an optional root level attribute to complement the "creator" attribute by indicating its (software) version. This was agreed to be passed to final email voting. 

## Inconsistent field naming conventions

This discussion covered the use of either a prefix or a suffix to indicate a more specific part of an item, such as where to place "x": "pixel_x" or "x_pixel" ? NeXus has been inconsistent in the past, it was agreed amongst those present to recommend a suffix (i.e. "\_x") to indicate a more specific part in future definitions, using a suffix makes items group more nicely in user interfaces. Voting and details are [here](https://github.com/nexusformat/definitions/issues/791#issuecomment-707365329)

Note: we are not planning to change any existing definitions, this is just a recommendation for future definitions

## Reserving prefixes

NeXus currently reserves the NX prefix for official use, this avoids potential clashes with other names that may be used. It was discussed that certain other groups may also wish to reserve a specific prefix for use within their domain to help with management of their namespace. While the general idea and use case was supported, it should not lead to an effective separate definition space and groups should still put forward definitions to be included officially. See the [proposal vote](https://github.com/nexusformat/NIAC/issues/49#issuecomment-707383140) and the [initial list of prefixes to reserve](https://github.com/nexusformat/NIAC/issues/49#issuecomment-707383223)

There was discussion of the mechanism for how new prefixes should be added, and it was proposed that such additions could be done via a simple email vote without needing a 2/3 NIAC discussion first  

[issue link](https://github.com/nexusformat/NIAC/issues/49#issuecomment-707384329)


## Elect officers

Nominations are [listed here](https://github.com/nexusformat/NIAC/issues/70) for votes to be added
  
## PIDs for NeXus terminology

Heike Görzig gave a presentation of persistent identifiers (PIDs) and their relation to Findable, Accessible, Interoperable and Reusable (FAIR) data. 
There are more details [contained here](https://github.com/nexusformat/NIAC/issues/73) but the general idea was to use PIDs to attach meaning to specific terms
that may have a different names in different domains, reducing issues caused by different use or changes of vocabulary, and making the item
very easily machine locatable. So for example a 
PID could be assigned (via the NXDL) to an item in the nexus file, this allows that particular item to be identified however 
it may be named (or changed) in different definitions. There was general support for the idea and it was proposed to explore 
a prototype via a branch of the nexus definitions repository and then return to the NIAC later with a demonstration and proposal. 

[issue link](https://github.com/nexusformat/NIAC/issues/73#issuecomment-716609739)
  
  
## Constitution changes

The only matter discussed was the rules for making offical decisions at teleconference meetings, these had originally come from [discussions at NIAC 2018](https://www.nexusformat.org/NIAC2018Minutes.html#decision_voting). 
The 2018 proposal had been incorporated verbatim into the constitution pages on the web and it was agreed that some context and clarification 
should be added to the original wording, but the meaning should reflect intent of the 2018 decision. Both sets of wording for comparison are
described [on the ticket](https://github.com/nexusformat/NIAC/issues/71) along with the [voting link](https://github.com/nexusformat/NIAC/issues/71#issuecomment-716617317) 
The 2/3 quorum requirement was again discussed as a possible difficulty for further decisions before the next full NIAC meeting. BW suggested that it simply requires adequate advertisement and organisation for properly engaging the NIAC members. It was further raised that substantial changes to the voting rules should be carefully considered in order to not repeat the mistakes made in 2018.
   
## Using soft links rather than target attribute  

The NeXus API only uses hardlinks, in HDF4 they were the only option. As both linked items are indistinguishable, the target attribute was used to indicate the "interesting" end of the link. E.g. if you have linked the detector counts dataset inside an NXdetector into an NXdata you could use the target attribute to locate the NXdetector and hence further metadata about the counts. Without the target attribute, the only way you could locate the NXdetector source would be by examining object ids within the file to see whether they referred to the same dataset. HDF5 soft links are more like symbolic links in a unix filesystem, they contain the name of the item referenced (in fact pretty much what a target attribute would contain). So there is no need for a target attribute in this case. 
 
It was agreed to propose:

* Any type of link (Soft, Hard and External) is allowed.
* The use of the target attribute is optional when using soft links.

[issue link](https://github.com/nexusformat/NIAC/issues/77#issuecomment-716643766)

## nexusformat python package

RO gave a presentation on the [nexusformat python package](https://github.com/nexusformat/NIAC/issues/78) which provides a simpler interface to create nexus files. It was agreed that the NeXus manual should be updated to include examples using both h5py and nexusformat as solutions. It was noted that there is an old python binding included as part of the NAPI, any use of this should be removed from examples, and the future of the NAPI itself is the subject of a user consultation as described above. We thank RO for his work on NeXus over the years. 

## Adding globally unique identifier to NXentry

The issue was introduced by SC. There is currently an "entry_identifier" field for storing a unique identifier, but at BNL they would like to store two identifiers: a "scan id" for the entry and also an "entry uuid". There was discussion as to whether the scheme for uuid should be made available to all objects e.g. a "uuid" attribute, and also if "entry_identifier_uuid" could be a group attribute of NXentry rather than a field. There are potential complications that may arise due to linking, so the proposal is to add entry_identifier_uuid as an optional NXentry field and the uuid attribute to other fields/groups. The reserving of a BS_ or BLUESKY_ prefix was also discussed and added to the ticket.
      
[issue link](https://github.com/nexusformat/NIAC/issues/80#issuecomment-716662624)

## other items mentioned

* SC has been looking to get the NeXus API (NAPI) included with Fedora and RHEL, he will enquire as to the state of the Debian package
* PJ is planning to drop NXspecdata from the contributed definitions, he will send an email to the list
* We will have the next teleconference early December, doodle poll to follow

 
## Summary

All NIAC members are requested to please vote on [each proposal](https://www.nexusformat.org/NIAC2020.html#decisions) by 3rd November 2020. You can either:
* use thumbs up/down emoji to indicate yes/no, any other emoji to indicate abstention, on the tickets; or  
* reply to the email circulated to [nexus-committee](https://lists.nexusformat.org/pipermail/nexus-committee/2020/001026.html)

Feel free to continue discussion on the ticket and/or NeXus mailing list. 

Decisions are [listed here](https://www.nexusformat.org/NIAC2020.html#decisions), including links to the votes.
