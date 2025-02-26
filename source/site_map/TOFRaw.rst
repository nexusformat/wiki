======
TOFRaw
======

NXTOFRAW - A proposal for a NeXus Time-of-Flight Raw Data File
Format

.. rubric:: Introduction
 :name: introduction

`NeXus <http://www.nexusformat.org/>`__ is moving onto the idea of
inherited incremental definitions as discussed at the last meeting
of the `NeXus International Advisory Committee
(NIAC) <../niac/niac.html>`__ " for example with powder diffractometers
there is a definition for both time focussing and total scattering
with one being a subset of the other; a file can conform to one or
both. The initial work on this definition comes from discussions
between `SNS <https://neutrons.ornl.gov/sns/>`__,
`J-PARC <http://j-parc.jp/index-e.html>`__ and
`ISIS <https://www.isis.stfc.ac.uk/>`__ - the three facilities are
interested in having a unified base for all instruments to allow
for low level instrument debugging tools to be used, without
change, in a given facility. Further discussions occured in the
TOF Breakout Group at NIAC 2006 <TOF_Group.html>

An example file is available in `HDF4
(2MB) <http://download.nexusformat.org/TOFRAW/examples/hrp08639.nx4>`__,
`HDF5 (2MB) <http://download.nexusformat.org/TOFRAW/examples/hrp08639.nx5>`__
and `XML(16MB) <http://download.nexusformat.org/TOFRAW/examples/hrp08639.xml>`__ format as well
as a `basic DTD <http://download.nexusformat.org/TOFRAW/examples/TOFRAW.xml>`__.

For historical information see the `draft proposal for an ISIS
NeXus based RAW data file format <../pdfs/Isis_nexus_016.pdf>`__.

.. rubric:: Goal of the Definition
 :name: goal-of-the-definition

The definition/format should:

- Be general i.e. not specific to any particular instrument type
   and so can be used as a common root/parent format across all
   instruments at a facility

- allow the sharing of diagnostic and "first look" data/detector
   display programs between the facilities.

- provide a common input format to metadata capture programs
   (such as the ISIS ICAT search interface)

With the above in mind the instrument components of most
importance are the ones related to the detector, data, user,
sample and sample conditions; other instrument components are, of
course, needed for analysis but will be covered by specific NeXus
instrument definitions. The NeXus classes we will ultimately
consider are then:

.. container:: language-plaintext highlighter-rouge

 .. container:: highlight

    - NXroot
    - NXdata
    - NXdetector
    - NXentry
    - NXgeometry
    - NXinstrument
    - NXlog
    - NXmoderator
    - NXmonitor
    - NXsample
    - NXuser
    - NXevent_data
    - NXsource
    - NXdetector_group (proposed)

Some of these classes, such as NXgeometry, are taken directly from
what was ratified by the `NIAC <../niac/niac.html>`__.

.. rubric:: Conventions Used in this Document
 :name: conventions-used-in-this-document

A tabular format is used for ease of viewing and printing rather
than the `NeXus XML meta-DTD format <Metaformat.html>`__. The Name
column in a table identifies an item in an instance of a NeXus
class. Items can have extra "meta data" associated with them,
which are called attributes " these, if any, are listed in the
next few lines in the attributes column. Any variables in the
attributes column are always attached to the previous variable in
the Name column above them; if the Name of the variable is the
same as the class (e.g. NXfile), then the attributes are
associated with an instance of that class (global) and not to any
of its specific members.

.. rubric:: Identifying Mandatory and Optional Components
 :name: identifying-mandatory-and-optional-components

The following convention will be used:

- Variables in **bold** in the Name column of tables are
     mandatory " they must be present in ALL NeXus files; otherwise
     they are optional and their inclusion will depend on the
     instrument, experiment or presence of other items in the class
     (see the class description of usage)

- Variables in *{italics}* in the Name column are examples of
     names and any variable name can in fact be used; variable names
     in normal type mean that exact name must be used

- Anything in red is currently an extension to NeXus

This information is also included in a RE column (the name derives
from the fact that a "Regular Expression" is used here in the `XML
DTD format <Metaformat.html>`__). Thus:

+-----------------+-----------+-----------------+----------------+
| Font/style in   | RE Column | Meaning         | XML DTD symbol |
| Name Column     |           |                 |                |
+=================+===========+=================+================+
| Something       | 0/1       | A single        | ?              |
|                 |           | instance of     |                |
|                 |           | this variable   |                |
|                 |           | may be present  |                |
|                 |           | (optional) " if |                |
|                 |           | it is, it must  |                |
|                 |           | be called       |                |
|                 |           | "something"     |                |
+-----------------+-----------+-----------------+----------------+
| **Something**   | 1         | A single        |                |
|                 |           | instance of     |                |
|                 |           | this variable   |                |
|                 |           | must be present |                |
|                 |           | (mandatory) and |                |
|                 |           | called          |                |
|                 |           | "something"     |                |
+-----------------+-----------+-----------------+----------------+
| *{Something}*   | 0+        | Zero or more    | -              |
|                 |           | variables of    |                |
|                 |           | this type/class |                |
|                 |           | may be present  |                |
|                 |           | (optional) and  |                |
|                 |           | can have any    |                |
|                 |           | unique name(s)  |                |
+-----------------+-----------+-----------------+----------------+
| **{Something}** | 1+        | One or more     | +              |
|                 |           | variables of    |                |
|                 |           | this type/class |                |
|                 |           | must be present |                |
|                 |           | (mandatory),    |                |
|                 |           | but can have    |                |
|                 |           | any name(s)     |                |
+-----------------+-----------+-----------------+----------------+

The above convention dictates that the name for any item that
occurs only 0 or 1 times is fixed; this is not required by the
current NeXus standard, but would add clarity and ease of location
if followed.

.. rubric:: Naming
 :name: naming

We will try and name logged variables (type NXlog) such that they
end in the \_log suffix

.. rubric:: NeXus Classes
 :name: nexus-classes

.. rubric:: NXroot
 :name: nxroot

The root is not a real class in the NeXus file, it is a convenient
name under which to group the global attributes of the file. This
is taken directly from the NeXus technical reference without
change.

+-----+---------+---------------+---------+-------+---------------+
| RE  | Name    | Attribute     | Type    | Value | Description   |
+=====+=========+===============+=========+=======+===============+
| 1   |         | NeXus_version | NX_CHAR |       |               |
+-----+---------+---------------+---------+-------+---------------+
| 0/1 |         | HDF_version   | NX_CHAR |       |               |
+-----+---------+---------------+---------+-------+---------------+
| 0/1 |         | HDF5_version  | NX_CHAR |       |               |
+-----+---------+---------------+---------+-------+---------------+
| 0/1 |         | XML_version   | NX_CHAR |       |               |
+-----+---------+---------------+---------+-------+---------------+
| 1   |         | creator       | NX_CHAR |       |               |
+-----+---------+---------------+---------+-------+---------------+
| 1   |         | file_name     | NX_CHAR |       | Original file |
|     |         |               |         |       | name          |
+-----+---------+---------------+---------+-------+---------------+
| 1   |         | file_time     | NX_CHAR |       | Original      |
|     |         |               |         |       | creation time |
|     |         |               |         |       | of file       |
+-----+---------+---------------+---------+-------+---------------+
| 1   |         | fil           | NX_CHAR |       | Last time     |
|     |         | e_update_time |         |       | file contents |
|     |         |               |         |       | were changed  |
+-----+---------+---------------+---------+-------+---------------+
| 1   |         | in            | NX_CHAR |       | Initial       |
|     |         | itial\_format |         |       | format file   |
|     |         |               |         |       | was created   |
|     |         |               |         |       | in (HDF4,HDF5 |
|     |         |               |         |       | or XML)       |
+-----+---------+---------------+---------+-------+---------------+
| 1+  | {entry} |               | NXentry |       |               |
+-----+---------+---------------+---------+-------+---------------+
| 0/1 |         | unique_id     | NX_CHAR |       | UUID to       |
|     |         |               |         |       | uniquely      |
|     |         |               |         |       | identify file |
|     |         |               |         |       | (even if name |
|     |         |               |         |       | changes       |
|     |         |               |         |       | .etc). Maybe  |
|     |         |               |         |       | useful to     |
|     |         |               |         |       | have it in    |
|     |         |               |         |       | the NXentry   |
|     |         |               |         |       | instead so    |
|     |         |               |         |       | that you can  |
|     |         |               |         |       | indentify     |
|     |         |               |         |       | where an      |
|     |         |               |         |       | entry comes   |
|     |         |               |         |       | from even if  |
|     |         |               |         |       | it is copied  |
|     |         |               |         |       | into a new    |
|     |         |               |         |       | file?         |
+-----+---------+---------------+---------+-------+---------------+

.. rubric:: NXentry
 :name: nxentry

