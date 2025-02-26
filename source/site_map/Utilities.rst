NeXus Browsers and Other Utilities
----------------------------------

`[NXbrowse] <NXbrowse.html>`__: 
A command-line utility for browsing NeXus files.

**NXtoXML**: 
A utility to translate NeXus files to XML, written in ISO C. If used from a terminal (and installed in the default PATH [u**x] or defined as a symbol [VMS]), type

    NXtoXML <NeXus_file> <XML_file>

On most systems, NXtoXML is compiled and linked during the standard NeXus installation (v2.0 and later). Precompiled binary versions are available for a limited number of operating systems (Linux, VMS, Macintosh). Please contact Ray Osborn for more information.

**NXtoDTD**: 
A utility to translate NeXus files to XML without including the data values, written in ISO C. This is useful in defining the structure of a NeXus file and can be used to produce the skeleton of a NeXus metaDTD file from an existing NeXus file. If used from a terminal (and installed in the default PATH [u**x] or defined as a symbol [VMS]), type

    NXtoDTD <NeXus_file> <XML_file>

On most systems, NXtoDTD is compiled and linked during the standard NeXus installation (v2.0 and later). Precompiled binary versions are available for a limited number of operating systems (Linux, VMS, Macintosh). Please contact Ray Osborn for more information.

`[NXdir] <NXdir.html>`__:
CLI tool that lists contents of NeXus file and convert selected portions to ASCII.

**NXtree**:
A utility to output the structure of a NeXus file in a tree structure. It has options to produce either HTML or LaTeX output, with or without data values and attributes.

    NXtree [-[no]attr] [-[no]data] [-html | -latex] <NeXus_file>

The file NXtree.tar.gz contains the source code to be used on u**x platforms and NXtree-win32.zip contains a binary version for various flavors of Windows. It was written by Thomas Proffen <tproffen@lanl.gov>

**NXvalid**:
GUI tool to interactively explore, plot, and validate NeXus files.

**NXtranslate**:
Anything to NeXus converter

**NDS**:
NeXus data server, publish NeXus files on TCP/IP, read only (SINQ)

**NNDB**:
Java program to browse NeXus files published through NDS (SINQ)

**HDFView**:
Java-based tool for browsing and visualizing HDF4/5 files.

**HDFExplorer**: Windows HDF viewer for HDF4, HDF5 and netCDF files from <http://www.space-research.org> offers grid/scalar image/vector images and data export.

**IgorPro HDF5 Browser**:
Windows and MacOSX HDF viewer for HDF4 and HDF5 files from <http://www.wavemetrics.com> provides views of raw content dumps, tables, plots, and images, and data import.

Plotting Applications
---------------------

`[NeXpy] <NeXpy.html>`__:
A Python-based approach to interactive data analysis that allows complete data structures to be read into a tree and new data structures to be created using a simple intuitive syntax. The data can be plotted, sliced, manipulated, and saved to a file.

**[Open Genie] <http://www.opengenie.org/)**:
Open Genie is an object-oriented data analysis and visualization package developed at the ISIS pulsed neutron facility. The latest version has the ability to load an entire NeXus file into a workspace structure, as well as write NeXus files.

**ISAW**:
ISAW is a java-based analysis package used to read, manipulate, view, and save neutron scattering data. ISAW can read data from NeXus files and can merge and sort data from separate measurements.

**IDL**:
Mark Koennecke has written a set of IDL utilities for interfacing to NeXus files.

**LAMP**:
This is a general purpose neutron data analysis package, developed at ILL and layered on IDL. A run-time version is available for those without an IDL license. It can read and write NeXus files.

**[KUPLOT] <http://discus.sourceforge.net)**:
This is a universal data plotting program, that is used to visualize DISCUS or PDFFIT results as well as for other plotting purposes.

**NXviewer**:
OpenDave based viewer (FRM2).

**HDFLook**:
Motif HDF viewer which has some impressive plotting capabilities. For example, it is possible to plot 2D data sets and then take arbitrary 1D cuts. However, it does not recognize Vgroups, so the NeXus file hierarchy is lost making it hard to identify the plottable data. However, the price is right (i.e. it's free).

**MATLAB**:
[MATLAB] <http://www.mathworks.com/products/matlab/) will read a general [HDF5] <http://www.hdfgroup.org/HDF5/) format file and so is able to import any NeXus file which used HDF5 as its underlying representation.

Data Analysis
-------------

`[NeXpy] <NeXpy.html>`__:
A Python-based approach to interactive data analysis that allows complete data structures to be read into a tree and new data structures to be created using a simple intuitive syntax. The data can be plotted, sliced, manipulated, and saved to a file.

**[Open Genie] <http://www.opengenie.org/)**:
I include Open Genie here as well since it is really more of a data analysis package than a plotting package per se. Support for performing analysis on NeXus files is currently limited, but can be accomplished by mapping parts of the imported NeXus file into a new workspace that to make it resemble an ISIS RAW data file.

**LAMP**:
LAMP is also designed for analyzing raw data in addition to visualizing the results.

**UDA and WIMDA**:
General purpose muon scattering analysis packages (ISIS)

**hdfb.sav and h5b.sav**:
Browser for any 1D/2D/3D data saved in HDF (APS)

**GumTree**:
Scientific workbench for instrument control (BI)

**ninx**:
Inx (ILL) adapted to read FOCUS TOF files (SINQ)

**Nathan**:
TOF data analysis for FOCUS (IDL based) (SINQ)

**anatric, cami4pcd**:
Four circle diffractometer data analysis (SINQ)

**BerSANS**:
Data analysis for SANS through adapter (SINQ)

**fit**:
Home grown fitting program (SINQ)

**addit, subi**:
Programs to add or subtract powder data and write files suitable for Rietveld programs (SINQ)

**Redas**:
Data analysis for Reflectometer, based on Scilab (SINQ)

**Amortool**:
Simple CLI tool for Reflectometer data analysis (SINQ)

**Scilab**:
General MATLAB-like data analysis tool - with a NeXus interface for that (SINQ)

**[Mantid] <http://www.mantidproject.org/)**:
An instrument independent data analysis framework that supports NeXus as an output format and both [TOFRaw] <TOFRaw.html>`__ and [Muon_Time_Differential] <Muon_Time_Differential.html>`__ as input formats.
