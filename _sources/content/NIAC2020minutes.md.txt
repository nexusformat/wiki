---
title: NIAC 2020 Minutes
permalink: NIAC2020minutes.html
layout: wiki
---
NIAC 2020 Minutes
=================

## Session A

This was a pre-meeting to do initial setup for subsequence sessions, a brief review of whether items had been assigned to the correct sessions was carried out   

## Session B

Present: HB, FA, PC, HG, PJ, MK, AB, BW, TM, SB, RO, AF

Upcoming issue assignment was reviewed, it was decided that the `NXmx` discussion should be moved to a major session, but as there was time in this session it was started early.

MK queried the use of `NXdetector_group` and whether it should have a `depends_on` and ususal NeXus geometry based members. 
The use of `NXdetector_group`, `NXdetector_module` and `NXdetector` was discussed. The `NXdetector_group` class pre-dates `NXdetector_module`
and encompasses some of its functionality. In its original incantation it could both subdivide and group detectors, but with the addition 
of  `NXdetector_module` is make more sense only to group NXdetector objects. AB showed an example of how it is used in `NXmx` and it was decided 
that rewording the `NXdetector_module` description to how it is being used there was most appropriate. PJ created [PR#802](https://github.com/nexusformat/definitions/pull/802) to cover the changes, BW suggested making it clear that use of `NXdetector_module` was optional but as SB pointed out we already use the work "optional" 
to mean specific things in definitions so have to be careful. As part of this the old wording "detector element" would be changed to just be "detector". 

## Session C

Present: HB FA SB HG AB PJ RO PC MK BW AS

The review of `NXmx` was completed. After checking the constitution, there were insufficent members present for a required 2/3 quorum so as per NIAC 2018 minutes there will be an email vote of the whoile NIAC. This will be achieved by members giving a thumbs up or thumbs down indication to relevant gitbub NIAC repository issues, a list of them to vote on will be send out post meeting. The changes to NXdetector_group are purely documentational so were passed by members present, this closed [PR#802](https://github.com/nexusformat/definitions/pull/802).

There was a discussion around `NXptychography`, this mainly related to how the beam centre should be stored - in `NXdetector` or using `NXtransformations`. RO asked if there were any examples of `NXtransformations`, there are some details on the [wiki](https://manual.nexusformat.org/design.html#coordinate-transformations) but MK will locate a previous presentation he did on the subject. PJ will take back a recommendation to the group for [issue#53](https://github.com/nexusformat/NIAC/issues/53) but further work may be done in the Code Camp on clarifying the documentation. There is code available in the CBF library to do the necessary maths for transformations.    

Representing [mathematical formulas in data files](https://github.com/nexusformat/definitions/issues/711) was discussed, PC added an interesting new [HDF5 approach](https://github.com/lucasvr/hdf5-udf) but HB raised concerns over its security model. AB will do further investigation of approaches.

There was some discussion about character encoding of strings, NeXus recommends UTF-8 (which is what h5py will use) but this is not enforced. The NAPI certainly doesn't enforce it. It was suggested cnxvalidate could raise a warnng if non-utf8 strings were detected, there is suport in HDF5 for [specifying and checking a character encoding](https://support.hdfgroup.org/HDF5/doc/Advanced/UsingUnicode/index.html). 

## Session D

Present: HB FA RB PC PJ AB RO SB MK TM AS BW

The addition of a `creator_version` top level attribute was discussed and submitted for [email voting](https://github.com/nexusformat/NIAC/issues/51).

Next, clarifying of [naming conventions](https://github.com/nexusformat/NIAC/issues/47) was discussed. PJ summarised main items in [issue#544](https://github.com/nexusformat/definitions/issues/544). Part of the history of this is that keeping field/group names to valid variable name characters allowed easy "a.b.c.d" syntax in some scripting languages and RO mentioned attribute references and command line completion in Python. However dictionary based completion is now possible and HDF5 allows a wider range of charaters. It was decided that official names for groups and fields should reamin as ASCII with the original restrictions, but the regular expression used for user specified fields would be extended to allow decimal point and items starting with a number e.g. an `NXentry` called "1.1". The wider regular expression just covers when warnings are printed, NIAC is not restricting your naming of fields and groups for special facility and program usage. The regular expression code check will be updated in the upcoming code camp.

The next discussion was a recommendation for where dimension information such as "x" should go in field names. NeXus is not consistent here e.g. "beam_centre_x" and "x_pixel_size". It was decided that "x" as a suffix was preferred, and will be recommended for new definitions (no changes to exiting definitions). The alternative of using an array/list was also mentioned e.g. using somethign like beam_centre[0] and beam_centre[1] instead of beam_centre_x and beam_centre_y. This arose from comments on the `NXdetector` where the documentation in the NXDL header states that the i index is the x axis and the slowest varying. Given detectors can be in different orientations, it was decided to [remove the references to x and y in this header](https://github.com/nexusformat/definitions/pull/804).

The next discussion involved inconsistent symbol naming, as noted by RB in [issue#802](https://github.com/nexusformat/definitions/issues/800) - these are names used in a definition to tie togther items with e.g. the same array length, they never appear in a data file. Across definitions there are mixtures of CamelCase v under_score and different names for "number of pixels". etc. It was agreed that standardising these would be good, and the change does not break any exisiting data files - it is purely an in-definition tool.    

[Reserved prefixes and suffixes](https://github.com/nexusformat/definitions/issues/769) were discussed next - reserving "nx" for use by the NIAC is one long standing example, but other communities may wish to reserve a prefix/suffix too. If approved by NIAC vote, a table will kept in the user manual detailing these and their owners, there will be a NIAC vote to approve the current list. It was also suggested that NIAC be asked to delegate additions (but not removals) to the table to Teleconference meetings. 

## Sessions E

did not take place

## Session F

did not take place

## Session G

Present: BW FA MK HG HN PJ PC RO SB AB TM RB

Discussed the [use of NX_DATE_TIME rather than NX_CHAR for file_time and file_update_time in NXroot](https://github.com/nexusformat/NIAC/issues/68). NeXus has always said to use ISO8601 for datetime, so this is just bringing the definition in line with the manual. Change was merged as effectively updating documentation. There was a discussion about timezones, which are not mandatory in ISO8601 - if none are specified local time is assumed. It was agreed to update the manual to say that supplying a timezone was recommended, this avoids issues if e.g. daylight saving time changes during an experiment. 

For the election of officers, names will be added to a [wiki page](https://github.com/nexusformat/NIAC/issues/70) for emoji based voting. A note would be sent to the NIAC, and additional names can be added during the time window.  A doodle poll will be created by BW and circulated to NIAC members for the date of a NIAC summary meeting, this will repalce the final summary session I of the current NIAC. The election of officers will be completed at this additional NIAC meeting, which will also summarise the NIAC and CodeCamp. There was a brief discussion about whether to merge the documentation release and technical release manager roles, since we are not making many releasees of the NAPI these days. It was decided to defer this to the next NIAC.  

In [isse#71](https://github.com/nexusformat/NIAC/issues/71) MK pointed put that guidelines agreed at NIAC 2018 concerning online voting and teleconference voting had not yet been added to the NIAC constitution. Action to add these. We have been considering the NIAC as a "teleconference" with regard to these guidelines. 

It was agreed to move [issue#48](https://github.com/nexusformat/NIAC/issues/48) (improvemnts to NXdata) to a later session

[Specifying precision in nexus files](https://github.com/nexusformat/NIAC/issues/69) has already been actioned and the underlying ticket closed, so no further NIAC discussion is required.

The [future of the NeXus C API (NAPI) was discussed](https://github.com/nexusformat/NIAC/issues/64) MK gave a brief overview of the history of the interface and how it simplified the generation of files when HDF4 was the main format. This library has been marked as bugfix only in the documentation, and there are some outstanding issues and pull requests to fix. Some of the issues related to incompatibilities with newer versions of packages such as MXML, and potentially HDF5 1.12  It was agreed that MK and FA would consult the nexus mailing list as to their usage and of NAPI, it may be possible to drop support for e.g. HDF4 or XML from NAPI that would aid future maintenance. RO mentioned that the examples in the user manual use the NAPI a lot. It was agreed the code camp should also revisit the examples in the user manual and makle sure it is clear that NAPI is receiving minimal support and provide equivalent HDF5 native API c/c++ examples. We should also update examples generating or referring to HDF4 in the manual, it should only be referenced in the history section. HB pointed out that HDF4 is only minimally supported by the HDF group.  


## Session H

RO gave an introduction to the nexusformat python package as part of [issue#43](https://github.com/nexusformat/NIAC/issues/43) it is a wrapper around h5py that provides a simpler interface, making the generation of NeXus files easier and less error prone for a new user. Being NeXus aware, it can handle axis attributes and conventions for you, add correct class attributes, string encoding. There is also a fully featured GUI NeXpy (which is NXDL aware) built on top of nexusformat, but the discussion here was concerning just the nexusformat package. 

Several members present, in particular AB and RB, were interested in investigaing its usage on future upcoming projects, but many people present had already invested heavily in h5py based approaches. It was agreed that the NeXus manual examples should be updated to show how to read/write files using both nexusformat and h5py, the simpler interface of nexusformat could be useful to many users. The example updating will be done at the upcoming code camp. BW also noted that the package is not mentioned on the nexus utilities page and will be added there too.   

An application definition that shows [mixed use of `NXreflections` and `NXmx`](https://github.com/nexusformat/NIAC/issues/54) was discussed next. Some issues arise that are realted to `NXmx` being an application definition and `NXreflections` being a base class. There was discussion as to whether an `NXprocess` in a separate `NXentry` or new application definition was appropriate. In effect `NXmx` is thge raw data, there can be many instances of `NXreflection` showing iterations of the data processing. This will be discussed more at code camp.

The [changes to `NXdata`](https://github.com/nexusformat/NIAC/issues/48) were briefly reviewed, the changes were mostly to wording and looked fair, but it was difficult to be sure as there were merge conflicts due to the age of the branch. It was agreed that the branch would be rebased back onto master and the changes reviews at code camp. 

BW will create a poll for a final NIAC session date and send to the mailing list, all voting will be left open until that session, which will be towards the end of October.  

## Session I

This was the final scheduled session, but was purely for summing up. It has been posponed to a later date in October, with date determined by poll to the nexus committee list. 
