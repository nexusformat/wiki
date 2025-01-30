==================
NXtofnref-NIAC2006
==================


--- title: NXtofnref-NIAC2006 permalink: NXtofnref-NIAC2006.html layout:
wiki --- Concerns: - mono and tof reflectometry must inherit from a
common base class; the current definition of tofnref inheriting from
monoref leaves the definition of the monochromator in the TOF
definition. - SNS Liquids has two monitors, but our definitions only
have one. Both are not always active.
NXtofnref { Distance from T_o to sample along beam-path. To calculate
wavelength: L[i] = wavelength at time T[i] T[i] = time of flight for
point i. d1 = distance from moderator to sample along beam path d2 =
distance from detector to sample along beam path h = Planck's constant
m_n = mass of the neutron L[i] = h/m_n \* T[i]/(d1+d2) } { Find the
center of mass of the pulse shape and use that as the T0 offset with
respect to the protons hitting the target. The TOF from target (which is
the real T0) to the moderator is insignficant compared to the
uncertainty from the pulse shape and so can be ignored. } \* { Guides in
total or in segments thgrough to sample position; may be interspersed
between other components - Check component index. Can be nested for
guides with multiple straight segments. Affects wavelength spectrum,
both in divergence and intensity. The spectrum scan will automatically
compensate for intensity effects. To compute divergence effects,
detailed information about the guide geometry will be required. } ? {
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
to have the correct cutoff. } { Total time of flight }
