========================
NXdetector documentation
========================

There are some flaws in the documentation of NXdetector which we need fix

+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NXdetector field                 | comment                                                                                                                                                                                             |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| distance                         | The distance field still requires documentation                                                                                                                                                     |
| polar\_angle                     | I guess here we have a collision with the definition for the canonical 'polar\_angle' in the user manual. Despite this, the reference manual still mentions that this field requires documentation. |
| azimuthal\_angle                 | Same as for polar\_angle (collision with definition of canonical rotations as well as missing documentation)                                                                                        |
| dead\_time                       | which dead time. What does term refer to?                                                                                                                                                           |
| count\_time                      | what do we mean with count time. Is this the time the each pixel was exposed to radiation (or particles)?                                                                                           |
| acquisition\_mode                | this is somehow confusing: what is the difference between 'gated' and 'triggered'? Is 'event' not simply gated/triggered by an event? Why does this have its own mode?                              |
| angular\_calibration             | we should definitely provide a formula here which explains how to use this numbers? Is a single number per pixel really enough?                                                                     |
| countrate\_correction\_\_applied | are the two underscores a typo or have they been used intentionally? What exactly does this mean? Is this something we have introduced for DECTRIS?                                                 |
| frame\_time                      | here we should replace the term 'exposure\_time' with 'count\_time' to avoid confusion                                                                                                              |
| gain\_setting                    | I guess this is something we made for DECTRIS                                                                                                                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

In order to make things easier we should somehow agree on a coherent
naming scheme for time values (maybe provide some timing diagram).

Update 01/2015
--------------

The fields listed here have proper documentation now. INHO, this really
did not belong here but should rather have been an issue on github. But
may be it did not get enough love there.....