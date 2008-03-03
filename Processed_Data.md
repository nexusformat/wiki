---
title: Processed Data
permalink: Processed_Data/
layout: wiki
---

Template of a generic NXentry containing processed data.

The assumption is that measured data, which could, for example, stored
in another NXentry within the same file, has been reduced to a standard
form, e.g., S(Q), so that the instrument information is no longer
required. It is only necessary, therefore, to store the multidimensional
array containing the processed data within one or more NXdata groups.

This is not a true metaDTD because both the values and the axis names
can use something more descriptive.

<nxformat file="NXprocessed.xml" tree="yes"></nxformat>
