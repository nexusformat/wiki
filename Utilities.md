---
title: Utilities
permalink: Utilities/
layout: wiki
---

NeXus Browsers and Other Utilities
----------------------------------

[NXbrowse](NXbrowse "wikilink"):A command-line utility for browsing NeXus files.  
NXtoXML:A utility to translate NeXus files to XML, written in ISO C. If used from a terminal (and installed in the default PATH \[u\*\*x\] or defined as a symbol \[VMS\]), type  

<!-- -->

    NXtoXML <NeXus_file> <XML_file>

  
On most systems, NXtoXML is compiled and linked during the standard
NeXus installation (v2.0 and later). Precompiled binary versions are
available for a limited number of operating systems (Linux, VMS,
Macintosh). Please contact Ray Osborn for more information.

NXtoDTD: A utility to translate NeXus files to XML without including the data values, written in ISO C. This is useful in defining the structure of a NeXus file and can be used to produce the skeleton of a NeXus metaDTD file from an existing NeXus file. If used from a terminal (and installed in the default PATH \[u\*\*x\] or defined as a symbol \[VMS\]), type  

<!-- -->

    NXtoDTD <NeXus_file> <XML_file>

  
On most systems, NXtoDTD is compiled and linked during the standard
NeXus installation (v2.0 and later). Precompiled binary versions are
available for a limited number of operating systems (Linux, VMS,
Macintosh). Please contact Ray Osborn for more information.

[NXdir](NXdir "wikilink"):CLI tool that lists contents of NeXus file and convert selected portions to ASCII.  
NXtree:A utility to output the structure of a NeXus file in a tree structure. It has options to produce either HTML or LaTeX output, with or without data values and attributes.  

<!-- -->

    NXtree [-[no]attr] [-[no]data] [-html | -latex] <NeXus_file>

  
The file NXtree.tar.gz contains the source code to be used on u\*\*x
platforms and NXtree-win32.zip contains a binary version for various
flavors of Windows. It was written by Thomas Proffen
&lt;tproffen@lanl.gov&gt;

NXvalid:GUI tool to interactively explore, plot, and validate NeXus files.  
NXtranslate:Anything to NeXus converter  
NDS:NeXus data server, publish NeXus files on TCP/IP, read only (SINQ)  
NNDB:Java program to browse NeXus files published through NDS (SINQ)  
HDFView:Java-based tool for browsing and visualizing HDF4/5 files.  
HDFExplorer:Windows 95/98/NT HDF viewer. Since this link is now broken, I have no idea if they are still maintaining the product.  
