---
title: 2014 How to find default data
permalink: 2014_How_to_find_default_data/
layout: wiki
---

(written for [NIAC2014\_Meeting](NIAC2014_Meeting "wikilink"))

One of the
[motivations](http://download.nexusformat.org/doc/html/motivations.html)
for NeXus is [simple
plotting](http://download.nexusformat.org/doc/html/motivations.html#simpleplotting).

The [procedure to find the default data to be
plotted](http://download.nexusformat.org/doc/html/datarules.html#find-plottable-data)
is convoluted. In some cases (files with multiple NXentry and/or NXdata
groups), it is not certain which data will be found.

This proposal is to add a new and simpler mechanism to manage (both set
and determine) the path to the default data. The intent is that this
addition to NeXus preserves backwards compatibility and becomes the
standard way for new data files to identify the default data to be
plotted.

Proposal
--------

-   add *default\_NXentry* attribute to the root of the file that states
    which NXentry is the default. The value is the name of the NXentry
    group.
-   add *default\_NXdata* attribute to each NXentry that states which
    NXdata is the default. The value is the name of the NXdata group.
-   add *default\_data* attribute to each NXdata that states which
    dataset is the default. The value is the name of the dataset to be
    plotted.

These default attributes only describe child elements, not child/object
or ../object or other hierarchy.

The procedure to identify the default data to be plotted is quite
simple, given any NeXus file, any NXentry, or any NXdata. Follow the
chain as it is described from that point.
