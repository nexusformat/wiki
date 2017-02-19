---
title: History
permalink: History.html
layout: wiki
---

The NeXus format has combined the ideas of different proposals
originating in the United States and Europe. It has been developed at
four workshops, SoftNeSS'94, '95 and '96 and NeXus'2001. This section
summarizes the motivation for developing the format in more detail, as
well as providing some historical background to its development. The
details of the format itself are discussed in subsequent sections.

Purpose of Format
-----------------

Until recently, the experimental research community did not have any
motivation to standardize the form in which data are stored on
computers. Scientists had self-contained, well-defined sets of programs
to process and display the data. However, it is now more common for
researchers both to perform experiments at a number of different
institutions, and to attempt novel ways of data reduction. When they do,
they quickly encounter the difficulties that arise from the lack of an
established standard for exchanging the data. We discuss below some of
the potential advantages of such a standard format.

### Advantages of a Common Data Format

Reduce need for local expertise:Before developing data analysis or visualization software, the programmer must learn how to obtain meaningful data from the existing data files. This can sometimes require a considerable investment in time and effort in order to acquire an adequate understanding of local formats. Small but important details, e.g. the sign convention used in angle offsets or the value of electronic time delays, are not always well documented but are vital to interpreting the data. A common data format will obviate the need to obtain this expertise at all the facilities that they visit.  

<!-- -->

Reduce number of conversion utilities:If researchers are to attempt their own analysis, it is necessary to write format conversion tools. Writing individual tools is not a serious problem, but with the growing number of research groups performing scattering experiments, we are faced with a combinatorial explosion of the number of converters. A common data format reduces the number of converters from n × n to 2n. If all newly-written programs would read and write the common format, the need for data conversion would disappear altogether.  

<!-- -->

Reduce redundant softare development:New software is being developed all the time at different facilities. However, the need for format conversion is normally a serious barrier to implementing these programs away from the institute in which they were developed. One result is that software with similar functionality is reproduced many times over.  

<!-- -->

Increase cooperation in software development:We believe that a common format will lead to greater cooperation in software development both within and between the neutron and X-ray synchrotron communities. Many of the techniques of data manipulation and display are common to both communities, but there has been very little interaction between them. The ability to use common utilities to browse and plot neutron and X-ray data should make it easier to share software solutions to common problems.  

<!-- -->

Increase sophistication of visualization software:There is an urgent need to develop more sophisticated visualization tools with the growth in the number of multidetector elements on new instruments. New scattering techniques (e.g. single crystal inelastic scattering on time-of-flight spectrometers) require novel ways of viewing the data. However, programmers are deterred from investing the necessary resources to produce these tools because their results are usually limited to single institutions, and in some cases, single instruments. It is also difficult to build on developments elsewhere.  

<!-- -->

Increase functionality of generic software:Increased standardization can lead to increased functionality. It is now possible to 'drag and drop' word processor files onto printer icons because both word processors and printers commonly understand the Postscript language. Similarly, it will be possible to develop more automated means of reading and viewing experimental data if that data is stored in a standard form. By basing the standard on a public domain format, such as HDF, we can immediately take advantage of the tools already developed for those formats.  

Guiding Principles
------------------

In designing the NeXus format, the team has been guided by a number of
general principles. These are intended to ensure that the format meets
the needs of as wide a cross section of the neutron and X-ray scattering
communities as possible. Fortunately, the computing technology available
to us now allows us to be very flexible in the organization and
comprehensiveness of the format without rendering the standard useless.

Allow different levels of implementation:It is up to those implementing the standard at any institution to decide how much information to include in the NeXus files. However, the standard defines how such information should be stored if it is included. This allows analysis programs to search for the information, and prompt for it if it is absent. There could be substantial benefits from including more detailed instrumental information, and users will be encouraged to do so. However, in many cases, the files will be produced by automatic translation utilities from existing data files, so we cannot require more detail than currently stored at any facility.  

<!-- -->

Provide flexibility of structure:Although some NeXus files will be extremely simple, perhaps containing a single data set, the standard should be flexible enough to be able to describe extremely complex instrumentation comprising many different components. At some facilities, the standard will be used to archive the raw data and all related parameters so there has to be a method of storing this information in an easily assimilated fashion.  

<!-- -->

Produce definitions of common instrumentation:It is our intention that the format be defined for generic forms of neutron and X-ray instrumentation e.g. triple-axis spectrometers, pulsed neutron powder diffractometers etc. This will show developers of analysis software what information should be available in typical data files, and how to access it.  

<!-- -->

