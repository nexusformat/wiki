===============
IndirectDiscuss
===============


--- title: IndirectDiscuss permalink: IndirectDiscuss.html layout: wiki
--- This file is from the old SWIKI and a starting point for discussion
... the idea is to come up with a definition based on inheritance from
other definitions such as [TOFRaw](TOFRaw.html "wikilink") NXtofnigs.xml
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
along beam path} ? \* {Chopper type
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
along beam path} {Coordinate system reference marker} 0 \* {"Beryllium"
\| "Pyrolytic Graphite" \| "Graphite" \| "Sapphire" \| "Silicon"}? {in
\| out}? {Wavelength transmission profile of filter}? {average/nominal
filter temperature} {Linked temperature_log for the filter}? {Sensor(s)
used to monitor the filter temperature}? {Unit cell parameters for
single crystal filter(lengths and angles)}? {Unit cell}? {Orientation
matrix of single crystal filter}? {Position and orientation of filters
within bank}? {(x,y,z) position coordinates relative to origin at sample
position}? {The orientation information is stored as direction cosines
relative to origin at sample position.} {"nxcylinder", "nxbox",
"nxsphere", ...}? { nshapepar dimensions for selected shape}?
{Sequential order of filter bank along beam path} \* "Soller"\|"radial"
{divergence of collimator in local x direction} {divergence of
collimator in local y direction}? {thickness of absorbing blades}? {gap
between absorbing blades}? {coating on or complete material of blades}?
{material separating absorbing blades}? {Position and orientation of
collimators within bank}? {(x,y,z) position coordinates relative to
origin at sample position}? {The orientation information is stored as
direction cosines relative to origin at sample position.} {"nxcylinder",
"nxbox", "nxsphere", ...}? { nshapepar dimensions for selected shape}?
{Sequential order of collimator bank along beam path} + { "PG (Highly
Oriented Pyrolytic Graphite)" \| "Ge" \| "Si" \| "Cu" \| "Fe3Si" \|
"CoFe" \| "Cu2MnAl (Heusler)" \| "Multilayer" } {horizontal mosaic Full
Width Half Maximum}? {vertical mosaic Full Width Half Maximum}? {Optimum
diffracted wavelength} {Bragg angle of nominal reflection} {Lattice
parameter of the nominal reflection}? {Scattering vector, Q, of nominal
reflection}? {Unit cell parameters (lengths and angles)}? {Volume of the
unit cell}? {(hkl) values of nominal reflection}? {average/nominal
crystal temperature}? {log file of crystal temperature}? {crystal
reflectivity versus wavelength}? {crystal transmission versus
wavelength}? {Horizontal width of individual segment}? {Vertical height
of individual segment}? {Thickness of individual segment}? {Typical gap
between adjacent segments}? {number of segment columns in horizontal
direction}? {number of segment rows in vertical direction}? {Horizontal
curvature of focusing crystal}? {Vertical curvature of focusing
crystal}? {Cut angle of reflecting Bragg plane and plane of crystal
surface}? {Position and orientation of crystals within bank}? {(x,y,z)
position coordinates relative to origin at sample position}? {The
orientation information is stored as direction cosines relative to
origin at sample position.} {"nxcylinder", "nxbox", "nxsphere", ...}? {
nshapepar dimensions for selected shape}? {Sequential order of analyser
bank along beam path} + {Identifier for detector}
{name/manufacturer/model/etc. information}? {Detector gas pressure}?
{maximum drift space dimension}? {Crate number of detector}? {Slot
number of detector}? {Input number of detector}? {"He3 gas
cylinder"\|He3 PSD"\|"He3 planar multidetector"\| "He3 curved
multidetector"\| "multi-tube He3 PSD"\|"BF3 gas"\|"scintillator"? {Total
distance from sample position to detector through secondary
spectrometer} {Position and orientation of detector elements in bank}?
{(x,y,z) position coordinates relative to origin at sample position}?
{The orientation information is stored as direction cosines relative to
origin at sample position.} {"nxcylinder", "nxbox", "nxsphere", ...}? {
nshapepar dimensions for selected shape}? {Sequential order of detector
bank along beam path} {Total time of flight from sample position to
detector through secondary spectrometer} {Detector dead time}? {Delay in
detector registering an event}? {date of last calibration (geometry
and/or efficiency) measurements}? {details of the calibration method}?
{Efficiency of detector with respect to e.g. wavelength}? \*?
