---
title: Code Camp 2017
permalink: Code_Camp_2017.html
layout: wiki
---
Code Camp 2017
==============

NeXus Code Camp - 24th to the 26th of October, 2017
===================================================

Location: The Cosener's house, Abingdon UK
-----------------------------------------

[Venue Website with contact details](http://www.stfc.ac.uk/about-us/where-we-work/rutherford-appleton-laboratory/the-cosener-s-house/)

Agenda
------

## Tuesday

### Morning
  * Shape descriptions (Dean Keeble and Tim Spain will be visiting)

### Afternoon
  * C++ wrappers for HDF5 
  * Versioning

### After Coffee
  * Features
  * Example files for Ray.
  
### Evening
  * 6:00 - 6:30 pre dinner drink
  * 7:00 - Dinner at cosners house
    * Main-Course: Rack of lamb with rosemary crumb, dauphinoise potato, chargrilled courgette, vine roasted cherry tomato, fine bean parcel and rosemary jus
    * Vegetarian Option: Asparagus and broad bean risotto, parmesan tuile and lemon balm
    * Pudding: Classic glazed lemon tart, crème fraiche and berries

## Wednesday

### Morning 
  * PDB integration (Greame Winter and Charles Mita will be visiting)
  * Dealing with dropped frames

### Afternoon
  * 3pm VC with Pete on Versioning
  * Detectors with modules in modules. (Aaron Brewster may be VCing in)

### Evening
  * Reservartion for 7:00 at [wildwood](https://wildwoodrestaurants.co.uk/restaurant/abingdon/)

## Thursday

### Morning
  * Event data (Alan Greer also attending)
  * Event log disscussion and focus on example files.

### Afternoon
  * Wrap up and Telco

The aim is to start at 10:00 on the 24th, 9:00 the other days and finish early afternoon on the 26th.


Minutes for the meeting
=======================

## Tuesday Morning

Introductions
  * Move the PDB and versions to the afternoons so that Pete Jemian can VC in
  
First item is to investigate the shape methodoloy as investigated by the ESS team
  * There is concern over how the shape can accurately describe detectors, and how the data is mapped to the shape.
  * Visualisation is important, but so it the use of full descriptions for analyis
  * The [OFF format](https://en.wikipedia.org/wiki/OFF_(file_format)) will be used for Mantid and McStas
  * A new description for [Quadrics](https://github.com/golosio/xrmc/wiki/User-guide#the-quadric-array-file) will be developed by DLS to deal with more complex descriptions for use with xrmc.  There should be a converter for this to the OFF NeXus description. 
  
## Tuesday Afternoon

2 Seperate threads

### Versioning
  * Looking at the versioning concept as in the [document](http://www.nexusformat.org/NIAC2016Minutes.html)
  * Big discussion about the complexity of local vrs. global versioning, i.e version on baseclasses vrs. versioning on the file.
  * Came to the conclusion of a single version number which increments gradually and incrementally to deal with new versions.
  * Things to do
    * UPDATE WORKFLOW - Questions here, but we will try to address at the code camp.
    * VERSIONING SEMANTIC - Big changes bump version by 1
    * VALIDATION - is easier now as there is only one global version to validate against
    * LEGACY DOC - Still in the repository.

### C++ wrappers for HDF5
  * On ess-dmsc github [h5cpp](https://github.com/ess-dmsc/h5cpp)
  * Came out of some HDF work, didn't like the C++ API.
  * Various parties were doing their own - Tobias asked them to work together.
  * Eugen and Martin, ocassionally Jonas Nilison
  * Auto builds docs, doxygen
  * Migration of Eugen PNI code at the beginning. Lack of tests, now adding more tests.
  * Aim to cover all of HDF5 features, e.g. SWMR, compound data types etc.
  * Examples of implementation: write_simple_vector
  * Suggest to use clang format.
  * Using google's style guide - need consistency
  * Fortnightly meetings
  * Implemented types: basic types int, float etc.
  * Going to be used in the file writer
  * Trying to make it as easy to use as h5py
  * Looked at internal Paths
  * Plan to create performance tests
  * Will put on to conan
  * Martin will replace the naïve version he is currently using.
  * Detector people are interested in using it to store diagnostic data.
  * Happy to take suggestions for things to be implement from other parties.
  * Discussed using in-memory files for performance tests
  * Setting up Windows automated build and hoping to OSX
  * MPI support in the future?
  * Using runtime exceptions - should it use something more tailored? Do something with the hdf error stack

## Wednesday Morning

### NXmx PDB discussion
  * It was decided that NXmx could easily contain an NXpdb which contains the basic information required for PDB ingest
  * Charles Mita from DLS will make a first pass at this for VMXi data
  
### Dropped frames
  * could the value be set to NXdetector.undefined, or NXdetector.saturation_value
  * Could the count_time value be set to zero (or annother value) for the frame which is not there. 
    * a valid count time is anything zero or above, anything other than this is an invalid frame.
  * The solution was to create a new dataset called frame_acquired
    * a boolean dataset
    * True if the frame is correcly collected, if the frame has been dropped by the datawriter and padded with fill value, then this shoud be set to False
    * The fill value should be set to a value larger than the NXdetector.saturation_value

## Wednesday Afternoon

### Features
  We all continued to work on features.
 
### Versions revisitited with Pete
 * It was agreed that Base class versions were not that useful, and so these can be made optional to inherit from the main version
 * Agreed with the concept of global versioning
 * in the January release the version numbers will move to Year.Month instead of 3.4
 
### Modules in Modules, with Aaron Brewster.
 * Seems like a sencible option
 * TASK on AB to update the documentaion on modules to clarify the usage of the depends-on and pixel size   
 * TASK on AB to make an NXlog index class for multiple event streams.
 
## Thursday Morning
 * Discussion on NXevent_data 
 * Continue on features
 
## Thursday Afternoon
