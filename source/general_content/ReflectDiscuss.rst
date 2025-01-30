==============
ReflectDiscuss
==============


--- title: ReflectDiscuss permalink: ReflectDiscuss.html layout: wiki
--- Three files as a starting point for discussion ... the idea is to
come up with reflectometer definitions based on inheritance from other
definitions such as [TOFRaw](TOFRaw.html "wikilink") - outline the parts
of tofraw needed for reflectometry. - create a reflectometry base -
create a TOF reflectometry from base+tofraw
\* intensity {Suggested spectrum measurement for intensity vs.
wavelength for a given slit setting. Warning: beam profile is not
regular, but this effect is accomodated in the spectrum measurement. May
measure monitor versus detector or monitor vs. monitor or simply
absolute detector counts for a particular slit setting.} \* background
{Suggested background measurement; needed for point detector
measurements} \* background {Suggested background measurement} ? {Angle
relative to the scattering plane, not to gravity.} {Reflectometry
characterization of samples is much more complex than given in
NXsample.} {Slits defining the beam width and possibly the height
relative to the surface of the sample.} ? ? ? ? ? ? { Need all fields so
that we can calculate shadow of beam stop on detector. } { Angle of the
detector relative to the scattering plane. } { Indicate sense of
scattering: 0 is front surface of sample, 180 is back surface of sample.
If 180, change the sign of the reflected angle in the data. It is also
possible for the beam to enter the substrate from the side and reflect
off the back surface of a film, in which case negative angles can be
interpreted as inverting the scattering length density profile of the
film (after accounting for absorption in the substrate. } ? {
"intensity"\|"background"\|"specular"\|"rock"\|"slice"\|"area" } ? {
"++"\|"+-"\|"-+"\|"--"\|"+"\|"-" } ? \* { Various logs for temperature,
field, etc. which are assumed to be constant over the duration of the
run. The reduction program should be able to display their values on a
parallel graph. Note that logs are not necessarily sampled synchronously
with the data points. } NXmonoref {\|Q\|}? ? ? ? ? ? ? ? ? ? ? ? ? {
Reduction software needs to ignore Q values outside the range defined by
the choppers. The T0 chopper is phased to the source to block fast
neutron and gamma flash. The frame overlap chopper is set to select low
wavelength neutrons (those from the current pulse) or high wavelength
neutrons (those from the previous pulse. On a properly tuned instrument,
the time bins recorded in the detector will reflect the actions of the
choppers and these fields can be ignored. } ? { The frame overlap mirror
is used to eliminate very long wavelength neutrons from previous pulses.
Together with the choppers, this helps to choose which pulse to use in
the TOF calculations. On a properly tuned instrument the time bins
recorded in the detector will account for the actions of the mirror.
There will be some attenuation but this will be compensated for when
correcting for the spectrum scan. For an ab initio calculation, you
would need to store the angle wrt the beam to compute the cutoff angle
but often this will not be explicit since the instrument is simply tuned
to have the correct cutoff. } also one from the old SWIKI NXtofnref.xml
{Name of instrument} {(x,y,z) position coordinates relative to origin at
sample position}? {The orientation information is stored as direction
cosines relative to origin at sample position.} {"nxcylinder", "nxbox",
"nxsphere", ...}? { nshapepar dimensions for selected shape}?
{Sequential order of target along beam path} {Optional
description/label}? {Sequential order of component along beam path}?
{"Engineering" position of moderator}? {Effective distance as seen by
measuring radiation}? { "H20" \| "D20" \| "Liquid H2" \| "Liquid CH4" \|
"Liquid D2" \| "Solid D2" \| "C" \|"Solid CH4" \| "Solid H2"}? {Poison
depth}? {whether the moderator is coupled}? { Gd \| Cd \|...}
{average/nominal moderator temperature} {log file of moderator
temperature} {moderator pulse shape} {Position and orientation of
moderator}? {(x,y,z) position coordinates relative to origin at sample
position}? {The orientation information is stored as direction cosines
relative to origin at sample position.} {"nxcylinder", "nxbox",
"nxsphere", ...}? { nshapepar dimensions for selected shape}?
{Sequential order of moderator along beam path} \* {} {} {Reflectivity
as function of wavelength [nsurf,i]} {} {} "vacuum"\|"helium"\|"argon"
{external material outside substrate} {} {} {} {} {} {} {number of
substrate sections} {Position and orientation of guide}? {(x,y,z)
position coordinates relative to origin at sample position}? {The
orientation information is stored as direction cosines relative to
origin at sample position.} {"nxcylinder", "nxbox", "nxsphere", ...}? {
nshapepar dimensions for selected shape}? {Sequential order of guide
along beam path} ? {Chopper type
single|contra_rotating_pair|synchro_pair}? {chopper rotation speed}?
{Number of slits} {angular opening} {disc spacing in direction of beam}?
{radius to centre of slit} {total slit height} {chopper phase angle}?
{pulse reduction factor of this chopper in relation to other
choppers/fastest pulse in the instrument}? {Effective distance to the
origin}? {low and high values of wavelength range transmitted}?
{Position and orientation of chopper}? {(x,y,z) position coordinates
relative to origin at sample position}? {The orientation information is
stored as direction cosines relative to origin at sample position.}
{"nxcylinder", "nxbox", "nxsphere", ...}? { nshapepar dimensions for
selected shape}? {Sequential order of chopper along beam path} \*
{Absorbing material of the aperture}? {Description of aperture}?
{Position and orientation of aperture}? {(x,y,z) position coordinates
relative to origin at sample position}? {The orientation information is
stored as direction cosines relative to origin at sample position.}
{"nxcylinder", "nxbox", "nxsphere", ...}? { nshapepar dimensions for
selected shape}? {Sequential order of aperture along beam path} +
"Fission Chamber"\|"Scintillator"? "monitor"\|"timer"? {preset value for
time or monitor}? {Distance of monitor from sample position}? {Monitor
efficiency as a function of wavelength}? {Proportion of incident beam
sampled by the monitor} {Position and orientation of monitor}? {(x,y,z)
position coordinates relative to origin at sample position}? {The
orientation information is stored as direction cosines relative to
origin at sample position.} {"nxcylinder", "nxbox", "nxsphere", ...}? {
nshapepar dimensions for selected shape}? {Sequential order of monitor
along beam path} {} {} {Reflectivity as function of wavelength} {} {}
"vacuum"\|"helium"\|"argon" {external material outside substrate} {} {}
{} {} {} {} {Position and orientation of mirror}? {(x,y,z) position
coordinates relative to origin at sample position}? {The orientation
information is stored as direction cosines relative to origin at sample
position.} {"nxcylinder", "nxbox", "nxsphere", ...}? { nshapepar
dimensions for selected shape}? {Sequential order of aperture along beam
path} \* {} {} {Reflectivity as function of wavelength} {} {}
"vacuum"\|"helium"\|"argon" {external material outside substrate} {} {}
{} {} {} {} {Position and orientation of polariser}? {(x,y,z) position
coordinates relative to origin at sample position}? {The orientation
information is stored as direction cosines relative to origin at sample
position.} {"nxcylinder", "nxbox", "nxsphere", ...}? { nshapepar
dimensions for selected shape}? {Sequential order of aperture along beam
path} \* {coil|current-sheet}? {Number of turns/cm in flipping field
coils}? {Number of turns/cm in compensating field coils}? {Number of
turns/cm in guide field coils}? {Flipping field coil current in "on"
state"}? {Compensating field coil current in "on" state"}? {Guide field
coil current in "on" state"}? {thickness along path of neutron travel}?
{Position and orientation of flipper}? {(x,y,z) position coordinates
relative to origin at sample position}? {The orientation information is
stored as direction cosines relative to origin at sample position.}
{"nxcylinder", "nxbox", "nxsphere", ...}? { nshapepar dimensions for
selected shape}? {Sequential order of aperture along beam path} + {Total
time of flight} {Identifier for detector}? {Data values}? {Data values}
{offset from the detector center in x-direction}? {offset from the
detector center in the y-direction}? {name/manufacturer/model/etc.
information}? {Position and orientation of detector element}?
{translation normal to direct beam}? {Solid angle subtended by the
detector at the sample}? {Size of each detector pixel. If it is scalar
all pixels are the same size}? {Size of each detector pixel. If it is
scalar all pixels are the same size}? {Detector dead time}? {Delay in
detector registering an event}? {Detector gas pressure}? {maximum drift
space dimension}? {Crate number of detector}? {Slot number of detector}?
{Input number of detector}? "He3 gas cylinder"\|He3 PSD"\|"He3 planar
multidetector"\| "He3 curved multidetector"\| "multi-tube He3 PSD"\|"BF3
gas"\|"scintillator"\|"fission chamber"? {Efficiency of detector with
respect to e.g. wavelength}? {date of last calibration (geometry and/or
efficiency) measurements}? {summary of conversion of array data to
pixels (e.g. polynomial approximations) and location of details of the
calibrations}? {Position and orientation of aperture}? {(x,y,z) position
coordinates relative to origin at sample position}? {The orientation
information is stored as direction cosines relative to origin at sample
position.} {"nxcylinder", "nxbox", "nxsphere", ...}? { nshapepar
dimensions for selected shape}? {Sequential order of aperture along beam
path}