Facilitate automated plotting:One aim of the standard is to facilitate automatic plotting and analysis as far as possible. This means that generic plotting software should be able to identify easily what parts of the file contain plottable data. These data should include independent axis scales, labeling, units and titles.  

Criteria for Data Format
------------------------

Modern data formats no longer require the programmer to learn the
details of the physical layout of the file in order to read or write
data. This is because the interaction with the data file is through a
program interface, commonly known as the Application Program Interface,
or API. If the format is self-describing, the progammer only needs to
know the keywords used to identify specific data sets, and perhaps the
logical framework in which the data is stored.

In our view, the neutron and X-ray community does not have the resources
to develop and maintain a completely new data format and its associated
interface software. An early decision therefore was to utilize one of
the many existing formats as the basis of the NeXus format. In our
selection, we used the following criteria:

It must be portable:The format must be network transparent and readable across a wide range of hardware platforms.  

<!-- -->

It must be self-describing:It should be possible to determine the contents of the file even without documentation.  

<!-- -->

It must be extensible:It should be possible to add extra information to the NeXus file without needing to reformat the whole file.  

<!-- -->

It must be flexible in data organization:The trend at neutron and X-ray facilities is toward the development of more complex instrumentation.  

<!-- -->

It must be efficient in data storage:The format must be able to handle the growing volumes of data produced at current and future scattering facilities. In most cases, this entails the use of binary data storage.  

<!-- -->

It must be available in the public domain:It is important that NeXus is not subject to commercial restrictions or dependent on the financial health of any individual company.  

Public-Domain Data Formats
--------------------------

The following data formats are widely used, well supported and available
in the public domain. All were considered as possible formats on which
to base NeXus, but rejected for the reasons given. The comments are not
meant to imply a criticism of the design or functionality of these
formats, all of which have served their user communities well, but
rather to give a justification for our eventual selection.

CIF:The Crystallography Information File format is supported by the International Union of Crystallography for the storage of crystallographic structure solutions and descriptive information concerning the experiments. It is an ASCII format and is not currently intended for storing raw data. There is a proposal to extend the CIF format to include binary images, imgCIF/CBF, which is being developed under the auspices of the IUCr, but we have concluded that it does not have sufficient flexibility to store data from more complex instrumentation (see note on imgCIF/CBF).  

<!-- -->

FITS:The Flexible Image Transport System, the astronomical data format, only addresses the issue of data portability, and is not self-describing. Therefore it requires problem-specific programs for both reading and writing the data.  

<!-- -->

ISO STEP/Express:This is a standard for describing database structures rather than a data format itself, and has been used for industrial applications more than scientific ones. However, it could be used to develop a formal model of a NeXus file and its constituent data objects which would then be “compiled” into the actual data format. The object-model of STEP/Express has influenced the NeXus design, but there are no plans to use it any further because of our limited resources.  

<!-- -->

