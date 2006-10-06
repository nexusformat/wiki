---
title: Archive Definition
permalink: Archive_Definition/
layout: wiki
---

Introduction
------------

This 'NeXus Archive Definition' proposal is similar to an 'Instrument
Definition' but it describe the required information for neXus files
that are meant to be centrally archived. It contains important
information that will not be found in the instrument definition as they
are not needed for data analysis.

The Instrument Definitions should allow the creation of analysis
software that are common among several instruments and/or facilities.
With the Archive Definition, the aim is to allow shared data management
tools, see below for more details.

The Instrument Definitions and the Archive definition should not
interfere with each other. To analyze the data of an instrument, you
don't need to know the owner of the data or the name of the sample. To
manage the data, you don't need the counts that have been measured by a
specific detector.

Before archiving and indexing the data, we need to define the
granularity with which to do it. HDF 5 should allow a user to extract
only one group from a file stored in a SRB system. I doubt that it would
be very practical to catalogue the data so finely, at least not at a
facility level. This definition assumes an indexing at the file level.

A large part of the definition are optional parameters for nice to have
information. It is build with RAW file in mind. other parameters may be
needed for processed / result or simulation files

Multiple NXentry issue
----------------------

In the case of archiving and cataloguing, multiple NXentry make it
difficult to extract metadata to characterize a file, (e.g. 1 file with
multiple samples in multiple NXentry?).

Only the metadata from the first NXentry will be used in the indexing of
the NeXus file. The first NXentry will be named 'Header' or '{name}\_0'
where name c an be any string (e.g. 'scan\_0').

Open Issue
----------

### NXentry order

The order of multiple NXentry is not recorded by the data format. Now,
we only have a naming convention to record the creation/logical order.
How well can we enforce such convention?

It could be good to add a 'entry\_num' parameter in NXentry class to
define the order.

### External links

For processed data, NIAC should define a way to link to external files.

