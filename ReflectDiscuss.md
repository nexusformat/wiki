---
title: ReflectDiscuss
permalink: ReflectDiscuss/
layout: wiki
---

Three files as a starting point for discussion ... the idea is to come
up with reflectometer definitions based on inheritance from other
definitions such as [TOFRaw](TOFRaw "wikilink")


    <?xml version="1.0" ?>
    <!--
    Instrument Definition for Reflectometers.
    Editor: Paul Kienzle <pkienzle@nist.gov>
    Mangled_by: Nick Maliszewskyj <nickm@nist.gov>
    $Id$
    See http://www.neutron.anl.gov:8080/NeXus/5 for component definitions.

    2006-02-03 Refined by NIAC group meetings.
    -->

    <NXentry>

      <NXcharacterization name="intensity#">*
        <type>intensity</type>
        {Suggested spectrum measurement for intensity vs. wavelength
         for a given slit setting.  Warning: beam profile is not 
         regular, but this effect is accomodated in the spectrum measurement.
         May measure monitor versus detector or monitor vs. monitor or
         simply absolute detector counts for a particular slit setting.}
      </NXcharacterization>
      <NXcharacterization name="background#">*
        <type>background</type>
        {Suggested background measurement; needed for point detector measurements}
      </NXcharacterization>
      <NXcharacterization name="background*">*
        <type>background</type>
        {Suggested background measurement}
      </NXcharacterization>


      <NXsample name="sample">
        <polar_angle type="NX_FLOAT[i]" units="degrees">?
           {Angle relative to the scattering plane, not to gravity.}
        </polar_angle>
        {Reflectometry characterization of samples is much more complex than
        given in NXsample.}
      </NXsample>


      <NXinstrument>

        <!-- collimation -->
        <NXaperture name="pre[sample|detector]_slit#">
          <opening type="FLOAT32[1|2]" units="mm" />
            {Slits defining the beam width and possibly the height relative
             to the surface of the sample.}
          <distance type="FLOAT32" units="m" />
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
        <NXbeam_stop>?
          { Need all fields so that we can calculate shadow of beam stop on detector. }
        </NXbeam_stop>

        <NXdetector>
          <polar_angle type="NX_FLOAT[np]">
            { Angle of the detector relative to the scattering plane. }
          </polar_angle>
          <azimuthal_angle type="NX_FLOAT" units="degrees">
            { Indicate sense of scattering: 0 is front surface of sample, 
              180 is back surface of sample.  If 180, change the sign of the
              reflected angle in the data.  It is also possible for the beam
              to enter the substrate from the side and reflect off the back 
              surface of a film, in which case negative angles can be 
              interpreted as inverting the scattering length density profile
              of the film (after accounting for absorption in the substrate. }
          </azimuthal_angle>
          <counts />
        </NXdetector>

      </NXinstrument>

      <NXtimer>?</NXtimer>

      <NXdata>
        <!-- Scan identification tags for the specific measurement type -->
        <measurement type="NX_CHAR"> 
          { "intensity"|"background"|"specular"|"rock"|"slice"|"area" }
        </measurement>
        <polarization type="NX_CHAR">?
          { "++"|"+-"|"-+"|"--"|"+"|"-" }
        </polarization>

        <!-- Counts and monitors -->
        <data NAPIlink="NXentry/NXdetector/data" signal="1" />
        <monitor NAPIlink="NXentry/NXmonitor/data">?</monitor>
      </NXdata>

      <NXlog name="">*
        { Various logs for temperature, field, etc. which are assumed to
          be constant over the duration of the run.  The reduction program
          should be able to display their values on a parallel graph.  Note
          that logs are not necessarily sampled synchronously with the
          data points. }
      </NXlog>

    </NXentry>

    <NXentry>
      <definition version="1.0" URL="http://www.nexus.anl.gov/instruments/xml/monoref.xml">
        NXmonoref
      </definition>
      <start_time type="ISO8601" />

      <NXsample>
        <momentum_transfer type="NX_FLOAT[i]">{|Q|}?</momentum_transfer>
      </NXsample>
      

      <NXinstrument>
        <!-- wavelength selection -->
        <NXcrystal name="monochromator">
          <!-- May want to include fields required to compute the wavelength L, and spread dL -->
          <wavelength />
          <wavelength_spread type="NX_FLOAT" units="Angstrom" />
        </NXcrystal>
      </NXinstrument>


      <NXmonitor>?
        <momentum_transfer NAPIlink="NXentry/NXsample/momentum_transfer" />
        <presample_slit1 NAPIlink="NXentry/presample_slit1/NXgeometry/NXshape/size" />
        <data type="FLOAT32[np]" signal="1" axes="momentum_transfer|presample_slit1" />
      </NXmonitor>

      <NXtimer>?</NXtimer>

      <NXdata>
        <!-- Scan variables
           *** Note: these are renamed from their original location, which
           *** which is a problem with the current API.
           *** Maybe require some of these, e.g., theta, two theta, momentum transfer, presample_slit1.
         -->
        <theta NAPIlink="NXentry/NXsample/polar_angle">?</theta>
        <twotheta NAPIlink="NXentry/NXdetector/polar_angle">?</twotheta>
        <momentum_transfer NAPIlink="NXentry/NXsample/momentum_transfer">?</momentum_transfer>
        <presample_slit1 NAPIlink="NXentry/presample_slit1/NXgeometry/NXshape/size">?</presample_slit1>
        <presample_slit2 NAPIlink="NXentry/presample_slit2/NXgeometry/NXshape/size">?</presample_slit2>
        <predetector_slit1 NAPIlink="NXentry/predetector_slit1/NXgeometry/NXshape/size">?</predetector_slit1>
        <predetector_slit2 NAPIlink="NXentry/predetector_slit2/NXgeometry/NXshape/size">?</predetector_slit2>
        <count_start NAPIlink="NXentry/NXtimer/start">?</count_start>
        <count_duration NAPIlink="NXentry/NXtimer/duration">?</count_duration>

      </NXdata>
    </NXentry>

    <NXentry>
      <NXinstrument>
        <NXchopper name="[T0_chopper|frame_overlap_chopper]">?
          <wavelength_range type="NX_FLOAT[2]" units="Angstrom">
            { Reduction software needs to ignore Q values outside the range
              defined by the choppers.  The T0 chopper is phased to the source 
          to block fast neutron and gamma flash.  The frame overlap
          chopper is set to select low wavelength neutrons (those from
          the current pulse) or high wavelength neutrons (those from
          the previous pulse.

          On a properly tuned instrument, the time bins recorded in 
          the detector will reflect the actions of the choppers and
          these fields can be ignored. }
          </wavelength_range>
        </NXchopper>
        <NXmirror name="frame_overlap_mirror">?
          <cutoff_wavelength mode="above|below">
        <!-- *** This is not part of standard NXmirror -->
            { The frame overlap mirror is used to eliminate very long wavelength 
          neutrons from previous pulses.  Together with the choppers, this
          helps to choose which pulse to use in the TOF calculations.  On a 
          properly tuned instrument the time bins recorded in the detector
          will account for the actions of the mirror.

          There will be some attenuation but this will be compensated for 
          when correcting for the spectrum scan.

          For an ab initio calculation, you would need to store the angle 
          wrt the beam to compute the cutoff angle but often this will not
          be explicit since the instrument is simply tuned to have the
          correct cutoff. }
          </cutoff_wavelength>
        </NXmirror>
      </NXinstrument>
    </NXentry>
