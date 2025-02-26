==========================
Associating Axes with Data
==========================

Associating Axes with Data
--------------------------

The current scheme we use in NeXus for associating axes with data was mainly devised as a means to work around a
limitation of HDF-4. Namely the fact that there was one global namespace for dimension scales. Dimension scales are
HDF's way of associating axes with data by storing them as properties of the data. Now, this limitation of HDF has
since long fallen. Moreover, there are a number of use cases which are not well covered by what we do today. Thus,
this page describes how to improve. Discussion comments should be placed on the discussion page.

### Requirements

This is a recapitulation of what we have to achieve for a multidimensional dataset:
- The axes give a plot meaning.
- For data reduction or analysis, we need to know exactly how data was measured in either the instrument or another
coordinate system.
- There may be different sets of axes for the same data in different coordinate schemes. An example: raw time of flight
binning versus the same axis converted to energy transfer or d-spacing.
- With multidimensional scans, we may have scan intent axes (describing how the scan was planned) and axes describing
what really happened. Giving motor readbacks for each motor for each point in the multidimensional dataset. This
situation can cause multiple axis fields for the data, one for each variable varied in the multidimensional scan.
- Axes may or may not be regular.

Solution
--------

See 2014_axes_and_uncertainties. This proposal has been accepted by NIAC at NIAC 2014 with a few modifications. There
is still some resistance to the new scheme, thus this page stays in place. This update: 01/2015