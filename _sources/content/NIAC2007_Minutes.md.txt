---
title: NIAC2007 Minutes
permalink: NIAC2007_Minutes.html
layout: wiki
---
NIAC2007 Minutes
================

Version in [PDF](../pdfs/NIAC2007HMI_minutes.pdf "wikilink") format

NIAC meeting – HMI, Berlin (Germany) 24, 25, 26 September 2007
--------------------------------------------------------------

The NIAC meeting for 2007 was held at HMI (Berlin) in September 2007.
List of attendees

-   Gwenaelle Abeille, Synchrotron Soleil, France
-   Freddie Akeroyd, ISIS Facility, Rutherford Appleton Laboratory, UK
-   Stuart Campbell, Diamond Light Source, UK
-   Stephen Cottrell, ISIS Facility, Rutherford Appleton Laboratory,
-   Matthias Drochner, Forschungzentrum Jülich, Germany
-   Stefan Flemming, The Open University, UK
-   Andrew Gotz, European Synchrotron Radiation Facility, France
-   Nick Hauser, Australian Nuclear Science and Technology Organisation,
    Australia
-   Jens-Uwe Hoffmann, Hahn-Meitner-Institut Berlin, Germany
-   Pete Jemian, Advanced Photon Source, USA
-   Mark Koennecke, Paul Scherrer Institut
-   Laurent Lerusse, Rutherford Appleton Laboratory , e-Science
-   Ray Osborn, Argonne National Laboratory, USA
-   Peter Peterson, Spallation Neutron Source, Oak Ridge National
    Laboratory, USA
-   Frédéric Picca, Synchrotron Soleil, France
-   Stephane Poirier, Synchrotron Soleil, France
-   Thomas Proffen, Lujan Neutron Scattering Center, Los Alamos National
    Laboratory, USA
-   Rainer Schneider, STRAINET c/o HMI Berlin, Germany
-   Jiro Suzuki, KEK, Japan

### Welcome

-   Pete Peterson (president) gave the welcome talk. In this talk he
    noted that the term of the current acting officers has come to an
    end and they should either be re-elected or new officers elected
-   Nick Hauser proposed to talk about NexusBeans and object
    orientation.
-   Mark Koennecke mentioned that he had also prepared a talk on object
    orientation.
-   It was also noted that the [NXgeometry] (NXgeometry.html "wikilink") class
    supported boxes and cylinders.
-   Nexus paper: Mark Koennecke noted that there is a publication on
    Nexus which appeared as part of the ICNS proceedings *Physica B
    385-386 (2006) 1343-1345*
-   There was a short discussion on scans and the role of
    [TOFRawScan](TOFRawScan.html "wikilink"). Nick Hauser wanted to know if
    there was a Nexus scan object

ACTION : Nick Hauser to take over the [NXgenericScan](GenericScan.html "wikilink") definition  

### Thanks

-   To Freddie Akeroyd for setting up the new MediaWiki
    **nexusformat.org** site
-   To Jens for organising the meeting

### Review of Outstanding Actions

#### Request NSF money was discussed

Paul Kienzle, Nick Hauser, and Peter Peterson would look into making an
NSF proposal to request for money. It was decided to leave this action
item open.

Nick and Peter Turner mentioned they have requested and obtained funds
for doing some work with NexusBeans.

ACTION : Pete + Nick to look into requesting money from the NSF for Nexus  

#### The linking problem for when you need the source and target names to be different

This has been fixed by Mark. A new API call has been added:

        NXMakeNamedLink()

#### There is no explanation on the wiki on how to change a Nexus class definition

ACTION : Pete Peterson to explain how to change a definition  

#### Some definitions exist only on the WIKI, some are in source control (Subversion)

They should all be moved into Subversion.

Current status is that Freddie Akeroyd has moved all base classes, but
input from other NIAC members is required on naming of instrument
definitions before moving them too. This leads onto the open question of
how to name definitions like [TOFRaw](TOFRaw.html "wikilink") – should all
definitions have an NX prefix like base classes or not?

