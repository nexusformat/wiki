===
SAS
===


--- title: SAS permalink: SAS.html layout: wiki --- Small-Angle
Scattering ====================== 2006-04-19 ---------- Given the
complex requirements for initial data treatment on pulsed source SANS
instruments there has been general agreement to separate these from the
much simpler pin-hole geometry cameras used for monochromatic X-ray and
Neutron SAS studies, shown together below as NXmonosas. 2006-10-05
---------- Effort was made to simplify the definition below, correct
errors (such as removed fields that did not exist in base classes), and
remove unnecessary information. Suggest that this be called
\*NXsas\\_mono\\_area\* (very cumbersome) since the fields are
appropriate to SAS instruments with area detectors at monochromatics
sources. The definition does not match well to other types of SAS
instrument such as USAS, Kratky, step-scanning, or slit-camera with PSD.
2006-10-06 ---------- A description of the wavelength and possibly a
spectral description (either vague or detailed such as a spectral
profile) is needed for analysis software to account for not only
wavelength but wavelength smearing and other spectral effects
(high-order harmonics, for example). Due to the variety of optics used
to provide such a beam, rather than define each of those possible optics
in the generic instrument definition, we define the spectral properties
of the beam incident on the sample that results from all the upstream
optics. Two possible ways: - Object-oriented approach - This needs a new
base class since a generic SAS description will define wavelength using
generic hardware; not everyone has helical velocity selector or a
crystal monochromator. X-rays are admittedly the more tedious case. -
NXspectrum might be a good choice. - NXwavelength\\_selector is more to
the point. - NXmonochromator is our choice. This will sit well next to
NXbending\\_magnet, NXcrystal, NXinsertion\\_device, NXmirror,
NXmoderator, and NXvelocity\\_selector. - NXbeam - Imperfect becuase
NXbeam was intended for the simulation community despite the note in the
documentation about beamline use. The fields are not entirely
appropriate and some questions will often arise.
{Name of instrument}? "neutron"\|"x-ray" {The nominal fraction of the
beam transmitted by the attenuator} {location and shape of aperture}
{location and shape of collimator} {characteristics of beam at sample}
{selected wavelength} {wavelength distribution full width at half
maximum}? ? {Data values}? {distance between sample and detector}
{X-direction pixel coordinate on the detector with origin at detector
center}? {Y-direction pixel coordinate on the detector with origin at
detector center}? {signal from detector when not illuminated}? {x,y
position of straight-through beam (a.k.a. beam center) on the detector}?
{shape, orientation and position of the beam stop} {"in"\|"out"}
"monitor"\|"timer"? {preset for terminating measurement} {Monitor value}
{signal from monitor when not illuminated}? {Elapsed actual counting
time, the time the instrument was really counting, without pauses or
times lost due beam unavailability} + {link to detector counts in
NXdetector} {link to x_offset in detector group} {link to y_offset in
detector group}
