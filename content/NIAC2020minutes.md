## Session B

Present: HB, FA, PC, HG, PJ, MK, AB, BW, TM, SB, RO, AF

Upcoming issue assignment was reviewed, it was decided that the NXmx assignment should be moved to a major session but as there was time in this session it was started early.

MK queried the use of `NXdetector_group` and whether it should have a `depends_on` and ususal NeXus geometry based members. 
The use of `NXdetector_group`, `NXdetector_module` and `NXdetector` was discussed. The `NXdetector_group` class pre-dates `NXdetector_module`
and encompasses some of its functionality. In its original incantation it could both subdivide and group detectors, but with the addition 
of  `NXdetector_module` is make more sense only to group NXdetector objects. AB showed an example of how it is used in NXmx and it was decided 
that rewording the description to how it is being used was most appropriate. PJ created https://github.com/nexusformat/definitions/pull/802 
to cover the changes, BW suggested making it clear that use of `NXdetector_module` was optional but as SB pointed out we already use the work “optional” 
to mean specific things in definitions so have to be careful. As part of this the old wording “detector element” would be changed to just be “detector”. 
