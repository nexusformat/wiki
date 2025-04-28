---
title: IndirectDiscuss
permalink: IndirectDiscuss.html
layout: wiki
---

This file is from the old SWIKI and a starting point for discussion ...
the idea is to come up with a definition based on inheritance from other
definitions such as [TOFRaw](TOFRaw.html "wikilink")

     
    NXtofnigs.xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    URL: http://http://www.neutron.anl.gov:8080/NeXus/88
    Editor: Martyn Bull (m.j.bull@rl.ac.uk)
    Version 1: 2004-10-18
    $Id$

    Instrument Definition for a Time-of-flight Inverse Geometry Spectrometer

    One of the interesting things about this definition is the need to
    decouple notions of logical neutron path in describing the instrument,
    and instead to consider the instrument symmetry. This is a very 
    different approach to constructing instrument definition files for 
    Monte Carlo simulations.

    The result is that analysers, collimators and filters are considered 
    in much the same way as banks of detectors. This leads to an implied 
    order and relationship between 'arms' of the instrument, which is 
    currently not handled by the definition. For example, it is implied 
    that the collimator in position 1 of the collimator bank array is 
    associated with the analyser in position 1 and the detector in 
    position 1. Currently, if these positions are mixed up, then it is 
    only by reconstructing the instrument via the (x,y,z) positions of 
    each element, and visually examining the result that any sense will be 
    made of the description.


    Primary spectrometer: refers to all components upstream of sample position
    Secondary spectrometer: refers to all components downstream of sample position

          *   Element may occur 0 or more times
          +   Element may occur one or more times (i.e. at least once)
          ?   Element may occur 0 or one times (i.e. no more than once)

    -->

    <NXinstrument name="TOFNIGS">
        <name short_name="{abbreviated name of instrument}">{Name of instrument}</name>
        <!-- I'm guessing here that "short_name" is something like 'IRIS'? -->

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

        <!--Primary Spectrometer-->
        
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
            <!-- 2004-10-18 MJB This is a T0 blocking chopper phased to the source to block fast neutron and gamma flash.
                                              None of the existing chopper types meets this requirement. 
                                              In fact, why don't we just have one chopper class?
                                              We don't have different detector classes for different varieties.-->
        </NXt0_chopper>
        
        <NXdisk_chopper name="{Name of disk chopper}">*
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

        <!-- Reference Sample position for clarity. Could be an isolated NXGeometry instance-->
        <NXsample name="samplePosition">
            <NXgeometry name="geometry">
                <description type="NX_CHAR">{Coordinate system reference marker}</description>
                <component_index type="NX_INT">0</component_index>
            </NXgeometry>
        </NXsample>

        <!-- Secondary Spectrometer-->
        <!-- In secondary spectrometer, index order is assumed to be consistently applied eg analyser 1 will be associated with detector 1, filter 1, collimator 1 etc. -->
        
        <NXfilter name="(Name of filter bank}">*
            <!--More than one instance of NXfilter may be needed if filters are placed both before and after analysers, or in incident beam-->
            <!--Physical properties-->
            <description type="NX_CHAR[i]">{"Beryllium" | "Pyrolytic Graphite" | "Graphite" | "Sapphire" | "Silicon"}?</description>
            <status type="NX_CHAR[i]"> {in | out}?</status>
            <transmission type="NXdata[i]">{Wavelength transmission profile of filter}?</transmission>
            <temperature type="NX_FLOAT[i]" Units="Kelvin">{average/nominal filter temperature}</temperature>
            <temperature_log type="NXlog[i]">{Linked temperature_log for the filter}?</temperature_log>
            <sensor_type type="NXsensor[i]">{Sensor(s) used to monitor the filter temperature}?</sensor_type>
            <unit_cell type="NX_FLOAT[i,6])">{Unit cell parameters for single crystal filter(lengths and angles)}?</unit_cell>
            <unit_cell_volume type="NX_FLOAT[i]" units="Angstroms3" rank="1">{Unit cell}?</unit_cell_volume>
            <orientation_matrix type="NX_FLOAT[i,6]">{Orientation matrix of single crystal filter}?</orientation_matrix>
            <!--Geometrical properties-->
            <NXgeometry name="geometry">{Position and orientation of filters within bank}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[i,3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[i,6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR[i]">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[i,nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of filter bank along beam path}</component_index>
            </NXgeometry>
        </NXfilter>

        <NXcollimator name="{Name of collimator bank}">*
            <!--More than one instance of NXcollimator may be needed if collimators are placed both before and after analysers, or in incident beam-->
            <!--Physical properties-->
            <type type="NX_CHAR[i]">"Soller"|"radial"</type>
            <divergence_x type="NX_FLOAT[i]" units="radians" exponent="?">{divergence of collimator in local x direction}</divergence_x>
            <divergence_y type="NX_FLOAT[i]" units="radians" exponent="?">{divergence of collimator in local y direction}?</divergence_y>
            <blade_thickness type="NX_FLOAT[i]" units="metre" exponent="?">{thickness of absorbing blades}?</blade_thickness> 
            <blade_spacing type="NX_FLOAT[i]" units="metre" exponent="?"> {gap between absorbing blades}?</blade_spacing> 
            <absorbing_material type="NX_CHAR[i]">{coating on or complete material of blades}?</absorbing_material> 
            <transmitting_material type="NX_CHAR[i]">{material separating absorbing blades}?</transmitting_material>
            <!--Geometrical properties--> 
            <NXgeometry name="geometry">{Position and orientation of collimators within bank}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[i,3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[i,6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR[i]">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[i,nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of collimator bank along beam path}</component_index>
            </NXgeometry>
        </NXcollimator>

        <NXcrystal name="{Name of crystal analyser bank}">+
            <!--More than one instance of NXcrystal may be needed for multi-analyser instruments eg. double-analyser instruments-->
            <!-- Indices are: i - detector number counting integer, x-axis counter; j,k - y,z-axis counters;l - time channel counting integer -->
            <!-- Units: measurement quantity; Exponent: power of 10 to be applied to values. eg. exponent="-3" means values are given in millimetres-->
            <!--Physical properties-->
            <type type="NX_CHAR[i]">{ "PG (Highly Oriented Pyrolytic Graphite)" | "Ge" | "Si" | "Cu" | "Fe3Si" | "CoFe" | "Cu2MnAl (Heusler)" | "Multilayer" }</type>
            <mosaic_horizontal type="NXFLOAT[i]" units="radians">{horizontal mosaic Full Width Half Maximum}?</mosaic_horizontal>
            <mosaic_vertical type="NXFLOAT[i]" units="radians">{vertical mosaic Full Width Half Maximum}?</mosaic_vertical>
            <wavelength type="NX_FLOAT[i]" units="metre" exponent="?">{Optimum diffracted wavelength}</wavelength>
            <bragg_angle type="NX_FLOAT[i]" units="radians">{Bragg angle of nominal reflection}</bragg_angle>
            <lattice_parameter type="NX_FLOAT[i]" units="metre" exponent="?">{Lattice parameter of the nominal reflection}?</lattice_parameter>
            <scattering_vector type="NX_FLOAT[i]" units="metre" exponent="?">{Scattering vector, Q, of nominal reflection}?</scattering_vector>
            <unit_cell type="NX_FLOAT[i,6])">{Unit cell parameters (lengths and angles)}?</unit_cell>
            <unit_cell_volume type="NX_FLOAT[i]" units="Angstroms3" rank="1">{Volume of the unit cell}?</unit_cell_volume>
            <reflection type="NX_INT[i,3]">{(hkl) values of nominal reflection}?</reflection>
            <temperature type="NX_FLOAT[i]" Units="Kelvin">{average/nominal crystal temperature}?</temperature>
            <temperature_log type="NXlog[i]">{log file of crystal temperature}?</temperature_log>
            <reflectivity type="NXdata[i]">{crystal reflectivity versus wavelength}?</reflectivity>
            <transmission type="NXdata[i]">{crystal transmission versus wavelength}?</transmission>
            <!-- Geometrical properties-->
            <!-- 2004-10-18 MJB Defining properties this way, can cope with a curved array of segments focussed on one detector, and repeated-->
            <segment_width type="NX_FLOAT[i]" units="metre">{Horizontal width of individual segment}?</segment_width>
            <segment_height type="NX_FLOAT[i]" units="metre">{Vertical height of individual segment}?</segment_height>
            <segment_thickness type="NX_FLOAT[i]" units="metre">{Thickness of individual segment}?</segment_thickness>
            <segment_gap type="NX_FLOAT[i]" units="metre">{Typical gap between adjacent segments}?</segment_gap>
            <segment_columns type="NXFLOAT[i]" units="metre">{number of segment columns in horizontal direction}?</segment_columns>
            <segment_rows type="NXFLOAT[i]" units="metre">{number of segment rows in vertical direction}?</segment_rows>
            <curvature_horizontal type="NX_FLOAT[i]" units="radians">{Horizontal curvature of focusing crystal}?</curvature_horizontal>
            <curvature_vertical type="NX_FLOAT[i]" units="radians">{Vertical curvature of focusing crystal}?</curvature_vertical>
            <cut_angle type="NXFLOAT" units="degrees">{Cut angle of reflecting Bragg plane and plane of crystal surface}?</cut_angle>
            <NXgeometry name="geometry">{Position and orientation of crystals within bank}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[i,3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[i,6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR[i]">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[i,nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of analyser bank along beam path}</component_index>
            </NXgeometry>
        </NXcrystal>

        <NXdetector name="{Name of detector bank}">+
            <!-- 2004-10-18 MJB Major hacking around of NXdetector to make sense of it.-->
            <!-- Indices are: i - detector number counting integer, x-axis counter; j,k - y,z-axis counters;l - time channel counting integer -->
            <!-- Units: measurement quantity; Exponent: power of 10 to be applied to values. eg. exponent="-3" means values are given in millimetres-->
            <!--Physical properties-->
            <detector_number type="NX_INT[i]">{Identifier for detector}</detector_number>
            <description type="NX_CHAR[i]">{name/manufacturer/model/etc. information}?</description>
            <gas_pressure type="NX_FLOAT[i]" units="pascal" exponent="?">{Detector gas pressure}?</gas_pressure>
            <detection_gas_path type="NX_FLOAT" units="metre" exponent="?">{maximum drift space dimension}?</detection_gas_path>
            <crate type="NX_INT[i]" local_name="{Equivalent local term}">{Crate number of detector}?</crate>
            <slot type="NX_INT[i]" local_name="{Equivalent local term}">{Slot number of detector}?</slot>
            <input type="NX_INT[i]" local_name="{Equivalent local term}">{Input number of detector}?</input>
            <type type="NX_CHAR[i]">{"He3 gas cylinder"|He3 PSD"|"He3 planar multidetector"| "He3 curved multidetector"| "multi-tube He3 PSD"|"BF3 gas"|"scintillator"?</type>
            <!-- 2004-10-18 MJB A lot of these detector types are replicas of each other-->
            <!-- Geometrical properties-->
            <distance type="NX_FLOAT[i]">{Total distance from sample position to detector through secondary spectrometer}</distance>        
            <NXgeometry name="geometry">{Position and orientation of detector elements in bank}?
                <NXtranslation name="?">
                    <value type="NX_FLOAT[i,3]" units="metre" exponent="?">{(x,y,z) position coordinates relative to origin at sample position}?</value>
                </NXtranslation>
                <NXorientation name="?">
                    <value type="NX_FLOAT[i,6]">{The orientation information is stored as direction cosines relative to origin at sample position.}</value>
                </NXorientation>
                <NXshape name="{name of shape}">
                    <shape type="NX_CHAR[i]">{"nxcylinder", "nxbox", "nxsphere", ...}?</shape>
                    <size type="NX_FLOAT[i,nshapepar]" units="metre" exponent="?">{ nshapepar dimensions for selected shape}?</size>
                </NXshape>
                <component_index type="NX_INT">{Sequential order of detector bank along beam path}</component_index>
             </NXgeometry>
            <!--Timing properties-->
            <time_of_flight type="NX_FLOAT[l+1]" units="second" exponent="?">{Total time of flight from sample position to detector through secondary spectrometer}</time_of_flight>
            <dead_time type="NX_FLOAT[i]" units="second" exponent="?">{Detector dead time}?</dead_time>
            <hold_off type="NX_FLOAT[i]" units="second" exponent="?">{Delay in detector registering an event}?</hold_off>
            <calibration_date type="ISO8601">{date of last calibration (geometry and/or efficiency)  measurements}?</calibration_date>
            <calibration_method type="NXnote">{details of the calibration method}?</calibration_method>
            <NXdata name="efficiency">{Efficiency of detector with respect to e.g. wavelength}?</NXdata>
        </NXdetector>
        
        <NXbeam_stop name="">*</NXbeam_stop>?

    </NXinstrument>