This is the top level group in a file that contains a complete set
of information (e.g. a "run") - raw, reduced, and analyzed data
can occur in the same file, each as a separate NXentry . The
definition below is taken from the NeXus technical reference
changing some elements to be required rather an optional.
Additional items are highlighted in

red
.

This definition covers a single run experiment - extensions are
proposed for `scan type experiments <TOFRawScan.html>`__

.. rubric:: NXentry
 :name: nxentry-1

+------+----------+----------+----------+----------+----------+
| RE   | Name     | A        | Type     | Value    | Des      |
|      |          | ttribute |          |          | cription |
+======+==========+==========+==========+==========+==========+
| 0/1  | title    |          | NX_CHAR  |          | run      |
|      |          |          |          |          | title    |
+------+----------+----------+----------+----------+----------+
| 1    | de       |          | NX_CHAR  |          | Official |
|      | finition |          |          |          | NeXus    |
|      |          |          |          |          | def      |
|      |          |          |          |          | initions |
|      |          |          |          |          | this     |
|      |          |          |          |          | file     |
|      |          |          |          |          | conforms |
|      |          |          |          |          | to       |
+------+----------+----------+----------+----------+----------+
| 1    |          | URL      | NX_CHAR  |          |          |
+------+----------+----------+----------+----------+----------+
| 1    |          | version  | NX_CHAR  |          |          |
+------+----------+----------+----------+----------+----------+
| 0/1  | d        |          | NX_CHAR  |          | Local    |
|      | efinitio |          |          |          | de       |
|      | n\_local |          |          |          | finition |
|      |          |          |          |          | this     |
|      |          |          |          |          | file     |
|      |          |          |          |          | also     |
|      |          |          |          |          | conforms |
|      |          |          |          |          | to "     |
|      |          |          |          |          | this     |
|      |          |          |          |          | will     |
|      |          |          |          |          | describe |
|      |          |          |          |          | the      |
|      |          |          |          |          | meaning  |
|      |          |          |          |          | of any   |
|      |          |          |          |          | ad       |
|      |          |          |          |          | ditional |
|      |          |          |          |          | local    |
|      |          |          |          |          | data     |
|      |          |          |          |          | items    |
|      |          |          |          |          | etc.     |
+------+----------+----------+----------+----------+----------+
| 1    |          | url      | NX_CHAR  |          |          |
+------+----------+----------+----------+----------+----------+
| 1    |          | version  | NX_CHAR  |          | This     |
|      |          |          |          |          | would    |
|      |          |          |          |          | co       |
|      |          |          |          |          | rrespond |
|      |          |          |          |          | to the   |
|      |          |          |          |          | ISIS     |
|      |          |          |          |          | Muon     |
|      |          |          |          |          | IDF      |
|      |          |          |          |          | _Version |
+------+----------+----------+----------+----------+----------+
| 1    | st       |          | ISO8601  |          | Time     |
|      | art_time |          |          |          | data     |
|      |          |          |          |          | co       |
|      |          |          |          |          | llection |
|      |          |          |          |          | started  |
+------+----------+----------+----------+----------+----------+
| 1    | end_time |          | ISO8601  |          | Time     |
|      |          |          |          |          | data     |
|      |          |          |          |          | co       |
|      |          |          |          |          | llection |
|      |          |          |          |          | ended    |
+------+----------+----------+----------+----------+----------+
| 1    | duration |          | NX_FLOAT |          | wall     |
|      |          |          |          |          | clock    |
|      |          |          |          |          | time     |
|      |          |          |          |          | tr       |
|      |          |          |          |          | anspired |
|      |          |          |          |          | (end "   |
|      |          |          |          |          | start)   |
+------+----------+----------+----------+----------+----------+
| 1    |          | units    | NX_CHAR  | second   |          |
+------+----------+----------+----------+----------+----------+
| 1    | collecti |          | NX_FLOAT |          | Time     |
|      | on\_time |          |          |          | tr       |
|      |          |          |          |          | anspired |
|      |          |          |          |          | actually |
|      |          |          |          |          | co       |
|      |          |          |          |          | llecting |
|      |          |          |          |          | data     |
|      |          |          |          |          | i.e.     |
|      |          |          |          |          | taking   |
|      |          |          |          |          | out time |
|      |          |          |          |          | when     |
|      |          |          |          |          | co       |
|      |          |          |          |          | llection |
|      |          |          |          |          | was      |
|      |          |          |          |          | s        |
|      |          |          |          |          | uspended |
|      |          |          |          |          | due to   |
|      |          |          |          |          | e.g.     |
|      |          |          |          |          | tem      |
|      |          |          |          |          | perature |
|      |          |          |          |          | out of   |
|      |          |          |          |          | range    |
+------+----------+----------+----------+----------+----------+
| 1    |          | units    | NX_CHAR  | second   |          |
+------+----------+----------+----------+----------+----------+
| 0/1  | proto    |          | NX_FLOAT |          |          |
|      | n_charge |          |          |          |          |
+------+----------+----------+----------+----------+----------+
| 1    |          | units    | NX_CHAR  | micro    |          |
|      |          |          |          | Amp*hour |          |
+------+----------+----------+----------+----------+----------+
| 0/1  | ra       |          | NX_INT   |          | number   |
|      | w_frames |          |          |          | of       |
|      |          |          |          |          | proton   |
|      |          |          |          |          | pulses   |
|      |          |          |          |          | on       |
|      |          |          |          |          | target   |
+------+----------+----------+----------+----------+----------+
| 0/1  | goo      |          | NX_INT   |          | number   |
|      | d_frames |          |          |          | of       |
|      |          |          |          |          | proton   |
|      |          |          |          |          | pulses   |
|      |          |          |          |          | used     |
|      |          |          |          |          | (i.e.    |
|      |          |          |          |          | not      |
|      |          |          |          |          | vetoed)  |
+------+----------+----------+----------+----------+----------+
| 0/1  | total    |          | NX_INT   |          | Total    |
|      | \_counts |          |          |          | number   |
|      |          |          |          |          | of       |
|      |          |          |          |          | detector |
|      |          |          |          |          | counts   |
|      |          |          |          |          | (events) |
+------+----------+----------+----------+----------+----------+
| 1    | exper    |          | NX_CHAR  |          | proposal |
|      | iment_id |          |          |          | number   |
|      | entifier |          |          |          |          |
+------+----------+----------+----------+----------+----------+
| 0/1  | di       |          | NX_CHAR  |          | Keyword  |
|      | scipline |          |          |          | domain   |
|      |          |          |          |          | (e.g.    |
|      |          |          |          |          | ch       |
|      |          |          |          |          | emistry, |
|      |          |          |          |          | as       |
|      |          |          |          |          | tronomy, |
|      |          |          |          |          | ecology, |
|      |          |          |          |          | )        |
+------+----------+----------+----------+----------+----------+
| 1    |          | i        | NX_CHAR  | propsal  | Source   |
|      |          | nfo\_src |          |          | of the   |
|      |          |          |          |          | inf      |
|      |          |          |          |          | ormation |
|      |          |          |          |          | (p       |
|      |          |          |          |          | roposal, |
|      |          |          |          |          | updated  |
|      |          |          |          |          | during   |
|      |          |          |          |          | exp      |
|      |          |          |          |          | eriment, |
|      |          |          |          |          | after,   |
|      |          |          |          |          | )        |
+------+----------+----------+----------+----------+----------+
| 0/1  | keyword  |          | NX_CHAR  |          | Keywords |
|      |          |          |          |          | defined  |
|      |          |          |          |          | for this |
|      |          |          |          |          | study.   |
+------+----------+----------+----------+----------+----------+
| 1    |          | i        | NX_CHAR  | propsal  | Source   |
|      |          | nfo\_src |          |          | of the   |
|      |          |          |          |          | inf      |
|      |          |          |          |          | ormation |
+------+----------+----------+----------+----------+----------+
| 0/1  | keyword  |          | NX_CHAR  |          | A        |
|      | \_source |          |          |          | pointer  |
|      |          |          |          |          | to a     |
|      |          |          |          |          | r        |
|      |          |          |          |          | eference |
|      |          |          |          |          | work     |
|      |          |          |          |          | p        |
|      |          |          |          |          | roviding |
|      |          |          |          |          | the      |
|      |          |          |          |          | de       |
|      |          |          |          |          | finition |
|      |          |          |          |          | of the   |
|      |          |          |          |          | re       |
|      |          |          |          |          | stricted |
|      |          |          |          |          | vo       |
|      |          |          |          |          | cabulary |
|      |          |          |          |          | of which |
|      |          |          |          |          | the      |
|      |          |          |          |          | keyword  |
|      |          |          |          |          | list is  |
|      |          |          |          |          | a        |
|      |          |          |          |          | subset.  |
+------+----------+----------+----------+----------+----------+
| 1    |          | i        | NX_CHAR  | propsal  | Source   |
|      |          | nfo\_src |          |          | of the   |
|      |          |          |          |          | inf      |
|      |          |          |          |          | ormation |
+------+----------+----------+----------+----------+----------+
| 0/1  | subject  |          | NX_CHAR  |          | Subject  |
|      |          |          |          |          | categor  |
|      |          |          |          |          | isations |
|      |          |          |          |          | for this |
|      |          |          |          |          | study    |
+------+----------+----------+----------+----------+----------+
| 1    |          | i        | NX_CHAR  | propsal  | Source   |
|      |          | nfo\_src |          |          | of the   |
|      |          |          |          |          | inf      |
|      |          |          |          |          | ormation |
+------+----------+----------+----------+----------+----------+
| 0/1  | desc     |          | NX_CHAR  |          | Brief    |
|      | ription\ |          |          |          | summary  |
|      | _summary |          |          |          | of the   |
|      |          |          |          |          | exp      |
|      |          |          |          |          | eriment, |
|      |          |          |          |          | i        |
|      |          |          |          |          | ncluding |
|      |          |          |          |          | key      |
|      |          |          |          |          | ob       |
|      |          |          |          |          | jectives |
+------+----------+----------+----------+----------+----------+
| 1    |          | i        | NX_CHAR  | propsal  | Source   |
|      |          | nfo\_src |          |          | of the   |
|      |          |          |          |          | inf      |
|      |          |          |          |          | ormation |
+------+----------+----------+----------+----------+----------+
| 0/1  | des      |          | NXnote   |          | Des      |
|      | cription |          |          |          | cription |
|      |          |          |          |          | of the   |
|      |          |          |          |          | full     |
|      |          |          |          |          | ex       |
|      |          |          |          |          | periment |
|      |          |          |          |          | (        |
|      |          |          |          |          | document |
|      |          |          |          |          | in pdf,  |
|      |          |          |          |          | latex,   |
|      |          |          |          |          | )        |
+------+----------+----------+----------+----------+----------+
| 1    |          | i        | NX_CHAR  | propsal  | Source   |
|      |          | nfo\_src |          |          | of the   |
|      |          |          |          |          | inf      |
|      |          |          |          |          | ormation |
+------+----------+----------+----------+----------+----------+
| 0/1  | req      |          | NX_CHAR  |          | Special  |
|      | uirement |          |          |          | requ     |
|      |          |          |          |          | irements |
|      |          |          |          |          | of       |
|      |          |          |          |          | in       |
|      |          |          |          |          | strument |
+------+----------+----------+----------+----------+----------+
| 1    |          | i        | NX_CHAR  | propsal  | Source   |
|      |          | nfo\_src |          |          | of the   |
|      |          |          |          |          | inf      |
|      |          |          |          |          | ormation |
+------+----------+----------+----------+----------+----------+
| 0/1  | publ     |          | NX_CHAR  |          | List of  |
|      | ications |          |          |          | pub      |
|      |          |          |          |          | lication |
|      |          |          |          |          | related  |
|      |          |          |          |          | to the   |
|      |          |          |          |          | proposal |
+------+----------+----------+----------+----------+----------+
| 1    |          | i        | NX_CHAR  | propsal  | Source   |
|      |          | nfo\_src |          |          | of the   |
|      |          |          |          |          | inf      |
|      |          |          |          |          | ormation |
+------+----------+----------+----------+----------+----------+
| 0/1  | facili   |          | NX_CHAR  |          | Facility |
|      | ty\_acce |          |          |          | access   |
|      | ss\_type |          |          |          | type     |
|      |          |          |          |          | (normal, |
|      |          |          |          |          | rapid    |
|      |          |          |          |          | access,  |
|      |          |          |          |          | p        |
|      |          |          |          |          | rogramme |
|      |          |          |          |          | access   |
|      |          |          |          |          | )        |
+------+----------+----------+----------+----------+----------+
| 1    |          | i        | NX_CHAR  | propsal  | Source   |
|      |          | nfo\_src |          |          | of the   |
|      |          |          |          |          | inf      |
|      |          |          |          |          | ormation |
+------+----------+----------+----------+----------+----------+
| 0/1  | g        |          | NX_CHAR  |          | Id       |
|      | rant\_id |          |          |          | entifier |
|      |          |          |          |          | of the   |
|      |          |          |          |          | funding  |
|      |          |          |          |          | grant.   |
+------+----------+----------+----------+----------+----------+
| 1    |          | i        | NX_CHAR  | propsal  | Source   |
|      |          | nfo\_src |          |          | of the   |
|      |          |          |          |          | inf      |
|      |          |          |          |          | ormation |
+------+----------+----------+----------+----------+----------+
| 1    | ru       |          | NX_INT   |          | Unique   |
|      | n_number |          |          |          | number   |
|      |          |          |          |          | ide      |
|      |          |          |          |          | ntifying |
|      |          |          |          |          | this     |
|      |          |          |          |          | data     |
|      |          |          |          |          | co       |
|      |          |          |          |          | llection |
+------+----------+----------+----------+----------+----------+
| 0 /1 | r        |          | NX_CHAR  |          |          |
|      | un_cycle |          |          |          |          |
+------+----------+----------+----------+----------+----------+
| 0/1  | prog     |          | NX_CHAR  |          |          |
|      | ram_name |          |          |          |          |
+------+----------+----------+----------+----------+----------+
| 1    |          | version  | NX_CHAR  |          |          |
+------+----------+----------+----------+----------+----------+
| 0/1  |          | comm     | NX_CHAR  |          |          |
|      |          | and_line |          |          |          |
+------+----------+----------+----------+----------+----------+
| 0/1  | relea    |          | NX_CHAR  |          | Date of  |
|      | se\_date |          |          |          | the      |
|      |          |          |          |          | public   |
|      |          |          |          |          | release  |
|      |          |          |          |          | of the   |
|      |          |          |          |          | data.    |
|      |          |          |          |          | (f       |
|      |          |          |          |          | ile_time |
|      |          |          |          |          | + X      |
|      |          |          |          |          | years)   |
+------+----------+----------+----------+----------+----------+
| 0/1  | revision |          | NX_CHAR  |          | Revision |
|      |          |          |          |          | id of    |
|      |          |          |          |          | the file |
|      |          |          |          |          | due to   |
|      |          |          |          |          | re-cali  |
|      |          |          |          |          | bration, |
|      |          |          |          |          | repro    |
|      |          |          |          |          | cessing, |
|      |          |          |          |          | new      |
|      |          |          |          |          | a        |
|      |          |          |          |          | nalysis, |
|      |          |          |          |          | new      |
|      |          |          |          |          | in       |
|      |          |          |          |          | strument |
|      |          |          |          |          | de       |
|      |          |          |          |          | finition |
|      |          |          |          |          | format,  |
|      |          |          |          |          |          |
+------+----------+----------+----------+----------+----------+
| 0/1  | notes    |          | NXnote   |          | User     |
|      |          |          |          |          | notes    |
+------+----------+----------+----------+----------+----------+
| 0/1  | t        |          | NXnote   |          |          |
|      | humbnail |          |          |          |          |
+------+----------+----------+----------+----------+----------+
| 1    |          | m        | NX_CHAR  | image/\* |          |
|      |          | ime_type |          |          |          |
+------+----------+----------+----------+----------+----------+
| 0+   | {c       |          | NX       |          |          |
|      | haracter |          | characte |          |          |
|      | isation} |          | rization |          |          |
+------+----------+----------+----------+----------+----------+
| 1+   | {user1,  |          | NXuser   |          |          |
|      | user2, } |          |          |          |          |
+------+----------+----------+----------+----------+----------+
| 1    | {sample} |          | NXsample |          |          |
+------+----------+----------+----------+----------+----------+
| 1    | {ins     |          | NXin     |          |          |
|      | trument} |          | strument |          |          |
+------+----------+----------+----------+----------+----------+
| 1+   | {        |          | N        |          |          |
|      | monitor} |          | Xmonitor |          |          |
+------+----------+----------+----------+----------+----------+
| 1+   | {data}   |          | NXdata   |          |          |
+------+----------+----------+----------+----------+----------+
| 0/1  | {        |          | N        |          |          |
|      | process} |          | Xprocess |          |          |
+------+----------+----------+----------+----------+----------+

