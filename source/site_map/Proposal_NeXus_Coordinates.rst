==========================
Proposal NeXus Coordinates
==========================

The current definition for NXdata groups assumes that the data (or signal) SDS is, in general, a multidimensional
array that can be plotted against one or more independent axes, equal in number to the rank of the signal SDS.
These axes are defined through the axes attribute. However, there are cases where the data represent a set of pixels
that are defined by their coordinates, *i.e.*, they do not form a contiguous array. The data would then consist of a
one-dimensional array. At present, such data can only be plotted against a single one-dimensional axis even if it is
distributed in two-, three-, or higher-dimensional space. If we are to have a standard method of plotting such data,
we need to have a way of identifying the pixel coordinates.

Proposal
--------

An extra attribute be defined for a data (or signal) SDS called coordinates, which would consist of a text string
containing the names of one or more SDSs that represent the coordinates of the signal SDS. The names will be separated
by the same delimiters allowed for the axes attribute. The signal SDS must be one-dimensional. There are two scenarios:

1. The coordinates represent the centre of each pixel, so each coordinate SDS is also one-dimensional of the same
length as the signal SDS.

2. The coordinates represent the vertices of each pixel, so each coordinate SDS would be two-dimensional, with the
slower changing dimension having the same length as the signal SDS and the faster changing dimension having a length of
the number of vertices (=2\ :sup:`n` for cartesian coordinates, where *n* is the number of coordinate SDSs). In that
case, an attribute number\_vertices containing an integer specifying the number of vertices will be added to the signal
SDS.

Discussion
----------

Here is an example NXdata group:
One problem is that the coordinates are not necessarily orthogonal. This is the case for the above example, in which the spherical polar coordinates, polar\_angle and azimuthal\_angle, are not orthogonal. Any plotting program will have to know that SDSs with those particular names have to be treated differently from those that are orthogonal. There may be a case for the standard stating how to handle a number of specific instances, *e.g.*, spherical polar coordinates, reciprocal-space coordinates in symmetries lower than orthorhombic, *etc*. In cases where the plotting program is only able to handle pixel centres, but vertices are provided, the pixel centres would have to be approximated by the average value of the vertices for each coordinate.

I propose to present this for discussion and a possible vote at the upcoming NIAC meeting at the SNS on October 7-8. Ray 19:08, 29 September 2010 (UTC)

Conclusion
----------

01/2015: This has been superseded by the new axes annotation scheme decided at NIAC 2014.