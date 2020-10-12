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

Representating mathematical formulas in data files https://github.com/nexusformat/definitions/issues/711 was discussed, PC added an interesting new HDF5 approach https://github.com/lucasvr/hdf5-udf but HB raised concerns over its security model. AB will do further investigation of approaches.

There was some discussion about character encoding of strings, NeXus recommends UTF-8 (whihc is what h5py will use) but this is not enforced. The NAPI certainly doesn't enforce it. It was suggested cnxvalidate could raise a warnng if non-utf8 strings were detected, there is suport in HDF5 for specifying and checking a character encoding https://support.hdfgroup.org/HDF5/doc/Advanced/UsingUnicode/index.html 

