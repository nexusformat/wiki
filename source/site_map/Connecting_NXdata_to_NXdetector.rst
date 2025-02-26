Connecting NXdata to NXdetector
===============================

This is an attempt to summarize the various proposals that have been
discussed on this page. Proposal 1 is, I believe (Ray Osborn <UserRay_Osborn.html>), the original proposal when NeXus
was first designed (although we didn't link the data item itself as
Freddie has sensibly suggested). If anyone thinks that the remaining
proposals have been incorrectly summarized, please let the NeXus
committee mailing list know as soon as possible.

Proposal 1
----------

All the items within an NXdata group (data, errors, and axes) are stored
as links to parent items stored in their logical location (NXdetector,
NXsample, etc). The absolute address of the parent item is stored as an
attribute on the data, so that other information can be conveniently
located. This is the only proposal that addresses the issue of
non-NXdetector axes.

This method implies a one-to-one correspondence of NXdata and NXdetector
groups; the names do not need to match, though they could.

Example::

    <NXsample>
       <magnetic_field link="entry/sample">
    </NXsample>
    <NXinstrument>
       <NXdetector>
          <data axes="time_of_flight:magnetic_field" link="/entry/instrument/detector">
          <time_of_flight link="entry/instrument/detector">
       </NXdetector>
    </NXinstrument>
    <NXdata>
       <data axes="time_of_flight:magnetic_field" link="/entry/instrument/detector">
       <time_of_flight link="entry/instrument/detector">
       <magnetic_field link="entry/sample">
    </NXdata>

Proposal 2
----------

There is a one-to-one correspondence between NXdata groups and the
corresponding NXdetector group, which should have the same name to
provide a logical association.

Example::

    <NXinstrument>
       <NXdetector name="Bank1">
          <data axes="polar_angle:time_of_flight">
          <time_of_flight>
          <polar_angle>
       </NXdetector>
       <NXdetector name="Bank2">
          <data axes="polar_angle:time_of_flight">
          <time_of_flight>
          <polar_angle>
       </NXdetector>
    </NXinstrument>
    <NXdata name="Bank1">
       <data axes="polar_angle:time_of_flight">
       <time_of_flight>
       <polar_angle>
    </NXdata>
    <NXdata name="Bank2">
       <data axes="polar_angle:time_of_flight">
       <time_of_flight>
       <polar_angle>
    </NXdata>

Proposal 3
----------

There is a one-to-one correspondence between NXdata groups and the
corresponding NXdetector group. The NXdata group is stored within its
respective NXdetector group and linked to the NXentry.

Example::

    <NXinstrument>
       <NXdetector>
          <NXdata>
             <data axes="polar_angle:time_of_flight">
             <time_of_flight>
             <polar_angle>
          </NXdata>
       </NXdetector>
    </NXinstrument>
    <NXdata (link only)::
       <data axes="polar_angle:time_of_flight">
       <time_of_flight>
       <polar_angle>
    </NXdata>

Proposal 4
----------

There can be multiple NXdata groups for a single NXdetector group or
multiple NXdetector groups for a single NXdata item (e.g. to cope with
groups of different types of detectors). Detector ID's are used to
provide the link between the two.

Example::

    <NXinstrument>
       <NXdetector>
          <detector(1:N)>
          <polar_angle(1:N)>
       </NXdetector>
    </NXinstrument>
    <NXdata name="Bank1">
       <data(1:i) axes="detector">
       <detector(1:i)>
    </NXdata>
    <NXdata name="Bank2">
       <data(i+1:N) axes="detector">
       <detector(i+1:N)>
    </NXdata>

or::

    <NXinstrument>
       <NXdetector name="Bank1">
          <detector(1:i)>
          <polar_angle(1:i)>
       </NXdetector>
       <NXdetector name="Bank2">
          <detector(i+1:N)>
          <polar_angle(i+1:N)>
       </NXdetector>
    </NXinstrument>
    <NXdata>
       <data(1:N) axes="detector">
      (1:N)>
    </NXdata>

Criteria of a Good Solution
---------------------------

A proper solution should address the following:

- Linking - should it be used as a method of saving space or carry
  relational information (associating things).
- Grouping information into NXdetectors in a logical manner. For
  example, an instrument may want to have a NXdetector for each bank,
  or one for each panel, irrespective of how the NXdata is grouped.
- NXdata must be rectangular ( lxm or lxmxn) so data that would be
  grouped together in the analysis needs to be split up to conform to
  the standard. How should the data be associated with each other.
- How do you properly deal with multi-dimensional detectors, i.e.
  single ended tubes AND linear position sensitive detectors AND area
  detectors all used in the same measurement.

Update 01/2015
--------------

This page is very old. I cannot remember that this has been decided
upon. The current usage though is along the lines of proposal 2:
Multiple detectors give rise to multiple NXdetector and NXdata groups
with preferably the same name. NXdata is supposed to contain links to
the relevant data items required for a default plot. There can be
additional NXdata groups for special purposes. See also the description
of NXsubentry in the NeXus manual.

The above is valid for raw data NeXus files. In processed data NeXus
files NXdata has a different meaning and contains the actual resulting
processed data.