---
title: NAPI Routines
permalink: NAPI_Routines/
layout: wiki
---

General Initialization and Shutdown
-----------------------------------

### NXopen (file\_name, access\_method, file\_id)

Opens the NeXus file, and creates and initializes the NeXus file
structure. The returned handle is a pointer to this structure. |- ! |
Input Arguments | file\_name | char \* | Name of NeXus file to be opened
|- |   | access\_method | int | NXACC\_READ - read only access  
NXACC\_RDWR - read and write access  
NXACC\_CREATE - create (HDF4) access  
NXACC\_CREATE4 - create HDF4 access  
NXACC\_CREATE5 - create HDF5 access  
|- ! | Output Arguments | file\_id | NXhandle \* | Identifier of NeXus
file |}

### NXclose (file\_id)

Closes NeXus file and deletes all associated data structures from
memory. |- ! | Input Arguments | file\_id | NXhandle \* | Identifier of
NeXus file |}

### NXmakegroup (file\_id, group\_name, group\_class)

Creates a NeXus group at the current level in the group hierarchy,
defining its name and class. This does not open the new group
automatically. |- ! | Input Arguments | file\_id | NXhandle | Identifier
of NeXus file |- |   | group\_name | char \* | Name of NeXus group |- |
  | group\_class | char \* | Class of NeXus group |}

### NXopengroup (file\_id, group\_name, group\_class)

Opens an existing NeXus group for input and output of data. |- ! | Input
Arguments | file\_id | NXhandle | Identifier of NeXus file |- |   |
group\_name | char \* | Name of NeXus group |- |   | group\_class | char
\* | Class of NeXus group |}

### NXclosegroup (file\_id)

Closes the currently open group. If this group is a top-level group
(i.e. with class NXentry), no groups are left open. Otherwise, the next
group up in the hierarchy (i.e. the group containing the currently open
group) is left open. |- ! | Input Arguments | file\_id | NXhandle |
Identifier of NeXus file |}

### NXmakedata (file\_id, data\_name, data\_type, rank, dimensions\[\])

Creates a new NeXus data set with the specified name, type, rank and
dimensions. |- ! | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- |   | data\_name | char \* | Name of NeXus data set |- |  
| data\_type | int | Type of data (see list of valid data types) |- |  
| rank | int | Rank of data |- |   | dimensions | int\[\] | Dimensions
of data. The array is of size 'rank' |}

### NXcompmakedata (file\_id, data\_name, data\_type, rank, dimensions\[\], compress\_type)

Creates a new NeXus data set with the specified name, type, rank and
dimensions, compressed using the specified protocol. |- ! | Input
Arguments | file\_id | NXhandle | Identifier of NeXus file |- |   |
data\_name | char \* | Name of NeXus data set |- |   | data\_type | int
| Type of data (see list of valid data types) |- |   | rank | int | Rank
of data |- |   | dimensions | int\[\] | Dimensions of data. The array is
of size 'rank' |- |   | compress\_type | int | Compression algorithm to
be used : NX\_COMP\_LZW - GZIP NX\_COMP\_HUF - Skipping Huffman
NX\_COMP\_RLE - Run Length Encoding |}

### NXopendata (file\_id, data\_name)

Opens an existing NeXus data set for further processing i.e. reading and
writing data or attributes, defining compression algorithms, and
obtaining data set information. |- ! | Input Arguments | file\_id |
NXhandle | Identifier of NeXus file |- |   | data\_name | char \* | Name
of NeXus data set |}

### NXcompress (file\_id, compress\_type)

Defines a compression algorithm for subsequent calls to NXputdata. This
routine is now deprecated; please use NXcompmakedata instead. |- ! |
Input Arguments | file\_id | NXhandle | Identifier of NeXus file |- |  
| compress\_type | int | Compression algorithm to be used :
NX\_COMP\_LZW - GZIP NX\_COMP\_HUF - Skipping Huffman NX\_COMP\_RLE -
Run Length Encoding |}

### NXclosedata (file\_id)

Ends access to the currently active data set |- ! | Input Arguments |
file\_id | NXhandle | Identifier of NeXus file |}

Reading and Writing
-------------------

### NXgetdata (file\_id, data)

Reads data values from the currently open data set. Please note that
memory overwrite occurs if the caller has not allocated enough memory to
hold all the data available. Call NXgetinfo to determine the required
dimension sizes. The data set must have been opened by NXopendata. |- !
| Input Arguments | file\_id | NXhandle | Identifier of NeXus file |- !
| Output Arguments | data | void \* | Data values |}

### NXgetslab (file\_id, data, start\[\], size\[\])

Reads a subset of the data in the current data set specifying the
starting indices and size of each dimension. The caller is responsible
for allocating enough memory for the data. |- ! | Input Arguments |
file\_id | NXhandle | Identifier of NeXus file |- |   | start\[\] | int
| Indices of starting values in each dimension |- |   | size\[\] | int |
Length of slab in each dimension |- ! | Output Arguments | data | void
\* | Data values |}

### NXgetattr (file\_id, attr\_name, value, length, type)

