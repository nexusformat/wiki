---
title: NIAC2022 Minutes
permalink: NIAC2022_minutes.html
layout: wiki
---

## NIAC2022 Minutes

### Session A

Present: BW, FA, PJ, LG, HG, SB, MK (Markus Kuhbach), RB, PC, SS (Sherjeel Shabih), AP (Allan Pinto), PM (Paolo Baraldi Mausbach)

BW began by summarising the meeting, and then there was a round of introductions as new people were present. As well as NIAC members, there were some observers from the Brazilian Synchrotron Light Laboratory (LNLS) and other facilities. AP mentioned that he had planned meeting with Diaomond and ESRF and was interested in learning more about NeXus, it was suggested that the monthly NeXus teleconferences would be good from this perspective. They are listed on the [Teleconferences]( https://www.nexusformat.org/Teleconferences.html) page and to be notified of their dates you can join the [nexus-tech](https://lists.nexusformat.org/mailman/listinfo/nexus-tech) mailing list. There is also the [nexus manual](https://manual.nexusformat.org/user_manual.html)

The list of items to discuss is kept as a [github project](https://github.com/orgs/nexusformat/projects/2) and the committee then took some time to look through the list and decide on who should represent a given issue at this or a future session.  

As there were not many members present it was decided to adjourn early and return in thew afternoon to discuss matters

### Session B

Present: HG, FA, WDN, SB, PJ, MarkuK, BW, PC, LG, TM, HB, CZ, MarkK

As many people were remote, voting on issues would be via thumbs up or down attached to a voting comment on a ticket

SB introduced [supporting the recommended property for Attributes](https://github.com/nexusformat/NIAC/issues/140) 
PJ asked if there was any python code to render this this change yet, SB said that was in progress but the change did not break any existing documentation generation.
It was proposed to  allow the "recommended" property (to complement "optional" which can be true or false) to be applied to attributes. This "recommended" property has already been approved for fields and groups, so this will just make attributes more consistent. VOTE: approved
 
PJ commented that in general it was good if people selected nexusformat/developers in teh reviewer of tickets/PRs as we require one review.

SB then introduced [Allow NXdata dimension variables to contain a list of strings](https://github.com/nexusformat/NIAC/issues/97) currently only NX_NUMBER data is allowed in axes, the change was to allow NX_CHAR too so e.g. channel names could be used as an axis for data. VOTE: approved 

SB then introduced [Support for non-dimensional coordinates in NXdata](https://github.com/nexusformat/NIAC/issues/139) which intends to introduce virtual axes, which are like the [non-dimensional coordinates of the python xarrays package](https://docs.xarray.dev/en/stable/user-guide/terminology.html?highlight=non%20dimensional#term-Non-dimension-coordinate). BW wondered if this was adding too specialist and adding too much complexity? SB mentioned that a separate NXdata of rearranged data could be created to acheieve the same result, but that would be duplicating data. WDN suggested that this could aslo be achieved by flattening the axis data and linking via a virtual dataset, he posted an example on the ticket.     VOTE: it was decided not to propose this feature for NeXus at this time

SB introduced [NeXus Ontology v2](https://github.com/nexusformat/NIAC/issues/136) The NIAC welcomed the update and unanimously supports the initiative and continuing work. PJ asked if this could be made more visible? HG said that she would be working with Steve Collins shortly to get things hosted via PURL with the new `nexus-purl` email address as the keeper.  

SB introduced [Group referencing an Application Definition](https://github.com/nexusformat/NIAC/issues/138) this listed three approaches to ther problem of a complex meaurement where you would like to apply validation to a set of entries. There was discussion about this, `NXsubentry` was mentioend but this normally applies to multiple simultaneous techniques (multi modal) as opposed to a sequence of techniques. NeXus currently treates each NXentry as validated separately, so a prescribed sequence of NXentry is not validated. WDN proposed a subentry stucture that may be appriopriate on the ticket, SB will consider this and bring back and examplefor further discussion as appropriate. HG mentioned the use of sequence_index in NXprocess that might provide some mechanism. VOTE: deferred

SB introduced [base classes always extend NXobject. Can a base class extend another base class?](https://github.com/nexusformat/NIAC/issues/135) The NIAC has traditionally avoided too much interitance in base classes to limit complexity, base classes are generally dictionaries.Such a change would also require a validator to follow the relationships.  


