---
title: ConcordanceDiscussion
permalink: ConcordanceDiscussion.html
layout: wiki
---
ConcordanceDiscussion
=====================

Concordance Summary
===================

Last update: July, 10, 2013, Mark Koennecke

This document summarizes the problems occurring when mapping CBF to
NeXus how I see them from the discussion with Herbert. In the following
discussion all groups which are not NeXus yet will be prefixed with TBD
for To Be Discussed. This is the version updated after the July, 10
teleconference.

Further details on [NeXus/HDF5/CBF
Integration](https://sites.google.com/site/nexuscbf/)

The Variant Issue
=================

CBF has the concept of variants for fields. For example there is a field
beam\_center\_x. This has somehow been determined and written to file.
Later this is refined in another way. CBF stores this then as
beam\_center\_x\_variant. This concept of variants is missing in NeXus.
Another way to understand this is to see it as a version control for
values. However, as this is rarely used, a complicated solution is not
desirable. Another requirement is that it must be possible to put
similar tags on variables which change at the same time.

So far there are three options to remedy this:

-   A TBDvariant group which can occur in all other groups and contains
    the variant values with the same field names as in the parent group.
    This is felt to be overkill.
-   Simply append \_variant to the existing NeXus name. If there is more
    then one variant append another qualifier to \_variant. For example:
    beam\_center\_x\_variant\_refined
-   As the request can rather be understood as a means to keep track of
    old versions of values, another option is this rule: When updating a
    value, update the value with the NeXus name. Store the old value in
    a new field labelled with nexusname\_old\_timestamp. Where nexusname
    is the original name of the field, for example beam\_center\_x, and
    timestamp is a: timestamp like 2013-05-23. Great care has to be
    taken to create a timestamp format which does not break the
    usability of the name as a field name in a programming language.
-   Another idea is to append \_var\_N where N is a number to the
    original NeXus field name and store the time stamp as an attribute
    to the field.
-   Yet another idea: do not create new fields but rather store the old
    values as variant attributes to the original field.

The Axisset Issue
=================

NeXus chooses to document axis names with a predefined meanings. The CBF
people learned that this did not work for them as people were using axes
differently, could not be bothered to even look which conventions others
used etc. Thus they choose rather to document axes by the way how they
operate. And a given component may even have more then one axes
description associated with it.

NeXus goes a long way to support this with the recently added offset,
type, vector and depends\_on attributes.

But mapping the full CBF scheme would require a TBDaxisset group which
can occur in any component which we care to place (sample, detector,...)
This group could look like this:

    TBDaxisset
       axis-name-or-id[NA]
       offset[3,NA]
       type[NA]
       vector[3,NA]
       depends_on[NA]

with NA being the number of axes.

I can see that such a scheme would also allow NeXus to neatly describe a
given data set in terms of different axis types: instrument coordinates,
q coordinates or whatever.

At the Telco the agreement was that the current NeXus scheme is
sufficient to do the CBF mapping. But for further use, it might be a
good idea to reserve the namespace for axisset. It was also felt that
there to many ways to describe axes in NeXus and we should discuss and
aggree on a preferred way to do axes in an upcoming NIAC meeting.

The Scan Issue
==============

NeXus chooses to store scans as it is done, with the positions of
components as read from the hardware in arrays. CBF chooses to rather
store the intent of the scan: i.e. the axis moved, their start and
increments etc. NeXus lacks such a intent description. This already
caused us problems because the intent axes are nice for plotting and the
actual positions as read are necessary for detailed DA.

Thus to capture the CBF description a new group may be required:

    TBDscan_intent
       axis-name-or-id[NSA]
       start[NSA]
       increment[NSA]
       NP

with NSA being the Number of Scan Axes and NP the number of points in
the scan. May be some more fields.

The agreement on the NeXus Telco was that the recently aggreed upon axes
scheme with the attributes on the NX group is sufficient to do the CBF
mapping. Again, it might be worth to reserve the namespace.

New Fields
==========

This may be a bit easier: the CBF mapping asks for a couple of fields to
be added to the NeXus base classes:

    NXxray_tube
       radiation_type         
       radiation_xray_symbol

Radiation\_type is different to probe. Probe gives a very general
description like neutrons, x-ray etc. This gives the type of radiation
like Cu Kalpha, Mo etc. The situation is further complicated by the fact
that even at synchrotrons wavelengths are selected which match the
characteristics of well known x-ray tube anode materials. Thus, a
NXxray\_tube group may not be the appropriate place.

    NXcollimator
       div_x_y_source
       radiation_filter_edge    # May belong into a NXfilter
       radiation_inhomegeneity  # May belong into NXsource or NXmonochromator

CBF stores polarisation information of the beam in NXmonochromator. It
is an open question where this belongs: NXbeam, NXpolariser or
NXmonochromator being candidates. The fields:

    polarisation_norm
    polarisation_ratio
    polarisation_source_norm
    polarisation_source_ratio

    NXdetector
      gain
      gain_esd
      linerarity
      offset
      scaling
      overload
      undefined_value

Some of these fields address the computed data value issue which we
discussed some time ago. The last state on this was that Armando was to
make a proposal for calculated data. Which, as far as I am aware, did
not happen.

CBF also has a structure to describe the elements of a multi component
detector. We discussed something similar recently with the DECTRIS
module . This was then added a s a non NeXus standard group. May be we
need to revise this with input from CBF?

The good news is that the proposed fields come with documentation which
we may directly copy from the CBF documents.

NXgoniometer
============

Consider the situaton when a sample is mounted on some sort of
positioning device: x-y tables, eulerian cradle goniometer or such. The
current NeXus convention is to store the values coming from such
positioning devices in the NXsample group. The rationale is that their
purpose is to position the sample. Now, the suggestion is to separate
such values out into a NXgoniometer group. This unloads the sample group
somewhat and makes for a cleaner separation. Where in the NeXus
hierarchy a NXgoniometer will be positioned is another question to be
discussed: NXsample or NXinstrument both being good candidates.
