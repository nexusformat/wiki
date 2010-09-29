---
title: Proposal: NeXus Coordinates
permalink: Proposal:_NeXus_Coordinates/
layout: wiki
---

- Still under construction -

The current definition for NXdata groups assumes that the data (or
signal) SDS is, in general, a multidimensional array that can be plotted
against one or more independent axes, equal in number to the rank of the
signal SDS. These are defined through the “axes” attribute. However,
there are cases where the data represent a set of pixels that are
defined by their coordinates, <em>i.e.</em>, they are not necessarily
contiguous.

Proposal
--------

An extra attribute be defined for a data (or signal) SDS called
“coordinates”, which would be a text string containing the names of one
or more SDSs that represent the coordinates of the signal SDS. The names
will be separated by the same delimiters allowed for the “axes”
attribute. The signal SDS and each of the coordinate SDSs must be
one-dimensional and of the same length.

Discussion
----------