Pete Jemian suggests differentiating names between Instruments + Base
classes – maybe using an NXD prefix for definitions?

#### Check old <http://www.nexus.anl.gov/> web site and report any content that has not been moved to new WIKI server

This has been done - Ray suggests leaving the site up but with a warning
message that the content had been moved.

VOTE to redirect site (pending moving logos) : FOR = all , AGAINST = none  
ACTION : redirect old site to new web site (Ray)  
ACTION : move logos to new web site  

#### Write down the current responsibilities for the officers and circulate to the committee for approval

In progress (Peter Peterson)

#### Write a report on NeXus and submit to both the Neutron News and Synchrotron News

Assigned to Andrew Götz and not yet done. Mark has an article in ICNS
2005 (Physica B 385–386 (2006) 1343–1345 ). Everyone is encouraged to
cite this paper.

ACTION : Andy to publish the article, don't wait for comments, set a deadline  

#### Existing definitions will be rendered in coloured meta-DTD and table formats on website

Completed by Freddie Akeroyd

#### Style sheets (XSLT) will be created to convert definitions into colorized meta-DTD and table formats

Assigned to Darren Kelly

#### Update website with constitution changes (some are even from the last meeting)

Currently Unassigned

ACTION : Pete Peterson to update website with constitution changes  

#### Modify/add base class definitions in accordance with what was voted on in February

Currently Unassigned. Some of the TOF base class has not made it to SVN.

ACTION : Freddie Akeroyd to add missing TOF base class to SVN  

### Completed Actions

#### From 2006 LBL Meeting

-   Freddie Akeroyd - to move NeXus code and definitions from CVS to
    Subversion
-   Freddie Akeroyd - to move NeXus mailing lists from anl.gov to
    <http://lists.nexusformat.org/>
-   Freddie Akeroyd - to provide a Mediawiki extension for rendering
    definitions held in Subversion onto a Wiki page in a tabular format
    on the fly
-   Mark Könnecke and Raymond Osborn - Shut down existing website and
    mirror, leaving a redirection page to new site. (The original
    website at <http://www.nexus.anl.gov/> contains a redirect message,
    but is still online so that NIAC members can check for content
    missing on the wiki.)
-   Peter Peterson - to write up the versioning mechanism

#### From 2006 ILL Meeting

-   Unassigned - [NXcharacterization] (NXcharacterization.html "wikilink")
    needs to be formalized and ratified - this has been repeated in \#11
-   Unassigned - Synchronize the website definitions with those in cvs
    (the website are considered more correct) - this is formalized as an
    action item at the 2006 LBL meeting

### Agreed Tags for NeXus definition versions

-   Version 1.0 = prior to 2006-2
-   Version 2.0 = everything ratified at 2006-2
-   Version 3.0 = next version

### Member Renewal

-   Matthias Drochner – to be renewed
-   Andy Gotz – to be renewed
-   Peter Link – expired (no news)
-   Nick Maliszewskyj – replaces Przemek for NIST

VOTE : to renew members FOR = all ; AGAINST = none  
ACTION : have meetings in October in the future, not in September at the end of the fiscal year  

### Officer Renewal

-   Andy gives up secretary
-   Freddie and Stuart ready to be secretary
-   Nick to stay technical chair if not Mark will take it

VOTE :for technical chair FOR = all ; AGAINST = none  
VOTE :for Freddie and Stuart as secretary FOR = all ; AGAINST = none  
VOTE : for Pete as president FOR = 1 ; AGAINST = none  

Nick Hauser raised the point of how to speed up adopting proposals.
Thomas mentioned there is a lack of manpower. Therefore we need a simple
web interface. Freddie suggested adding an upload page. Mark said put
new proposals on the wiki or send an email to the NIAC via the
nexus-committee mailing list.

Andy raised the point that we need a manual. The current documentation
is very techie oriented. There is no introduction for beginners. Ray
said the wiki is the documentation. Pete Jemian suggested making full
use of the wiki and the discussion page on the wiki. Mark said the
problem is the wiki is not kept updated. Conclusion – breakout group on
how to organise wiki for users

