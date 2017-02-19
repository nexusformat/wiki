---
title: DECTRIS Example
permalink: DECTRIS_Example.html
layout: wiki
---

DECTRIS Example 1/2013
======================

There are the following problems with 1/2013 example file:

-   Structure is wrong regarding linked data sets. Should be either:
    -   entry:NXentry/data\_00001:NXdata/data
    -   entry:NXData/data:NXdata/data\_0001
-   On data, signal=1 attribute is missing
-   On external link, NeXus attribute
    NAPIMOUNT=nxfile:///th02c\_ps02\_1\_data\_000001.h5\#data missing
-   In detector, flatfield, effivciency data is missing. This is not
    critical, just wondering.

