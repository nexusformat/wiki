---
title: Proposal to Simplify Nexus
permalink: Proposal_to_Simplify_Nexus.html
layout: wiki
---
Proposal to Simplify Nexus
==========================


*E. Farhi (ILL), A. Gotz (ESRF), R. Ghosh (ILL), D. Richard (ILL), M.
Johnson (ILL), R. Wilcke (ESRF)*

This document presents conclusions and proposals from the NeXus ILL/ESRF
Local Advisory Committee (NLAC).

NeXus *raison d'etre*
---------------------

-   NeXus is an exchange format to all n,X,muon scattering techniques in
    large facilities.
    -   This implicitely limits the scope of NeXus to all that is common
        to these techniques, while excluding instrument/technique
        peculiarities. Further descriptions (instrument details) are in
        principle out of scope, but may be specified as extensions to
        the basis requirements.
    -   The scientific data set is intrinsically the most important to
        physicists, compared with the exact instrument definition (which
        is essentially relevant for instrument debugging and simulation
        purposes). The official 'base' NeXus format should focus on the
        former rather than the latter.
-   NeXus must be easy to use.
    -   This means that there is an efficient API (and this is the case,
        thanks Mark K.)
    -   At the same time, NeXus should be flexible enough to potentially
        evolve from HDF and XML towards other physical storage format
        (Open Document, ...)
-   NeXus must be appealing for people to voluntarily use it (in
    programs).
    -   This means that the format structure must be clear, simple and
        easy to understand. This is probably the most important point,
        otherwise it will push people to develop their own NeXus format,
        or event use their own non-NeXus format (based on HDF or not)
    -   The NeXus web server must present usage examples and distribute
        associated software.
-   NeXus must be flexible and expandible.
    -   This means that there should be a recommanded mechanism for
        extension of the 'base' NeXus into 'proprietary' NeXus. At the
        same time, a clear statement must be done concerning a limited
        number of absolute requirements, as well as 'official'
        recommandations for extensions.
-   The scientific Data must be immediately visible in the NeXus
    structure, as well as essential parameters for the data analysis.
    This means that the NXData must be directly in the NXentry, that
    essential parameters should be as well there (in an NXparameters
    class, see below). Further information (NXinstrument, ...) is
    optional.

Format requirements
-------------------

### Proposal R1: Simplified NeXus hierarchy

The base NeXus format should contain the following hierarchy:

    NXentry  
       NXdata  
       NXsample  
       NXparameters

Other classes should be mentioned as optional, eventhough NXmonitor and
NXuser are recommanded.

### Proposal R2: simplified NXdata

       * rename 'long_name' into 'label' in 'variable'  
       * suppress 'first_good' and 'last_good'  
       * add a 'range' attribute to 'variable' so that it can be given as a regularly sampled range.

### Proposal R3: scanning mechanism (dim &lt;= 3)

For low dimensionality data sets (dim &lt;= 3), the scan may be stored
as a array in the NXdata, with associated axis.

### Proposal R4: scanning mechanism (general): NXgroup

As an alternative, or for higher dimensionality, each scan step is
stored as a single NXdata, with one 'master' NXgroup describing how to
assemble scan steps into series. The assembling mechanism is to be
discussed further.

### Proposal R5: the NXparameters class

As an alternative to the NXinstrument, which brings usually too much
information as required for a basic data analysis, a new NXparameters
class should be defined next to the NXdata, and gather 'important'
parameters to be used by scientists. The NXparameter is a kind of
'abstract' of NXinstrument. The list of these parameters should be
defined per class of instrument, based on requirements from existing
data analysis programs (FullProf, INX, Sqw, Dave, Isaw, Nathan, ...), to
be discussed further. Format extensions (optional)

### Proposal E1: NXinstrument is optional

The NXinstrument class is optional. No NXinstrument class should be
specifically defined as 'official'. However, some examples per class of
instrument will be available to programmers. Indeed, as all instruments
as essentially unique, no description can cope with all of them. The
usage of NXinstrument usually concerns instrument simulations (McStas,
Vitess, NISP, ResTrax, IDEAS, ...) as well as exact configuration (e.g.
for repeating experiment and debuging purposes).

### Proposal E2: NXinstrument vs NXdata and redudancy

If present, NXinstrument should contain all the relevant information
concerning the instrument parameters. In order to prevent redundancy for
the data set (in detector and NXdata), the usage of links is required. A
NXsample class should better appear in the NXinstrument as a link to the
NXentry/NXsample. One or more NXmonitor class should better appear in
the NXinstrument as a link to the NXentry/NXmonitor.

### Proposal E3: positioning and distances

The 'official' mechanism for distance/geometry specification is
NXgeometry. It derives from McStas positioning system. Other distance
specification attributes defined within NXinstrument objects should be
avoided.

### Proposal E4: no object definition

The usage of objects and inheritance is not envisaged as it bring too
much complexity in the associated definitions. We rather promote a
simplification of the existing NeXus.

### Proposal E5: grouping of equivalent elements

The NXgroup class could be used to assemble other items than scan steps
in order to define super-classes, e.g. sets of detectors and
monochromators.
