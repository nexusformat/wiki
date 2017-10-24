---
title: Code Camp 2017
permalink: Code_Camp_2017.html
layout: wiki
---

NeXus Code Camp - 24th to the 26th of October, 2017
===================================================

Registration
------------

Please register for the event using the [linked form](https://fs3.formsite.com/DiamondLightSource/form136/index.html), for numbers and requirements.

You also need to book a room!

Location: The Cosener's house, Abingdon UK
-----------------------------------------

Please book using the group reference code **63197**

[Venue Website with contact details](http://www.stfc.ac.uk/about-us/where-we-work/rutherford-appleton-laboratory/the-cosener-s-house/)

Agenda
------

**Tuesday**

Morning
  * Shape descriptions (Dean Keeble and Tim Spain will be visiting)

Afternoon
  * C++ wrappers for HDF5 
  * Features
  * Example files for Ray.
  
Evening
  * 6:00 - 6:30 pre dinner drink
  * 7:00 - Dinner at cosners house
    * Main-Course: Rack of lamb with rosemary crumb, dauphinoise potato, chargrilled courgette, vine roasted cherry tomato, fine bean parcel and rosemary jus
    * Vegetarian Option: Asparagus and broad bean risotto, parmesan tuile and lemon balm
    * Pudding: Classic glazed lemon tart, crème fraiche and berries
    *	5 x bottles of wine (2 x red, 3 x white)

**Wednesday**

Morning 
  * PDB integration (Greame Winter and Charles Mita will be visiting)
  * Dealing with dropped frames

Afternoon
  * Detectors with modules in modules. (Aaron Brewster may be VCing in)

Evening
  * Reservartion for 7:00 at [wildwood](https://wildwoodrestaurants.co.uk/restaurant/abingdon/)

**Thursday**

Morning
  * Event data (Alan Greer also attending)
  * Event log disscussion and focus on example files.

Afternoon
  * Versions

The aim is to start at 10:00 on the 24th and finish early afternoon on the 26th.


Minutes for the meeting
=======================

Introductions
  * Move the PDB and versions to the afternoons so that Pete Jamian can VC in
  
**Tuesday Morning**

First item is to investigate the shape methodoloy as investigated by the ESS team
  * There is concern over how the shape can accurately describe detectors, and how the data is mapped to the shape.
  * Visualisation is important, but so it the use of full descriptions for analyis
  * The [OFF format](https://en.wikipedia.org/wiki/OFF_(file_format)) will be used for MANTIS and MCStas
  * A new description for [Quadrics](https://github.com/golosio/xrmc/wiki/User-guide#the-quadric-array-file) will be developed by DLS to deal with more complex descriptions for use with xrmc.  There should be a converter for this to the OFF NeXus description. 
  
**Tuesday Afternoon**

2 Seperate threads

Versioning
  * Looking at the versioning concept as in the [document](http://www.nexusformat.org/NIAC2016Minutes.html)
  * Big discussion about the complexity of local vrs. global versioning, i.e version on baseclasses vrs. versioning on the file.
  * Came to the conclusion of a single version number which increments gradually and incrementally to deal with new versions.
  * Things to do
    * UPDATE WORKFLOW - Questions here, but we will try to address at the code camp.
    * VERSIONING SEMANTIC - Big changes bump version by 1
    * VALIDATION - is easier now as there is only one global version to validate against
    * LEGASY DOC - Still in the repository.

C++ wrappers for HDF5
