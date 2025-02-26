==================
NXmonoref-NIAC2006
==================


The following is the proposed monochromatic reflectometry definition.

Concerns:
----------

- Using classes rather than names in links (e.g., NXdetector) will break if the user adds another detector group to the entry.

- I don't record whether the reflectometer is horizontal or vertical geometry, but with slit and angles defined relative to the sample surface, this doesn't matter.

- I'm asking the control software to write the wavelength divergence into the file so that the user can read it off directly without performing calculations.

- Not recording the region of interest used to measure count duration. Could create a virtual detector for this.

- Normalization by monitor/timer is not currently supported.

- For backgrounds, don't know if the nominal Qz should be calculated from the theta or twotheta. The correct choice depends on the source of background.

Example:
--------

`[NXmonoref_example-NIAC2006] <NXmonoref_example-NIAC2006.html>`__

.. code-block:: xml

    <?xml version="1.0" ?>
    <!--
    Instrument Definition for Monochromatic Source Reflectometers.
    Editor: Paul Kienzle <pkienzle@nist.gov>
    Mangled_by: Nick Maliszewskyj <nickm@nist.gov>
    $Id$
    See http://www.neutron.anl.gov:8080/NeXus/5 for component definitions.

    2006-02-03 Refined by NIAC group meetings.
    -->

    <NXentry>

      <definition version="1.0" URL="http://www.nexus.anl.gov/instruments/xml/monoref.xml">
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


      <NXsample>
        <polar_angle type="NX_FLOAT[i]" units="degrees">?
           {Angle relative to the scattering plane, not to gravity.}
        </polar_angle>
        <momentum_transfer type="NX_FLOAT[i]">{|Q|}?</momentum_transfeer>
      </NXsample>


      <NXinstrument>

        <!-- wavelength selection -->
        <NXcrystal name="monochromator">
          <!-- May want to include fields required to compute the wavelength L, and spread dL -->
          <wavelength />
          <wavelength_spread type="NX_FLOAT" units="Angstrom" />
        </NXcrystal>

        <!-- collimation -->
        <NXaperture name="pre[sample|detector]_slit#">
          <NXgeometry name="geometry">?
            <NXtranslation name="translation">
              <distances type="NX_FLOAT" units="mm">
                { Location of slit along beamline (midway between slits
                  if slits are not coplanar).  This is required to compute
                  instrument resolution. }
              </distances>
            </NXtranslation>
            <NXshape name="shape">
              <shape>
                { Need to add "nxslit" to list of possible shapes.  If the
                  shape is a box, first dimension changes the sample footprint. }
              </shape>
              <size type="NX_FLOAT[nshapepars,np]" units="mm" />
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
        <NXbeam_stop>?
          { Need all fields so that we can calculate shadow of beam stop on detector. }
        </NXbeam_stop>

        <NXdetector>
          <polar_angle type="NX_FLOAT[np]>
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

      <NXmonitor>?
        <momentum_transfer NAPIlink="NXentry/NXsample/momentum_transfer" />
        <presample_slit1 NAPIlink="NXentry/presample_slit1/NXgeometry/NXshape/size" />
        <data type="FLOAT32[np]" signal=1 axes="momentum_transfer|presample_slit1" />
      </NXmonitor>

      <NXtimer>?</NXtimer>

      <NXdata>
        <!-- Scan identification tags for the specific measurement type -->
        <scan_type type="NX_CHAR">
          { "intensity"|"background"|"specular"|"rock"|"slice"|"area" }
        </scan_type>
        <polarization_crosssection type="NX_CHAR">?
          { "++"|"+-"|"-+"|"--"|"+"|"-" }
        </polarization_crosssection>

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
        <predetector_slit1 NAPIlink="NXentry/predetector_slit1/NXgeometry/NXshape/size">?<predetector_slit1>
        <predetector_slit2" NAPIlink="NXentry/predetector_slit2/NXgeometry/NXshape/size">?<predetector_slit2>

        <!-- Counts and monitors -->
        <counts NAPIlink="NXentry/NXdetector/counts" signal="1" axes="momentum_transfer|presample_slit1" />
        <count_start NAPIlink="NXentry/NXtimer/start">?</count_start>
        <count_duration NAPIlink="NXentry/NXtimer/duration">?</count_duration>
        <monitor NAPIlink="NXentry/NXmonitor/data">?</count_monitor>
      </NXdata>

      <NXlog name="">*
        { Various logs for temperature, field, etc. which are assumed to
          be constant over the duration of the run.  The reduction program
          should be able to display their values on a parallel graph.  Note
          that logs are not necessarily sampled synchronously with the
          data points. }
      </NXlog>

    </NXentry>
