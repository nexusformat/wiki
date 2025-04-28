---
title: Scans
permalink: Scans.html
layout: wiki
---
Scans
=====

This page is currently under construction
-----------------------------------------

When completed, this page will be used as the basis of a discussion on
how to represent scans within a NeXus file. It will bring together ideas
and discussions from [TOFRawScan](TOFRawScan.html "wikilink"),
<NIAC2006:_Scanning_Group> and [GenericScan](GenericScan.html "wikilink")

### What is a Scan

In its broadest sense, a scan is a set of measurements where parameters
have been varied in a systematic way. These separate measurements may
all be stored in the same file (via an additional array dimension or
additional separate [NXentry] (NXentry.html "wikilink")), several files or a
mixture of the two schemes.

Issues
------

The goal is to be able to identify what parameters have been varied as
part of the scan. Some of the issues to consider are:

-   How to build parametric scans such as 10 temperatures for 5 fields.
-   How to identify all files associated with a scan.
-   How to identify whether a particular file is associated with a scan.
-   What to do if a part of the scan is missing?
-   What if the scan is not rectilinear?

NXscan proposal
---------------

Three proposals:

### NXscan proposal - Mark

    <NXscan>
       <scan_dimensions type="NX_INT[dim]"/>
       <slice_start type="NX_INT[dim]"/>
       <slice_end type="NX_INT[dim]"/>
       <scanvars type="NX_CHAR">
          {comma separated list of scanned variables}
       </scanvars>
       <scanlinks type="NX_CHAR">
          {comma separated list of path strings to the scan variables in the file}
       </scanlinks>
    </NXscan>

### NXscan proposal - Paul

      <NXscan>
        <variable label="" units="" type=FLOAT[2] dims=[ndims] slice=[ndims,2] 
            index="" value="" axis="" primary="0|1">
          {value store is the minimum and maximum of variable range.  
     
           label and units help you create the axis labels for the plot.
     
           num_points is the number of points intended in the scan (the 
           actual value may be less if the scan was aborted).  The intended 
           number may be indefinite, in which case it is absent.
     
           index is the position in the scan if the scan spans multiple 
           entries, or it is absent if all scan points are within this entry.  
           index is 1-orgin.
     
           if index is specified, it has an associated value, otherwise the
           values will need to be stored elsewhere in the entry.  where?
           Can value be the name of a field?
     
           For raster scans axis will be 1, 2, 3, ... and primary will be 0
           For each axis there should be a single primary.
     
           For dependent variables axis will be the 1, 2, 3, ... for the variable
           it is dependent upon and primary will be 1.  You can have any number
           of dependents.
          }
        </variable>
      </NXscan>


      <-- Example temperature scan -->
      <NXscan>
        <temperature label="T" units="K" type=FLOAT[2] num_points=25 index=3>
          10,100
        </temperature>
      </NXscan>

      <-- Example raster scan -->
      <NXscan>
         <x name="x" type=FLOAT[2] num_points=11 index 4>
             0,10
         </x>
         <y name="y" type=FLOAT[2] num_points=4 index 3>
             5,8
         </y>
       </NXscan>

### NXscan - Ray

Link entry to next entry in the scan in some way so that the system can
find all the pieces by itself.
