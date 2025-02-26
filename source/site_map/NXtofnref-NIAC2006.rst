Concerns
--------

- Mono and TOF reflectometry must inherit from a common base class; the current definition of `tofnref` inheriting from `monoref` leaves the definition of the monochromator in the TOF definition.

- SNS Liquids has two monitors, but our definitions only have one. Both are not always active.

.. raw:: xml

   <?xml version="1.0" ?>
   <!--
   Instrument Definition for a Time of Flight Neutron Reflectometer
   Refines monochromatic reflectometer.

   Editor: Robert Dalgliesh <r.m.dalgliesh@rl.ac.uk>
   Initial version: October 2004
   $Id$

   See http://www.neutron.anl.gov:8080/NeXus/5 for component definitions.

   2005-04-28 Paul Kienzle <pkienzle@nist.gov>
   * Only include information that may be used for reduction/analysis
   * Make it a subclass of NXmonoref
   2006-02-03 Paul Kienzle <pkienzle@nist.gov>
   * Inherit more from NXmonoref.
   -->

   <NXentry>
     <definition version="1.0" URL="http://www.nexus.anl.gov/instruments/xml/NXtofnref.xml">
       NXtofnref
     </definition>

     <NXinstrument>
       <NXmoderator name="{Name of moderator}">
         <distance type="NX_FLOAT" units="metre">
           { Distance from T₀ to sample along beam-path. To calculate wavelength:
             L[i] = wavelength at time T[i]
             T[i] = time of flight for point i.
             d1 = distance from moderator to sample along beam path
             d2 = distance from detector to sample along beam path
             h = Planck's constant
             mₙ = mass of the neutron

             L[i] = h/mₙ * T[i]/(d1+d2)
           }
         </distance>
         <pulse_shape type="NXdata">
           { Find the center of mass of the pulse shape and use that
           as the T₀ offset with respect to the protons hitting the target.
           The TOF from target (which is the real T₀) to the moderator is
           insignificant compared to the uncertainty from the pulse shape and
           so can be ignored.
           }
         </pulse_shape>
       </NXmoderator>

       <NXguide name="{Name of guide section}">*
         { Guides in total or in segments through to sample position; may be
           interspersed between other components - Check component index.
           Can be nested for guides with multiple straight segments.

           Affects wavelength spectrum, both in divergence and intensity. The
           spectrum scan will automatically compensate for intensity effects.
           To compute divergence effects, detailed information about the guide
           geometry will be required.
         }
       </NXguide>

       <!--
         Some instruments will require gravitational corrections. Neutrons
         travel on a parabolic trajectory. For long-wavelength neutrons
         this changes incident and reflected angle and results in the
         neutron appearing on a lower detector pixel than expected. The
         information required for these corrections comes from the instrument
         geometry.
       -->

       <NXchopper name="[T₀_chopper|frame_overlap_chopper]">?
         <wavelength_range type="NX_FLOAT[2]" units="Angstrom">
           { Reduction software needs to ignore Q values outside the range
             defined by the choppers. The T₀ chopper is phased to the source
             to block fast neutron and gamma flash. The frame overlap
             chopper is set to select low-wavelength neutrons (those from
             the current pulse) or high-wavelength neutrons (those from
             the previous pulse.

             On a properly tuned instrument, the time bins recorded in
             the detector will reflect the actions of the choppers and
             these fields can be ignored.
           }
         </wavelength_range>
       </NXchopper>
       <NXmirror name="frame_overlap_mirror">?
         <cutoff_wavelength mode="above|below">
           <!-- *** This is not part of standard NXmirror -->
           { The frame overlap mirror is used to eliminate very long wavelength
             neutrons from previous pulses. Together with the choppers, this
             helps to choose which pulse to use in the TOF calculations. On a
             properly tuned instrument the time bins recorded in the detector
             will account for the actions of the mirror.

             There will be some attenuation but this will be compensated for
             when correcting for the spectrum scan.

             For an ab initio calculation, you would need to store the angle
             with respect to the beam to compute the cutoff angle but often this
             will not be explicit since the instrument is simply tuned to have the
             correct cutoff.
           }
         </cutoff_wavelength>
       </NXmirror>

       <NXdetector name="detector">
         <time_of_flight
           type="NX_FLOAT[l+1]"
           units="10⁻⁶ second|10⁻⁷ second">
           { Total time of flight }
         </time_of_flight>
       </NXdetector>
     </NXinstrument>

     <NXdata>
       <time_of_flight type="NX_FLOAT[k]" units="second"
         NAPIlink="entry/instrument/detector/time_of_flight"/>
     </NXdata>
   </NXentry>
