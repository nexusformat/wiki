---
title: NIAC2014 CodeCamp
permalink: NIAC2014_CodeCamp.html
layout: wiki
---
NIAC2014 CodeCamp
=================

The code camp allows existing NeXus developers to meet and work together
on developing software or resolving particular NeXus design issues.

See [NIAC2014](NIAC2014.html "wikilink") for administrative details about
this meeting.

Planned Schedule (subject to change)
------------------------------------

![2014-CodeCamp-Schedule-MTW.png](2014-CodeCamp-Schedule-MTW.png "2014-CodeCamp-Schedule-MTW.png")

Topics to be Considered
-----------------------

A subset will be chosen on the first day of the meeting.

Walk through

-   [Issues](https://github.com/nexusformat/definitions/issues) posted
    on the [NeXus GitHub](https://github.com/nexusformat) repository
-   Proposals and other topics listed on the
    [Discussions] (Discussions.html "wikilink") page
-   Close issues that are of minor importance and not of particular
    concern to anybody and not likely to be resolved any soon.

Choose topics from the preliminary list below:

-   Procedural questions:
    -   How to organize proposals and discussions
    -   How to remove ballast, when to break compatibility, versioning
        and validation
-   Fundamental design issues:
    -   Clarify rank specification
        -   related to
            [\#266](https://github.com/nexusformat/definitions/issues/266):
            implement difference in rules between base classes and
            application definitions
    -   Discuss [NeXus interfaces](Objects_or_Interfaces.html "wikilink")
    -   [How to avoid name clashes during future extensions of the Nexus
        standard](How_to_avoid_name_clashes_during_future_extensions_of_the_Nexus_standard.html "wikilink")
    -   Optional contents in application definitions?
    -   Discuss lightweight tags versus application definitions
    -   Rules for multi file NeXus files
-   Class specifications:
    -   NXformula?
    -   NXdata: Assigning axes to data once more again
    -   Prepare contributed definitions for ratification
-   Work on software:
    -   validation tools (nxvalidate or NXvalidate): state (cf
        [\#169/defs](https://github.com/nexusformat/definitions/issues/169),
        [\#251/defs](https://github.com/nexusformat/definitions/issues/251),
        [\#300/defs](https://github.com/nexusformat/definitions/issues/300),
        [\#363/code](https://github.com/nexusformat/code/issues/363)),
        further development, WWW service, use of NeXpy/Python-API for
        validation
    -   New NAPI release?
    -   [\#230](https://github.com/nexusformat/definitions/issues/230):
        use cmake to build Sphinx documentation
-   Finish support for attribute arrays (who proposed this? please
    provide details!)
-   Off-site excursion to -tba-

Agenda
------

<table>
<thead>
<tr class="header">
<th><p> </p></th>
<th><p>*Monday*</p></th>
<th><p>*Tuesday*</p></th>
<th><ul>
<li>Wednesday*</li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>9:00-10:00</p></td>
<td><p>Review</p></td>
<td><p>Short procedural</p></td>
<td><p>NAPI issues</p></td>
</tr>
<tr class="even">
<td><p>10:00-10:30</p></td>
<td><p>Coffee</p></td>
<td><p>Coffee</p></td>
<td><p>Coffee</p></td>
</tr>
<tr class="odd">
<td><p>10:30-12:00</p></td>
<td><p>Cansas<br />
Axes<br />
Error</p></td>
<td><p>Telco with DECTRIS</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>12:00-13:00</p></td>
<td><p>Lunch</p></td>
<td><p>Lunch</p></td>
<td><p>Lunch</p></td>
</tr>
<tr class="odd">
<td><p>13:00-15:00</p></td>
<td><p>DECTRIS,<br />
NXmx etc</p></td>
<td><p>nexpy</p></td>
<td><p>HDF-5 talk</p></td>
</tr>
<tr class="even">
<td><p>15-15:30</p></td>
<td><p>Coffee</p></td>
<td><p>Coffee</p></td>
<td><p>Coffee</p></td>
</tr>
<tr class="odd">
<td><p>15:30-18:00</p></td>
<td><p>MXmx,<br />
when time smaller issues</p></td>
<td><p>Reprioritise for last day<br />
Lightweight tags and interfaces</p></td>
<td></td>
</tr>
</tbody>
</table>

### Tuesday

-   teleconference with Dectris: 10:30 AM

#### for end of day review

-   [axes](http://wiki.nexusformat.org/2014_axes_and_uncertainties#Proposal_to_describe_multi-dimensional_data_.28Axes.29)
-   [uncertainties](http://wiki.nexusformat.org/2014_axes_and_uncertainties#Uncertainties)

### Wednesday

-   public talk: *Current State of HDF5*, Elena Pourmal, The HDF Group,
    location: 401/A1100