### Pete Petersons' talk - Trees

Pete gave a fascinating talk about trees and Nexus. In his vision Nexus
would be machine validated in future versions (V2.1), object oriented
definitions (V3.0) i.e. get rid of meta-DTD

### Nick's talk - Meta-DTD vs. Schema

Schema are machine readable XML. How to generate the schema ? A small
group of specialists will do this. Use a graphical schema editor. Easy
to generate meta-DTD from schema. Tools – emacs, Eclipse + WTP, Netbeans
are all free. General interest in using Eclipse + WTP and providing it
as a web start. Jens showed his C++ tool for defining instruments.

PROPOSAL : canonical Nexus definitions to be stored in schema. Meta-dtd can be generated from these  

Thomas – 3 action types – move to schema, explain tools,

VOTE : Nexus meta-DTD to be moved to schema FOR : all ; AGAINST : none  

Mark use schema for V3.0 and object oriented

VOTE : Version 3.0 will be schema based  

Nick happy to manage this move with help others What other formats
should we support e.g. html, tables, uml

### Mark's talk – Primer on Nexus and object oriented

Mark presented uml diagrams for the different base classes. Thomas said
an Instrument definition is actually an experiment definition i.e.
analysis-driven. Thomas suggested having multiple instrument classes
stored for the same instrument stored in the same file e.g. GSAS class
and Instrument class.

Nick presented NexusBeans as a Java technology. Ray said there is
general agreement that an object oriented type api is the way to go.
Pete Petersons's talk – on URL's URI – version, implementation version
e.g.

