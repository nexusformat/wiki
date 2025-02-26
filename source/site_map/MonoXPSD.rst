========
MonoXPSD
========

Monochromatic Single Crystal Diffractometer with Position Sensitive Detector
----------------------------------------------------------------------------

Instrument definition for a single crystal diffractometer at a
monochromatic neutron or X-ray beam. This is the version for a position
sensitive detector. Such an instrument can be used in various ways:

In one mode the instrument is driven to each reflection individually and
a short scan is performed in order to measure the reflections intensity.
In such cases each reflection should be stored in either separate files
or in separate entries as they constitute separate measurements.

In another mode a larger range in omega is scanned, saving detector data
at each step. This is similar to the way PX instruments operate. In such
a case, omit the Miller indices in the sample group.

A Eulerian cradle is assumed. If you do not have this, or you are using
a rotation camera, feel free to adapt the Nxsample group.

The definition assumes the measurement to be an omega - two-theta or
omega scan of a given reflection.

This definition is fairly minimal and shall cater for standard data
reduction needs. If your most favourite items are missing, feel free to
add them. If you think something is missing which is required for
standard data reduction tasks, please contact the maintainer of this
definition.

If you to choose to store PSD scans in separate files or separate
entries, it is the users responsibility to process the data in the right
order.

NP is again the number of scan points

.. code-block:: xml

    <?xml version="1.0"?>
    <!--
    URL:
    Editor: Mark Koennecke <Mark.Koennecke@psi.ch>
    version: October 2006
    $Id$

    Instrument definition for a single crystal diffractometer at a monochromatic
    neutron or X-ray beam.  This is the version for a position sensitive detector.
    Such an instrument can be used in various ways:

    In one mode the instrument is driven to each reflection individually and a short scan is
    performed in order to measure the reflections intensity. In such cases each reflection should be
    stored in either separate files or in separate entries as they constitute separate measurements.

    In another mode a larger range in omega is scanned, saving detector data at each step. This is similar to the way
    PX instruments operate. In such a case, omit the Miller indices in the sample group.

    A Eulerian cradle is assumed. If you do not have this, or you are using a rotation camera, feel free
    to adapt the Nxsample group.

    The definition assumes the measurement to be an omega - two-theta or omega scan of a given reflection.

    This definition is fairly minimal and shall cater for standard data reduction needs. If your most favourite items are missing, feel free to add them. If you think something is missing which is required for standard
    data reduction tasks, please contact the maintainer of this definition.

    If you to choose to store PSD scans in separate files or separate entries, it is the users responsibility to process the data in the right order.

    NP is again the number of scan points
    -->
    <NXroot>
      <NXentry name="{Entry Name}">+
         <title type="NX_CHAR">{Title of the experiment}</title>
         <start_time type="ISO8601">{start time of measurement}
         </start_time>
         <NXinstrument name="instrument">
            <NXcrystal name="{Name of Monochromator Crystal}">
           <wavelength type="NX_FLOAT32" units="Angstroems">
                   {nominal wavelength selected}
               </wavelength>
            </NXcrystal>
            <NXdetector name="{Name of Detector}">+
           <polar_angle type="NX_FLOAT32[np]" axis="1">
                 {Polar Angle, or two theta as an array with values for each scan point}
               </polar_angle>
           <data type="NX_INT32[np,xdim,ydim]" signal="1" axes="polar_angle">
              {The counts detected in the area detector, np is the
                    number of scan points}
           </data>
               <distance units="mm" type="NX_FLOAT">
                 {distance to sample position}
               </distance>
               <pixel_offset_x units="mm" type="NX_FLOAT[]">
                {offsets of each pixels centers x-value  to the detector center}
               </pixel_offset_x>
               <pixel_offset_y units="mm" type="NX_FLOAT[]">
                {offsets of each pixels centers y-value  to the detector center}
               </pixel_offset_y>
            </NXdetector>
         </NXinstrument>
         <NXmonitor name="control">
            <mode type="NX_CHAR">monitor | timer</mode>
            <preset type="NX_FLOAT32">
              {preset value for monitor or timer}
            </preset>
            <data type="NX_INT32[np]">
              {Monitor counts at each scan point}
            </data>
         </NXmonitor>
        <NXsample name="{Name of Sample">
         <name type="NX_CHAR">
          {Descriptive name of sample}
         </name>
         <rotation_angle type="NX_FLOAT[np]" units="degree">
            { Sample rotation, also known as omega }
         </rotation>
         <chi type="NX_FLOAT[np]" units="degree">
            { chi angle }
         </chi>
         <phi type="NX_FLOAT[np]" units="degree">
            { phi angle }
         </phi>
         <orientation_matrix type="NX_FLOAT32[3,3]">
           {Orientation matrix of single crystal according to conventions
            established by Busing, Levy, 1967 }
          </orientation_matrix>
          <miller_indices type="NX_FLOAT[3]">?
           { Miller indices of the target reflection}
          </miller_indices>
       </NXsample>
       <NXdata name="{Name of Data Block}">+
          <data type="NX_INT32[np,xdim,ydim]" signal="1">
             {Link to detector counts in NXdetector}
          </data>
          <polar_angle type="NX_FLOAT32[np]" axis="1">
             {Link to polar angle data in NXdetector}
          </polar_angle>
          <pixel_offset_x units="mm" type="NX_FLOAT[]">
              {Link to pixel_offset_x in NXdetector}
          </pixel_offset_x>
           <pixel_offset_y units="mm" type="NX_FLOAT[]">
              {Link to pixel_offset_y in NXdetector}
          </pixel_offset_y>
       </NXdata>
      </NXentry>
    </NXroot>

