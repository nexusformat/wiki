=============================================
Monochromatic Neutron and X-ray Reflectometry
=============================================

**Please add comments to the discussion tab of this page and sign them**

This proposed instrument definition adds a new class (NXspin) and also incorporates a few additions to existing base classes.

Additions
---------

### New background

NXcharacterization type: `specular_offset_background`

The two existing backgrounds are `isotropic_scatter` and `empty_container`. Physically, we are moving the detector/sample slightly away from the specular reflection condition and measuring the strength of the signal rather than putting an isotropic scatter at the sample position or leaving it empty. Note: this simply identifies the location of the background scan, but does not specify how the background was measured.

### Need to know the sample angle

Propose adding the following to NXsample:
- Polar angle of the sample with respect to the beam incident on the monochromator
- Azimuthal angle of the sample with respect to the beam incident on the monochromator
- Rotation angle of the sample

These fields are already used in the ratified NXmonotas, so there should be no problem ratifying them in the base class.

### Record Spin State

For polarized neutron reflectometry, the control software allows the user to select and tune a particular spin state. Expressed in terms of the individual filters and flipper currents, it is difficult to determine which spin state is desired. Instead, the instrument component should record the target spin state. Propose NXspin class to record the target spin at the sample or at the detector:
- 90 for spin up, -90 for spin down
- Constant usually ignored. 0 in the direction of the beam path.

### Accurate record of the start and stop of every scan

We need an accurate record of the start and stop of every measurement in a scan (e.g., to normalize by measurement time, and to correct for He3 polarizer efficiency decay). NXmonitor already stores count duration. Propose adding `count_start_time` as well:
- Start time for each scan point

The alternative is to use NXlog and assume a particularly named log corresponds to the NXmonitor, with the same length as the measured points:
- Start of the measurement of point np
- Durations of the measurement point np

The first solution is cleaner.

Full Definition
---------------