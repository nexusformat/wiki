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

As there were not many members present it was decided to adjourn early and return in the afternoon to discuss matters

### Session B

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

## Session C

Present: AB, FA, SB, RO, PJ, LG, BW, RB, PC, MK, PC, HB, HG, WDN, CZ

As this was a larger group with some new people, BW summariesed use of the [project board](https://github.com/orgs/nexusformat/projects/2/views/1) and people taking ownership of issues to champion. 

RO mentioned he had a PR about changes to documentation and asked if it needed a vote? BW confirmed that if it did not change how files were written (i.e. was e.g. clarification) then it did not need NIAC and could just go via normal PR approval. 

It was discussed when to have a session to elect officers, later in the day looked better for best attendance due to time zones. The third session on Thursday (session F) was agreed.

SB introduced [symbols to be connected to Field values](https://github.com/nexusformat/NIAC/issues/141) Symbols are used in definitions as placeholders for values and allow you to indicate that two arrays must have the same (or a related) size. Symbols themselves are, however, not explicitly documented and a new symbol cannot be defined in terms of existing symbols. The proposal was for a symbols table that would allow both. The NIAC likes the ideas put forward here and encourages preparatation of a more complete proposal.

As an offshoot of this, use of math within a nexus definition of file was discussed. For the general case, a machine parsable syntax would need to be chosen - HB suggested Javascript might be a good one. As this point math was only being considered for dimension attributes, and the math is contained in the NXDL. AB mentioned [math support in nexus](https://github.com/nexusformat/definitions/issues/711)    which is having math applied in the NeXus file during reading, which has potential security issues if an arbitrary equation is allowed leading to a denial of service attack. However it was pointed out that reading an extremely large dataset in an incorrect way can lead to such a thing anyway! It was discussed if a simpler set of operations rather than full equations could be used, but in this case the equation is quite complex. WDN mentioned [HDF5 UDF](https://hdf5-udf.readthedocs.io/en/latest/) which is an interesting option but this would tie nexus to HDF5. HDF5 UDF also has security issues. PC asked if there was a determined list of approved expressions would that give AB, HB what they need? SB suggested that there be a table called expressions similar to a symbols table, the NXentry would allow expressions to be defined by an applpication definition with the burden of security executing the expresion falling on the community that is supporting the application definition. PJ thinks that the point of NEXUS is to provide data, not data processing. AB said that at the moment the data isnt 100% useful without the processing so it would be great to find a solution to this.

WDN introduced [NXdata: errors on auxiliary signals](https://github.com/nexusformat/definitions/issues/1044) which was to allow use of `VARIABLE_errors` on additional signal arrays, it is currently allowed on axes and the main signal array. NIAC agrees that this is just a documentation bug that should be fixed. Also the `errors` field was already decided to be deprecated in 2018, this was just not yet actioned.

There was a rediscusison of [Support for non-dimensional coordinates in NXdata](https://github.com/nexusformat/NIAC/issues/139) introduced by SB as RO was now present. RO and WDN has been doing something similar using transformation matrices for the axes, so it will be considereded if allowing the addition of a transformatioin matrix to the dataset would be able t solve the use case. PC requests that there be a human readable field added to the documentation.

AB introduced [Flux changes for NXmx](https://github.com/nexusformat/definitions/pull/1035). The NIAC agreed that this did not need to wait for [Can we have a standard rule in NeXus to validate presence of one item from a list of possibles](https://github.com/nexusformat/definitions/issues/1002) to be resolved and could be voted on and merged. The outstanding ticket referred to being able to specify that one of: flux, total_flux, flux_integrated, total_flux_integrated being present, which is currently not a rule available in NDXL. It is not possible just to use an enum for these option as one can refer to an external arbitrary named NXmonitor. 




