---
title: 2014 How to find default data
permalink: 2014_How_to_find_default_data/
layout: wiki
---

One of the
[motivations](http://download.nexusformat.org/doc/html/motivations.html)
for NeXus is [simple
plotting](http://download.nexusformat.org/doc/html/motivations.html#simpleplotting).

The [procedure to find the default to be
plotted](http://download.nexusformat.org/doc/html/datarules.html#find-plottable-data)
is convoluted. In some cases (files with multiple NXentry and/or NXdata
groups), it is not certain which data will be found.

This proposal is to add a new and simpler mechanism to determine the
path to the default data. The intent is that this addition to NeXus
preserves backwards compatibility and becomes the standard way for new
data files to identify the default data to be plotted.
