---
title: ReflectDiscuss
permalink: ReflectDiscuss.html
layout: wiki
---
ReflectDiscuss
==============

Three files as a starting point for discussion ... the idea is to come
up with reflectometer definitions based on inheritance from other
definitions such as [TOFRaw](TOFRaw.html "wikilink")

-   outline the parts of tofraw needed for reflectometry.
-   create a reflectometry base
-   create a TOF reflectometry from base+tofraw

```xml


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
```
also one from the old SWIKI NXtofnref.xml

```xml    
    <?xml version="1.0" ?>
    <!--
    URL: http://www.neutron.anl.gov/nexus/xml/NX.xml
    Editor: Robert Dalgliesh <r.m.dalgliesh@rl.ac.uk>
    Initial version: October 2004
    $Id$

    Instrument Definition for a Polarised Time of Flight Neutron Reflectometer

    Please note this is a rough first draft.

    By removing the polarising elements you should be left with a description for a TOF reflectometer
    There are a number of  additional components such as guide fields and other collimation components which I have not included. 
    -->

    <NXinstrument name="TOFNIGS">
        <name short_name="{abbreviated name of instrument}">{Name of instrument}</name>
        <!-- I'm guessing here that "short_name" is something like 'CRISP'? -->

        <NXsource name="{Name of facility}">
            <NXgeometry name="geometry">
                <NXtranslation name="?">
                    <value type="NX_FLOAT[3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of target along beam path}</component_index>
                <description type="NX_CHAR">{Optional description/label}?</description>
                <component_index type="NX_INT">{Sequential order of component along beam path}?</component_index>
                <!--If using XML Schema instead would be able to denote that '0' cannot be selected for this component-->
            </NXgeometry>
        </NXsource>

        <NXmoderator name="{Name of moderator}">
            <NXgeometry name="geometry">{"Engineering" position of moderator}?</NXgeometry>
            <distance type="NX_FLOAT">{Effective distance as seen by measuring radiation}?</distance>
                <!-- 2004-10-18 MJB Distance from where? The sample or the target? Can this be combined with NXGeometry? What is engineering position?-->
            <type type="NX_CHAR">{ "H20" | "D20"  |  "Liquid H2"  | "Liquid CH4" | "Liquid D2" | "Solid D2" | "C" |"Solid CH4" | "Solid H2"}?</type>
            <poison_depth type="NX_FLOAT" units="metre" exponent="?">{Poison depth}?</poison_depth>
            <coupled type="NX_BOOLEAN">{whether the moderator is coupled}?</coupled>
            <poison_material type="NX_CHAR">{ Gd | Cd |...}</poison_material>
            <temperature type="NX_FLOAT" Units="Kelvin" exponent="?">{average/nominal moderator temperature}</temperature>
            <temperature_log type="NXlog">{log file of moderator temperature}</temperature_log>
            <pulse_shape type="NXdata">{moderator pulse shape}</pulse_shape>
            <!--Geometrical properties-->
            <NXgeometry name="geometry">{Position and orientation of moderator}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of moderator along beam path}</component_index>
            </NXgeometry>
        </NXmoderator>

        <NXGuide name="{Name of guide section}">*
            <!--Guides in total or in segments thgrough to sample position; may be interspersed between other components - Check component index-->
            <!--Can be nested for guides with multiple straight segments-->
            <description type="NX_CHAR">{}</description> 
            <incident_angle type="NX_FLOAT">{}</incident_angle> 
            <reflectivity type="NXdata">{Reflectivity as function of wavelength [nsurf,i]}</reflectivity> 
            <bend_angle_x type="NX_FLOAT">{}</bend_angle_x> 
            <bend_angle_y type="NX_FLOAT">{}</bend_angle_y> 
            <interior_atmosphere type="NX_CHAR">"vacuum"|"helium"|"argon"</interior_atmosphere> 
            <external_material type="NX_CHAR">{external material outside substrate}</external_material> 
            <m_value type="NX_FLOAT[nsurf]">{}</m_value> 
            <substrate_material type="NX_FLOAT[nsurf]">{}</substrate_material> 
            <substrate_thickness type="NX_FLOAT[nsurf]">{}</substrate_thickness> 
            <coating_material type="NX_FLOAT[nsurf]">{}</coating_material> 
            <substrate_roughness type="NX_FLOAT[nsurf]">{}</substrate_roughness> 
            <coating_roughness type="NX_FLOAT[nsurf]">{}</coating_roughness> 
            <number_sections type="NX_INT">{number of substrate sections}</number_sections> 
            <!--Geometrical properties-->
            <NXgeometry name="geometry">{Position and orientation of guide}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of guide along beam path}</component_index>
            </NXgeometry>
        </NXGuide>


        <NXt0_chopper name="{Name of chopper}">?
            <!-- 2004-10-18 MJB+RMD This is a T0 blocking chopper phased to the source to block fast neutron and gamma flash.
                                              None of the existing chopper types meets this requirement. 
                                              In fact, why don't we just have one chopper class?
                                              We don't have different detector classes for different varieties.-->
        </NXt0_chopper>
        
        <NXdisk_chopper name="{Name of disk chopper}">
            <!--Some instruments can have multiple choppers in the incident beam-->
            <type type="NX_CHAR">{Chopper type single|contra_rotating_pair|synchro_pair}?</type>
            <rotation_speed type="NX_FLOAT" units="hertz" exponent="?">{chopper rotation speed}?</rotation_speed>
            <slits type="NX_INT">{Number of slits}</slits>
           <slit_angle type="NX_FLOAT" units="radians" exponent="?">{angular opening}</slit_angle>
           <pair_separation type="NX_FLOAT" units="metre" exponent="?"> {disc spacing in direction of beam}?</pair_separation>
           <radius type="NX_FLOAT" units="metre" exponent="?"> {radius to centre of slit}</radius>
           <slit_height type="NX_FLOAT" units="metre" exponent="?"> {total slit height}</slit_height>
           <phase type="NX_FLOAT" units="radians" exponent="?">{chopper phase angle}? </phase>
           <ratio type="NX_INT">{pulse reduction factor of this chopper in relation to other choppers/fastest pulse in the instrument}?</ratio>
           <distance type="NX_FLOAT" units="metre" exponent="?"> {Effective distance to the origin}?</distance>
           <wavelength_range type="NX_FLOAT[2]" units="metre" exponent="?">{low and high values of wavelength range transmitted}?</wavelength_range>
            <!--Geometrical properties-->
            <NXgeometry name="geometry">{Position and orientation of chopper}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of chopper along beam path}</component_index>
            </NXgeometry>
        </NXdisk_chopper>   
        
        <NXaperture name="{Name of beamline aperture}">*        
            <material type="NX_CHAR">{Absorbing material of the aperture}?</material>
            <description type="NX_CHAR">{Description of aperture}?</description>
            <!--Geometrical properties-->
            <NXgeometry name="geometry">{Position and orientation of aperture}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of aperture along beam path}</component_index>
            </NXgeometry>
        </NXaperture>
        
        <NXmonitor name="{Name of monitor}">+
            <type type="NX_CHAR">"Fission Chamber"|"Scintillator"?</type>
            <mode type="NX_CHAR">"monitor"|"timer"?</mode>
            <preset type="NX_FLOAT">{preset value for time or monitor}?</preset>
            <distance type="NX_FLOAT" units="metre" exponent="?">{Distance of monitor from sample position}?</distance>
            <efficiency type="Nxdata">{Monitor efficiency as a function of wavelength}?</efficiency>
            <sampled_fraction type="NX_FLOAT" units="dimensionless">{Proportion of incident beam sampled by the monitor}</sampled_fraction>
            <!--Geometrical properties-->
            <NXgeometry name="geometry">{Position and orientation of monitor}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of monitor along beam path}</component_index>
            </NXgeometry>
        </NXmonitor>

        <NXmirror name="{Name of supermirror}">
            <!-- Frame overlap mirror -->
            <description type="NX_CHAR">{}</description> 
            <incident_angle type="NX_FLOAT">{}</incident_angle> 
            <reflectivity type="NXdata">{Reflectivity as function of wavelength}</reflectivity> 
            <bend_angle_x type="NX_FLOAT">{}</bend_angle_x> 
            <bend_angle_y type="NX_FLOAT">{}</bend_angle_y> 
            <interior_atmosphere type="NX_CHAR">"vacuum"|"helium"|"argon"</interior_atmosphere> 
            <external_material type="NX_CHAR">{external material outside substrate}</external_material> 
            <m_value type="NX_FLOAT">{}</m_value> 
            <substrate_material type="NX_CHAR">{}</substrate_material> 
            <substrate_thickness type="NX_FLOAT">{}</substrate_thickness> 
            <coating_material type="NX_CHAR">{}</coating_material> 
            <substrate_roughness type="NX_FLOAT">{}</substrate_roughness> 
            <coating_roughness type="NX_FLOAT">{}</coating_roughness> 
            <!--Geometrical properties-->
            <NXgeometry name="geometry">{Position and orientation of mirror}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of aperture along beam path}</component_index>
            </NXgeometry>
        </NXmirror>

        <NXpolarizer name="{Name of supermirror}">*
            <!-- Polarising Supermirror -->
            <!-- Not sure how best to deal with this. A polarising supermirror needs the properties of NXmirror
            the NXData class should hopefully be able to take care of the polarisation dependent wavelength spectra 
            In addition the mirror may operate in reflection or transmission geometry which would add the need for an
            absorption correction.
            -->
            <description type="NX_CHAR">{}</description> 
            <incident_angle type="NX_FLOAT">{}</incident_angle> 
            <reflectivity type="NXdata">{Reflectivity as function of wavelength}</reflectivity> 
            <bend_angle_x type="NX_FLOAT">{}</bend_angle_x> 
            <bend_angle_y type="NX_FLOAT">{}</bend_angle_y> 
            <interior_atmosphere type="NX_CHAR">"vacuum"|"helium"|"argon"</interior_atmosphere> 
            <external_material type="NX_CHAR">{external material outside substrate}</external_material> 
            <m_value type="NX_FLOAT">{}</m_value> 
            <substrate_material type="NX_CHAR">{}</substrate_material> 
            <substrate_thickness type="NX_FLOAT">{}</substrate_thickness> 
            <coating_material type="NX_CHAR">{}</coating_material> 
            <substrate_roughness type="NX_FLOAT">{}</substrate_roughness> 
            <coating_roughness type="NX_FLOAT">{}</coating_roughness> 
            <!--Geometrical properties-->
            <NXgeometry name="geometry">{Position and orientation of polariser}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of aperture along beam path}</component_index>
            </NXgeometry>
        </NXmirror>

        <NXflipper name="{Name of flipper}">*
            <!-- This class may well need to be generalised to include spin manipulation devices such as neutators, precession coils and guide fields
            it would also be useful to have room for an NXData section for the wavelength dependent efficiency of the device
            -->
            <type type="NX_CHAR">{coil|current-sheet}?</type>
            <flip_turns type="NX_FLOAT">{Number of turns/cm in flipping field coils}?</flip_turns>
            <comp_turns type="NX_FLOAT">{Number of turns/cm in compensating field coils}?</comp_turns>
            <guide_turns type="NX_FLOAT">{Number of turns/cm in guide field coils}?</guide_turns>
            <flip_current type="NX_FLOAT" units="amperes">{Flipping field coil current in "on" state"}?</flip_current>
            <comp_current  type="NX_FLOAT" units="amperes">{Compensating field coil current in "on" state"}?</comp_current>
            <guide_current type="NX_FLOAT" units="amperes">{Guide field coil current in "on" state"}?</guide_current>
            <thickness type="NX_FLOAT" units="cm">{thickness along path of neutron travel}?</thickness>
            <!--Geometrical properties-->
            <NXgeometry name="geometry">{Position and orientation of flipper}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of aperture along beam path}</component_index>
            </NXgeometry>
        </NXflipper>

        <NXdetector name="{Name of detector bank}">+
            <time_of_flight type="NX_FLOAT[j+1]" axis="1" primary="1?"
          long_name="{Axis label}" units="10^-6 second|10^-7 second" link="{absolute path to location in NXdetector}">
          {Total time of flight}</time_of_flight>
            <detector_number type="NX_INT[i]" axis="2" primary="1?" long_name="{Axis label}" link="{absolute path to location in NXdetector}">{Identifier for detector}?</detector_number>
            <data type="NX_FLOAT[i,j,k?,l?]|NX_INT[i,j,k?,l?]" signal="1" axes="[time_of_flight,detector_number,x_offset?,y_offset?]?" long_name="{Title of measurement}?"
          check_sum="{Integral of data as check of data
          integrity} (NX_INT)?" units="number"  link="{absolute path to location in NXdetector}">
          {Data values}?</data>
            <data_error type="NX_FLOAT[i,j,k?,l?]|NX_INT[i,j,k?,l?]" units="number"  link="{absolute path to location in NXdetector}">
          {Data values}</data_error>
            <x_offset axis="3" primary="1?" type="NX_FLOAT[k+1]" units="10^-3
            meter|10^-2 meter" long_name="{Axis label}"  link="{absolute path to location in NXdetector}">{offset from the
            detector center in x-direction}?</x_offset>
            <y_offset axis="4" primary="1?" type="NX_FLOAT[l+1]" units="10^-3
            meter|10^-2 meter" long_name="{Axis label}"  link="{absolute path to location in NXdetector}">{offset from the
            detector center in the y-direction}?</y_offset>
            <distance type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?"></distance>
            <polar_angle type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?"></polar_angle>
            <azimuthal_angle type="NX_FLOAT[j,k?,l?]" axes="detector_number,x_offset?,y_offset?"></azimuthal_angle>
            <description type="NX_CHAR">{name/manufacturer/model/etc. information}?</description>
            <NXgeometry name="">{Position and orientation of detector element}?</NXgeometry>
            <translation type="NX_FLOAT[2]" units="centimeter">{translation normal to direct beam}?</translation>
            <solid_angle type="NX_FLOAT[i]" units="steradians">{Solid angle subtended by the detector at the sample}?</solid_angle>
            <x_pixelsize type="NX_FLOAT[i?]" units="mili*metre">{Size of each detector pixel. If it is scalar all pixels are the same size}?</x_pixelsize>
            <y_pixelsize type="NX_FLOAT[i?]" units="mili*metre">{Size of each detector pixel. If it is scalar all pixels are the same size}?</y_pixelsize>
            <dead_time type="NX_FLOAT[i]">{Detector dead time}?</dead_time>
            <hold_off type="NX_FLOAT[i]" units="micro.second">{Delay in detector registering an event}?</hold_off>
            <gas_pressure type="NX_FLOAT[i]" units="bars">{Detector gas pressure}?</gas_pressure>
            <detection_gas_path type="NX_FLOAT" units="cm">{maximum drift space dimension}?</detection_gas_path>
            <crate type="NX_INT[i]" local_name="{Equivalent local term}">{Crate number of detector}?</crate>
            <slot type="NX_INT[i]" local_name="{Equivalent local term}">{Slot number of detector}?</slot>
            <input type="NX_INT[i]" local_name="{Equivalent local term}">{Input number of detector}?</input>
            <type type="NX_CHAR">"He3 gas cylinder"|He3 PSD"|"He3 planar multidetector"| "He3 curved multidetector"| "multi-tube He3 PSD"|"BF3 gas"|"scintillator"|"fission chamber"?</type>
            <NXdata name="efficiency">{Efficiency of detector with respect to e.g. wavelength}?</NXdata>
            <calibration_date type="ISO8601">{date of last calibration (geometry and/or efficiency)  measurements}?</calibration_date>
            <calibration_method type="NXnote">{summary of conversion of array data to pixels  (e.g.
            polynomial approximations) and location of details of the calibrations}?</calibration_method>
            <!--Geometrical properties-->
            <NXgeometry name="geometry">{Position and orientation of aperture}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of aperture along beam path}</component_index>
            </NXgeometry>
        </NXdetector>
    </NXinstrument>
```        
