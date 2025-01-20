======
DLSraw
======


--- title: DLSraw permalink: DLSraw.html layout: wiki --- \\\* --> Zero
or many + --> One or more ? --> 0 or 1
{Extended title for entry}?
{unique identifier for the experiment, defined by the facility, possibly
linked to the proposals}? {Number of run or scan stored in this entry}?
{}? { Date of the public release of the data. (file_time + X years)} {
Revision id of the file due to re-calibration, reprocessing new
analysis, new instrument definition format, ... } { Reason for the new
revision. (e.g. first revision, re-calibration, ) } {Name of entry DTD}?
{Name of entry DTD}? {Name of entry DTD}? {Starting time of
measurement}? {Ending time of measurement}? {Duration of measurement
(end_time - start_time)}? {Time transpired actually collecting data i.e.
taking out time when collection was suspended due to e.g. temperature
out of range}? {information on the reliability/source of the information
provided by the experimenter. (e.g.: From proposal, updated at
experiment time, ...} {Keyword domain (e.g. chemistry, astronomy,
ecology, ...)}? {Keywords defined for this study}? {A pointer to a
reference work providing the definition of the restricted vocabulary of
which the keyword list is a subset}? {Subject categorisations for this
study}? {Brief summary of the experiment, including key objectives}?
{Description of the full experiment (document in pdf, latex, ...)}?
{Special requirements of instrument}? {List of publications related to
the proposal}? {Facility access type (normal, rapid access, program
access, ...)}? {Identifier of the funding grant}? {Name of program used
to generate this file}? {Name of command line used to generate this
file}? + {Descriptive name of the input data} {Uniform Resource
Identifier of the input data} {Notes describing entry}? {An small image
that is representative of the entry.} {An example of this is a 640x480
jpeg image automatically produced by a low resolution plot of the
NXdata.}? 1+ {Name of user responsible for this entry} {role of user
responsible for this entry, comma separated list} {Suggested roles are
"local_contact", "principal_investigator", "proposer", "experimenter",
"funding_agency"} {Affiliation of user}?
{Address of user}?
{Telephone number of user}? {Fax number of user}? {Email of user}?
{Facility based unique identifier for this person e.g. their
identification code on the facility address/contact database, should
allow owner identification by the archive system.} {Affiliation unique
identifier.}? {Descriptive name of sample} {Sample identifier} {The
chemical formula specified using CIF conventions.}{Abbreviated version
of CIF standard: 1. Only recognized element symbols may be used. 2. Each
element symbol is followed by a 'count' number. A count of '1' may be
omitted. 3. A space or parenthesis must separate each cluster of
(element symbol + count). 4. Where a group of elements is enclosed in
parentheses, the multiplier for the group must follow the closing
parentheses. That is, all element and group multipliers are assumed to
be printed as subscripted numbers. 5. Unless the elements are ordered in
a manner that corresponds to their chemical structure, the order of the
elements within any group or moiety depends on whether or not carbon is
present. If carbon is present, the order should be: C, then H, then the
other elements in alphabetical order of their symbol. If carbon is not
present, the elements are listed purely in alphabetic order of their
symbol. This is the 'Hill' system used by Chemical Abstracts.}
{Description of the sample}? {20 character fixed length sample
description for legends}? {Sample temperature.}? {Applied electric
field}? {Applied magnetic field}? {External stress}? {Applied pressure}?
{Name of instrument} {Name of source}? "Spallation Neutron
Source"\|"Pulsed Reactor Neutron Source"\| "Reactor Neutron
Source"\|"Synchrotron X-ray Source"\| "Pulsed Muon Source"\|"Rotating
Anode X-ray"\|Fixed Tube X-ray" neutron|x-ray|muon|electron? {Effective
distance from sample}{Distance as seen by radiation from sample. This
number should be negative to signify that it is upstream of the
sample.}? {Source power}? {Accelerator current}? {Accelerator voltage}?
{any source/facility related messages/events that occurred during the
experiment}? {synchrotron operating mode}{"Single Bunch"\|"Multi
Bunch"}? {Is the synchrotron operating in top_up mode}? {"Engineering"
location of source}? {critical energy}? {bending radius}? {spectrum of
bending magnet}? {"Engineering" position of bending magnet}?
{"undulator"\|"wiggler"\|...}? {gap}? {taper}? {phase}? {number of
poles}? {length of insertion device}? {total power delivered by
insertion device}? {energy of peak}? {bandwidth of peak energy}?
{harmonic of peak}? {spectrum of insertion device}? {"Engineering"
position of insertion device}? + {value of motor - need [n] as may be
scanned} {Hardware device record, e.g. EPICS process variable,
taco/tango ...} 1+ {Data values} {Data values}
{name/manufacturer/model/etc. information}? "He3 gas cylinder"\|He3
PSD"\|"He3 planar multidetector"\| "He3 curved multidetector"\|
"multi-tube He3 PSD"\|"BF3 gas"\|"scintillator"\|"fission
chamber"\|"CCD"\|...? {Identifier for detector}? {offset from the
detector center in x-direction}? {offset from the detector center in the
y-direction}? {Size of each detector pixel. If it is scalar all pixels
are the same size}? {Size of each detector pixel. If it is scalar all
pixels are the same size}? {Distance}? {Polar Angle}? {Azimuthal Angle}?
{Position and orientation of detector element}? {translation normal to
direct beam}? {Solid angle subtended by the detector at the sample}?
{Detector dead time}? {Delay in detector registering an event}?
{Detector gas pressure}? {maximum drift space dimension}? {Crate number
of detector}? {Slot number of detector}? {Input number of detector}?
{Efficiency of detector with respect to e.g. wavelength}? {date of last
calibration (geometry and/or efficiency) measurements}? {summary of
conversion of array data to pixels (e.g. polynomial approximations) and
location of details of the calibrations}? 1+ {Data Values}? {Standard
deviations of data values - the data array is identified by the
attribute signal="1". This array must have the same dimensions as the
data}? {Dimension scale defining an axis of the data}? {Errors
associated with axis "variable"}?
