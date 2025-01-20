==================
NXmonoref-NIAC2006
==================


--- title: NXmonoref-NIAC2006 permalink: NXmonoref-NIAC2006.html layout:
wiki --- The following is the proposed monochromatic reflectometry
definition. Concerns: - Using classes rather than names in links (e.g.,
NXdetector) will break if the user adds another detector group to the
entry. - I don't record whether the reflectometer is horizontal or
vertical geometry, but with slit and angles defined relative to the
sample surface this doesn't matter. - I'm asking the control software to
write the wavelength divergence into the file so that the user can read
it off directly without performing calculations. - Not recording region
of interest used to measure count duration. Could create a virtual
detector for this. - Normalization by monitor/timer not currently
supported - For backgrounds, don't know if the nominal Qz should be
calculated from the theta or twotheta. The correct choice depends on
the source of background. Example:
[NXmonoref\\_example-NIAC2006](NXmonoref_example-NIAC2006.html
"wikilink")
NXmonoref \* {Suggested spectrum measurement for intensity vs.
wavelength for a given slit setting. Warning: beam profile is not
regular, but this effect is accomodated in the spectrum measurement} \*
{Suggested background measurement} ? {Angle relative to the scattering
plane, not to gravity.} {\|Q\|}? ? { Location of slit along beamline
(midway between slits if slits are not coplanar). This is required to
compute instrument resolution. } { Need to add "nxslit" to list of
possible shapes. If the shape is a box, first dimension changes the
sample footprint. } ? ? ? ? ? ? { Need all fields so that we can
calculate shadow of beam stop on detector. } { Indicate sense of
scattering: 0 is front surface of sample, 180 is back surface of sample.
If 180, change the sign of the reflected angle in the data. It is also
possible for the beam to enter the substrate from the side and reflect
off the back surface of a film, in which case negative angles can be
interpreted as inverting the scattering length density profile of the
film (after accounting for absorption in the substrate. } ? ? {
"intensity"\|"background"\|"specular"\|"rock"\|"slice"\|"area" } ? {
"++"\|"+-"\|"-+"\|"--"\|"+"\|"-" } ? ? ? ? ? ? ? ? ? ? \* { Various logs
for temperature, field, etc. which are assumed to be constant over the
duration of the run. The reduction program should be able to display
their values on a parallel graph. Note that logs are not necessarily
sampled synchronously with the data points. }