.. rubric:: NXuser
 :name: nxuser

As denoted in NXentry, there can be multiple NXuser, one for each
person involved with an experiment. This definition of user
requires only a name and a facility identifier and this is taken
directly from the NeXus technical reference changing some elements
to be required rather an optional.

+-----+-----------+-----------+---------+-----------+-----------+
| RE  | Name      | Attribute | Type    | Value     | De        |
|     |           |           |         |           | scription |
+=====+===========+===========+=========+===========+===========+
| 1   | name      |           | NX_CHAR |           |           |
+-----+-----------+-----------+---------+-----------+-----------+
| 0/1 |           | info\_src | NX_CHAR | "p        | Source of |
|     |           |           |         | roposal", | the       |
|     |           |           |         | "         | in        |
|     |           |           |         | updated", | formation |
|     |           |           |         | "co       |           |
|     |           |           |         | rrected", |           |
|     |           |           |         | "logging" |           |
+-----+-----------+-----------+---------+-----------+-----------+
| 0/1 | role      |           | NX_CHAR | "local_c  |           |
|     |           |           |         | ontact"," |           |
|     |           |           |         | Principle |           |
|     |           |           |         | Inves     |           |
|     |           |           |         | tigator", |           |
|     |           |           |         |           |           |
+-----+-----------+-----------+---------+-----------+-----------+
| 0/1 | af        |           | NX_CHAR |           |           |
|     | filiation |           |         |           |           |
+-----+-----------+-----------+---------+-----------+-----------+
| 0/1 | address   |           | NX_CHAR |           |           |
+-----+-----------+-----------+---------+-----------+-----------+
| 0/1 | telepho   |           | NX_CHAR |           |           |
|     | ne_number |           |         |           |           |
+-----+-----------+-----------+---------+-----------+-----------+
| 0/1 | f         |           | NX_CHAR |           |           |
|     | ax_number |           |         |           |           |
+-----+-----------+-----------+---------+-----------+-----------+
| 0/1 | email     |           | NX_CHAR |           |           |
+-----+-----------+-----------+---------+-----------+-----------+
| 1   | facilit   |           | NX_CHAR |           |           |
|     | y_user_id |           |         |           |           |
+-----+-----------+-----------+---------+-----------+-----------+
| 0/1 | affili    |           | NX_CHAR |           |           |
|     | ation\_id |           |         |           |           |
+-----+-----------+-----------+---------+-----------+-----------+

