DLSraw
======

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL:      http://www.nexus.anl.gov/
    Editor:   Stuart Campbell, DLS
    $Id$
    Draft definition of a Diamond Light Source raw Nexus file.
    -->
    <NXroot file_name="{File name of original NeXus file}"
            file_time="{Date and time of file creation}"
            file_update_time="{Date and time of last file change at close}"
            NeXus_version="{Version of NeXus API used in writing the file}"
            HDF_version="?"
            HDF5_version="?"
            XML_version="?"
            initial_format="{Initial format for file}"
            creator="{facility or program where file originated}?"
            unique_id="{unique file identifier}">

       <NXentry name="{Name of entry}">

            <!--Identification metadata -->
            <title>{Extended title for entry}?</title>
            <experiment_identifier type="NX_CHAR[]">
                {unique identifier for the experiment, defined by the facility, possibly
                linked to the proposals}?
            </experiment_identifier>
            <run_number type="NX_INT">
                {Number of run or scan stored in this entry}?
            </run_number>
            <run_cycle type="NX_CHAR[]">
                {}?
            </run_cycle>

            <!-- Data Management metadata-->
            <release_date type="NX_CHAR">
                { Date of the public release of the data. (file_time + X years)}
            </release_date>
            <revision type="NX_CHAR">
                { Revision id of the file due to re-calibration, reprocessing
                new analysis, new instrument definition format, ... }
            </revision>
            <revision_comment type="NX_CHAR">
                { Reason for the new revision. (e.g. first revision, re-calibration, ) }
            </revision_comment>

            <!--NeXus format information-->
            <definition type="NX_CHAR" version="{DTD version number}" URL="{URL of DTD file}">
                {Name of entry DTD}?
            </definition>
            <archive_definition type="NX_CHAR" version="{DTD version number}" URL="{URL of DTD file}">
                {Name of entry DTD}?
            </archive_definition>
            <local_definition type="NX_CHAR" version="{DTD version number}" URL="{URL of DTD file}">
                {Name of entry DTD}?
            </local_definition>

            <!--Timing metadata
                    start_time and end_time are mandatory
                    duration and/or collection_time would be nice to have
            -->
            <start_time type="ISO8601">
                {Starting time of measurement}?
            </start_time>
            <end_time type="ISO8601">
                {Ending time of measurement}?
            </end_time>
            <duration type="NX_INT" units="seconds">
                {Duration of measurement (end_time - start_time)}?
            </duration>
            <collection_time type="NX_FLOAT" units="seconds">
                {Time transpired actually collecting data i.e. taking out time when
                collection was suspended due to e.g. temperature out of range}?
            </collection_time>

            <!--Reliability metadata
                    Having the wrong information may be worst than having no information.
                    The accuracy of the information provided by the experimenter may be
                    difficult to determine. The minimum we can do is determine in which
                    condition the information was filled.
            -->
            <info_reliability type="NX_CHAR">
                {information on the reliability/source of the information provided by
                the experimenter. (e.g.: From proposal, updated at experiment time, ...}
            </info_reliability>

            <!--Experiment metadata-->
            <discipline type="NX_CHAR">
                {Keyword domain (e.g. chemistry, astronomy, ecology, ...)}?
            </discipline>
            <keyword type="NX_CHAR">
                {Keywords defined for this study}?
            </keyword>
            <keyword_source type="NX_CHAR">
                {A pointer to a reference work providing the definition of the
                restricted vocabulary of which the keyword list is a subset}?
            </keyword_source>
            <subject type="NX_CHAR">
                {Subject categorisations for this study}?
            </subject>
            <description_summary type="NX_CHAR">
                {Brief summary of the experiment, including key objectives}?
            </description_summary>
            <description type="NXnote">
                {Description of the full experiment (document in pdf, latex, ...)}?
            </description>
            <requirement type="NX_CHAR">
                {Special requirements of instrument}?
            </requirement>
            <publications type="NX_CHAR">
                {List of publications related to the proposal}?
            </publications>
            <facility_access_type type="NX_CHAR">
                {Facility access type (normal, rapid access, program access, ...)}?
            </facility_access_type>
            <grant_id type="NX_CHAR">
                {Identifier of the funding grant}?
            </grant_id>


            <!--Software metadata
                    may be useful to retrieve all data from a versioning case of problem
                    related to a specific version of the acquisition/analysis program.
            -->
            <program_name type="NX_CHAR" version="{Program version number}">
                {Name of program used to generate this file}?
            </program_name>
            <command_line type="NX_CHAR">
                {Name of command line used to generate this file}?
            </command_line>


            <!-- External reference
                    To archive processed data, you need to be able to point to the input
                    data that were used.

                    This class is not an official neXus class. When the NIAC decide for
                    a way to link to external resources. ; it will have to be replaced by
                    its official equivalent.
            -->
                <external_reference name="input data XX">+
                <name type="NX_CHAR" >
                    {Descriptive name of the input data}
                </name>
                <uri type="NX_CHAR">
                    {Uniform Resource Identifier of the input data}
                </uri>
            </external_reference>

            <notes>
                {Notes describing entry}?
            </notes>
            <thumbnail type="NXnote" mime_type="{image/*}">
                {An small image that is representative of the entry.} {An example of
                this is a 640x480 jpeg image automatically produced by a low resolution
                plot of the NXdata.}?
            </thumbnail>


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
            <NXuser name="{user}">1+
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
                <affiliation_id type="NX_CHAR">
                    {Affiliation unique identifier.}?
                </affiliation_id>
            </NXuser>


            <NXsample name="{sample}">
                <name type="NX_CHAR">
                    {Descriptive name of sample}
                </name>
                <sample_id type="NX_CHAR">
                    {Sample identifier}
                </sample_id>
                <chemical_formula type="NX_CHAR">
                    {The chemical formula specified using CIF conventions.}{Abbreviated
                    version of CIF standard:
                    1. Only recognized element symbols may be used.
                    2. Each element symbol is followed by a 'count' number. A count
                       of '1' may be omitted.
                    3. A space or parenthesis must separate each cluster of (element
                       symbol + count).
                    4. Where a group of elements is enclosed in parentheses, the
                       multiplier for the group must follow the closing parentheses. That
                       is, all element and group multipliers are assumed to be printed as
                       subscripted numbers.
                    5. Unless the elements are ordered in a manner that corresponds to
                       their chemical structure, the order of the elements within any group
                       or moiety depends on whether or not carbon is present. If carbon is
                       present, the order should be: C, then H, then the other elements in
                       alphabetical order of their symbol. If carbon is not present, the
                       elements are listed purely in alphabetic order of their symbol. This
                       is the 'Hill' system used by Chemical Abstracts.}
                </chemical_formula>
                <description type="NX_CHAR">
                    {Description of the sample}?
                </description>
                <short_title type="NX_CHAR">
                    {20 character fixed length sample description for legends}?
                </short_title>

                <!-- Sample Environment metadata
                        These parameters are to give an idea of the sample environment.
                        One value may seems too limited but it is mostly to understand under
                        which type of condition the experiment occurs (high, low, very
                        high, very low temperature, pressure, ...) Very few experiment will
                        go from 5 to 5000 Kelvin in one scan.
                        For actual analysis, time dependent measurement, the
                        data are stored in an NXlog (e.g temperature_log, ..).
                -->
                <temperature type="NX_FLOAT" param_type="fixed|scanned|free"
                             sampled="start|end|middle|average">
                    {Sample temperature.}?
                </temperature>
                <electric_field type="NX_FLOAT" param_type="fixed|scanned|free"
                                direction="x|y|z" sampled="start|end|middle|average">
                    {Applied electric field}?
                </electric_field>
                <magnetic_field type="NX_FLOAT" param_type="fixed|scanned|free"
                                direction="x|y|z" sampled="start|end|middle|average">
                    {Applied magnetic field}?
                </magnetic_field>
                <stress_field type="NX_FLOAT" param_type="fixed|scanned|free"
                              direction="x|y|z" sampled="start|end|middle|average">
                    {External stress}?
                </stress_field>
                <pressure type="NX_FLOAT" param_type="fixed|scanned|free"
                          sampled="start|end|middle|average">
                    {Applied pressure}?
                </pressure>
            </NXsample>


            <!-- Instruments metadata
                    The instrument name should be descriptive as much as possible,
                    telling in which mode the instrument was working.
            -->
            <NXinstrument name="{Name of instrument}">
                <name type="NX_CHAR" short_name="{addreviated name of instrument}">
                    {Name of instrument}
                </name>
                <NXsource name="{Name of facility}">
                    <name type="NX_CHAR">
                        {Name of source}?
                    </name>
                    <type type="NX_CHAR">
                        "Spallation Neutron Source"|"Pulsed Reactor Neutron Source"|
                        "Reactor Neutron Source"|"Synchrotron X-ray Source"|
                        "Pulsed Muon Source"|"Rotating Anode X-ray"|Fixed Tube X-ray"
                    </type>
                    <probe type="NX_CHAR">
                        neutron|x-ray|muon|electron?
                    </probe>

                    <distance type="NX_FLOAT" units="m">
                        {Effective distance from sample}{Distance as seen by radiation from
                        sample.  This number should be negative to signify that it is upstream
                        of the sample.}?
                    </distance>
                    <power type="NX_FLOAT" units="MW">
                        {Source power}?
                    </power>
                    <current type="NX_FLOAT" units="milliamps">
                        {Accelerator current}?
                    </current>
                    <voltage type="NX_FLOAT" units="MeV">
                        {Accelerator voltage}?
                    </voltage>
                    <notes type="NX_CHAR">
                        {any source/facility related messages/events that occurred during the
                        experiment}?
                    </notes>
                    <mode type="NX_CHAR">
                        {synchrotron operating mode}{"Single Bunch"|"Multi Bunch"}?
                    </mode>
                    <top_up type="NX_BOOLEAN">
                        {Is the synchrotron operating in top_up mode}?
                    </top_up>
                    <NXgeometry name="">
                        {"Engineering" location of source}?
                    </NXgeometry>
                </NXsource>

                <!--
                    Usually we will either include NXbending_magnet or NXinsertion_device.
                -->
                <NXbending_magnet name="{name of bending magnet}">
                        <critical_energy type="NX_FLOAT">
                            {critical energy}?
                        </critical_energy>
                        <bending_radius type="NX_FLOAT">
                            {bending radius}?
                        </bending_radius>
                        <spectrum type="NXdata">
                            {spectrum of bending magnet}?
                        </spectrum>
                        <NXgeometry name="">
                            {"Engineering" position of bending magnet}?
                        </NXgeometry>
                </NXbending_magnet>

                <NXinsertion_device name="{Name of insertion device}">
                    <type type="NX_CHAR">
                        {"undulator"|"wiggler"|...}?
                    </type>
                    <gap type="NX_FLOAT" units="milimetre">
                        {gap}?
                    </gap>
                    <taper type="NX_FLOAT" units="milimetre">
                        {taper}?
                    </taper>
                    <phase type="NX_FLOAT" units="degrees">
                        {phase}?
                    </phase>
                    <poles type="NX_INT">
                        {number of poles}?
                    </poles>
                    <length type="NX_FLOAT" units="mili*metre">
                        {length of insertion device}?
                    </length>
                    <power type="NX_FLOAT">
                        {total power delivered by insertion device}?
                    </power>
                    <energy type="NX_FLOAT">
                        {energy of peak}?
                    </energy>
                    <bandwidth type="NX_FLOAT">
                        {bandwidth of peak energy}?
                    </bandwidth>
                    <harmonic type="NX_INT">
                        {harmonic of peak}?
                    </harmonic>
                    <spectrum type="NXdata">
                        {spectrum of insertion device}?
                    </spectrum>
                    <NXgeometry name="">
                        {"Engineering" position of insertion device}?
                    </NXgeometry>
                </NXinsertion_device>

                <!--
                    We would include a different NXmotor entry for each 'scannable' or
                    motor/variable that we want to record the position of at each scan point.
                -->
                <NXpositioner name="{Name of scannable}">+
                    <value type="NX_FLOAT[n]" units="{}">
                        {value of motor - need [n] as may be scanned}
                    </value>
                    <controller_record type="NX_CHAR">
                        {Hardware device record, e.g. EPICS process variable, taco/tango ...}
                    </controller_record>
                </NXpositioner>


                <NXdetector name="{Name of detector}">1+
                    <data type="NX_FLOAT[nx?,ny?,n]|NX_INT[nx?,ny?,n]" signal="1" units="number" axes="{...}"
                          check_sum="{Integral of data as check of data integrity} (NX_INT)?" link="{absolute path to location}">
                        {Data values}
                    </data>
                    <data_error type="NX_FLOAT[i,j,k?,l?]|NX_INT[i,j,k?,l?]" units="number" link="{absolute path to location}">
                        {Data values}
                    </data_error>
                    <description type="NX_CHAR">
                        {name/manufacturer/model/etc. information}?
                    </description>

                    <type type="NX_CHAR">
                        "He3 gas cylinder"|He3 PSD"|"He3 planar multidetector"| "He3 curved multidetector"|
                        "multi-tube He3 PSD"|"BF3 gas"|"scintillator"|"fission chamber"|"CCD"|...?
                    </type>

                    <detector_number type="NX_INT[i]" axis="2" primary="1?" long_name="{Axis label}" link="{absolute path to location}">
                        {Identifier for detector}?
                    </detector_number>
                    <x_offset axis="3" primary="1?" type="NX_FLOAT[k+1]" units="10^-3 meter|10^-2 meter"
                                long_name="{Axis label}" link="{absolute path to location in NXdetector}">
                        {offset from the detector center in x-direction}?
                    </x_offset>
                    <y_offset axis="4" primary="1?" type="NX_FLOAT[l+1]" units="10^-3 meter|10^-2 meter"
                                long_name="{Axis label}" link="{absolute path to location in NXdetector}">
                        {offset from the detector center in the y-direction}?
                    </y_offset>
                    <x_pixelsize type="NX_FLOAT[i?]" units="mili*metre">
                        {Size of each detector pixel. If it is scalar all pixels are the same size}?
                    </x_pixelsize>
                    <y_pixelsize type="NX_FLOAT[i?]" units="mili*metre">
                        {Size of each detector pixel. If it is scalar all pixels are the same size}?
                    </y_pixelsize>


                    <distance type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?">
                        {Distance}?
                    </distance>
                    <polar_angle type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?">
                        {Polar Angle}?
                    </polar_angle>
                    <azimuthal_angle type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?">
                        {Azimuthal Angle}?
                    </azimuthal_angle>
                    <NXgeometry name="">
                        {Position and orientation of detector element}?
                    </NXgeometry>
                    <translation type="NX_FLOAT[2]" units="centimeter">
                        {translation normal to direct beam}?
                    </translation>
                    <solid_angle type="NX_FLOAT[i]" units="steradians">
                        {Solid angle subtended by the detector at the sample}?
                    </solid_angle>

                    <dead_time type="NX_FLOAT[i]">
                        {Detector dead time}?
                    </dead_time>
                    <hold_off type="NX_FLOAT[i]" units="micro.second">
                        {Delay in detector registering an event}?
                    </hold_off>
                    <gas_pressure type="NX_FLOAT[i]" units="bars">
                        {Detector gas pressure}?
                    </gas_pressure>
                    <detection_gas_path type="NX_FLOAT" units="cm">
                        {maximum drift space dimension}?
                    </detection_gas_path>

                    <crate type="NX_INT[i]" local_name="{Equivalent local term}">
                        {Crate number of detector}?
                    </crate>
                    <slot type="NX_INT[i]" local_name="{Equivalent local term}">
                        {Slot number of detector}?
                    </slot>
                    <input type="NX_INT[i]" local_name="{Equivalent local term}">
                        {Input number of detector}?
                    </input>


                    <NXdata name="efficiency">
                        {Efficiency of detector with respect to e.g. wavelength}?
                    </NXdata>
                    <calibration_date type="ISO8601">
                        {date of last calibration (geometry and/or efficiency) measurements}?
                    </calibration_date>
                    <calibration_method type="NXnote">
                        {summary of conversion of array data to pixels (e.g. polynomial approximations) and location of details of the calibrations}?
                    </calibration_method>
                </NXdetector>


            </NXinstrument>

            <!--
                The data section contains links back to the actual data which is contained within the
                NXdetector and NXmotor entries.
            -->
            <NXdata name="{Name of data block}">1+

                <data NAPIlink="{absolute path to location in NXdetector}" signal="1"
                      axes="{...}" long_name="{Title of data}">
                    {Data Values}?
                </data>
                <errors type="NX_FLOAT[:...]" NAPIlink="{absolute path to location in NXdetector}">
                    {Standard deviations of data values - the data array is identified by the attribute signal="1". This array must have the same dimensions as the data}?
                </errors>
                <variable type="NX_FLOAT[:]|NX_INT[:]" long_name="{Axis label}" distribution="0|1" first_good="{Index of first good value}"
                          last_good="{Index of last good value}" NAPIlink="{absolute path to location}">
                    {Dimension scale defining an axis of the data}?
                </variable>
                <variable_errors type="NX_FLOAT[:]|NX_INT[:]" NAPIlink="{absolute path to location}">
                    {Errors associated with axis "variable"}?
                </variable_errors>

            </NXdata>



       </NXentry>
    </NXroot>