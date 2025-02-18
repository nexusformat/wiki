NIAC Decisions on NeXus Classes
-------------------------------

This section records NIAC decisions on NeXus base classes and
application definitions.

NIAC 2003: Instrument definitions and base classes will be fully self
describing

NIAC 2003: Instrument definitions and base classes to go into CVS

NIAC 2003: analysis item in NXentry to be replaced with definition

NIAC 2003: NXroot will be defined as

::

   <NXroot file_name="{File name of original NeXus file}"
        file_time="{Date and time of file creation}"
        file_update_time="{Date and time of last file change at close}"
        NeXus_version="{Version of NeXus API used in writing the file}"
        HDF_version="?"
        HDF5_version="?"
        creator="{facility or program where file originated}?">
        <NXentry name="{entry name}">+</NXentry>
   </NXroot>

NIAC 2003: base classes and instrument definitions will not define bit
length for primitives. This means that NX_UINT, NX_INT or NX_FLOAT are
all that are allowed for numerical items.

NIAC 2003: The template for NXentry is

::

   <NXentry name="{Entry Name}">
        <title>{Extended title for entry}</title>
        <definition version="{DTD version number}" URL="{URL of DTD file}">{Name of entry DTD}</definition>
         <start_time type="ISO8601">{Starting time of measurement}</start_time>
        <end_time type="ISO8601">{Ending time of measurement}</end_time>
        <duration type="NX_INT" units="seconds">{Duration of measurement}</duration>
        <experiment_identifier
           type="NX_CHAR[]">{}</experiment_identifier>
        <run_number type="NX_INT">{Number of run or scan stored in this entry}</run_number>
        <run_cycle type="NX_CHAR[]">{}</run_cycle>
        <program_name version="{Program version number}">{Name of program used to generate this file}</program_name>
        <command_line>{Name of command line used to generate this file}</command_line>
        <notes>{Notes describing entry}</notes>
        <NXuser name="{user}"></NXuser>
        <NXsample name="{sample}"></NXsample>
        <NXinstrument name="{Name of instrument}"></NXinstrument>
        <NXmonitor name="{Name of monitor}"></NXmonitor>
        <NXdata name="{Name of data block}"></NXdata>
   </NXentry>

NIAC 2003: NXinstrument template consists of at least the following
groups

::

   <NXinstrument> 
        <name short_name=”{abbreviated name of instrument}”>{name of instrument}</name> 
        <NXsource/> 
         <NXcrystal/> 
         <NXdisk_chopper/>
         <NXfermi_chopper/>
          <NXvelocity_selector/> 
          <NXguide/> 
          <NXcollimator/>
          <NXaperture/>
          <NXfilter/>
          <NXattenuator/>
          <NXpolarizer/>
           <NXflipper/>
           <NXmirror/>
           <NXdetector/> 
           <NXbeam_stop/> 
   </NXinstrument>

NIAC 2003: Each NXlog will contain information for one variable The
definition of a NXlog is

::

   <NXlog name=”{identifier for the log}”> 
           <description>{longer description of what is logged}</description>
           <time start=”{written in ISO8601}” units=””  type=”NX_FLOAT”>{time axis for logged quantity}
           </time> 
          <value units=”{units of logged value}”  type=”NX_FLOAT|NX_INT”>{array of logged value, such as temperature}</value> 
          <raw_value units=”{units of raw values}”
               type=”NX_FLOAT|NX_INT”>{array of raw information, such as voltage on a thermocouple}?</raw_value> 
   </NXlog>

NIAC 2004: NXcharacterisations is removed from NXentry

NIAC 2004: End-of-line in NXnote is cr

NIAC 2005: describe links as NAPIlink in metaDTD

NIAC 2005: Allow ? and \* in definitions to denote groups and fields
that are desirable but not necessary.

NIAC 2006: TOF Raw definition ratified

NIAC 2006: Add synchrotron changes to NXsource

NIAC 2006: Add NXinsertion_device

NIAC 2006: Add NXbending_magnet

NIAC 2007: NXmonopowder ratified

NIAC 2007: NXpositioner ratified

NIAC 2007: NXmonitor ratified

NIAC 2007: All classes ratified will be NeXus 2.0.

NIAC 2007HMI: ratified NXcone definition (check where this one is)

NIAC 2007HMI: replace run_number with entry_identifier in NXentry

NIAC 2007HMI: ratified NXarchive

NIAC 2007HMI: ratified NXdetector extensions for CCD cameras: 1. extend
type to include: ccd,pixel,image_plate, cmos 2. add field data_file 3.
add field flood 4. add field flood_file 5. add field dark 6. add file
dark_file 7. add field spatial_distortion 8. add field
spatial_distortion_file

NIAC 2010: NXcollection ratified

NIAC 2010: tags scalar, image for datasets

NIAC 2010: muon application definition ratified with some changes

NIAC 2012: NXcharacterisation deprecated

NIAC 2012: add some DECTRICS required fields to NXdetector

NIAC 2014: NXmx, NXtransformations and variants ratified

NIAC 2014: Ratified NXarpes, NXCite with addition of URL,
NXfresnel_zone_plate

NIAC 2014: Add a default attribute at root and NXentry level to help in
finding default data to plot

NIAC 2014: added decimated as a possible enum to acquisition_mode in
NXdetector

NIAC 2014: additional field nominal added to NXmonitor to keep the
nominal flux

NIAC 2014: “rgbimage”, “rgbaimage”, “hslimage”, “hslaimage”, “cmykimage”
to be added to the interpretation attribute of datasets to encode 3d
datasets with colour as added dimension to the 2d image.
