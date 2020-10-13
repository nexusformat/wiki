---
title: NIAC 2020 Minutes
permalink: NIAC2020minutes.html
layout: wiki
---

## Session A

This was a pre-meeting to do initial setup for subsequence sessions, a brief review of whether items had been assigned to the correct sessions was carried out   

## Session B

Present: HB, FA, PC, HG, PJ, MK, AB, BW, TM, SB, RO, AF

Upcoming issue assignment was reviewed, it was decided that the `NXmx` discussion should be moved to a major session, but as there was time in this session it was started early.

MK queried the use of `NXdetector_group` and whether it should have a `depends_on` and ususal NeXus geometry based members. 
The use of `NXdetector_group`, `NXdetector_module` and `NXdetector` was discussed. The `NXdetector_group` class pre-dates `NXdetector_module`
and encompasses some of its functionality. In its original incantation it could both subdivide and group detectors, but with the addition 
of  `NXdetector_module` is make more sense only to group NXdetector objects. AB showed an example of how it is used in `NXmx` and it was decided 
that rewording the `NXdetector_module` description to how it is being used there was most appropriate. PJ created https://github.com/nexusformat/definitions/pull/802 
to cover the changes, BW suggested making it clear that use of `NXdetector_module` was optional but as SB pointed out we already use the work "optional" 
to mean specific things in definitions so have to be careful. As part of this the old wording "detector element" would be changed to just be "detector". 

## Session C

Present: HB FA SB HG AB PJ RO PC MK BW AS

The review of NXmx was completed. After checking the constitution, there were insufficent members present for a required 2/3 quorum so as per NIAC 2018 minutes there will be an email vote of the whoile NIAC. This will be achieved by members giving a thumbs up or thumbs down indication to relevant gitbub NIAC repository issues, a list of them to vote on will be send out post meeting. The changes to NXdetector_group are purely documentational so were passed by members present, this closed https://github.com/nexusformat/definitions/pull/802

There was a discussion arpound NXptychography, this mainly related to how th ebeam centre should be stored - in NXdetector or using NXtransformations. RO asked if there were any examples of NXtransformations, there are some details on the wiki https://manual.nexusformat.org/design.html#coordinate-transformations but MK will locate a previous presentation he did on the subject. PJ will take back a recommendation to the group for https://github.com/nexusformat/NIAC/issues/53 but further work may be done in the Code CAmp on clarifying the documentation. There is code available in the CBF library to do the necessary maths for transformations.    

Representing mathematical formulas in data files https://github.com/nexusformat/definitions/issues/711 was discussed, PC added an interesting new HDF5 approach https://github.com/lucasvr/hdf5-udf but HB raised concerns over its security model. AB will do further investigation of approaches.

There was some discussion about character encoding of strings, NeXus recommends UTF-8 (whihc is what h5py will use) but this is not enforced. The NAPI certainly doesn't enforce it. It was suggested cnxvalidate could raise a warnng if non-utf8 strings were detected, there is suport in HDF5 for specifying and checking a character encoding https://support.hdfgroup.org/HDF5/doc/Advanced/UsingUnicode/index.html 

## Session D

Present: HB FA RB PC PJ AB RO SB MK TM AS BW

The addition of a `creator_version` top klevel attribute was discussed and submitted for email voting https://github.com/nexusformat/NIAC/issues/51

Next clarifying of naming conventions https://github.com/nexusformat/NIAC/issues/47 was discussed. PJ summarised main items in https://github.com/nexusformat/definitions/issues/544 Part of the history of this is that keeping field/group names to valid variable name characters allowed easy "a.b.c.d" syntac in some scripting languages and RO mentioned attribute references and command line completion in Python. However dictionary based completion is now possible and HDF5 allows a wider range of charaters. It was decided that official names for groups and fields should reamin as ASCII with the original restrictions, but the regular expression used for user specified fields would be extended to allow decimal point and items starting with a number e.g. an NXentry called "1.1". The wider regular expression just covers when warnings are printed, NIAC is not restricting your naming of fields and groups for special facility and program usage. The regular expression code check will be updated in the upcoming code camp.

The next discussion was a recommendation for where suffixes such as "x" should go in field names. NeXus is no consistemt here e.g. "beam_centre_x" and "x_pixel_size". It was decided that "x" as a suffix was preferred, and will be receommended for new definitions (no changes to exiting definitions). The al;ernative is using and array/list was also mentioned e.g. using somethign like beam_centre[0] and beam_centre[1] instead of x and y. This arose from commanes in the NXdetector where the documentation in the NXDL header states that the i index is the x axis and the slowest varying. Given detectors can be in different orientations, it was decoided to remove the references to x and y in this header https://github.com/nexusformat/definitions/pull/804

The next discussion involved inconsistent symbol naming, as noted by RB https://github.com/nexusformat/definitions/issues/800 - these are names used in a definition to tie togther items with e.g. the same array length, they never appear in a data file. Across definitions there are mixtures of CamelCase v under_score and different names for "number of pixels". etc. It was agreed that standardising these would be good, and the change does not break any exisiting data files - it is purely an in definition tool.    

Reserved prefixes and suffixes were discussed next https://github.com/nexusformat/definitions/issues/769 - reserving "nx" for use by the NIAC is one long standing example, but other communities may wish to reserve a prefix/suffix too. A table will kept in the user manual detailing these and their owners, there will be a NIAC vote to approve the current list. It was also suggested that NIAC be asked to delegate additions (but not removals) to the table to Teleconference meetings. 