netCDF:The netCDF standard developed at Unidata fulfils many of our criteria since it is binary, portable, self-describing and extensible. It has a very attractive data model, allowing for the annotation of multidimensional data with axes, units and other attributes. This led to its proposed adoption by the European neutron scattering community (See Ref. 1 of the SoftNeSS'94 report). It is also widely supported by public-domain and commercial applications. The main drawback of netCDF is that it is a flat-file format. This means that all data sets must have unique names and cannot be organized into hierarchical groups.  

### Choice of HDF

The Hierarchical Data Format has been developed at the National Center
for Supercomputing Applications (University of Illinois, Urbana
Champaign). Like netCDF, it is binary, self-describing and extensible,
and has been ported to a wide range of computer platforms, including PC
and Macintosh, workstations and minicomputers, mainframes and massively
parallel environments. It is actively maintained and used by an
increasing number of organizations and scientific communities.
Furthermore, many data visualization packages, such as IDL, MatLab,
PV-wave, AVS and Data Explorer can access HDF files. It is even possible
to view HDF files using web browsers, although this is not yet available
for all platforms.

We have chosen HDF over netCDF because of the greater flexibility it
gives us in organizing the instrument descriptions to be contained in
NeXus files. This is because it is possible to organize data sets into a
hierarchy of data ensembles. Many of the most attractive features of
netCDF have been incorporated into recent versions of HDF (after v3.3r3)
removing any obstacles to its adoption as the NeXus format.

History of Format
-----------------

Three parallel developments have led to the idea of a common data format
for neutron and X-ray scattering data.

-   Jon Tischler (ORNL) proposed an HDF-based format as a standard for
    data storage at the Advanced Photon Source (Argonne National
    Laboratory) (Ref. 1).

<!-- -->

-   Mark Koennecke (PSI) made a similar proposal using netCDF for the
    European neutron scattering community while working at the ISIS
    pulsed neutron facility (Ref. 2).

<!-- -->

-   Przemek Klosowski (NIST) produced a first draft of the NeXus
    proposal drawing on ideas from both sources (Ref. 3).

This formed the basis for the current design of the NeXus standard which
has been developed at two workshops, SoftNeSS'95 (NIST Sept. 1995) and
SoftNeSS'96 (Argonne Oct. 1996). A brief description was published in
the proceedings of the International Conference on Neutron Scattering,
Toronto, 1997 (Ref. 4)

Several steps have been taken to obtain the support of the neutron and
X-ray scattering communities:

-   The report of the original SoftNeSS workshop, SoftNeSS'94, was sent
    to over one hundred neutron and X-ray scatterers around the world
    inviting their comments and involvement in the format development.

<!-- -->

-   One result is that many scattering facilities sent representatives
    to the next workshops, including Brookhaven, Chalk River, ILL, IPNS,
    ISIS, LANSCE, NIST and PSI. In addition, we obtained the support of
    many other facilities.

<!-- -->

-   John White, the president of the neutron commission of the IUCr, has
    proposed that we seek the formal approval of the IUCr. Informal
    contacts have been made prior to a formal approach.

<!-- -->

-   In January 1996, the proposal was presented by Ray Osborn to the
    Workshop on New Opportunities for Better User Group Software
    (NOBUGS), jointly organized by the ILL and ESRF, and attended by
    both X-ray and neutron scattering scientists and software developers
    from around the world.

<!-- -->

-   In August 1996, the proposal was presented by Przemek Klosowski to
    the Neutron Scattering Satellite Meeting of the IUCr, NIST,
    Maryland.

<!-- -->

-   A symposium was held during ICNS'97 in Toronto to present the NeXus
    format to the neutron scattering community. Ray Osborn described the
    design philosophy and Przemek Klosowski gave a technical
    presentation followed by demonstration of the Tcl/Tk interface that
    he and Nick Maliszewskyj have developed.

<!-- -->

-   Przemek Klosowski attended the imgCIF Workshop held at Brookhaven
    National Laboratory on October 20 and 21, 1997, to discuss relations
    between the NeXus and imgCIF formats (See Note).

<!-- -->

-   In December 1997, Mark Koennecke and Przemek Klosowski gave a
    tutorial session on using NeXus to the second Workshop on New
    Opportunities for Better User Group Software (NOBUGS), jointly
    organized by the APS and IPNS. As with the first workshop, it was
    attended by both X-ray and neutron scattering scientists and
    software developers from around the world.

<!-- -->

-   Mark Koennecke and Przemek Klosowski represented the NeXus format at
    two canSAS workshops, which aimed to define interchange standards
    for neutron and x-ray small angle scattering.

<!-- -->

-   In September 1999, Mark Koennecke attended a round-table discussion
    on data formats in muon spin relaxation. There was some interest in
    using NeXus, particularly since muon facilities at PSI and ISIS can
    cooperate with their neutron scattering neighbours. The minutes of
    their discussion are available on the web.

<!-- -->

-   In August 1999 and January 2000, Ray Osborn gave introductions to
    the NeXus format to instrument scientists at ISIS and IPNS/SNS
    respectively. The talks included online demonstrations of the
    portability of the NeXus files (from VMS to Windows NT to Linux to
    Macs) and the ability to browse or display NeXus data with
    third-party HDF utilities, both freeware and commercial.

<!-- -->

-   At the recent NOBUGS III conference, several members of the NeXus
    design team made presentations of their work on NeXus. Mark
    Koennecke described a java web-based data server and browser,
    Przemek Klosowski discussed efforts at NIST to build a Tcl/Tk-based
    data explorer, and Chris Moreton-Smith presented a proposal to
    formalize the NeXus format in XML. There was also discussion of data
    formats in a workshop subgroup.

<!-- -->

-   The first completely open NeXus workshop was held at the Paul
    Scherrer Institut, Switzerland, on March 20-21, 2001. It was
    attended by thirty-five scientists and software developers
    representing fourteen different neutron, x-ray, and muon facilities,
    and user institutions.

<!-- -->

-   A breakout session was held at the first American Conference on
    Neutron Scattering, attended by representatives from Argonne, Los
    Alamos, SNS, ISIS, and ANSTO.

### References

1.  Jon Tischler, ORNL and UNI-CAT. (Chairman of the data standards
    committee for the APS CATs.) “Draft of Proposed Data Standards for
    the APS”, version 6, August 19, 1994.
2.  Mark Koennecke, PSI. “Proposal for a European Neutron Scattering
    Data Exchange Format”, version 4.2, June 17, 1994.
3.  Przemek Klosowski, NIST. “NEXUS - a portable, extensible,
    self-describing data format for neutron and X-ray scattering data,”
    version 1.24, October 7 1996.
4.  P. Klosowski, M. Koennecke, J. Z. Tischler and R. Osborn, “NeXus: A
    common format for the exchange of neutron and synchrotron data”
    Physica B **241-243**, 151-153 (1998)

Current Status
--------------

NeXus is still in the early stages of its development. We consider that
it is now ready for evaluation by any interested members of the neutron
and X-ray scattering communities. We therefore invite them to subscribe
to the NeXus Mailing List to receive news updates and to send feedback.
A critical component of the NeXus format is the Application Program
Interface for reading and writing NeXus files. Mark Koennecke, Przemek
Klosowski, and Freddie Akeroyd have produced the first version of the
API, along with more detailed documentation for the interested
programmer, which is available for downloading. Please see the API
section for more details.

We intend to monitor the support of NeXus in the neutron and X-ray
communities. If your home institute intends to support the format in any
way, or if any of the following information is inaccurate, please let me
know so that this record is kept up-to-date.

**For an up-to-date list of Facilities using NeXus please check the
[facilities page](Facilities.html "wikilink")**

### Neutron Scattering Facility Support

Chalk River Laboratories:Chalk River was involved in the development of NeXus with the participation of Ron Rogge in the SoftNeSS workshops.  

<!-- -->

Institut Laue-Langevin:The ILL has been active in the development of NeXus and intends to provide conversion utilities. Its data analysis software package, LAMP, can read and write NeXus files.  

<!-- -->

Intense Pulsed Neutron Source:IPNS was actively involved in the development of NeXus. The IPNS was shut down at the end of 2007.  

<!-- -->

ISIS Pulsed Neutron Facility:Apart from being involved in the development of NeXus, ISIS has incorporated the NeXus API into the new openGENIE data analysis package. Chris Moreton-Smith and Freddie Akeroyd are helping to develop the API.  

<!-- -->

Joint Institute for Nuclear Research:The Laboratory of Neutron Physics has expressed interest in using NeXus as their internal data format.  

<!-- -->

KEK Neutron Scattering Facility:KENS is redesigning their internal data format and is planning to use NeXus, both on existing instruments and at the proposed new Japanese spallation neutron source being built jointly by JAERI and KEK.  

<!-- -->

Laboratoire Léon Brillouin:The NeXus mailing list was recently informed that NeXus is currently in use on 5 spectrometers at the Saclay reactor facility.  

<!-- -->

Los Alamos Neutron Scattering Center:LANSCE has been active in the development of NeXus. New instruments being developed as part of the LANSCE upgrade, e.g. HIPPO, will use NeXus as their storage format.  

<!-- -->

NIST Center for Neutron Research:NIST has been actively involved in the development of NeXus and will eventually use the format to archive their data. Przemek Klosowski and Nick Maliszewskyj are on the API development team.  

<!-- -->

Paul Scherrer Institut:PSI is using NeXus as their raw data format in the SINQ Instrument Control Software, developed by Mark Koennecke, who was also responsible for writing much of the NeXus API.  

<!-- -->

Spallation Neutron Source:Although the SNS will not produce neutrons until 2006, preliminary discussions of possible data formats have already begun. NeXus is under serious consideration. I hope to be able to upgrade this status in the next few months. It is also being considered as an exchange format for the results of Monte Carlo instrument simulations during the design phase of the project.  

### X-ray Scattering Facility Support

Advanced Photon Source:NeXus-compliant files are one of the file format options in the [CCD Image Server software](http://www.aps.anl.gov/bcda/dataAcq/) developed and used at the APS. The [X-ray microtomography](http://www.aps.anl.gov/Xray_Science_Division/Xray_Microscopy_and_Imaging/Science_and_Research/Techniques/Tomography/index.html) instrument is a major user of this software and records some *O*(10<sup>5</sup>) images per month of operation. APS hopes that the NeXus committee will consider and provide for the storage of reduced data, analyzed data, simulated data, and the history of processing steps, in addition to the storage of raw data in NeXus files.  

<!-- -->

European Synchrotron Radiation Facility:The ESRF has developed its own binary data format, but has agreed to write conversion utilities to the NeXus format.  

<!-- -->

Diamond Light Source:The new Diamond Synchrotron Source is committed to use the NeXus format.  