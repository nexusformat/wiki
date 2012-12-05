---
title: NXaperture and Slits
permalink: NXaperture_and_Slits/
layout: wiki
---

The actual *NXaperture* base class is far to complex for most of the
apertures used at synchrotron facilities. Currently the most commonly
used apperture types are

-   pinholes
-   2 or 4 blade slits.

From the current implementation of NXaperture it would be rather
difficult to obtain relevant quantities like the size of the slit gap or
the offsets of the gap. There are basically two ways how to face this
problem

-   redesign *NXaperture*
-   or introduce new classes for more specific aperture types.

Which of them is appropriate for us should be the topic of this
discussion.

Introducing new classes
-----------------------

#### Pinholes - *NXpinhole*

![c|A pinhold in the
beam.](Pinhole_2D.png "fig:c|A pinhold in the beam.") Pinholds are most
probably the simplest apertures available. The only parameter of
importance is the diameter of the pinhole and its position with respect
to the beam (as shown in the image). From this sketch one could easily
deduce a new class *NXpinhole* with the following parameters

    NXpinhole
      diameter:NX_FLOAT
      x_offset:NX_FLOAT
      y_offset:NX_FLOAT

The last two paramters determine the offset of the pinhole center to the
incident beam.

#### Slits - *NXslit*

![A four-blade slit in the
beam.](Slit_2d.png "fig:A four-blade slit in the beam.") Two or four
blade slits are the most common apertures used at synchrotrons. In this
example a 4-blade slit is shown. 2-blade slits could be realized easily
by simply omitting slits blades, offset-, and gap-parameters. A base
class *NXslit* could look like this

    NXslit
     x_gap:NX_FLOAT
     y_gap:NX_FLOAT
     x_offset:NX_FLOAT
     y_offset:NX_FLOAT
     top_blade:NX_FLOAT
     bottom_blade:NX_FLOAT
     right_blade:NX_FLOAT
     left_blade:NX_FLOAT

The last four parameters determine the positions of the slit blades.

#### What happens to *NXaperture*

The original *NXaperture* remains unchanged (for the sake of
compatability) and can still be used for all kind of more complex
apertures which cannot be represented by the the new classes.
