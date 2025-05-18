---
title: Multi Method Instruments
permalink: Multi_Method_Instruments.html
layout: wiki
---
Multi Method Instruments
========================

Multi Method Instruments
------------------------

This suggestion is one of the outcomes of the NeXus for Synchrotrons
Workshop at PSI: <http://lns00.psi.ch/nexus2010>

### The Suggestion

Add to NXentry a new class named NXsubentry which has the same structure
as NXentry. Each NXsubentry is to hold the data or links thereto of a
single application definition in a multi method instrument.

### The Reasoning

Synchrotron beamlines often utilise several different detectors and
detector types in order to combine multiple techniques in simultaneous
measurements. NeXus currently asks for separate NXentry groups to be
written for each technique. This is good if one measurement is written
to a file. However, there is a second requirement that multiple scans,
multiple measurements, possibly a whole log of an experimental session
is written to one NeXus file. Then having different techniques in
different NXentries will make the files difficult to understand as the
relationship between different measurements is lost. Thus, in order to
keep the data from these multiple techniques together, it is desirable
to have the ability to write it all into a single NXentry in a NeXus.
The current NeXus application definitions refer to the same names and
paths and so there are many name collisions when trying to satisfy two
application definitions in one NXentry in a file. The ability to combine
application definitions could be enabled by modifying the application
definitions to refer to new and separate groups inside the main NXentry
of the NeXus file that refer to the particular application/technique
name and which contains all of the data (or links to it) that is
relevant to that application/technique. For an example experiment that
involves a combination of SAS and Fluorescence, the proposed NeXus
structure could look like:


    entry:NXentry/
      definition = "NXSas, NXFluo"
      user:NXuser/
      sample:NXsamle/
      instrument:NXinstument/
        SASdet:NXdetector/
        fancyname:NXdetector/
        fancyname2:NXdetector/
        ...
      SAS:NXsubentry/
        definition = "NXSas"
        instrument:NXinstrument/
          detector:link to SASdet
        data:NXdata/
      Fluo:NXsubentry/
        definition = "NXFluo"
        instrument:NXinstrument/
          detector:link to fancyname
          detector2:link to fancyname2
        data:NXdata/

In the above NeXus tree, the entire beamline state could be stored in
entry/instrument and then any subset of this that is relevant to the SAS
or Fluorescence techniques would then be linked within the
entry/SAS/instrument and the entry/Fluo/instrument groups as defined by
the current application definitions with a minor change in the
heirarchy. The advantages of this approach are:

-   Only minor changes from current practice.
-   The only name collisions to worry about are the names of the
    applications/techniques themselves.
-   Application definitions need not be concerned with the names and
    paths that other application definitions proscribe.
-   The paths for each application remains well defined and an analysis
    program for either technique can find the relevant data without
    having to understand the other techniques present in the file.
    Further, the same analysis programs can read the multi-technique
    files in the same way (i.e. with the same code) exactly the same as
    they read single-technique files.
-   A user inspecting the data manually can find all the relevant
    information for a particular analysis in the one group and so
    doesn't need to understand the entire beamline.

One drawback of this approach is that the beamline staff would have to
define many links when configuring the data acquisition software.
However, this is necessary work regardless of how the data is saved
since the user must be informed of how the different instrument
components and detectors relate to the various analyses anyway. In fact,
NeXus and the above proposal simplifies this task by clearly documenting
in a formal manner where the relevant information can be read.

Some examples of beamlines that would benefit from this proposal
include:

-   Fluorescence + Absorption + Diffraction (Beamline L, Doris, Beamline
    P06, PETRA III).
-   PX + fluorescence: In PX often a fluorescence-signal is recorded,
    especially for SAD-/MAD-measurements (PETRA beamlines P11 P13 P14).
-   SAXS+fluorescence: fluorescence is often used as a second signal in
    SAXS (PETRA P03).
-   SAXS + ellipsometry: Beamline BW4, DORIS

Summarizing this discussion, the suggestion is to allow NXentry or
possibly new NXsubentry groups underneath NXentry. Each of which can
adhere to a different application definition. All participants agreed
that a good means of handling multi technique instruments in NeXus is
essential for the adoption of NeXus at synchrotron facilities. This is a
MUST HAVE!
