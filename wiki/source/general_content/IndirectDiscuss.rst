===============
IndirectDiscuss
===============

This file is from the old SWIKI and a starting point for discussion. The idea is to come up with a definition
based on inheritance from other definitions such as `TOFRaw <TOFRaw>`__, NXtofnigs.xml.

- **Name of instrument**:
  - (x,y,z) position coordinates relative to origin at sample position?
  - The orientation information is stored as direction cosines relative to origin at sample position.

- **Shape**:
  - Options: "nxcylinder", "nxbox", "nxsphere", etc.
  - nshapepar dimensions for selected shape?

- **Sequential order of target along beam path**.

- **Optional description/label**:
  - Sequential order of component along beam path?

- **Moderator information**:
  - "Engineering" position of moderator.
  - Effective distance as seen by measuring radiation.
  - Moderator type: "H2O" | "D20" | "Liquid H2" | "Liquid CH4" | "Solid D2", etc.
  - Poison depth and moderator coupling details.
  - Average/nominal moderator temperature and temperature log.

- **Guide details**:
  - Position and orientation of guide (x, y, z coordinates relative to origin at sample position).
  - Shape: "nxcylinder", "nxbox", "nxsphere", etc.
  - Sequential order of guide along beam path.

- **Chopper details**:
  - Chopper type: "single", "contra_rotating_pair", "synchro_pair".
  - Chopper rotation speed.
  - Number of slits, angular opening, disc spacing, and radius to center of slit.
  - Chopper phase angle and pulse reduction factor.

- **Aperture information**:
  - Absorbing material, description of aperture.
  - Position and orientation of aperture.
  - Shape: "nxcylinder", "nxbox", "nxsphere", etc.

- **Monitor information**:
  - Type: "Fission Chamber" | "Scintillator".
  - Monitor efficiency, proportion of incident beam sampled, and distance from sample.
  - Wavelength transmission profile of filter.
  - Filter temperature and sensor log.

- **Collimator details**:
  - Type: "Soller" | "radial".
  - Divergence in local x and y directions, thickness of absorbing blades.
  - Position and orientation within bank.

- **Crystal details**:
  - Type: "PG", "Ge", "Si", "Cu", etc.
  - Horizontal and vertical mosaic Full Width Half Maximum.
  - Bragg angle, lattice parameter, and scattering vector for nominal reflection.
  - Unit cell parameters, volume, and (hkl) values.
  - Crystal reflectivity and transmission profiles.

- **Detector details**:
  - Type: "He3 gas cylinder" | "He3 PSD" | "scintillator", etc.
  - Total distance from sample position to detector.
  - Position and orientation in detector bank.
  - Total time of flight and detector dead time.
  - Efficiency of detector with respect to wavelength.