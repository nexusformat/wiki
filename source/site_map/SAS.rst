===
SAS
===

Small-Angle Scattering
======================

2006-04-19
----------

Given the complex requirements for initial data treatment on pulsed
source SANS instruments there has been general agreement to separate
these from the much simpler pin-hole geometry cameras used for
monochromatic X-ray and Neutron SAS studies, shown together below as
NXmonosas.

2006-10-05
----------

Effort was made to simplify the definition below, correct errors (such
as removed fields that did not exist in base classes), and remove
unnecessary information.

Suggest that this be called *NXsas_mono_area* (very cumbersome) since
the fields are appropriate to SAS instruments with area detectors at
monochromatics sources. The definition does not match well to other
types of SAS instrument such as USAS, Kratky, step-scanning, or
slit-camera with PSD.

2006-10-06
----------

A description of the wavelength and possibly a spectral description
(either vague or detailed such as a spectral profile) is needed for
analysis software to account for not only wavelength but wavelength
smearing and other spectral effects (high-order harmonics, for example).
Due to the variety of optics used to provide such a beam, rather than
define each of those possible optics in the generic instrument
definition, we define the spectral properties of the beam incident on
the sample that results from all the upstream optics.

Two possible ways:

- Object-oriented approach
    - This needs a new base class since a generic SAS description will
        define wavelength using generic hardware; not everyone has
        helical velocity selector or a crystal monochromator. X-rays are
        admittedly the more tedious case.
    - NXspectrum might be a good choice.
    - NXwavelength_selector is more to the point.
    - NXmonochromator is our choice. This will sit well next to
        NXbending_magnet, NXcrystal, NXinsertion_device, NXmirror,
        NXmoderator, and NXvelocity_selector.

.. code-block:: xml

    <!-- -->

    - NXbeam
        - Imperfect because NXbeam was intended for the simulation
            community despite the note in the documentation about beamline
            use. The fields are not entirely appropriate and some questions
            will often arise.

        <!-- -->

        <?xml version="1.0" encoding="utf-8"?>
        <!--
        URL: ?
        Name:     NXsas_mono_area (candidate name)
        Editor:   Ron Ghosh <ron@ill.fr>
        Principal Contributors:
                  Steve King <s.m.king@rl.ac.uk>,
                  Mark Koennecke <Mark.Koennecke@psi.ch>,
                  P.Jemian APS,
                  J.Suzuki-san JPARC,
                  A.Gotz ESRF

        Valuable comments from
                  N. Maliszewskyj,
                  P Kienzle NIST,
                  N. Terrill DIAMOND

        Version October 2006
        -->
        <NXroot>
            <NXentry name="{Entry Name}">
                <NXinstrument name="{Name of instrument}">
                    <name short_name="{short name of instrument}">{Name of instrument}?</name>
                    <NXsource name="{Name of facility}">
                        <probe type="NX_CHAR">"neutron"|"x-ray"</probe>
                    </NXsource>

                    <NXattenuator name="{Name of beam attenuator}">
                        <attenuator_transmission type="NX_FLOAT">
                            {The nominal fraction of the beam transmitted by the attenuator}
                        </attenuator_transmission>
                    </NXattenuator>

                    <NXaperture name="Name of beamline aperture">
                        <NXgeometry name="geometry">{location and shape of aperture}</NXgeometry>
                    </NXaperture>
                    <NXcollimator name="Name of beam collimator">
                        <NXgeometry name="geometry">{location and shape of collimator}</NXgeometry>
                    </NXcollimator>

                    <!--
                    A description of the wavelength and possibly a spectral description
                    (either vague or detailed such as a spectral profile) is needed for
                    analysis software to account for not only wavelength but wavelength
                    smearing and other spectral effects (high-order harmonics, for example).
                    Due to the variety of optics used to provide a generic beam, define
                    the spectral properties of the beam incident on the sample
                    that results from all the upstream optics.
                    -->

                    <NXmonochromator name="Beam_at_sample"> {characteristics of beam at sample}
                        <wavelength type="NX_FLOAT[]" units="angstrom">{selected wavelength}</wavelength>
                        <wavelength_fwhm type="NX_FLOAT[]" units="angstrom">
                            {wavelength distribution full width at half maximum}?
                        </wavelength_fwhm>
                        <NXdata name="wavelength_distribution">?</NXdata>
                    </NXmonochromator>

                    <NXdetector name="{Name(s) of detector(s)}">
                        <data type="NX_FLOAT[i,j,...]|NX_INT[i,j,...]" signal="1">
                            {Data values}?
                        </data>
                        <distance type="NX_FLOAT" units="mm">
                            {distance between sample and detector}
                        </distance>
                        <x_offset type="NX_FLOAT[k+1]" axis="1">
                            {X-direction pixel coordinate on the detector with origin at detector center}?
                        </x_offset>
                        <y_offset type="NX_FLOAT[l+1]" axis="2">
                            {Y-direction pixel coordinate on the detector with origin at detector center}?
                        </y_offset>
                        <quiet_count type="NX_FLOAT[i,j,...]|NX_INT[i,j,...]">
                            {signal from detector when not illuminated}?
                            <!-- This field needs to be added to NXdetector -->
                        </quiet_count>
                        <NXgeometry name="beam_center">
                            {x,y position of straight-through beam (a.k.a. beam center) on the detector}?
                        </NXgeometry>
                    </NXdetector>
                    <NXbeam_stop name="Name of beam stop">
                        <NXgeometry name="geometry">{shape, orientation and position of the beam stop}</NXgeometry>
                        <status type="NX_CHAR">{"in"|"out"}</status>
                    </NXbeam_stop>
                </NXinstrument>

                <NXmonitor name="control {Name of the monitor}">
                    <mode type="NX_CHAR">
                        "monitor"|"timer"?
                    </mode>
                    <preset type="NX_FLOAT">{preset for terminating measurement}</preset>
                    <data type="NX_INT[i]|NX_FLOAT[i]">
                        {Monitor value}
                    </data>
                    <quiet_count type="NX_FLOAT[i,j,...]|NX_INT[i,j,...]">
                        {signal from monitor when not illuminated}?
                        <!-- This field needs to be added to NXmonitor -->
                    </quiet_count>
                    <count_time type="NX_FLOAT" units="second">
                        {Elapsed actual counting time, the time the instrument
                        was really counting, without pauses or times lost due
                        to beam unavailability}
                    </count_time>
                </NXmonitor>

                <NXsample name="{Name of sample}"></NXsample>

                <NXdata name="Datablock name">+
                    <data type="NX_INT[...] | NX_FLOAT[...]" signal="1">
                        {link to detector counts in NXdetector}
                    </data>
                    <x_offset type="NX_FLOAT[k+1]">
                        {link to x_offset in detector group}
                    </x_offset>
                    <y_offset type="NX_FLOAT[l+1]">
                        {link to y_offset in detector group}
                    </y_offset>
                </NXdata>
            </NXentry>
        </NXroot>