`    `[`http://www.nexusformat.org/instruments/NXmonotas`](http://www.nexusformat.org/instruments/NXmonotas)

Laurent suggested do not include the version in the uri. Freddie wanted
to have a url and uri.

### imgCIF

A discussion ensued on imgCIF and what is happening in this field. Nick
read an email from Herbert Bernstein. Freddie mentioned the imgCIF
meeting in Manchester. There it was decided that the first step is to do
an imgCIF to NX and back converter, Freddie and Herbert Bernstein will
handle this. Stuart is our official contact with imgCIF.

### netCDF

Nick gave a talk about netCDF. netCDF has a number of advantages e.g.
gives array manipulation in Java. Nick proposes to promote netCDF within
the Nexus community as a tool for reading and writing HDF5 in Nexus.
netCDF have added support for HDF5. Mark said there are a lot of issues
to consider, array manipulation of netCDF is an advantage, we need to
discuss with netCDF team to see how far they can go to support us. Pete
P. said there is a discussion on an Nxutility api. Nick said netCDF
provides a memory object. Pete P. discussion is about an in memory data
format. Ray needs a white paper with more information. Pete P. create a
separate api based on netCDF. Nick noted if the NIAC adopts netCDF for
internal data representation then this opens the way to sharing more
code. Andy suggested to start sharing netCDF between a few institutes to
gain more experience and then report back to the committee before making
a general decision on whether to support netCDF or not.

CONCLUSION : more people to try out netCDF and bring this up again at the meeting  

### Nexus top level entry

Ray relayed a request from microscopists to have a top level entry which
identifies Nexus files e.g. /nexus. Mark said we should invite someone
from this community to discuss with us. NXEntry is an attribute on a
name and not a namespace. This could be done automatically by the napi.
Nick said there was a problem with conformity and validation.

### Laser community want to use Nexus

Laurent mentioned the laser community would like to use Nexus. Laurent
will the representative

### Argonne Scattering and Imaging Institute

Ray gave a talk on the ASI^2 proposal. If it gets funding then would be
largest investment by the DOE in software. Other communities are solving
problems which are of interest to us, idea is to get these people on
board. How should this group interact with the Nexus group ? ASI^2 could
replace IPNS as institute. Pete Jemian proposed next NIAC to be held at
Argonne

### Improving Scientific efficiency at APS

Pete Jemian gave a talk on Improving Scientific Efficiency at APS. He
showed the canonical Scientific Workflow Diagram – feedback is open loop
at the moment. There is a working group headed by Ken Evans. APS has
created a Scientific Software Section for solving local challenges as
opposed to the ASI^2 which is for grand challenges. The group consists
of one person at present, it will grow in time. There is a pilot
visualisation application with 1-ID. There is resistance to Java +
Eclipse - Python is the lingua franca of scientists. This group could
look after a Nexus person. Nick said the NIAC should endorse this
position. The group is interested in helping the community. Ray said we
need funding for Nexus meetings. Thomas suggested this should be
contributed by each institute.

ACTION : Pete P to talk to SNS to setup a fund for Nexus MeetingsBeans  
ACTION : everyone to talk to their management on how much they can contribute to the fund  
ACTION : everyone to send their Berlin trip costs to the secretaries  
ACTION : Thomas to look into how much it costs to finance half a person  

Next meeting candidates are :

-   Argonne
-   Australia (NOBUGS)
-   SNS

CONCLUSION : next NIAC meeting at NOBUGS with 6 month meeting possibility at Argonne if ASI^2 is funded  

There was a long discussion about breakout groups.

### Nexus API OO

Mark gave a talk about the Nexus OO API. He made the following proposals
:

-   maintain file structure as a tree in memory
-   larger data sets are left on file and retrieved or written on demand
-   Nxclose, Nxflush serialise all changes to disk
-   how to link items together ?
-   what shall the shape of the Iterator class be ?
-   how much leeway are implementers allowed ?

There was a counter proposal by Pete Peterson. A python api which uses
the Nxfile as an object. Ray said this is not object oriented. Ray wants
to add to NXData together. Pete is against building a Nexus scripting
framework like Ray wants it. Pete P. said for python drop swig and write
python binding by hand, return NumPy objects. Pete proposes to write
zeroth level python binding – strings are python strings, scalars are
python basic types (he has already done most of the work)

ACTION : Pete to do Python binding to NumPy  

Ray will play with the Python binding to generate a library for
manipulating Nexus data

ACTION : Ray to play with Python binding and make a proposal for manipulating Nexus data  

Pete proposed code for C++ binding, supports void and std::vector
put\_slab() Pete – current Java binding returns an object which has to
be cast to the right type, Pete proposes to extend the api to return a
typed type

ACTION : Freddie to add Pete's C++ binding to be added to Nexus source code distribution  

Mark would like templates to be an option in the C++ binding Pete would
like to have doxygen comments in the C napi,

ACTION : Mark will add doxygen comments to napi.h  

Mark proposed an IDL binding

ACTION : Freddie to add Mark's IDL binding to Nexus repository  

### TRAC items

Went through open items and closed those that could be. Discussion on
memory allocation in the NXU utility library

ACTION : Freddie to add an *Unassigned* user to TRAC backend  

Could we add an external link to a non-Nexus file

-   Pete – should we write native bindings for Matlab, IDL, etc
-   Mark – no, NAPI is 3 to 4000 lines

### Nxtranslate

Pete P. gave a talk on Nxtranslate, a plugin based system. All plugins
are statically linked. Walked through test\_simple.nxs example. SNS uses
Nxtranslate. Freddie has developed a dynamic retriever which uses
dynamic shared libraries.

### HDF4

HDF4 to be marked as deprecated. New users should use only HDF5.

VOTE : all in favour of deprecating HDF4 i.e. do not add new features to NAPI for HDF4  

FOR = all-2 ; AGAINST = 2 (Freddie + Steve)

ACTION : Freddie to put a How To on the wiki for Nxtranslate and other programs with links to the pdf and doxygen  

### Documentation

ACTION : Pete to propose an outline for a Nexus manual in docbook  
ACTION : Freddie to look how to integrate this into the wiki  

Long discussion about how to integrate the docbook into the wiki and
include user comments. Frederic Picca suggested taking a look at
asciidoc. Pete P comments should go on the wiki, changes on subversion.

### NXGeometry

Mark presents simple coordinate system + polar coordinate system. Ray
corrected Mark's notion of polar angle, Ray says polar angle should be
defined wrt to beam direction (Z). Pete P. said do not call it theta or
whatever, it should be called polar angle.

ACTION : Pete to dig out jpeg demonstrating NXGeometry  
ACTION : document the McStas convention for coordinate transformation i.e. translate then rotate or vice versa – pick one  

Jens wants to store only the information about the physical information
concerning the detector. Pete P. said do consumer's need to calculate
how to convert your Nxpositioners to scientific units e.g. HKL. Ray
wants to add cylindrical coordinates.

VOTE : accept NXcone definition  

FOR = all ; AGAINST = none

### Nxarchive + Nxingest

Laurent Lerusse gave a talk on NXarchive and Nxingest. Some points he
raised :

-   do not archive multiple Nxentry, only archive metadata in first
    Nxentry
-   this caused discussion about not enforcing one Nxentry per file,
    ICAT should be changed
-   this is a limitation of ICAT
-   Nxarchive is simply a definition i.e. what ICAT expects, and does
    not exist per se in the Nexus file

### Event data in Nexus

Pete Peterson gave a talk on event data in Nexus and how SNS event data
are being stored in Nexus

ACTION : Pete P to look at th Root toolkit to see how they handle events  

### Nxextract – extracting data from Nexus at Soleil

Stephan Poirier gave a talk on a tool he has developed (Nxextract) which
allows data to be extracted from Nexus files into almost any format.
Some points raised :

-   tool is called Nxextract
-   allows data to be extracted from a Nexus file using a proprietary
    extraction language
-   Pete P – would like a feature to do maths on extracted data
-   why not use an existing scripting language
-   binding Nxextract to a scripting language is a new project

ACTION : Stephane to upload Nxextract to Nexus applications  

### Flat Cone diffractometer

Jens gave a talk on Nexus and the Flat Cone diffractometer.

-   Tvtueb a platform for analysing data from powder + flat cone
    diffractometer written in VC++ and MFC
-   TVNexus is the new program for doing Reciprocal Space Explorer of
    Nexus files (similar to HDFView currently)
-   TVNexus uses Win64 to be able to display large data sets &gt; 4GB

NAPI is thread safe if you read/write to different files, but not if
sharing the same Nxhandle in the different threads

### Laurent – multiple Nxentry issue for archiving

-   extended to support multiple Nxentries for indexing
-   tools used to index data will not archive data if necessary items
    are not found
-   killed run\_number , replaced with entry\_identifier as string

VOTE : replace run\_number with entry\_identifier  

FOR = ALL-1 ; AGAINST = 1 (Andy) ; ABSTAINED = 1 (Nick)

VOTE on NXarchive proposal :  

FOR = all ; AGAINST = none

ACTION : Laurent to get NXarchive information back to base class  
ACTION : Nick to check the result with the schema  

All changes must be reflected in the base class

### Rainer Schneider's talk – STRAINET

-   will make a proposal for STRAINET scanning Nexus format
-   NIAC – would like to work with STRAINET and help them
-   will start with powder definitions and then add missing tags needed
    by scanners

### Breakout groups for CCD's

The breakout group for CCD's proposed adding the following to Nxdetector
to accommodate CCD

-   extended type to include “ccd, pixel, image plate, cmos”
-   data\_file
-   flood
-   flood\_file
-   dark
-   dark\_file
-   spatial\_distortion
-   spatial\_distortion\_file

Discussion on whether Nxcharacterization would be more suitable. The
flood, dark and spatial\_distortion would be added as extra types of
NXcharacterization. There can be multiple NXcharacterization entries
with the NXdetector class. These would link to either another NXentry or
external file. The data\_file is added to NXdetector as an Nxnote.
NXcharacterizations to be renamed to NXcharacterisation.

VOTE on CCD proposal :  

FOR = all ; AGAINST = none

### Breakout groups for Documentation

The breakout group on documentation reported the following :

-   Use Docbook for user manuals, including
    -   introduction
    -   FAQ
    -   HowTo
    -   JPEGs of UML schema
-   Doxygen for source code and API
-   Schema in UML
-   HTML version of docbook for wiki

Have a section for active discussions and an archive for closed
discussions (which should be marked closed). Create a “DISCUSSION”
namespace to restrict editing of these pages to NIAC members only. The
“discussion” tab would be open for everyone to edit for all pages.

More detailed minutes, prepared by Nick Hauser, are in the appendix

ACTION: Freddie Akeroyd to add voting to the wiki.  

Creation of a document editorial review committee (with initial members
Freddie Akeroyd, Peter Peterson, Ray Osborn, Nick Hauser, Laurent L,
Stuart Campbell)

ACTION: Ray Osborn to provide the skeleton structure for the document editorial review committee.  

<!-- -->

VOTE to create a Definition Release Manager role :  

(VOTE): YES:ALL (12)

This required a 2/3 majority of all committee members as it is creating
a new officer's post: as 12 of the 17 committee members were present and
the vote was unanimous, this was achieved.

VOTE Nick Hauser to take this role :  

(VOTE): YES:ALL (12)

A proposal for a definition change should be discussed on the wiki for a
period of time (6 weeks to 6 months). After this a vote would be held to
ratify the changes. These would then be committed to the trunk. Then it
would be at the Definition Release Manager's discretion to create a
release.

### Meeting Closed.

### APPENDIX 1 – Herbert Bernstein's email

    ---------- Forwarded message ----------
    Date: Fri, 21 Sep 2007 01:37:27 -0400
    From: Herbert J. Bernstein <yaya@bernstein-plus-sons.com>
    To: Peter Turner <turner_p@chem.usyd.edu.au>
    Cc: p.turner@chem.usyd.edu.au, message@arcib.org,
         "Akeroyd, FA (Freddie)" <F.A.Akeroyd@rl.ac.uk>
    Subject: Re: NIAC meeting (fwd)

    Dear Peter,

       Here is the current status.

       cif2nx:  I have been working on a conversion utility from CIF or CBF
    to a NeXus file, but with additional groups so all the CIF tags can have
    a home without colliding with the existing NeXus tags.  The idea will be
    to then complete the cross-mapping of the CIF table-oriented structure
    to the NeXus tree structure using the NeXus API and then to prune out
    the duplications.  So far I have the complete parse of the CIF data and
    the loading of the CIF dictionaries and am working on the following
    initial mapping:

       Each CIF data block maps to group NXentry, with the name of the
    datablock prefixed by "NXcif_"

       Each CIF category within a CIF data block maps to a new group
    NXcifcat (as a subgroup of NXentry) with the name of the CIF category
    prefixed by "NXcif_"

       Each column within a CIF category maps in one of two ways depending
    on whether it contains any binary sections.  If there are no binary
    sections, the entire column maps as a rank 2 data array with a column of
    the CIF data values as strings and a column of the CIF data types as
    strings.  In this case the entire column is one NeXus data set with the
    name of the CIF column prefixed by "NXcif_"  If there are  binary
    sections, then instead of using one data set, a column is mapped to a
    new group NXcifcol that contains multiple arrays of whatever ranks fit
    the binary sections, and the data sets are given names consisting of the
    row number converted to a string and prefixed by NXcif_.  (This is a
    rework of the approach to the handling of columns that I had been
    following in which each data item in a column was a separate data set to
    allow for the handling of binary section.  I think this new mixed
    approach will provide a reasonable balance between performance 
    and flexibility.)

       Each CIF save frame within a CIF data block maps to a new group
    NXcifsf (as a subgroup of NXentry).  Each CIF category within a CIF save
    frame maps to the group NXcifcat (as a subgroup of NXcifsf in this case)
    and then the columns are handled as above.

       It would be nice if we could add the packed and byte offset
    compressions to the current list of NeXus compressions, but this is not
    critical.

       I hope to have this first cut done and tested in a few more days, and
    then I will try to upload this phase to the NeXus repository under
    contrib. Freddie offered to handle the NeXus side of the code, but I
    seem to be getting along well with the API, so I will try to go a little
    further first.

       Once that is done, the next step is to do the denormalization of the
    CIF categories, using the dictionary information that has been loaded to
    identify the cases in which tables in subcategories should be broken up
    and moved under the parent items in the supercategories.

       Finally, the last step will be to translate those CIF tags that match
    NeXus tags into the equivalent NeXus tags.  Those that don't match would
    stay as CIF tags.

       nx2cif:  If the cif2nx works out the other direction should be a lot
    easier, since there are fewer NeXus tags than CIF tags.   The biggest
    problem will be preserving the finer type details from NeXus on the CIF
    side.

       binutf:  G. Darakev is working on integrating binutf into the NeXus
    API.  Thsi will allow fairly efficient handling of NeXus binaries in
    XML.


       Regards,
         Herbert

### APPENDIX 2 - Process and documentation breakout session

Tuesday, 25th September, 2007. 11.00am

Present: Peter Peterson, Ray Osborn, Laurent Lerusse, Freddie Akeroyd, Nick Hauser.  

#### Controlled user and developer documentation

1.  The list of documents to be produced. The group proposes the
    following list as a minimal set of documentation required for NeXus.
    1.  Docbook for user manuals, including
        1.  Introduction
        2.  FAQ,
        3.  How To
        4.  jpeg’s of UML schema
    2.  Doxygen for source code and api
    3.  HTML version of docbook for wiki
2.  How is the documents produced? This group will provide a report on
    the tools used for generating the documentation.
3.  Who produces the documentation? Anyone from the NeXus community may
    submit documentation. This group will be responsible for editorial
    control & release. This group is responsible to ensure the
    completeness of the documentation.

ACTION: Nick to ensure the above actions are completed  

#### Discussions on the nexusformat.org wiki

1.  It was decided to have 2 types of Discussion. ‘Open forums’ open to
    the entire community, and ‘NIAC only’ discussions. To enable this,
    each discussion requires a namespace. The ‘NIAC only’ discussions
    are read-write to the community
2.  Discussions have 2 attributes, active & closed. Closed discussions
    will be marked as closed
3.  The ‘NIAC only’ discussions may have a voting attribute. Only NIAC
    members may vote.
4.  It was decided to have the design area in the open forum.

ACTION: Freddie to enable voting on the wiki, and the discussion types and attributes.  

#### Document editorial review committee

1.  The document editorial review committee is Peter Peterson, Ray
    Osborn, Laurent Lerrusse, Freddie Akeroyd, Nick Hauser
2.  Document release manager is Nick Hauser

ACTION: Nick to provide documentation for the tasks & responsibilities of the document editorial review committee, document release manager & NIAC  

<!-- -->

ACTION: Ray to provide the structure of the user documentation  

<!-- -->

ACTION: Freddie to provide Doxygen documentation of the API on the web.  

#### SQA Process

1.  It was decided that the NeXus definitions, napi and documentation
    should be versioned and packaged. Compatibility between versions
    should be explicit.
2.  The required version of autoconf should be in the
    [README.developers](http://svn.nexusformat.org/code/trunk/README.developers)
    file
3.  SQA\_process for the napi is documented at
    <http://www.nexusformat.org/SQA_Process>
4.  As part of an integrated SQA, it was proposed that releases be:
    1.  Patch level releases would be unit tested and released every 2
        months,
    2.  Major revisions would be unit tested and a release candidate
        built. Frequency of major revision is approximately every 18
        months.

ACTION: Nick to provide a proposal to the for an integrated SQA on the SQA discussion page  

#### Proposals

1.  Proposals are additions or modifications to NeXus class definitions,
    napi & documentation.
    1.  Additions are to be posted as a new article. Discussion of the
        addition is posted on the discussion tab of the article.
    2.  Modifications are to be posted on the discussion tab of the
        relevant article.
2.  When proposals are posted, it is the responsibility of the proposer
    to send an email to the <nexus@nexusformat.org> with a link to the
    proposal.
3.  Discussions of a proposal will have duration of 6 weeks. Minor
    impact proposals e.g. additions or modification of a class, can be
    voted for after this period. Major impact proposals e.g. additions
    or modifications of a class of global scope will go to the annual
    NIAC for discussion and voting.