.. rubric:: NXsample
 :name: nxsample

This list is limited to items that were desired by the group. See
the NeXus technical reference for a full list of possible items.

+-----+-------+-------+-------+-------+-------+-------+-------+---+
| RE  | Name  | Attr  | Type  | Value | D     |       |       |   |
|     |       | ibute |       |       | escri |       |       |   |
|     |       |       |       |       | ption |       |       |   |
+=====+=======+=======+=======+=======+=======+=======+=======+===+
| 1   | Name  |       | NX    |       |       |       |       |   |
|     |       |       | _CHAR |       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 1   | ident |       | NX    |       | Ide   |       |       |   |
|     | ifier |       | _CHAR |       | ntity |       |       |   |
|     |       |       |       |       | given |       |       |   |
|     |       |       |       |       | to    |       |       |   |
|     |       |       |       |       | the   |       |       |   |
|     |       |       |       |       | s     |       |       |   |
|     |       |       |       |       | ample |       |       |   |
|     |       |       |       |       | by    |       |       |   |
|     |       |       |       |       | h     |       |       |   |
|     |       |       |       |       | ealth |       |       |   |
|     |       |       |       |       | ph    |       |       |   |
|     |       |       |       |       | ysics |       |       |   |
|     |       |       |       |       | or    |       |       |   |
|     |       |       |       |       | s     |       |       |   |
|     |       |       |       |       | ample |       |       |   |
|     |       |       |       |       | en    |       |       |   |
|     |       |       |       |       | viron |       |       |   |
|     |       |       |       |       | ment. |       |       |   |
|     |       |       |       |       | (     |       |       |   |
|     |       |       |       |       | Could |       |       |   |
|     |       |       |       |       | be a  |       |       |   |
|     |       |       |       |       | bar   |       |       |   |
|     |       |       |       |       | code) |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 |       | Type  | NX    | e.    |       |       |       |   |
|     |       |       | _CHAR | g."ba |       |       |       |   |
|     |       |       |       | rcode |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | c     |       | NX    |       |       |       |       |   |
|     | hemic |       | _CHAR |       |       |       |       |   |
|     | al_fo |       |       |       |       |       |       |   |
|     | rmula |       |       |       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | mass  |       | NX    |       |       |       |       |   |
|     |       |       | _FLOAT|       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 1   |       | units | NX    |       |       |       |       |   |
|     |       |       | _CHAR |       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | v     |       | NX    |       |       |       |       |   |
|     | olume |       | _FLOAT|       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 1   |       | units | NX    |       |       |       |       |   |
|     |       |       | _CHAR |       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | geo   |       | NXgeo |       |       |       |       |   |
|     | metry |       | metry |       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 1   | n     |       | NX    | solid | p     | l     | s     |   |
|     | ature |       | _CHAR |       | owder | iquid | ingle |   |
|     |       |       |       |       |       |       | cr    |   |
|     |       |       |       |       |       |       | ystal |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | p     |       | NX    |       | S     |       |       |   |
|     | repar |       | _CHAR |       | ample |       |       |   |
|     | ation |       |       |       | handl |       |       |   |
|     |       |       |       |       | ing/p |       |       |   |
|     |       |       |       |       | repar |       |       |   |
|     |       |       |       |       | ation |       |       |   |
|     |       |       |       |       | prior |       |       |   |
|     |       |       |       |       | to    |       |       |   |
|     |       |       |       |       | exper |       |       |   |
|     |       |       |       |       | iment |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | c     |       | N     |       | S     |       |       |   |
|     | hange |       | X_INT |       | ample |       |       |   |
|     | r_pos |       |       |       | ch    |       |       |   |
|     | ition |       |       |       | anger |       |       |   |
|     |       |       |       |       | pos   |       |       |   |
|     |       |       |       |       | ition |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | samp  |       | NX    |       |       |       |       |   |
|     | le\_h |       | _CHAR |       |       |       |       |   |
|     | older |       |       |       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | pr    |       | IS    |       |       |       |       |   |
|     | epara |       | O8601 |       |       |       |       |   |
|     | tion\ |       |       |       |       |       |       |   |
|     | _date |       |       |       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | thic  |       | NX    |       |       |       |       |   |
|     | kness |       | _FLOAT|       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | t     |       | NX    |       |       |       |       |   |
|     | emper |       | _FLOAT|       |       |       |       |   |
|     | ature |       |       |       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+

.. rubric:: Sample environment parameters
 :name: sample-environment-parameters

By these we mean "temperature", "magnetic_field" etc. which may be
considered to be outside of the remit of this document, but we
will just add a reminder that if the file represents a scan then
these values will be annotated as described in the NXentry
section.

.. rubric:: NXinstrument
 :name: nxinstrument

This is the class that contains all information about instrument
components except the monitors and sample (which are just inside
the NXentry). This is taken directly from the NeXus technical
reference changing some elements to be required rather an
optional.

+-----+----------+------------+------------+-------+------------+
| RE  | Name     | Attribute  | Type       | Value | D          |
|     |          |            |            |       | escription |
+=====+==========+============+============+=======+============+
| 1   | name     |            | NX_CHAR    |       |            |
+-----+----------+------------+------------+-------+------------+
| 1   |          | short_name | NX_CHAR    |       |            |
+-----+----------+------------+------------+-------+------------+
| 1   | beamline |            | NX_CHAR    |       | Beamline   |
|     |          |            |            |       | instrument |
|     |          |            |            |       | is         |
|     |          |            |            |       | attached   |
|     |          |            |            |       | to         |
+-----+----------+------------+------------+-------+------------+
| 0/1 |          |            | NXsource   |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NXdi       |       |            |
|     |          |            | sk_chopper |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NXfer      |       |            |
|     |          |            | mi_chopper |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NXvelocit  |       |            |
|     |          |            | y_selector |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NXguide    |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NXcrystal  |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | N          |       |            |
|     |          |            | Xaperature |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NXfilter   |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NX         |       |            |
|     |          |            | collimator |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NX         |       |            |
|     |          |            | attenuator |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | N          |       |            |
|     |          |            | Xpolarizer |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NXflipper  |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NXmirror   |       |            |
+-----+----------+------------+------------+-------+------------+
| 1+  |          |            | NXdetector |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | NXdetec    |       |            |
|     |          |            | tor\_group |       |            |
+-----+----------+------------+------------+-------+------------+
| 0+  |          |            | N          |       |            |
|     |          |            | Xbeam_stop |       |            |
+-----+----------+------------+------------+-------+------------+

.. rubric:: NXmonitor
 :name: nxmonitor

