---
title: Monochromatic Neutron and X-ray Reflectometry
permalink: Monochromatic_Neutron_and_X-ray_Reflectometry/
layout: wiki
---

    <?xml version="1.0" ?>
    <!--
    Instrument Definition for Monochromatic Source Reflectometers.
    Editor: Paul Kienzle <pkienzle@nist.gov>
    Mangled_by: Nick Maliszewskyj <nickm@nist.gov>
    $Id$
    See http://www.neutron.anl.gov:8080/NeXus/5 for component definitions.
      
    Not handled: recording both the transmitted and the reflected beam off
    the polarizer onto the 2D detector.  Multiple analyzers is a similar
    problem.  In either case a solution similar to that in TAS can be applied.
      
    2006-02-03 Refined by NIAC group meetings.
    2006-10-04 Refined by NIAC group meetings.
    -->

    <NXentry>

      <definition version="1.0" 
          URL="http://www.nexusformat.org/instruments/xml/monoref.xml"
          instrument_geometry="vertical|horizontal"
          >
        NXmonoref
      </definition>
      <start_time type="ISO8601" />

      <NXcharacterization name="intensity">*
        {Suggested spectrum measurement for intensity vs. wavelength
         for a given slit setting.  Warning: beam profile is not 
         regular, but this effect is accomodated in the spectrum measurement}
      </NXcharacterization>
      <NXcharacterization name="background">*
        {Suggested background measurement}
      </NXcharacterization>

      <!-- Scan identification tags for the specific measurement type -->
      <measurement_type type="NX_CHAR">
          { "intensity"|"background"|"specular"|"rock"|"slice"|"area" }
      </measurement_type>

      <NXsample>
        <polar_angle type="NX_FLOAT[np]" units="degree">?
           {Angle relative to beam}
        </polar_angle>
        <polarization type="NX_CHAR">?
          { "++"|"+-"|"-+"|"--"|"+"|"-" }
        </polarization>
      </NXsample>


      <NXinstrument>
        <instrument_geometry>"vertical|horizontal"</instrument_geometry>

        <!-- wavelength selection -->
        <NXsource><probe /></NXsource>
        <NXmonochromator name="monochromator">
          <wavelength />
          <wavelength_error type="NX_FLOAT" units="Angstrom" />
        </NXmonochromator>

        <!-- collimation -->
        <NXaperture name="pre[sample|detector]_slit#">
          <NXgeometry name="geometry">?
            <NXtranslation name="translation">
              <distances type="NX_FLOAT" units="">
                { Location of slit along beamline (midway between slits 
                  if slits are not coplanar).  This is required to compute 
                  instrument resolution. }
              </distances>          
            </NXtranslation>
            <NXshape name="shape">
              <shape>"nxsquare"</shape>
              <size type="NX_FLOAT[np,nshapepars]" units="" />
            </NXshape>
          </NXgeometry>
        </NXaperture>

        <!-- 
          The polarizer-flipper-guidefield combination selects polarization vectors 
          in and out of the sample.  A number of scans are required to tune the 
          instrument so that polarization is either 'up' or 'down' on the sample.  
          On correctly tuned instruments the polarization angle selected should 
          be recorded by the flipper using polar_angle relative to the surface 
          (0/180 for +/-, or with out of plane polarization, 90/270 for +/-).  
          The polarization efficiency must be determined from a spectrum scan
          and the appropriate correction applied to the data.
          Raw values from the instrument, such as time dependent field applied
          to flipper coils or current on the current sheet can be recorded for
          specialized reduction programs which know how to handle them.

          In practice, these fields can be dropped because we are tagging the
          data entry with polarization ++, etc.
          -->
        <NXpolarizer name="presample_polarizer">?</NXpolarizer>
        <NXflipper name="presample_flipper">?</NXflipper>

        <NXpolarizer name="predetector_polarizer">?</NXpolarizer>
        <NXflipper name="predetector_flipper">?</NXflipper>


        <!-- detector may be protected by an attenuator and/or a beam stop -->
        <NXattenuator>?
          <attenuator_transmission />
        </NXattenuator>
        <NXbeam_stop>
          { Need all fields so that we can calculate shadow of beam stop on detector, and not use those pixels when calculating background. }?
        </NXbeam_stop>

        <NXdetector>
          <polar_angle type="NX_FLOAT[np]>
            { Angle of the detector relative to the scattering center. }
          </polar_angle>
          <azimuthal_angle type="NX_FLOAT" units="degree">
            { Indicate sense of scattering: 0 is front surface of sample, 
              180 is back surface of sample.  If 180, change the sign of the
              reflected angle in the data.  It is also possible for the beam
              to enter the substrate from the side and reflect off the back 
              surface of a film, in which case negative angles can be 
              interpreted as inverting the scattering length density profile
              of the film (after accounting for absorption in the substrate.
              90
            }
          </azimuthal_angle>
        </NXdetector>

      </NXinstrument>

      <NXdata>
        <!-- NXdata is broken and should not be required; propose dropping it -->

      </NXdata>

      <NXtimer>?
        <start_time type="NXFLOAT[np]" units="second">
          { Start of measurement relative to start of measurement }
        </start_time>
        <elapsed_time type="NXFLOAT[np]" units="second">
          { Elapsed time during measurement (in general not equal to count_time)
            because the detector may be off e.g., when the field is outside
            a particular range}
        </elapsed_time>
      </NXtimer>


      <NXlog name="">*
        { Various logs for temperature, field, etc. which are assumed to
          be constant over the duration of the run.  The reduction program
          should be able to display their values on a parallel graph.  Note
          that logs are not necessarily sampled synchronously with the
          data points; use NXtimer and plot data points vs. start_time}
      </NXlog>
      <NXlog name="elapsed">?
         <time type="FLOAT[np]" unit="second">{Start of the measurement of point np}</time>
         <value type="FLOAT[np]" unit="second">{Duration of the measurement of point}</value>
      </NXlog>

    </NXentry>
