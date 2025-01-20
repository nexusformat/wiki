========
MonoXPSD
========


--- title: MonoXPSD permalink: MonoXPSD.html layout: wiki ---
Monochromatic Single Crystal Diffractometer with Position Sensitive
Detector
----------------------------------------------------------------------------
Instrument definition for a single crystal diffractometer at a
monochromatic neutron or X-ray beam. This is the version for a position
sensitive detector. Such an instrument can be used in various ways: In
one mode the instrument is driven to each reflection individually and a
short scan is performed in order to measure the reflections intensity.
In such cases each reflection should be stored in either separate files
or in separate entries as they constitute separate measurements. In
another mode a larger range in omega is scanned, saving detector data at
each step. This is similar to the way PX instruments operate. In such a
case, omit the Miller indices in the sample group. A Eulerian cradle is
assumed. If you do not have this, or you are using a rotation camera,
feel free to adapt the Nxsample group. The definition assumes the
measurement to be an omega - two-theta or omega scan of a given
reflection. This definition is fairly minimal and shall cater for
standard data reduction needs. If your most favourite items are missing,
feel free to add them. If you think something is missing which is
required for standard data reduction tasks, please contact the
maintainer of this definition. If you to choose to store PSD scans in
separate files or separate entries, it is the users responsibility to
process the data in the right order. NP is again the number of scan
points
+
{Title of the experiment}
{start time of measurement} {nominal wavelength selected} + {Polar
Angle, or two theta as an array with values for each scan point} {The
counts detected in the area detector, np is the number of scan points}
{distance to sample position} {offsets of each pixels centers x-value to
the detector center} {offsets of each pixels centers y-value to the
detector center} monitor \| timer {preset value for monitor or timer}
{Monitor counts at each scan point} {Descriptive name of sample} {
Sample rotation, also known as omega } { chi angle } { phi angle }
{Orientation matrix of single crystal according to conventions
established by Busing, Levy, 1967 } ? { Miller indices of the target
reflection} + {Link to detector counts in NXdetector} {Link to polar
angle data in NXdetector} {Link to pixel_offset_x in NXdetector} {Link
to pixel_offset_y in NXdetector}