+-----+-----------+-----------+-----------+-----------+-----------+---+
| RE  | Name      | Attribute | Type      | Value     | De        |   |
|     |           |           |           |           | scription |   |
+=====+===========+===========+===========+===========+===========+===+
| 0/1 | mode      |           | NX_CHAR   | monitor   | timer     |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | preset    |           | NX_FLOAT  |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | distance  |           | NX_FLOAT  |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 |           | units     | NX_CHAR   | metre     |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | range     |           | NX        |           |           |   |
|     |           |           | _FLOAT[2] |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 1   |           | units     | NX_CHAR   |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | integral  |           | NX_FLOAT  |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 1   |           | units     | NX_CHAR   |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | int       |           | NXlog     |           | Time log  |   |
|     | egral_log |           |           |           | of        |   |
|     |           |           |           |           | monitor   |   |
|     |           |           |           |           | integrals |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | type      |           | NX_CHAR   |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 1   | time      |           | NX_F      |           |           |   |
|     | _of_flight|           | LOAT[i+1] |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 1   |           | units     | NX_CHAR   | mi        |           |   |
|     |           |           |           | crosecond |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | e         |           | NX        |           |           |   |
|     | fficiency |           | _FLOAT[i] |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 1   | data      |           | NX        |           |           |   |
|     |           |           | _FLOAT[i] |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 1   |           | units     | NX_CHAR   |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 1   |           | signal    | NX_INT    |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 1   |           | axes      | NX_CHAR   |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | sampled   |           | NX_FLOAT  |           |           |   |
|     | _fraction |           |           |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 1   |           | units     | NX_CHAR   | unitless  |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | geometry  |           | N         |           |           |   |
|     |           |           | Xgeometry |           |           |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | monito    |           | NX_INT    |           | If        |   |
|     | r\_number |           |           |           | monitors  |   |
|     |           |           |           |           | are       |   |
|     |           |           |           |           | numbered, |   |
|     |           |           |           |           | this is   |   |
|     |           |           |           |           | what it   |   |
|     |           |           |           |           | is known  |   |
|     |           |           |           |           | as        |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+
| 0/1 | detecto   |           | NX_INT    |           | Detector  |   |
|     | r\_number |           |           |           | /spectrum |   |
|     |           |           |           |           | number    |   |
|     |           |           |           |           | for this  |   |
|     |           |           |           |           | monitor   |   |
+-----+-----------+-----------+-----------+-----------+-----------+---+

Note that for a position sensitive monitor detector_number etc.
will need to be an array and NXmonitor will have other fields and
look more like NXdetector.

.. rubric:: NXdetector
 :name: nxdetector

We will now look at possible representations of the detector " we
will start with a general one and then consider the special case
of an area detector. Though the general (point) detector
representation would cover all cases, if the detector is
physically "rectangular" in nature there are advantages in using
this symmetry in the representation. Which representation is used
is recorded in the layout attribute

.. rubric:: Point Detector
 :name: point-detector

The general representation is to consider a detector as just a
group of pixels arranged in no particular order. Each pixel will
be identified by a unique single index i and then the following
information will be stored:

