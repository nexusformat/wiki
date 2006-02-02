---
title: NIAC2006: Scanning Group
permalink: NIAC2006:_Scanning_Group/
layout: wiki
---

Present
-------

-   Paul Kienzle (NIST)
-   Nick Maliszewskyj (NIST)
-   Stephen Cotrell (RAL)
-   Ron Ghosh (ILL)
-   Mark Konnecke (PSI)
-   Stefan Flemming (HMI)

Decisions
---------

1. A scan is a set of tuples.

Scan dimension is the slowest moving dimension, and is of length np.

2. Components of the tuples are stored in separate vectors in the
instrument definition.

Components/environment parameters which can change during the scan may
have an additional scan dimension, as will monitors and detectors.
Scalars become vectors.

The vectors are stored where they usually are in the instrument
definition, and linked to from NXdata. We rejected the idea of storing
an arbitrary state in the instrument definition and storing the vectors
in a new NXscan class even though this would mean that further entries
in the file could link to the instrument rather than having to copy all
the details of the instrument definition.

3. Multidetector systems have an additional dimension, nd the number of
detectors.

Some instruments have multiple moving detectors, e.g., separated by 5
degrees. If these are fixed relative to each other and do not have an
analyzer then the resulting bank of detectors can be treated as a linear
detector with gaps and no special encoding is needed.

If the detectors can move relative to each other, or if they have
separate analyzers, then we need a bank of detectors and analyzers. The
Q/HKL coordinates are defined in NXsample as usual, but there is an
additional leading dimension of length nd for each detector angle and
analyzer.

4. Optional components such as polarizers and analyzers are listed.

Optional components possibly appear on the particular class of
instrument though not required. Software which claims to fully support
e.g. monochromatic reflectometers should treat polarizers and analyzers
correctly.

5. Sample contains optional |Q| for powder data samples with no HKL.

6. Agree on the definition of sample.

7. Agree to not included scan range metadata in the file.

Applications which want to help the user select the appropriate runs
will need to keep track of the range of data in the datafiles
themselves. This may be part of the data catalogue at the institution.

To be decided
-------------

-   How are detectors associated with detector number in the bank of
    analyzer case? Or is there only one detector with an additional
    dimension?

<!-- -->

-   Are we using names such as precollimator\_analyzer or are we using
    NXgeometry.component\_index instead to figure out where things are.
    Latter is slightly more work for reduction, but otherwise better.
    What happens with multiple beam paths?

<!-- -->

-   How do we know it is a scan?
-   What about scan intent, such as spec/back/slit?
-   Where to store start time for each measurement?
    -   NXmonitor? Okay.
    -   NXdata? Data doesn't otherwise contain data.
    -   NXentry? Okay.
    -   New NXscan class? Too complex, unless needed for other things.
    -   NXlog? No synchronization with scan points in general.
    -   NXsample? Maybe.

<!-- -->

-   Definition should list fields and maybe attributes needed for
    reduction; others should be dropped.

<!-- -->

-   Monitor and detector need efficiency and dead time correction
    information

<!-- -->

-   Need NXbeamstop for details such as shadow on the detector.

<!-- -->

-   Polarizer/flipper: only want the angle of incidence on the sample,
    not things such as flipper current from which it is derived.

<!-- -->

-   Partial reduction
    -   Summary data
    -   treated data
    -   excluded data
    -   resolution function

<!-- -->

-   TAS
    -   Fewer collimator types available than in NXcollimator...is this
        what we want? Similarly for filter.
    -   HKL in sample rather than detector still feels wrong.
    -   Add efficiency, deadtime and sampled portion to monitor
        description
    -   Need polarizers and flippers?

<!-- -->

-   Reflectometry
    -   Generic scan for things which are not reflectometry
        measurements?
    -   How to link to background and slit scan
    -   NXcrystal is missing wavelength spread
    -   How to store slits; how to reference in-plane and out of plane
        slits?
    -   Raw counts may be meaningless without normalization.
    -   Combine spec, back, slit, rock for all +- polarization in one
        entry? Or use separate entries?

<!-- -->

-   SAS

