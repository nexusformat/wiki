===========
MonoXSingle
===========


--- title: MonoXSingle permalink: MonoXSingle.html layout: wiki ---
Monochromatic Single Crystal Diffractometer with Single Detector
----------------------------------------------------------------
Instrument definition for a single crystal diffractometer at a
monochromatic neutron or X-ray beam. This is the single detector
version. General Notes: - A Eulerian cradle is assumed. If you do not
have this, or you are using a rotation camera, feel free to adapt the
Nxsample group. - If you put measurements for multiple reflections in
one file, they should go into separate entries. - The definition assumes
the measurement to be an omega - two-theta or omega scan of a given
reflection. If this is not the case, i.e. a general scan is performed,
feel free to make HKL, chi and phi arrays with the length of the scan as
a dimension. As the NeXus scan paradigm of the day requires. - This
definition is fairly minimal and shall cater for standard data reduction
needs. If your most favourite items are missing, feel free to add them.
If you think something is missing which is required for standard data
reduction tasks, please contact the maintainer of this definition.
+
{Title of the experiment}
{start time of measurement} {nominal wavelength selected} + {Polar
Angle, commonly known as two theta} {Polar Angle, or two theta as an
array with values for each detector element} {The counts detected in the
detector} monitor \| timer {preset value for monitor or timer} {Monitor
counts} {Descriptive name of sample} { Sample rotation, aslo known as
omega } { chi angle } { phi angle } {Orientation matrix of single
crystal according to conventions established by Busing, Levy, 1967 } {
Miller indices of the target reflection} + {Link to detector counts in
NXdetector} {Link to polar angle data in NXdetector}