+-----+-----------+-----------+-----------+-----------+-----------+
| RE  | Name      | Attribute | Type      | Value     | De        |
|     |           |           |           |           | scription |
+=====+===========+===========+===========+===========+===========+
| 1   | layout    |           | NX_CHAR   | point     | How       |
|     |           |           |           |           | detector  |
|     |           |           |           |           | is        |
|     |           |           |           |           | re        |
|     |           |           |           |           | presented |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | detect    |           | NX_INT[i] |           |           |
|     | or_number |           |           |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | po        |           | NX        |           |           |
|     | lar_angle |           | _FLOAT[i] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | azimut    |           | NX        |           |           |
|     | hal_angle |           | _FLOAT[i] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | so        |           | NX        |           |           |
|     | lid_angle |           | _FLOAT[i] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | distance  |           | NX        | distance  |           |
|     |           |           | _FLOAT[i] | from      |           |
|     |           |           |           | sample    |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | time      |           | NX_F      |           | Bin       |
|     | _of_flight|           | LOAT[j+1] |           | b         |
|     |           |           |           |           | oundaries |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 |           | units     | NX_CHAR   | Mic       |           |
|     |           |           |           | ro.second |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | time of_f |           | NX        |           | in DAQ    |
|     | light_raw |           | _INT[j+1] |           | clock     |
|     |           |           |           |           | pulses    |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 |           | units     | NX_CHAR   | Clo       |           |
|     |           |           |           | ck_pulses |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 |           | frequency | NX_FLOAT  |           | Clock     |
|     |           |           |           |           | frequency |
|     |           |           |           |           | of        |
|     |           |           |           |           | ac        |
|     |           |           |           |           | quisition |
|     |           |           |           |           | system    |
|     |           |           |           |           | (Hz)      |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | data      |           | NX_F      |           |           |
|     |           |           | LOAT[i,j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | geometry  |           | NXge      |           | These     |
|     |           |           | ometry[i] |           | will be   |
|     |           |           |           |           | relative  |
|     |           |           |           |           | to        |
|     |           |           |           |           | "Origin"  |
|     |           |           |           |           | below     |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | gro       |           | NX_INT[i] |           | Detector  |
|     | up\_index |           |           |           | grouping  |
|     |           |           |           |           | in        |
|     |           |           |           |           | formation |
|     |           |           |           |           | " see     |
|     |           |           |           |           | NXdetect  |
|     |           |           |           |           | or_groups |
|     |           |           |           |           | class     |
+-----+-----------+-----------+-----------+-----------+-----------+

The detector data would be plotted with axes (detector number,
tof) by any program. An NXgeometry object included in the detector
contains arrays that store the position and orientation of each
pixel. As this detector representation imposes no constraint on
the relationship between pixels, a single NXdetector could
represent the entire instrument (so long as all detectors have the
same time of_flight) " however in practice an NXdetector and
NXdata would be created for each bank. The "origin" object
provides a reference point for the pixel geometries " the "shape"
part of origin is the bounding box of the entire detector/detector
bank.

.. rubric:: Linear Detector
 :name: linear-detector

Here we mean a collection of linear straight strips e.g. tubes. We
have two indicies: **j** will label the strip/tube and **i** the
position along the tube. All tubes must have the same number of
pixels; if not, you must use the point detector representation
above. The tubes do not need to be parallel - they just need to be
straight. Thus:

+-----+-----------+-----------+-----------+-----------+-----------+
| RE  | Name      | Attribute | Type      | Value     | De        |
|     |           |           |           |           | scription |
+=====+===========+===========+===========+===========+===========+
| 1   | layout    |           | NX_CHAR   | linear    | How       |
|     |           |           |           |           | detector  |
|     |           |           |           |           | is        |
|     |           |           |           |           | re        |
|     |           |           |           |           | presented |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | detect    |           | NX        |           |           |
|     | or_number |           | _INT[i,j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | po        |           | NX_F      |           |           |
|     | lar_angle |           | LOAT[i,j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | azimut    |           | NX_F      |           |           |
|     | hal_angle |           | LOAT[i,j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | distance  |           | NX_F      |           |           |
|     |           |           | LOAT[i,j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | time      |           | NX_F      |           | Bin       |
|     | _of_flight|           | LOAT[k+1] |           | b         |
|     |           |           |           |           | oundaries |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 |           | Units     | NX_CHAR   | Mic       |           |
|     |           |           |           | ro.second |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | raw_time  |           | NX        |           | in DAQ    |
|     | _of_flight|           | _INT[k+1] |           | clock     |
|     |           |           |           |           | pulses    |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 |           | Units     | NX_CHAR   | Clo       |           |
|     |           |           |           | ck_pulses |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 |           | Frequency | NX_FLOAT  | Clock     |           |
|     |           |           |           | frequency |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | data      |           | NX_FLO    |           |           |
|     |           |           | AT[i,j,k] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | geometry  |           | NXge      |           | These     |
|     |           |           | ometry[i] |           | will be   |
|     |           |           |           |           | relative  |
|     |           |           |           |           | to        |
|     |           |           |           |           | "Origin"  |
|     |           |           |           |           | below     |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | pix       |           | NX        |           | 0 at      |
|     | el_offset |           | _FLOAT[j] |           | origin    |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | p         |           | NX        |           |           |
|     | ixel_size |           | _FLOAT[j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
|     |           |           |           |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+

By specifying both size and offset "dead space" between pixels can
be accounted for.

This looks similar to a point detector, but with two array indices
rather than one. However note the geometry information is
different - as the tubes are straight we need only specify a
location of the tube centre and an offset along the tube. Thus:

-  NXgeometry geometry[i] # defines tube/strip centre; each
    NXshape member give the tube size and shape; each NXorientation
    member rotates the axes such that **x** points along each tube.
-  pixel_offset[j] # offset from tube centre of each pixel centre

-  pixel_size[j] # size of each pixel

.. rubric:: Area Detector
 :name: area-detector

A flat rectangular area detector could be described by the
"general" representation above, but taking account of the two
dimensional symmetry of the detector allows several potential
savings in the calculation of angles and in plotting time of the
data. An area detector will have indices (i,j) indexing each pixel
with i along the local detector "x" axis and j along the local
detector "y". In the case of curved detectors the offsets and
sizes are to be considered as arc lengths along the face of the
detector. An offset of "0" is the origin of the detector and the
NXgeometry named "origin" describes the geometry of the entire
detector: the NXtranslation part describes the position of the
detector, the NXorientation part defines the local coordinates
(local x and y axes) with respect to the global position, and the
NXshape describe the size (bounding box) and topology of the
detector as a whole. The NXgeometry named "geometry" describes the
pixels and their shape (assuming that they are uniform). The
necessary shapes are: rectangular prism, cylindrical slice, and
spherical slice.

Below are the three cases for describing the pixels on a detector.

+-----+-----------+-----------+-----------+-----------+-----------+
| RE  | Name      | Attribute | Type      | Value     | De        |
|     |           |           |           |           | scription |
+=====+===========+===========+===========+===========+===========+
| 1   | layout    |           | NX_CHAR   | area      | How       |
|     |           |           |           |           | detector  |
|     |           |           |           |           | is        |
|     |           |           |           |           | re        |
|     |           |           |           |           | presented |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | detect    |           | NX        |           |           |
|     | or_number |           | _INT[i,j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | po        |           | NX_F      |           |           |
|     | lar_angle |           | LOAT[i,j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | azimut    |           | NX_F      |           |           |
|     | hal_angle |           | LOAT[i,j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | distance  |           | NX_F      |           |           |
|     |           |           | LOAT[i,j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | time      |           | NX_F      |           | Bin       |
|     | _of_flight|           | LOAT[k+1] |           | b         |
|     |           |           |           |           | oundaries |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 |           | Units     | NX_CHAR   | Mic       |           |
|     |           |           |           | ro.second |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | raw_time  |           | NX        |           | in DAQ    |
|     | _of_flight|           | _INT[k+1] |           | clock     |
|     |           |           |           |           | pulses    |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 |           | Units     | NX_CHAR   | Clo       |           |
|     |           |           |           | ck_pulses |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 |           | Frequency | NX_FLOAT  | Clock     |           |
|     |           |           |           | frequency |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   | data      |           | NX_FLO    |           |           |
|     |           |           | AT[i,j,k] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | geometry  |           | NXgeom    |           | These     |
|     |           |           | etry[i,j] |           | will be   |
|     |           |           |           |           | relative  |
|     |           |           |           |           | to        |
|     |           |           |           |           | "Origin"  |
|     |           |           |           |           | below     |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | x_pix     |           | NX        |           | 0 at      |
|     | el_offset |           | _FLOAT[i] |           | origin    |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | x_p       |           | NX        |           |           |
|     | ixel_size |           | _FLOAT[i] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | y_pix     |           | NX        |           | 0 at      |
|     | el_offset |           | _FLOAT[j] |           | origin    |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | y_p       |           | NX        |           |           |
|     | ixel_size |           | _FLOAT[j] |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | x\_radius |           | NX_FLOAT  |           | If we are |
|     |           |           |           |           | curved,   |
|     |           |           |           |           | the       |
|     |           |           |           |           | radius of |
|     |           |           |           |           | curvature |
|     |           |           |           |           | (         |
|     |           |           |           |           | \*_offset |
|     |           |           |           |           | above     |
|     |           |           |           |           | will then |
|     |           |           |           |           | be arc    |
|     |           |           |           |           | lengths)  |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | y\_radius |           | NX_FLOAT  |           | If we are |
|     |           |           |           |           | curved,   |
|     |           |           |           |           | the       |
|     |           |           |           |           | radius of |
|     |           |           |           |           | curvature |
|     |           |           |           |           | (         |
|     |           |           |           |           | \*_offset |
|     |           |           |           |           | above     |
|     |           |           |           |           | will then |
|     |           |           |           |           | be arc    |
|     |           |           |           |           | lengths)  |
+-----+-----------+-----------+-----------+-----------+-----------+

You can either specify an NXgeometry[i,j] for the pixels or
instead use the x_pixel\* arrays. By specifying both size and
offset "dead space" between pixels can be accounted for.

azimuthal_angle, polar_angle and distance can be left out of
NXdetector as they can be calculated from the detector geometry

**Hardware ganging of detector elements**

In some cases individual detector elements are ganged together by
the acquisition system for symmetry reasons or to create a smaller
data files. In these cases the above formalisms can still be used,
but the "detector number" does not correspond to a real physical
detector and so the values of "polar_angle", "distance",
"azimuthal_angle" are some sort of average over the ganged
elements. When analysis and simulation of the data is performed,
it is sometimes necessary to know the details of the individual
detectors that have been ganged together. An initial proposal was
that these additional arrays would be stored with the "_unganged"
suffix e.g. "Polar_angle_unganged", "distance_unganged",
"detector_number_unganged". However after discussions of TOF Group <TOF_Group.html> if was decided to move these arrays into
a substructure of NXdetector so we would have
NXdetector.polar_angle and NXdetector.distance for the ganed
values; NXdetector.unganged.polar_angle and
NXdetector.unganged.distance for the raw values.

To relate the ganged and unganged arrays, a simple grouping scheme
can usually be used: detector.unganged.grouping[j] give the value
[i] detector.polar_angle[i] that this detector contributes to.
This covers most cases, except for when a detector may have its
signal fed into more than one place; in which case a more complex
mapping scheme is needed.

To cover the general case the "unganged" arrays are arranged so
that elements that are ganged together appear sequentially and
information to relate these arrays to the hardware ganged
"polar_angle" etc arrays are provided by

+-----+-----------+-----------+-----------+-----------+-----------+
| RE  | Name      | Attribute | Type      | Value     | De        |
|     |           |           |           |           | scription |
+=====+===========+===========+===========+===========+===========+
| 0/1 | ga        |           | NX_INT[i] | Number of |           |
|     | ng\_count |           |           | physical  |           |
|     |           |           |           | detectors |           |
|     |           |           |           | elements  |           |
|     |           |           |           | ganged    |           |
|     |           |           |           | together  |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | ga        |           | NX_INT[i] | Index of  |           |
|     | ng\_index |           |           | first     |           |
|     |           |           |           | ganged    |           |
|     |           |           |           | element   |           |
+-----+-----------+-----------+-----------+-----------+-----------+

Detector_number[i] is ganged from gang_count[i] elements. The
values of polar_angle[i] was obtained by average the gang_count[i]
values of polar_angle_unganged[gang_index[i]],
polar_angle_unganged[gang_index[i]+1],   ,
polar_angle[gang_index[i]+gang_count[i]-1]

.. rubric:: NXdata
 :name: nxdata

=== ============== ========= ================= ===== =============
RE  Name           Attribute Type              Value Description
=== ============== ========= ================= ===== =============
0/1                          NXdata
1   data                     NX_FLOAT[i,j,k,m]
1                  units     NX_CHAR
1                  long_name NX_CHAR                 Title of data
1   time of_flight           NX_FLOAT[k+1]
0/1 x_pixel_offset           NX_FLOAT[i]
0/1 y_pixel_offset           NX_FLOAT[j]

=== ============== ========= ================= ===== =============

The exact format of this will depend on the NXdetector definition
used.

.. rubric:: NXmoderator
 :name: nxmoderator

The moderator is the effective source for all time-of-flight
instruments. This is taken directly from the NeXus technical
reference changing some elements to be required rather an
optional. Additional items are in red.

=== =============== ========= ========== ====== ======================
RE  Name            Attribute Type       Value  Description
=== =============== ========= ========== ====== ======================
1   distance                  NX_FLOAT
1                   units     NX_CHAR
1   type                      NX_CHAR           The moderator material
0/1 poison_depth              NX_FLOAT
1                   units     NX_CHAR
0/1 coupled                   NX_BOOLEAN
0/1 poison_material           NX_CHAR
0/1 temperature               NX_FLOAT
1                   units     NX_CHAR    Kelvin
0/1 temperature_log           NXlog
0/1 pulse_shape               NXdata
0/1 geometry                  NXgeometry
=== =============== ========= ========== ====== ======================

.. rubric:: NXgeometry
 :name: nxgeometry

This group describes the shape, position, and orientation of a
component. Almost all of the information is actually stored in
subgroups. This is taken directly from the NeXus technical
reference without change.

+-----+------------+-----------+------------+-------+------------+
| RE  | Name       | Attribute | Type       | Value | D          |
|     |            |           |            |       | escription |
+=====+============+===========+============+=======+============+
| 0/1 |            |           | NXshape    |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 |            |           | NXt        |       |            |
|     |            |           | ranslation |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 |            |           | NXo        |       |            |
|     |            |           | rientation |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | d          |           | NX_CHAR    |       |            |
|     | escription |           |            |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | compo      |           | NX_INT     |       | Position   |
|     | nent_index |           |            |       | of         |
|     |            |           |            |       | component  |
|     |            |           |            |       | along the  |
|     |            |           |            |       | beam path. |
+-----+------------+-----------+------------+-------+------------+

The sample has a component_index of 0, components upstream have
negative component_index.

.. rubric:: NXlog
 :name: nxlog

Contains log information monitored during the run in a timed
fashion. This can contain the time-stamped values, or the average
(with standard deviation), minimum, maximum and total time log was
taken. This is taken directly from the NeXus technical reference
without change.

+-----+------------+-----------+------------+-------+------------+
| RE  | Name       | Attribute | Type       | Value | D          |
|     |            |           |            |       | escription |
+=====+============+===========+============+=======+============+
| 0/1 | time       |           | NX_FLOAT   |       | relative   |
|     |            |           |            |       | to "start" |
+-----+------------+-----------+------------+-------+------------+
| 1   |            | units     | NX_CHAR    |       |            |
+-----+------------+-----------+------------+-------+------------+
| 1   |            | start     | ISO8601    |       | start time |
|     |            |           |            |       | of logging |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | value      |           | NX_FLOAT / |       |            |
|     |            |           | NX_INT     |       |            |
+-----+------------+-----------+------------+-------+------------+
| 1   |            | units     | NX_CHAR    |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | raw_value  |           | NX_FLOAT / |       | e.g.       |
|     |            |           | NX_INT     |       | voltage    |
|     |            |           |            |       | from       |
|     |            |           |            |       | th         |
|     |            |           |            |       | ermocouple |
+-----+------------+-----------+------------+-------+------------+
| 1   |            | units     | NX_CHAR    |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | d          |           | NX_CHAR    |       |            |
|     | escription |           |            |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | ave        |           | NX_FLOAT   |       |            |
|     | rage_value |           |            |       |            |
+-----+------------+-----------+------------+-------+------------+
| 1   |            | units     | NX_CHAR    |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | average_v  |           | NX_FLOAT   |       |            |
|     | alue_error |           |            |       |            |
+-----+------------+-----------+------------+-------+------------+
| 1   |            | units     | NX_CHAR    |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | min        |           | NX_FLOAT   |       |            |
|     | imum_value |           |            |       |            |
+-----+------------+-----------+------------+-------+------------+
| 1   |            | units     | NX_CHAR    |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | max        |           | NX_FLOAT   |       |            |
|     | imum_value |           |            |       |            |
+-----+------------+-----------+------------+-------+------------+
| 1   |            | units     | NX_CHAR    |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | duration   |           | NX_FLOAT   |       |            |
+-----+------------+-----------+------------+-------+------------+
| 1   |            | units     | NX_CHAR    |       |            |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | dis        |           | NX_CHAR    |       | short name |
|     | play\_name |           |            |       | displayed  |
|     |            |           |            |       | on         |
|     |            |           |            |       | instrument |
|     |            |           |            |       | dashboard  |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | software   |           | NX_CHAR    |       | program or |
|     |            |           |            |       | software   |
|     |            |           |            |       | used to    |
|     |            |           |            |       | measure    |
|     |            |           |            |       | value      |
+-----+------------+-----------+------------+-------+------------+
| 0/1 | hardware   |           | NX_CHAR    |       | hardware   |
|     |            |           |            |       | used to    |
|     |            |           |            |       | measure    |
|     |            |           |            |       | value      |
+-----+------------+-----------+------------+-------+------------+

.. rubric:: NXorientation
 :name: nxorientation

+-----+-------+-----------+-------------+-------+-------------+
| RE  | Name  | Attribute | Type        | Value | Description |
+=====+=======+===========+=============+=======+=============+
| 0/1 |       |           | NXgeometry  |       | Link to     |
|     |       |           |             |       | another     |
|     |       |           |             |       | object for  |
|     |       |           |             |       | relative    |
|     |       |           |             |       | positioning |
+-----+-------+-----------+-------------+-------+-------------+
| 0/1 | value |           | NX_FLOA     |       | The         |
|     |       |           | T[numobj,6] |       | orientation |
|     |       |           |             |       | information |
|     |       |           |             |       | is stored   |
|     |       |           |             |       | as 6        |
|     |       |           |             |       | direction   |
|     |       |           |             |       | cosines for |
|     |       |           |             |       | each object |
+-----+-------+-----------+-------------+-------+-------------+

.. rubric:: NXshape
 :name: nxshape

+-----+-------+--------+--------+--------+--------+--------+---+
| RE  | Name  | Att    | Type   | Value  | Descr  |        |   |
|     |       | ribute |        |        | iption |        |   |
+=====+=======+========+========+========+========+========+===+
| 0/1 | shape |        | N      | nxcy   | nxbox  | nx     |   |
|     |       |        | X_CHAR | linder |        | sphere |   |
+-----+-------+--------+--------+--------+--------+--------+---+
| 0/1 | size  |        | NX_F   |        |        |        |   |
|     |       |        | LOAT[n |        |        |        |   |
|     |       |        | umobj, |        |        |        |   |
|     |       |        | nsha   |        |        |        |   |
|     |       |        | pepar] |        |        |        |   |
+-----+-------+--------+--------+--------+--------+--------+---+
| 1   |       | units  | N      | metre  |        |        |   |
|     |       |        | X_CHAR |        |        |        |   |
+-----+-------+--------+--------+--------+--------+--------+---+

The interpretation of the "shapepar" depends on the "shape"

.. rubric:: NXtranslation
 :name: nxtranslation

+-----+----------+-----------+------------+-------+------------+
| RE  | Name     | Attribute | Type       | Value | D          |
|     |          |           |            |       | escription |
+=====+==========+===========+============+=======+============+
| 0/1 |          |           | NXgeometry |       | Link to    |
|     |          |           |            |       | another    |
|     |          |           |            |       | object for |
|     |          |           |            |       | relative   |
|     |          |           |            |       | p          |
|     |          |           |            |       | ositioning |
+-----+----------+-----------+------------+-------+------------+
| 0/1 | distance |           | NX_FLOAT   |       |            |
|     |          |           | [numobj,3] |       |            |
+-----+----------+-----------+------------+-------+------------+
| 1   |          | Units     | NX_CHAR    | metre |            |
+-----+----------+-----------+------------+-------+------------+

.. rubric:: NXevent_data
 :name: nxevent_data

This requires that a Pixel_number field is provided in the
NXdetector for determining geometry information. While normally
this takes the place of the NXdata in a NXentry, there is no
reason that the two cannot coexist. The index I runs over events -
the index j runs counts pulses.

+-----+-----------+-----------+-----------+-----------+-----------+
| RE  | Name      | Attribute | Type      | Value     | De        |
|     |           |           |           |           | scription |
+=====+===========+===========+===========+===========+===========+
| 0/1 | time      |           | NX_INT[i] |           | A list of |
|     | _of_flight|           |           |           | time of   |
|     |           |           |           |           | flight    |
|     |           |           |           |           | for each  |
|     |           |           |           |           | event as  |
|     |           |           |           |           | it comes  |
|     |           |           |           |           | in. This  |
|     |           |           |           |           | list is   |
|     |           |           |           |           | for all   |
|     |           |           |           |           | pulses    |
|     |           |           |           |           | with      |
|     |           |           |           |           | in        |
|     |           |           |           |           | formation |
|     |           |           |           |           | to attach |
|     |           |           |           |           | to a      |
|     |           |           |           |           | p         |
|     |           |           |           |           | articular |
|     |           |           |           |           | pulse     |
|     |           |           |           |           | located   |
|     |           |           |           |           | in        |
|     |           |           |           |           | events    |
|     |           |           |           |           | per_pulse |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   |           | units     | NX_CHAR   | Mic       |           |
|     |           |           |           | ro.second |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | pix       |           | NX_INT[i] |           | There     |
|     | el_number |           |           |           | will be   |
|     |           |           |           |           | extra     |
|     |           |           |           |           | in        |
|     |           |           |           |           | formation |
|     |           |           |           |           | in the    |
|     |           |           |           |           | N         |
|     |           |           |           |           | Xdetector |
|     |           |           |           |           | to        |
|     |           |           |           |           | convert   |
|     |           |           |           |           | pix       |
|     |           |           |           |           | el_number |
|     |           |           |           |           | to        |
|     |           |           |           |           | detecto   |
|     |           |           |           |           | r_number. |
|     |           |           |           |           | This list |
|     |           |           |           |           | is for    |
|     |           |           |           |           | all       |
|     |           |           |           |           | pulses    |
|     |           |           |           |           | with      |
|     |           |           |           |           | in        |
|     |           |           |           |           | formation |
|     |           |           |           |           | to attach |
|     |           |           |           |           | to a      |
|     |           |           |           |           | p         |
|     |           |           |           |           | articular |
|     |           |           |           |           | pulse     |
|     |           |           |           |           | located   |
|     |           |           |           |           | in        |
|     |           |           |           |           | events    |
|     |           |           |           |           | per_pulse |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | p         |           | NX_INT[j] |           | The time  |
|     | ulse_time |           |           |           | that each |
|     |           |           |           |           | pulse     |
|     |           |           |           |           | started   |
|     |           |           |           |           | with      |
|     |           |           |           |           | respect   |
|     |           |           |           |           | to the    |
|     |           |           |           |           | offset    |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   |           | Units     | NX_CHAR   |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 1   |           | Offset    | ISO8601   |           |           |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | events    |           | NX_INT[j] |           | This      |
|     | per_pulse |           |           |           | connects  |
|     |           |           |           |           | the index |
|     |           |           |           |           | "i" to    |
|     |           |           |           |           | the index |
|     |           |           |           |           | "j". The  |
|     |           |           |           |           | jth       |
|     |           |           |           |           | element   |
|     |           |           |           |           | is the    |
|     |           |           |           |           | number of |
|     |           |           |           |           | events in |
|     |           |           |           |           | "i" that  |
|     |           |           |           |           | occured   |
|     |           |           |           |           | during    |
|     |           |           |           |           | the jth   |
|     |           |           |           |           | pulse     |
+-----+-----------+-----------+-----------+-----------+-----------+
| 0/1 | pul       |           | NX_FL     |           | If        |
|     | se_height |           | OAT[I,k?] |           | voltages  |
|     |           |           |           |           | from the  |
|     |           |           |           |           | ends of   |
|     |           |           |           |           | the       |
|     |           |           |           |           | detector  |
|     |           |           |           |           | are read  |
|     |           |           |           |           | out this  |
|     |           |           |           |           | is where  |
|     |           |           |           |           | they go.  |
|     |           |           |           |           | This list |
|     |           |           |           |           | is for    |
|     |           |           |           |           | all       |
|     |           |           |           |           | events    |
|     |           |           |           |           | with      |
|     |           |           |           |           | in        |
|     |           |           |           |           | formation |
|     |           |           |           |           | to attach |
|     |           |           |           |           | to a      |
|     |           |           |           |           | p         |
|     |           |           |           |           | articular |
|     |           |           |           |           | pulse     |
|     |           |           |           |           | height.   |
|     |           |           |           |           | The       |
|     |           |           |           |           | in        |
|     |           |           |           |           | formation |
|     |           |           |           |           | to attach |
|     |           |           |           |           | to a      |
|     |           |           |           |           | p         |
|     |           |           |           |           | articular |
|     |           |           |           |           | pulse is  |
|     |           |           |           |           | located   |
|     |           |           |           |           | in        |
|     |           |           |           |           | events    |
|     |           |           |           |           | per_pulse |
+-----+-----------+-----------+-----------+-----------+-----------+

.. rubric:: NXsource
 :name: nxsource

+-----+-------+-------+-------+-------+-------+-------+-------+---+
| RE  | Name  | Attr  | Type  | Value | D     |       |       |   |
|     |       | ibute |       |       | escri |       |       |   |
|     |       |       |       |       | ption |       |       |   |
+=====+=======+=======+=======+=======+=======+=======+=======+===+
|     | NXs   |       |       | Name  |       |       |       |   |
|     | ource |       |       | of    |       |       |       |   |
|     |       |       |       | s     |       |       |       |   |
|     |       |       |       | ource |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 1   | name  |       | NX    |       | Fac   |       |       |   |
|     |       |       | _CHAR |       | ility |       |       |   |
|     |       |       |       |       | name  |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 1   | type  |       | NX    | "     | "P    | "Re   | "S    |   |
|     |       |       | _CHAR | Spall | ulsed | actor | ynchr |   |
|     |       |       |       | ation | Re    | Ne    | otron |   |
|     |       |       |       | Ne    | actor | utron | X-ray |   |
|     |       |       |       | utron | So    | So    | So    |   |
|     |       |       |       | So    | urce" | urce" | urce" |   |
|     |       |       |       | urce" |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 1   | probe |       | NX    | "neut | "m    | "x-   |       |   |
|     |       |       | _CHAR | rons" | uons" | rays" |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 1   | freq  |       | NX_FL |       | Freq  |       |       |   |
|     | uency |       | OAT32 |       | uency |       |       |   |
|     |       |       |       |       | of    |       |       |   |
|     |       |       |       |       | p     |       |       |   |
|     |       |       |       |       | ulsed |       |       |   |
|     |       |       |       |       | s     |       |       |   |
|     |       |       |       |       | ource |       |       |   |
|     |       |       |       |       | at    |       |       |   |
|     |       |       |       |       | the   |       |       |   |
|     |       |       |       |       | t     |       |       |   |
|     |       |       |       |       | arget |       |       |   |
|     |       |       |       |       | "at   |       |       |   |
|     |       |       |       |       | ta    |       |       |   |
|     |       |       |       |       | rget" |       |       |   |
|     |       |       |       |       | a     |       |       |   |
|     |       |       |       |       | llows |       |       |   |
|     |       |       |       |       | for   |       |       |   |
|     |       |       |       |       | the   |       |       |   |
|     |       |       |       |       | main  |       |       |   |
|     |       |       |       |       | p     |       |       |   |
|     |       |       |       |       | roton |       |       |   |
|     |       |       |       |       | beam  |       |       |   |
|     |       |       |       |       | being |       |       |   |
|     |       |       |       |       | split |       |       |   |
|     |       |       |       |       | wi    |       |       |   |
|     |       |       |       |       | th.g. |       |       |   |
|     |       |       |       |       | 1 in  |       |       |   |
|     |       |       |       |       | 5     |       |       |   |
|     |       |       |       |       | p     |       |       |   |
|     |       |       |       |       | ulses |       |       |   |
|     |       |       |       |       | div   |       |       |   |
|     |       |       |       |       | erted |       |       |   |
|     |       |       |       |       | to    |       |       |   |
|     |       |       |       |       | an    |       |       |   |
|     |       |       |       |       | other |       |       |   |
|     |       |       |       |       | t     |       |       |   |
|     |       |       |       |       | arget |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 1   |       | units | NX    | Hertz |       |       |       |   |
|     |       |       | _CHAR |       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | p     |       | NX    |       |       |       |       |   |
|     | eriod |       | _FLOAT|       |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 |       | units | NX    | mi    | L     |       |       |   |
|     |       |       | _CHAR | crose | ength |       |       |   |
|     |       |       |       | conds | of an |       |       |   |
|     |       |       |       |       | a     |       |       |   |
|     |       |       |       |       | cquis |       |       |   |
|     |       |       |       |       | ition |       |       |   |
|     |       |       |       |       | frame |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+
| 0/1 | notes |       | NX    | Sourc | At    |       |       |   |
|     |       |       | _TEXT | e/fac | ISIS, |       |       |   |
|     |       |       |       | ility | the   |       |       |   |
|     |       |       |       | re    | MCR   |       |       |   |
|     |       |       |       | lated | beam  |       |       |   |
|     |       |       |       | mes   | mes   |       |       |   |
|     |       |       |       | sages | sages |       |       |   |
|     |       |       |       | or    |       |       |       |   |
|     |       |       |       | ann   |       |       |       |   |
|     |       |       |       | ounce |       |       |       |   |
|     |       |       |       | ments |       |       |       |   |
|     |       |       |       | d     |       |       |       |   |
|     |       |       |       | uring |       |       |       |   |
|     |       |       |       | the   |       |       |       |   |
|     |       |       |       | exper |       |       |       |   |
|     |       |       |       | iment |       |       |       |   |
+-----+-------+-------+-------+-------+-------+-------+-------+---+

.. rubric:: NXdetector_groups
 :name: nxdetector_groups

This class is used to allow a logical grouping of detector
elements (e.g. which tube, bank or group of banks) to be recorded
in the file. As well as allowing you to e.g just select the "left"
or "east" detectors, it may also be useful for determining which
elements belong to the same PSD tube and hence have e.g. the same
dead time.

+----+-----------+-----------+-----------+-----------+-----------+
| RE | Name      | Attribute | Type      | Value     | De        |
|    |           |           |           |           | scription |
+====+===========+===========+===========+===========+===========+
| RE | Name      | Attribute | Type      | Value     | De        |
|    |           |           |           |           | scription |
+----+-----------+-----------+-----------+-----------+-----------+
| 1  | gr        |           | NX_CHAR   |           | Comma     |
|    | oup_names |           |           |           | separated |
|    |           |           |           |           | list of   |
|    |           |           |           |           | name      |
+----+-----------+-----------+-----------+-----------+-----------+
| 1  | gr        |           | NX_INT[i] |           | Unique ID |
|    | oup_index |           |           |           | for group |
+----+-----------+-----------+-----------+-----------+-----------+
| 1  | gro       |           | NX_INT[i] | Index of  | -1 means  |
|    | up_parent |           |           | group     | no parent |
|    |           |           |           | parent in | i.e. a    |
|    |           |           |           | the       | top level |
|    |           |           |           | hierarchy | group     |
+----+-----------+-----------+-----------+-----------+-----------+
| 1  | g         |           | NX_INT[i] | Code      | e.g.      |
|    | roup_type |           |           | number    | bank=1,   |
|    |           |           |           | for group | tube=2    |
|    |           |           |           | type      | etc.      |
+----+-----------+-----------+-----------+-----------+-----------+

For example of we had "bank1" composed of "tube1", "tube2" and
"tube3" then Group_names would be the string "bank1, bank1/tube1,
bank1/tube2,bank1/tube3" Group_index would be {1,2,3,4}
Group_parent would be {-1,1,1,1}

The mapping array is interpreted as group 1 is a top level group
containing groups 2, 3 and 4

A group_index array in NXdetector give the base group for a
detector element.
