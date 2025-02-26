==================
Archive Definition
==================

Introduction
------------

The **NeXus Archive Definition** proposal is similar to an **Instrument Definition** but describes the required information for NeXus files intended for central archival. It includes essential information not found in the instrument definition, as it is not required for data analysis.

The Instrument Definitions should enable the creation of archiving software shared among multiple instruments or facilities. The Archive Definition aims to facilitate shared data management tools and emphasizes information useful for data search and retrieval from the archive. The Instrument Definitions and Archive Definition are complementary and do not interfere with each other.

For data analysis, information such as the data owner's name or the sample's name is not necessary. However, before archiving and indexing data, it is essential to define the granularity for indexing. While HDF5 allows extracting a single group from a file in an SRB system, cataloging data at such a fine level may not be practical at a facility level. This definition assumes indexing occurs at the file level.

Optional parameters are provided for highly recommended but not required information. The definition is primarily designed for **RAW files**, though additional parameters may be necessary for **processed/result** or **simulation files**.

Multiple NXentry Issue
----------------------

A NeXus file may contain several NXentry groups, each requiring separate indexing. However, not all NXentry groups need to be indexed. For instance, one entry may contain event data while another holds histograms for the same measurement.

- NXentry groups requiring indexing will have the attribute `index="yes"`.
- NXentry groups not requiring indexing will have `index="no"`.
- Non-indexed NXentry groups can be associated with an indexed NXentry group using the attribute `index_group`.

If there is only one NXentry group, or if all metadata are identical across entries, the `index` or `index_group` attribute is unnecessary.

Parameter Names
---------------

When extracting metadata, users are not limited to the parameters listed here. Facility, instrument, or sample-specific information may also be extracted.

Descriptive and consistently meaningful parameter names are preferable. For example, use `temp_control` and `temp_sample` rather than `temp_1` and `temp_2`, which may vary in meaning across experiments.

Too Much Metadata Is Better Than Too Little
-------------------------------------------

Missing information cannot be extracted later. Providing as much metadata as possible ensures future usability.

DTD Definition
--------------

- `{Extended title for file}`
- `{Unique identifier for the experiment, defined by the facility, possibly linked to proposals (see: proposal_identifier below)}`
- `{Brief summary of the experiment, including key objectives.}`
- `{Description of the full experiment (document in PDF, LaTeX, etc.)}?`
- `{User or Data Acquisition-defined group of NeXus files or NXentry}?`
- `{Brief summary of the collection, including grouping criteria.}?`
- `{Unique identifier for the measurement, defined by the facility.}?`
- `{Starting time of measurement}`
- `{Ending time of measurement}`
- `{Duration of measurement (end_time - start_time)}?`
- `{Actual data collection time, excluding suspensions (e.g., temperature out of range)}?`
- `{Revision ID of the file (e.g., due to re-calibration, reprocessing, new analysis, new instrument definition format)}`
- `{Name of entry DTD}`
- `{Name of entry DTD}?`
- `{Name of program used to generate this file}`

### User Information
- `{Name of user responsible for this entry}`
- `{Role of user (comma-separated list, e.g., "local_contact", "principal_investigator", "proposer", "experimenter", "funding_agency")}`
- `{Facility-based unique identifier for this person (e.g., identification code in the facility's address/contact database)}`

### Instrument Information
- `{Name of instrument}`
- `{Brief description of the instrument}?`
- `{Name of source}`
- `{Source type: "Spallation Neutron Source" | "Pulsed Reactor Neutron Source" | "Reactor Neutron Source" | "Synchrotron X-ray Source" | "Pulsed Muon Source" | "Rotating Anode X-ray" | "Fixed Tube X-ray"}`
- `{Radiation type: neutron | x-ray | muon | electron}`

### Sample Information
- `{Descriptive name of the sample}`
- `{Unique identifier for the sample in the experiment}`
- `{Description of the sample}?`
- `{Sample type: sample | sample+can | can | calibration sample | normalization sample | simulated data | none | sample environment}`
- `{Chemical formula (using CIF conventions)}?`
- `{Date of sample preparation}?`
- `{Atmosphere during experiment: air | vacuum | inert atmosphere | oxidizing atmosphere | reducing atmosphere | sealed can | other}`
- `{Sample temperature}?`
- `{Applied electric field}?`
- `{Applied magnetic field}?`
- `{External stress}?`
- `{Applied pressure}?`

### Additional Metadata
- `{Public release date of the data (e.g., file_time + X years)}?`
