---
title: NIACClasses
permalink: NIACClasses.html
layout: wiki
---

NIAC Decisions on NeXus Classes
-------------------------------

This section records NIAC decisions on NeXus base classes and
application definitions.

NIAC 2003: Instrument definitions and base classes will be fully self
describing

NIAC 2003: Instrument definitions and base classes to go into CVS

NIAC 2003: analysis item in NXentry to be replaced with definition

NIAC 2003: NXroot will be defined as

    &lt;NXroot file_name=&quot;{File name of original NeXus file}&quot;
         file_time=&quot;{Date and time of file creation}&quot;
         file_update_time=&quot;{Date and time of last file change at
         close}&quot;
         NeXus_version=&quot;{Version of NeXus API used in writing the
         file}&quot;
         HDF_version=&quot;?&quot;
         HDF5_version=&quot;?&quot;
         creator=&quot;{facility or program where file originated}?&quot;&gt;
         &lt;NXentry name=&quot;{entry name}&quot;&gt;+&lt;/NXentry&gt;
    &lt;/NXroot&gt;

NIAC 2003: base classes and instrument definitions will not define bit
length for primitives. This means that NX\_UINT, NX\_INT or NX\_FLOAT
are all that are allowed for numerical items.

NIAC 2003: The template for NXentry is

    &lt;NXentry name=&quot;{Entry Name}&quot;&gt;
         &lt;title&gt;{Extended title for entry}&lt;/title&gt;
         &lt;definition version=&quot;{DTD version number}&quot; URL=&quot;{URL of DTD
            file}&quot;&gt;{Name of entry DTD}&lt;/definition&gt;
          &lt;start_time type=&quot;ISO8601&quot;&gt;{Starting time of
            measurement}&lt;/start_time&gt;
         &lt;end_time type=&quot;ISO8601&quot;&gt;{Ending time of
            measurement}&lt;/end_time&gt;
         &lt;duration type=&quot;NX_INT&quot; units=&quot;seconds&quot;&gt;{Duration of
            measurement}&lt;/duration&gt;
         &lt;experiment_identifier
            type=&quot;NX_CHAR[]&quot;&gt;{}&lt;/experiment_identifier&gt;
         &lt;run_number type=&quot;NX_INT&quot;&gt;{Number of run or scan stored in
            this entry}&lt;/run_number&gt;
         &lt;run_cycle type=&quot;NX_CHAR[]&quot;&gt;{}&lt;/run_cycle&gt;
         &lt;program_name version=&quot;{Program version number}&quot;&gt;{Name of
            program used to generate this file}&lt;/program_name&gt;
         &lt;command_line&gt;{Name of command line used to generate this
            file}&lt;/command_line&gt;
         &lt;notes&gt;{Notes describing entry}&lt;/notes&gt;
         &lt;NXuser name=&quot;{user}&quot;&gt;&lt;/NXuser&gt;
         &lt;NXsample name=&quot;{sample}&quot;&gt;&lt;/NXsample&gt;
         &lt;NXinstrument name=&quot;{Name of instrument}&quot;&gt;&lt;/NXinstrument&gt;
         &lt;NXmonitor name=&quot;{Name of monitor}&quot;&gt;&lt;/NXmonitor&gt;
         &lt;NXdata name=&quot;{Name of data block}&quot;&gt;&lt;/NXdata&gt;
    &lt;/NXentry&gt;

NIAC 2003: NXinstrument template consists of at least the following
groups

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

NIAC 2006: Add NXinsertion\_device

NIAC 2006: Add NXbending\_magnet

NIAC 2007: NXmonopowder ratified

NIAC 2007: NXpositioner ratified

NIAC 2007: NXmonitor ratified

NIAC 2007: All classes ratified will be NeXus 2.0.

NIAC 2007HMI: ratified NXcone definition (check where this one is)

NIAC 2007HMI: replace run\_number with entry\_identifier in NXentry

NIAC 2007HMI: ratified NXarchive

NIAC 2007HMI: ratified NXdetector extensions for CCD cameras: 1. extend
type to include: ccd,pixel,image\_plate, cmos 2. add field data\_file 3.
add field flood 4. add field flood\_file 5. add field dark 6. add file
dark\_file 7. add field spatial\_distortion 8. add field
spatial\_distortion\_file

NIAC 2010: NXcollection ratified

NIAC 2010: tags scalar, image for datasets

NIAC 2010: muon application definition ratified with some changes

NIAC 2012: NXcharacterisation deprecated

NIAC 2012: add some DECTRICS required fields to NXdetector

NIAC 2014: NXmx, NXtransformations and variants ratified

NIAC 2014: Ratified NXarpes, NXCite with addition of URL,
NXfresnel\_zone\_plate

NIAC 2014: Add a default attribute at root and NXentry level to help in
finding default data to plot

NIAC 2014: added decimated as a possible enum to acquisition\_mode in
NXdetector

NIAC 2014: additional field nominal added to NXmonitor to keep the
nominal flux

NIAC 2014: "rgbimage", "rgbaimage", "hslimage", "hslaimage", "cmykimage"
to be added to the interpretation attribute of datasets to encode 3d
datasets with colour as added dimension to the 2d image.