Reads attribute values associated with the currently open data set. The
attribute is defined by its name. Attributes are meta-data; data that
provides information on the associated data set such as units, long
names etc. If no data set is open, it looks for a global attribute i.e.
attributes of the NeXus file. The caller is responsible for allocating
enough memory for the attribute values. Note, however, that only the
first 'length' bytes of the attribute are read to prevent memory
overwrite. |- ! | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- |   | attr\_name | char \* | Name of attribute |- |   |
length | int \* | Length of buffer for storing attribute data |- |   |
type | int \* | Type of attribute data (see list of valid data types) |-
! | Output Arguments | value | void \* | Value of attribute |- |   |
length | int \* | Actual length of attribute data |}

### NXputdata (file\_id, data\[\])

Writes data into the specified data set. |- ! | Input Arguments |
file\_id | NXhandle | Identifier of NeXus file |- |   | data | void \* |
Data values |}

### NXputslab (file\_id, data, start\[\], size\[\])

Writes a subset of a multidimensional data array, specified by the
starting indices and size of each dimension, into the currently open
dataset. |- ! | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- |   | data | void \* | Data values |- |   | start\[\] |
int | Indices of starting values in each dimension |- |   | size\[\] |
int | Length of slab in each dimension |}

### NXputattr (file\_id, attr\_name, value, length, type)

Writes an attribute of the currently open data set. If no data set is
open, a global attribute is generated. The attribute has both a name and
a value. | Name |Type |Description |- ! | Return Value | status | int |
Error status |- ! | Input Arguments | file\_id | NXhandle | Identifier
of NeXus file |- |   | attr\_name | char \* | Name of attribute |- |   |
value | void \* | Value of attribute |- |   | length | int | Length of
data |- |   | type | int | Type of attribute data (see list of valid
data types) |}

### NXflush (file\_id)

Flushes all data to the NeXus file. Since this command closes and
reopens the file, a new file handle is returned. The command leaves the
program in the same state, i.e. with the same group and/or data set
open. |- ! | Input Arguments | file\_id | NXhandle \* | Identifier of
NeXus file |- ! | Output Arguments | file\_id | NXhandle \* | Identifier
of NeXus file |}

Meta-Data Routines
------------------

### NXgetinfo (file\_id, rank, dimensions\[\], data\_type)

Gets the rank, dimensions and data type of the currently open data set.
|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! | Output Arguments | rank | int \* | Rank of data |- |   |
dimensions | int\[\] | Dimensions of data |- |   | data\_type | int \* |
Type of data (see list of valid data types) |}

### NXgetgroupinfo (file\_id, item\_number, group\_name, group\_class)

Returns the number of items in the current group, and the name and class
of the current group. |- ! | Input Arguments | file\_id | NXhandle |
Identifier of NeXus file |- ! | Output Arguments | item\_number | int \*
| Number of NeXus data items in the current group |- |   | group\_name |
char \* | Name of currently open NeXus group |- |   | group\_class |
char \* | Class of currently open NeXus group |}

### NXinitgroupdir (file\_id)

Initializes directory searches of the currently open group. This is
required to reset searches using NXgetnextentry that may have been
interrupted before completion. |- ! | Input Arguments | file\_id |
NXhandle | Identifier of NeXus file |}

### NXgetnextentry (file\_id, name, class, data\_type)

Implements a directory search facility on the current group level. The
first call initializes the search and returns information on the first
data item in the list. Subsequent calls yield information about the
remaining items. If the item is a group, its name and class is returned.
If it is a data set, its name and type is returned with a class of
“SDS.” |- ! | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- ! | Output Arguments | name | char \* | Name of NeXus data
item (group or set) |- |   | class | char \* | Class of NeXus group |- |
  | data\_type | int \* | Type of data set (see list of valid data
types) |}

### NXgetattrinfo (file\_id, attr\_number)

Returns the number of attributes in the current data set. |- ! | Input
Arguments | file\_id | NXhandle | Identifier of NeXus file |- ! | Output
Arguments | attr\_number | int \* | Number of attributes in the current
data set |}

### NXinitattrdir (file\_id)

Initializes attribute searches of the currently open data set. This is
required to reset searches using NXgetnextattr that may have been
interrupted before completion. |- ! | Input Arguments | file\_id |
NXhandle | Identifier of NeXus file |}

### NXgetnextattr (file\_id, attr\_name, length, type)

Implements a search facility of the attributes of the currently open
data set. The first call initializes the search and returns information
on the first attribute in the list. Subsequent calls yield information
about the remaining attributes. This routine returns global attributes
if no data set is open. |- ! | Input Arguments | file\_id | NXhandle |
Identifier of NeXus file |- ! | Output Arguments | attr\_name | char \*
| Name of next attribute |- |   | length | int \* | Length of next
attribute |- |   | type | int \* | Type of next attribute (see list of
valid data types) |}

### NXgetgroupID (file\_id, group\_id)

Returns the identifier of the currently open group as an NXlink
structure. |- ! | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- ! | Output Arguments | group\_id | NXlink \* | Identifier
of NeXus group |}

### NXgetdataID (file\_id, data\_id)

Gets the identifier of the currently open data set as an NXlink
structure. Returns NX\_ERROR if there is no open data set. |- ! | Input
Arguments | file\_id | NXhandle | Identifier of NeXus file |- ! | Output
Arguments | data\_id | NXlink \* | Identifier of NeXus data set |}

### NXmakelink (file\_id, link)

Links a data item (group or set) to a NeXus group. Returns NX\_ERROR if
the current group level is the root level, since no data item can be
linked here. |- ! | Input Arguments | file\_id | NXhandle | Identifier
of NeXus file |- ! | Output Arguments | link | NXlink \* | Identifier of
linked group |}
