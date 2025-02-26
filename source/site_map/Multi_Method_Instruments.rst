========================
Multi-Method Instruments
========================

This suggestion is one of the outcomes of the NeXus for Synchrotrons Workshop at PSI:

### The Suggestion

Add to `NXentry` a new class named `NXsubentry`, which has the same structure as `NXentry`. Each `NXsubentry` is to
hold the data or links thereto of a single application definition in a multi-method instrument.

### The Reasoning

Synchrotron beamlines often utilize several different detectors and detector types to combine multiple techniques in
simultaneous measurements. NeXus currently asks for separate `NXentry` groups to be written for each technique.
This works well if one measurement is written to a file. However, there is a second requirement: multiple scans,
multiple measurements, or even a whole log of an experimental session must sometimes be written to one NeXus file.
In such cases, having different techniques in separate `NXentry` groups makes the files difficult to understand, as
the relationship between different measurements is lost.

To address this issue and keep data from these multiple techniques together, it is desirable to write all data into a
single `NXentry` in a NeXus file. Currently, NeXus application definitions refer to the same names and paths, leading
to many name collisions when trying to satisfy two application definitions in one `NXentry` in a file.

The ability to combine application definitions could be enabled by modifying the application definitions to refer to
new and separate groups inside the main `NXentry` of the NeXus file. These groups would be named after the particular
application/technique and would contain all the data (or links to it) relevant to that application/technique.

For an example experiment that involves a combination of SAS and Fluorescence, the proposed NeXus structure could look like:

.. code-block:: xml

    <entry type="NXentry">
      <definition>NXSas, NXFluo</definition>
      <user type="NXuser" />
      <sample type="NXsample" />
      <instrument type="NXinstrument">
        <SASdet type="NXdetector" />
        <fancyname type="NXdetector" />
        <fancyname2 type="NXdetector" />
        <!-- Additional detectors can be added here -->
      </instrument>
      <SAS type="NXsubentry">
        <definition>NXSas</definition>
        <instrument type="NXinstrument">
          <detector link="SASdet" />
        </instrument>
        <data type="NXdata" />
      </SAS>
      <Fluo type="NXsubentry">
        <definition>NXFluo</definition>
        <instrument type="NXinstrument">
          <detector link="fancyname" />
          <detector2 link="fancyname2" />
        </instrument>
        <data type="NXdata" />
      </Fluo>
    </entry>

In the above NeXus tree, the entire beamline state could be stored in
``entry/instrument`` and then any subset of this that is relevant to the SAS
or Fluorescence techniques would then be linked within the
``entry/SAS/instrument`` and the ``entry/Fluo/instrument`` groups as defined
by the current application definitions with a minor change in the hierarchy.

The advantages of this approach are:

- Only minor changes from current practice.
- The only name collisions to worry about are the names of the applications/techniques themselves.
- Application definitions need not be concerned with the names and paths that other application definitions proscribe.
- The paths for each application remain well-defined, and an analysis program for either technique can find the relevant data without having to understand the other techniques present in the file. Further, the same analysis programs can read the multi-technique files in the same way (i.e., with the same code) exactly the same as they read single-technique files.
- A user inspecting the data manually can find all the relevant information for a particular analysis in one group and so doesn't need to understand the entire beamline.

One drawback of this approach is that the beamline staff would have to define many links when configuring the data acquisition software. However, this is necessary work regardless of how the data is saved since the user must be informed of how the different instrument components and detectors relate to the various analyses anyway. In fact, NeXus and the above proposal simplify this task by clearly documenting in a formal manner where the relevant information can be read.

Some examples of beamlines that would benefit from this proposal include:

- **Fluorescence + Absorption + Diffraction:** Beamline L, Doris, Beamline P06, PETRA III.
- **PX + Fluorescence:** In PX, a fluorescence signal is often recorded, especially for SAD-/MAD-measurements (PETRA beamlines P11, P13, P14).
- **SAXS + Fluorescence:** Fluorescence is often used as a secondary signal in SAXS (PETRA P03).
- **SAXS + Ellipsometry:** Beamline BW4, DORIS.

Summarizing this discussion, the suggestion is to allow ``NXentry`` or possibly new
``NXsubentry`` groups underneath ``NXentry``, each of which can adhere to a
different application definition. All participants agreed that a good means of
handling multi-technique instruments in NeXus is essential for the adoption of
NeXus at synchrotron facilities. **This is a MUST HAVE!**