DTD definition
--------------

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL     : http://www.nexusformat.org/
    Editor  : L. Lerusse, CCLRC e-Science
    Version : October 2006

    Template of the Archive Definition.

    line starting with 
         * are element not yet in the base classes. 
         # are a addition or modification of the TOFraw definition.
    -->
    <NXroot>
     <NXentry name="entry 0"> <!-- See Multiple Entry comment above -->
       <!-- Identification metadata
            A unique identifier separate from the filename should be defined. 
            These parameters seems the more promising for this. 
            The control system should not allow creation of file with already 
            existing parameters.
        -->
        <title>{Extended title for file}?</title> 
        <experiment_identifier type="NX_CHAR">
            {unique identifier for the experiment, defined by the facility, possibly
            linked to the proposals (see : proposal_identifier below)}
        </experiment_identifier>
        <run_number type="NX_INT">
            {Data file sequence number}
        </run_number>
        <run_cycle type="NX_CHAR">
            {}?
        </run_cycle>   


        <!-- Data management metadata -->
        <release_date type="NX_CHAR">        
            { Date of the public release of the data. (file_time + X years)}?
        </release_date>
        <revision type="NX_CHAR">
            { Revision id of the file due to re-calibration, reprocessing, 
              new analysis, new instrument definition format, ... }
        </revision>
        <revision_comment type="NX_CHAR">
        {Reason for the new revision. {e.g.: first revision, re-calibration,}?
        </revision_comment>

        <!-- Nexus format information
            The definition tag is meant to contains the most precise instrument 
            definition that apply to the data set. 
            
            The instrument definition is there to tell what analysis package 
            should be able to analyze the data.
        -->
        <definition type="NX_CHAR" version="{DTD version number}" URL="{URL of DTD file}">
            {Name of entry DTD}
        </definition>
        
        <!-- Timing metadata : 
            start_time and end_time are mandatory
            duration and/or collection_time would be nice to have
        --> 
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
            collection was suspended due to e.g. temperature out of range}
        </collection_time>
            
    *#    <!-- Reliability metadata
    *#      Having the wrong information may be worst than having no information. 
    *#      The accuracy of the information provided by the experimenter may be  
    *#      difficult to determine. The minimum we can do is determine in which
    *#      condition the information was filled. 
    *#    -->
    *#    <info_reliability  type="NX_CHAR">
    *#      {information on the reliability/source of the information provided by
    *#      the experimenter.(e.g. : From proposal, updated at experiment time, ...}?
    *#    </info_reliability>

        
    *    <!-- Experiment metadata
    *       Description of the science related to the data.
    *    -->
    *#       <proposal_identifier>
    *#              {identification of the proposal}?
    *#       </proposal_identifier>
    *        <discipline type="NX_CHAR">
    *               {Keyword domain (e.g. chemistry, astronomy, ecology, … )}?
    *        </discipline>
    *   <keyword type="NX_CHAR">
    *       {Keywords defined for this study.}?
    *   </keyword>
    *   <keyword_source type="NX_CHAR">
    *       {A pointer to a reference work providing the definition of the 
    *       restricted vocabulary of which the keyword list is a subset.}?
    *   </keyword_source>
    *   <subject type="NX_CHAR">    
    *       {Subject categorizations for this study}?
    *   </subject>
    *#  <description type="NX_CHAR">
    *#      {Brief summary of the experiment, including key objectives}
    *#  </description>
    *#  <description_document type="NXNote">
    *#      {Description of the full experiment (document in pdf, latex, …)}?
    *#  </description_document>
    *   <requirement type="NX_CHAR">
    *       {Special requirements of instrument}?
    *   </requirement>
    *   <publications type="NX_CHAR">
    *       {List of publication related to the proposal}?
    *   </publications>
    *   <publication_references type="NX_CHAR">
    *       {List of publication references related to the proposal.}?
    *   </publication_references>
    *   <facility_access_type type="NX_CHAR">
    *       {Facility access type (normal, rapid access, program access …)}?
    *   </facility_access_type>
    *   <grant_id  type="NX_CHAR" type="NX_CHAR">       
    *       {Identifier of the funding grant.}?
    *   </grant_id>
                
                
        <!-- Software metadata
            May be useful to retrieve all data from a versioning case of problem 
            related to a specific version of the acquisition/analysis program. 
        -->
        <program_name type="NX_CHAR" version="{Program version number}">
            {Name of program used to generate this file}?
        </program_name>

        <!-- User metadata
        At least one user with role 'principal_investigator' must be present to 
        define the owner of the data. 
        Other important roles are :
                'experimenter' to know who physically made the experiment,
            'local_contact' for any instrument configuration questions,
        Nice to have would be 'funding_agency', it may help to get money for 
        the next experiments. 
            
            I think that the users with role 'principal_investigator', 'proposer'  
        and 'experimenter' should be given access to the data. 
        To be define in the data right policy of the facility.
        -->     
        <NXuser name="user XX">1+
            <name type="NX_CHAR">
                {Name of user responsible for this entry}
            </name>
            <role type="NX_CHAR">
                {role of user responsible for this entry, comma separated list}
                {Suggested roles are "local_contact", "principal_investigator", 
                "proposer", "experimenter", "funding_agency"}
            </role>
            <affiliation type="NX_CHAR">
                {Affiliation of user}?
            </affiliation>
            <address type="NX_CHAR">
                {Address of user}?
            </address>
            <telephone_number type="NX_CHAR">
                {Telephone number of user}?
            </telephone_number>
            <fax_number type="NX_CHAR">
                {Fax number of user}?
            </fax_number>
            <email type="NX_CHAR">
                {Email of user}?
            </email>
            <facility_user_id type="NX_CHAR">
                {Facility based unique identifier for this person e.g. their 
                identification code on the facility address/contact database, 
                should allow owner identification by the archive system.}
            </facility_user_id>
    *        <affiliation_id type="NX_CHAR">
    *            {Affiliation unique identifier.}?
    *        </affiliation_id>'''
        </NXuser>

        <!-- Instruments metadata
        The instrument name should be descriptive as much as possible, 
        telling in which mode the instrument was working.
        -->
        <NXinstrument name="{Name of instrument}">
            <name type="NX_CHAR" short_name="{abbreviated name of instrument}">
                {Name of instrument}
            </name>
    *#  <description type="NX_CHAR">
    *#      {Brief description of the instrument}?
    *#  </description_summary>
    *#  <description_document type="NXNote">
    *#      {Description of the instrument (document in pdf, latex, …)}?
    *#  </description>
            <NXsource name="{Name of facility}">
                <name type="NX_CHAR">
                    {Name of source}
                </name>
                <type type="NX_CHAR">
                    "Spallation Neutron Source"|"Pulsed Reactor Neutron Source"| 
                    "Reactor Neutron Source"|"Synchrotron X-ray Source"|
                    "Pulsed Muon Source"|"Rotating Anode X-ray"|"Fixed Tube X-ray"
                </type>
                <probe type="NX_CHAR">
                    neutron|x-ray|muon|electron
                </probe>
            </NXsource>
        </NXinstrument>

        <!-- Sample metadata
        -->
        <NXsample name="{name of sample}">
            <name type="NX_CHAR">
                {Descriptive name of sample}
            </name>
            <sample_id type="NX_CHAR">
                {Sample identifier}
            </sample_id>
            <chemical_formula type="NX_CHAR">
                {The chemical formula specified using CIF conventions.}?
            </chemical_formula>
        <description type="NX_CHAR">
                {Description of the sample}?
            </description>       

            
    *        <!-- Sample Environment metadata
    *           These parameters are to give an idea of the sample environment. 
    *       
    *           The data are stored in an NXlog (e.g temperature, ..) 
    *               those could have been links from a sensor class located in the 
    *               NXinstrument class. But in that case, the name would all 
    *               be value and that would cause problems. 
    *        -->
    *        <NXlog name="temperature_log"> {Sample temperature. }? </NXlog>
    *        <NXlog name="electric_field_log"> {Applied electric field}? </NXlog>
    *        <NXlog name="magnetic_field_log"> {Applied magnetic field}? </NXlog>
    *        <NXlog name="stress_field_log"> {External stress}? </NXlog>
    *        <NXlog name="pressure_log"> {Applied pressure}?  </NXlog>   
        </NXsample>
     </NXentry>
    </NXroot>
