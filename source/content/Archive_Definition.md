---
title: Archive Definition
permalink: Archive_Definition.html
layout: wiki
---
Archive Definition
==================

Introduction
------------

This 'NeXus Archive Definition' proposal is similar to an 'Instrument
Definition' but it describe the required information for neXus files
that are meant to be centrally archived. It contains important
information that will not be found in the instrument definition as they
are not needed for data analysis.

The Instrument Definitions should allow the creation of archiving
software that are common among several instruments and/or facilities.
With the Archive Definition, the aim is to allow shared data management
tools. It also emphasize important information that will be useful for
search and retrieve of the data once stored in the archive.

The Instrument Definitions and the Archive definition should not
interfere with each other. To analyze the data of an instrument, you
don't need to know the owner of the data or the name of the sample.

Before archiving and indexing the data, we need to define the
granularity with which to do it. HDF 5 should allow a user to extract
only one group from a file stored in a SRB system. I doubt that it would
be very practical to catalogue the data so finely, at least not at a
facility level. This definition assumes an indexing at the file level.

Part of the definition are optional parameters for information that are
highly recommended but not required . It is build with RAW file in mind.
other parameters may be needed for processed / result or simulation
files

Multiple NXentry issue
----------------------

A NeXus file may contain several NXentry that needs to be indexed
separately. But it may also occur that not all NXentry has to be indexed
(e.g. when one entry contains the events data and the other the
histograms for the same measurement. )

The entry that has to be indexed will have the attribute 'index' with
the value 'yes'. The one which doesn't have to be indexed, will have the
value 'no'. If some of the NXentry doesn't have to be indexed, they will
have the value 'no'. Those NXentry may be associated to one of the
indexed NXentry with the attribute 'index\_group'.

     <NXroot>
       <NXentry index="yes" index_group="sample_01"/
       <NXentry index="no" index_group="sample_01"/>
       <NXentry index="yes" index_group="sample_02"/>
       <NXentry index="yes" index_group="sample_03"/>
     </NXroot>

If there is only one entry or if it does not matter which entry will be
indexed (all metadata are the same in all entries) then there is no need
to put the attribute 'index' or 'index\_group'.

Parameter Names
---------------

When extracting the metadata, we will not be limited to the one in this
list. Facility, Instrument, Sample specific information may be
extracted. It would then be useful to chose names that are descriptive
and have a constant meaning between experiments. It is preferable to use
temp\_control and temp\_sample than temp\_1 and temp\_2 with the sample
temperature being sometimes temp\_1, sometimes temp\_2.

Too much metadata is better than too little
-------------------------------------------

You can't extract information that are not there.

