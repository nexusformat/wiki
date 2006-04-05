---
title: MonoXSingle
permalink: MonoXSingle/
layout: wiki
---

Monochromatic Single Crystal Diffractometer with Single Detector
----------------------------------------------------------------

The XML source file can be downloaded from:
<http://lns00.psi.ch/NXexample/NXmonosinglex.xml>

    <?xml version="1.0"?>
    <!--
    URL:
    Editor: Mark Koennecke <Mark.Koennecke@psi.ch>
    version: April 2006
    $Id$

    Instrument definition for a single crystal diffractometer at a monochromatic
    neutron or X-ray beam.  This is the single detector version.

    General Notes:
     - A Eulerian cradle is assumed. If you do not have this, or you are
       using a rotation camera, feel free to adapt the Nxsample group. 
     - If you put measurements for multiple reflections in one file, they 
       should go into separate entries.
     - The definition assumes the measurement to be an omega - two-theta or 
       omega scan of a given reflection. If this is not the case,  i.e. a 
       general scan is performed, feel free to make HKL, chi and phi arrays
       with the length of the scan as a dimension. As the  NeXus scan 
       paradigm of the day requires.
    - This definition is fairly minimal and shall cater for standard data
      reduction needs. If your most favourite items are missing, feel free to
      add them. If you think something is missing which is required for standard
      data reduction tasks, please contact the maintainer of this definition.
    -->
    <NXroot  file_name="{File name of original NeXus file}"
             file_time="{Date and time of file creation}"
             file_update_time="{Date and time of last file change at close}"
             NeXus_version="{Version of NeXus API used in writing the file}"
             HDF_version="?"
             HDF5_version="?">
      <NXentry name="{Entry Name}">+
         <title type="NX_CHAR">{Title of the experiment}</title>
         <start_time type="ISO8601">?{start time of measurement}
         </start_time>
         <end_time type="ISO8601">?{end time of measurement}
         </end_time>
         <NXinstrument name="instrument">
            <NXcrystal name="{Name of Monochromator Crystal}">

           <wavelength type="NX_FLOAT32" units="Angstroems">
                   {nominal wavelength selected}
               </wavelength>
            </NXcrystal>
            <NXdetector name="{Name of Detector}">+
           <polar_angle type="NX_FLOAT32[]" axis="1">
                 {Polar Angle, commonly known as two theta}
                 {Polar Angle, or two theta as an array with values for each
                  detector element}
               </polar_angle>
           <data type="NX_INT32[]" signal="1" axes="polar_angle">
              {The counts detected in the detector}
           </data>

            </NXdetector>
         </NXinstrument>
         <NXmonitor name="control">
            <mode type="NX_CHAR">monitor | timer</mode>
            <preset type="NX_FLOAT32">
              {preset value for monitor or timer}
            </preset>
            <data type="NX_INT32">
              {Monitor counts}
            </data>

         </NXmonitor>
         <NXuser name="">+
           <name type="NX_CHAR">
              {Name of user responsible for this entry}
           </name>
           <affiliation type="NX_CHAR">
              {Affiliation of user}?
           </affiliation>
         <address type="NX_CHAR">
          {Address of user}
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
       </NXuser>

       <NXsample name="{Name of Sample">
         <name type="NX_CHAR">
          {Descriptive name of sample}
         </name>
         <rotation type="NX_FLOAT[]" units="degree">
            { Sample rotation, aslo known as omega }
         </rotation>
         <chi type="NX_FLOAT" units="degree">
            { chi angle }
         </chi>

         <phi type="NX_FLOAT" units="degree">
            { phi angle }
         </phi>
         <orientation_matrix type="NX_FLOAT32[3,3]">
           {Orientation matrix of single crystal according to conventions
            established by Busing,  Levy, 1967 }
          </orientation_matrix>
          <miller_indices type="NX_FLOAT[3]">
           { Miller indices of the target reflection}
          </miller_indices>
       </NXsample>

       <NXdata name="{Name of Data Block}">+
          <data type="NX_INT32[i]" signal="1">
             {Link to detector counts in NXdetector}
          </data>
          <polar_angle type="NX_FLOAT32[i]" axis="1">
             {Link to polar angle data in NXdetector}
          </polar_angle>
       </NXdata>
      </NXentry>
    </NXroot>
