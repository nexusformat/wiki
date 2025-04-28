---
title: Proposal NeXus Errors
permalink: Proposal_NeXus_Errors.html
layout: wiki
---

The current definition for the [NXdata
group](http://www.nexusformat.org/NXdata) (which, incidentally, is
misleading on the wiki since it implies that the data SDS should be
called “data”) defines an error SDS with the name “errors” (in this
case, the name <em>is</em> fixed). This is a workable solution when
there is only one signal. However, the original plan for NXdata groups
(again, not particularly clear on the wiki) was that they could contain
more than one data SDS. The primary one has the attribute “signal=1”,
but secondary data sets with “signal=2”, etc., were to be allowed. This
is of particular importance to the synchrotron community, who frequently
measure, for example, fluorescence counts in addition to the main
detector counts. In principle, each one of these could have their own
errors, but there is no way in the current scheme to associate different
SDSs with those errors.

Proposal
--------

An extra attribute be defined for each data (or signal) SDS called
“errors”, which would be a text string defining the name of the SDS
within the same NXdata group to contain the errors SDS. The rank and
dimensions of the errors SDS must match the signal SDS. The original
method, <em>i.e.</em>, associating an SDS with the name “errors” with
the primary signal SDS will be allowed in cases where there is no
ambiguity, and for reasons of backward compatibility.

Discussion
----------

This is analogous to the use of the “axes” attribute to define the
independent axes associated with each signal SDS. However, this
attribute will only ever contain one name, since there is no reason to
associate more than one error array with a single signal array.

Here is an example NXdata group using the proposed new attribute:

<NXdata name="data">  
`   `<primary_data signal="1" axes="x1:y1" errors="e1">`...`</primary_data>  
`   `<x>`...`</x>  
`   `<y>`...`</y>  
`   `<e1>`...`</e1>  
`   `<secondary_data signal="2" axes="x:y" errors="e2">`...`</secondary_data>  
`   `<e2>`...`</e2>  
</NXdata>

I propose to present this for discussion and a possible vote at the
upcoming NIAC meeting at the SNS on October 7-8.

  
[Ray](User%3ARay_Osborn.html "wikilink") 16:29, 29 September 2010 (UTC)

Conclusion: 01/2015
-------------------

At NIAC 2014, the NIAC ratified a scheme for describing uncertainties.
See
[2014\_axes\_and\_uncertainties](2014_axes_and_uncertainties.html "wikilink")
and, in a short while, the NeXus manual.
