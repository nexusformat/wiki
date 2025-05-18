---
title: NIAC2006 Scanning Group
permalink: NIAC2006_Scanning_Group.html
layout: wiki
---
NIAC2006 Scanning Group
=======================

Definitions for some measurement classes:

-   Triple axis definition:
    [NXmonotas-NIAC2006](NXmonotas-NIAC2006.html "wikilink")
-   Reflectometry definition:
    [NXmonoref-NIAC2006](NXmonoref-NIAC2006.html "wikilink")
-   TOF Reflectometry definition:
    [NXtofnref-NIAC2006](NXtofnref-NIAC2006.html "wikilink")

Session 1
---------

-   Paul Kienzle (NIST)
-   Nick Maliszewskyj (NIST)
-   Stephen Cotrell (RAL)
-   Ron Ghosh (ILL)
-   Mark Konnecke (PSI)
-   Laurent Lerusse(RAL)
-   Stefan Flemming (HMI)
-   Jens-Uwe Hoffmann (HMI)

1. A scan is a set of tuples.

The intention is to associate intensity data with a collection of
independent variables (e.g., motor positions, tunable physical
quantities, etc.).

Scan dimension is the slowest moving dimension, and is of length np
(number of points).

Scans can be an extension to “sit and count” measurements and may
therefore be applied to parametric studies (e.g., varying sample
temperature).

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
analyzer. Quantities that can be used as dimension scales must have the
same dimensionality as the stored dataset (to make the association of
intensity data with the other members of the measurement tuple).

4. Optional components such as polarizers and analyzers are listed.

Optional components possibly appear on the particular class of
instrument though not required. Software which claims to fully support
e.g. monochromatic reflectometers should treat polarizers and analyzers
correctly.

5. Sample contains optional momentum transfer |Q| for powder data
samples with no HKL.

6. Agree on the definition of sample.

7. Agree to not included scan range metadata in the file.

Applications which want to help the user select the appropriate runs
will need to keep track of the range of data in the datafiles
themselves. This may be part of the data catalogue at the institution
(but not explicitly in the datafile?).

Session 2
---------

Present: NickM, MarkK, PaulK, MatthiasD, Jens-UweH

-   How are detectors associated with detector number in the bank of
    analyzer case? Or is there only one detector with an additional
    dimension? \[option 2\]

<!-- -->

-   Are we using names such as precollimator\_analyzer or are we using
    NXgeometry.component\_index instead to figure out where things are.
    Latter is slightly more work for reduction, but otherwise better.
    \[answer: use symbolic name in NXdata and link to appropriate
    element for varying; can reconstruct order from geometry;
    NXgeometry.component\_index is required for each component; names of
    particular components are part of the definition, matching the names
    in the NXdata\]

<!-- -->

-   What happens with multiple beam paths? \[ignore this issue for now
    since we invented analyzer banks\]

<!-- -->

-   How do we know it is a scan?
-   What about scan intent, such as spec/back/slit and ++/--
    polarization?
-   Where to store start time for each measurement?
    -   NXmonitor? Okay.
    -   NXdata? Data doesn't otherwise contain data.
    -   NXentry? Okay.
    -   New NXscan class? Too complex, unless needed for other things.
    -   NXlog? No synchronization with scan points in general.
    -   NXsample? Maybe.

<!-- -->

-   Definition should list fields and maybe attributes needed for
    standard reduction for that instrument class; others should be
    dropped from definition. \[agreed elsewhere\]

<!-- -->

-   Monitor and detector need efficiency and dead time correction
    information \[out of scope\]

<!-- -->

-   Need NXbeamstop for details such as shadow on the detector.

<!-- -->

-   Polarizer/flipper: reduction only wants the angle of incidence on
    the sample, not things such as flipper current from which it is
    derived. Alternatively, use a scan intent tag such as
    polarization=++. \[unresolved\]

<!-- -->

-   Links to calibration files \[out of scope\]

<!-- -->

-   Partial reduction \[out of scope\]
    -   Summary data
    -   treated data
    -   excluded data
    -   resolution function

<!-- -->

-   TAS \[agreed\]
    -   Fewer collimator types available than in NXcollimator...is this
        what we want? Similarly for filter. \[use base component as is\]
    -   HKL in sample rather than detector still feels wrong.
        \[overruled\]
    -   Add efficiency, deadtime and sampled portion to monitor
        description \[out of scope\]
    -   Polarization analysis:
        -   Store cross section measurements in separate NXentries
            \[agreed\]
        -   Need refinements to NXflipper, NXpolarizer base classes
            \[deferred\]
        -   Still need symbolic means of identifying which cross section
            is which \[deferred\]

<!-- -->

-   Reflectometry \[good progress\]
    -   Generic scan for things which are not reflectometry
        measurements? \[out of scope\]
    -   How to link to background and slit scan? \[deferred\]
    -   NXcrystal is missing wavelength spread \[calculate from mosaic\]
    -   How to store slits; how to reference in-plane and out of plane
        slits? \[box or slit; need 'vertical/horizontal slit' shapes in
        NXshape\]
    -   Raw counts may be meaningless without normalization.
        \[deferred\]
    -   Combine spec, back, slit, rock for all +- polarization in one
        entry? Or use separate entries? \[separate\]
    -   Scan start times \[in NXlog called 'timer'\]

Note: Paul Kienzle added wavelength\_spread back into NXcrystal. May
want to simply list the formula for calculating it from other NXcrystal
fields instead.