DTD definition
--------------

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL:     http://www.nexusformat.gov/classes/xml/NXarchive.xml
    Editor:  NIAC
    NIAC Version: 2.1
    Editor  : L. Lerusse, SciTech e-Science

    Definition for RAW data the will be centrally archived by the facilities.
    -->
    <NXroot>
      <NXentry name="{Entry Name}" index="{Should this entry be indexed?}" index_group="{Group of entry that are not indexed!">+
        <title type="NX_CHAR">
            {Extended title for file}
        </title> 
        <experiment_identifier type="NX_CHAR">
            {unique identifier for the experiment, defined by the facility, possibly 
             linked to the proposals (see : proposal_identifier below)}
        </experiment_identifier>
        <experiment_description type="NX_CHAR">
        {Brief summary of the experiment, including key objectives.}
        </description>
        <experiment_documentation type="NXNote">
        {Description of the full experiment (document in pdf, latex, …)}?
        </description_document>
        <collection_identifier type="NX_CHAR">
             {User or Data Acquisition defined group of NeXus files or NXentry}?
        </collection_identifier>
        <collection_description type="NX_CHAR">
        {Brief summary of the collection, including grouping criteria.}?
        </description>
        <entry_identifier type="NX_CHAR">
            {unique identifier for the measurement, defined by the facility.}?
        </entry_identifier>
        <start_time type="ISO8601">
            {Starting time of measurement}
        </start_time>
        <end_time type="ISO8601">
            {Ending time of measurement}
        </end_time>
        <duration type="NX_FLOAT" units="seconds">
            {Duration of measurement (end_time - start_time)}?
        </duration>
        <collection_time type="NX_FLOAT" units="seconds">
            {Time transpired actually collecting data i.e. taking out time when 
            collection was suspended due to e.g. temperature out of range}?
        </collection_time>
        <run_cycle type="NX_CHAR">
            {}?
        </run_cycle>   
        <revision type="NX_CHAR" comment="">
            { Revision id of the file due to re-calibration, reprocessing, 
              new analysis, new instrument definition format, ... }
        </revision>
        <definition type="NX_CHAR" version="{DTD version number}" URL="{URL of DTD file}">
            {Name of entry DTD}
        </definition>
        <definition_local type="NX_CHAR" version="{DTD version number}" URL="{URL of DTD file}">
            {Name of entry DTD}?
        </definition_local>
        <program_name type="NX_CHAR" version="{Program version number}" configuration="{program configuration information}">
            {Name of program used to generate this file}
        </program_name>
        <NXuser name="user XX">+
            <name type="NX_CHAR">
                {Name of user responsible for this entry}
            </name>
            <role type="NX_CHAR">
                {role of user responsible for this entry, comma separated list}
                {Suggested roles are "local_contact", "principal_investigator", 
                "proposer", "experimenter", "funding_agency"}
            </role>
            <facility_user_id type="NX_CHAR">
                {Facility based unique identifier for this person e.g. their 
                identification code on the facility address/contact database, 
                should allow owner identification by the archive system.}
            </facility_user_id>
        </NXuser>
        <NXinstrument name="{Name of instrument}">
            <name type="NX_CHAR" short_name="{abbreviated name of instrument}">
                {Name of instrument}
            </name>
        <description type="NX_CHAR">
            {Brief description of the instrument}?
        </description_summary>
            <NXsource name="{Name of facility}">
                <name type="NX_CHAR">
                    {Name of source}
                </name>
                <type type="NX_CHAR">
                    {"Spallation Neutron Source"|"Pulsed Reactor Neutron Source"| 
                    "Reactor Neutron Source"|"Synchrotron X-ray Source"|
                    "Pulsed Muon Source"|"Rotating Anode X-ray"|"Fixed Tube X-ray"}
                </type>
                <probe type="NX_CHAR">
                    neutron|x-ray|muon|electron
                </probe>
            </NXsource>
        </NXinstrument>
        <NXsample name="{name of sample}">
            <name type="NX_CHAR">
                {Descriptive name of sample}
            </name>
            <sample_id type="NX_CHAR">
                {Unique identifier for the sample in the experiment.}
            </sample_id>
        <description type="NX_CHAR">
                {Description of the sample}?
            </description>
            <type type="NX_CHAR">
            { sample | sample+can | can | calibration sample | 
                  normalisation sample | simulated data | none | sample environment }
        </type>
            <chemical_formula type="NX_CHAR">
                {The chemical formula specified using CIF conventions.}?
            </chemical_formula>
            <preparation_date type="ISO8601">
            {Date of preparation of the sample}?
        </preparation_date>
        <situation type="NX_CHAR">
            { air | vacuum | inert atmosphere | oxidising atmosphere | reducing atmosphere | sealed can | other }
                {The atmosphere will be one of the components, which is where its details will be stored; 
                the relevant components will be indicated by the entry in the sample_component member.}?
        </situation>
            <NXlog name="temperature_log"> 
                {Sample temperature. }? 
            </NXlog>
            <NXlog name="electric_field_log"> 
                {Applied electric field}? 
            </NXlog>
            <NXlog name="magnetic_field_log"> 
                {Applied magnetic field}? 
            </NXlog>
            <NXlog name="stress_field_log"> 
                {External stress}? 
            </NXlog>
            <NXlog name="pressure_log"> 
                {Applied pressure}?  
            </NXlog> 
            <temperature type="NX_FLOAT" units="kelvin">
                {Sample temperature. }? 
            </temperature>
            <magnetic_field type="NX_FLOAT" units="gauss">
                {Sample magnetic_field. }? 
            </magnetic_field>
            <electric_field type="NX_FLOAT" units="">
                {Sample electric_field. }? 
            </electric_field>
            <stress_field type="NX_FLOAT" units="">
                {Sample stress_field. }? 
            </stress_field>
            <pressure type="NX_FLOAT" units="pascal">
                {Sample pressure. }? 
            </pressure>
        </NXsample>
        <release_date type="NX_CHAR">        
            { Date of the public release of the data. (file_time + X years)}?
        </release_date>     
     </NXentry>
    </NXroot>
