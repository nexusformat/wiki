---
title: NAPI Routines
permalink: NAPI_Routines/
layout: wiki
---

General Initialization and Shutdown
-----------------------------------

### NXopen

Opens the NeXus file, and creates and initializes the NeXus file
structure. The returned handle is a pointer to this structure.

;Usage:

    status = NXopen (file_name, access_method, file_id)

|- ! rowspan=“2” | Input Arguments | file\_name | char \* | Name of
NeXus file to be opened |- | access\_method | int |

File Access:NXACC\_READ - read only  
NXACC\_RDWR - read and write access

NXACC\_CREATE - create (HDF4) file

NXACC\_CREATE4 - create HDF4 file

NXACC\_CREATE5 - create HDF5 file

NXACC\_CREATEXML - create XML file

|- ! | Output Arguments | file\_id | NXhandle \* | Identifier of NeXus
file |}

### NXclose

Closes NeXus file and deletes all associated data structures from
memory.

;Usage:

    status = NXclose (file_id)

|- ! | Input Arguments | file\_id | NXhandle \* | Identifier of NeXus
file |}

### NXmakegroup

Creates a NeXus group at the current level in the group hierarchy,
defining its name and class. This does not open the new group
automatically.

;Usage:

    status = NXmakegroup (file_id, group_name, group_class)

|- ! rowspan=“3” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | group\_name | char \* | Name of NeXus group |- |
group\_class | char \* | Class of NeXus group |}

### NXopengroup

Opens an existing NeXus group for input and output of data.

;Usage:

    status = NXopengroup (file_id, group_name, group_class)

|- ! rowspan=“3” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | group\_name | char \* | Name of NeXus group |- |
group\_class | char \* | Class of NeXus group |}

### NXclosegroup

Closes the currently open group. If this group is a top-level group
(i.e. with class NXentry), no groups are left open. Otherwise, the next
group up in the hierarchy (i.e. the group containing the currently open
group) is left open.

;Usage:

    status = NXclosegroup (file_id)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|}

### NXmakedata

Creates a new NeXus data set with the specified name, type, rank and
dimensions.

;Usage:

    status = NXmakedata (file_id, data_name, data_type, rank, dimensions[])

|- ! rowspan=“5” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | data\_name | char \* | Name of NeXus data set |- |
data\_type | int | Type of data (see list of valid data types) |- | rank
| int | Rank of data |- | dimensions | int\[\] | Dimensions of data. The
array is of size 'rank' |}

### NXcompmakedata

Creates a new NeXus data set with the specified name, type, rank and
dimensions, compressed using the specified protocol.

;Usage:

    status = NXcompmakedata (file_id, data_name, data_type, rank, dimensions[], compress_type)

|- ! rowspan=“6” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | data\_name | char \* | Name of NeXus data set |- |
data\_type | int | Type of data (see list of valid data types) |- | rank
| int | Rank of data |- | dimensions | int\[\] | Dimensions of data. The
array is of size 'rank' |- | compress\_type | int |

Compression algorithm:NX\_COMP\_LZW - GZIP  
NX\_COMP\_HUF - Skipping Huffman

NX\_COMP\_RLE - Run Length Encoding

|}

### NXopendata

Opens an existing NeXus data set for further processing i.e. reading and
writing data or attributes, defining compression algorithms, and
obtaining data set information.

;Usage:

    status = NXopendata (file_id, data_name)

|- ! rowspan=“2” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | data\_name | char \* | Name of NeXus data set |}

### NXcompress

Defines a compression algorithm for subsequent calls to NXputdata. This
routine is now deprecated; please use NXcompmakedata instead.

;Usage:

    status = NXcompress (file_id, compress_type)

|- ! rowspan=“2” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | compress\_type | int |

Compression algorithm:NX\_COMP\_LZW - GZIP  
NX\_COMP\_HUF - Skipping Huffman

NX\_COMP\_RLE - Run Length Encoding

|}

### NXclosedata

Ends access to the currently active data set

;Usage:

    status = NXclosedata (file_id)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|}

Reading and Writing
-------------------

### NXgetdata

Reads data values from the currently open data set. Please note that
memory overwrite occurs if the caller has not allocated enough memory to
hold all the data available. Call NXgetinfo to determine the required
dimension sizes. The data set must have been opened by NXopendata.

;Usage:

    status = NXgetdata (file_id, data)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! | Output Arguments | data | void \* | Data values |}

### NXgetslab

Reads a subset of the data in the current data set specifying the
starting indices and size of each dimension. The caller is responsible
for allocating enough memory for the data.

;Usage:

    status = NXgetslab (file_id, data, start[], size[])

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- |   | start\[\] | int | Indices of starting values in each dimension
|- |   | size\[\] | int | Length of slab in each dimension |- ! | Output
Arguments | data | void \* | Data values |}

### NXgetattr

Reads attribute values associated with the currently open data set. The
attribute is defined by its name. Attributes are meta-data; data that
provides information on the associated data set such as units, long
names etc. If no data set is open, it looks for a global attribute i.e.
attributes of the NeXus file. The caller is responsible for allocating
enough memory for the attribute values. Note, however, that only the
first 'length' bytes of the attribute are read to prevent memory
overwrite.

;Usage:

    status = NXgetattr (file_id, attr_name, value, length, type)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- |   | attr\_name | char \* | Name of attribute |- |   | length | int
\* | Length of buffer for storing attribute data |- |   | type | int \*
| Type of attribute data (see list of valid data types) |- ! | Output
Arguments | value | void \* | Value of attribute |- |   | length | int
\* | Actual length of attribute data |}

### NXputdata

Writes data into the specified data set.

;Usage:

    status = NXputdata (file_id, data[])

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- |   | data | void \* | Data values |}

### NXputslab

Writes a subset of a multidimensional data array, specified by the
starting indices and size of each dimension, into the currently open
dataset.

;Usage:

    status = NXputslab (file_id, data, start[], size[])

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- |   | data | void \* | Data values |- |   | start\[\] | int | Indices
of starting values in each dimension |- |   | size\[\] | int | Length of
slab in each dimension |}

### NXputattr

Writes an attribute of the currently open data set. If no data set is
open, a global attribute is generated. The attribute has both a name and
a value.

;Usage:

    status = NXputattr (file_id, attr_name, value, length, type)

|- ! | Return Value | status | int | Error status |- ! | Input Arguments
| file\_id | NXhandle | Identifier of NeXus file |- |   | attr\_name |
char \* | Name of attribute |- |   | value | void \* | Value of
attribute |- |   | length | int | Length of data |- |   | type | int |
Type of attribute data (see list of valid data types) |}

### NXflush

Flushes all data to the NeXus file. Since this command closes and
reopens the file, a new file handle is returned. The command leaves the
program in the same state, i.e. with the same group and/or data set
open.

;Usage:

    status = NXflush (file_id)

|- ! | Input Arguments | file\_id | NXhandle \* | Identifier of NeXus
file |- ! | Output Arguments | file\_id | NXhandle \* | Identifier of
NeXus file |}

Meta-Data Routines
------------------

### NXgetinfo

Gets the rank, dimensions and data type of the currently open data set.

;Usage:

    status = NXgetinfo (file_id, rank, dimensions[], data_type)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! | Output Arguments | rank | int \* | Rank of data |- |   |
dimensions | int\[\] | Dimensions of data |- |   | data\_type | int \* |
Type of data (see list of valid data types) |}

### NXgetgroupinfo

Returns the number of items in the current group, and the name and class
of the current group.

;Usage:

    status = NXgetgroupinfo (file_id, item_number, group_name, group_class)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! | Output Arguments | item\_number | int \* | Number of NeXus data
items in the current group |- |   | group\_name | char \* | Name of
currently open NeXus group |- |   | group\_class | char \* | Class of
currently open NeXus group |}

### NXinitgroupdir

Initializes directory searches of the currently open group. This is
required to reset searches using NXgetnextentry that may have been
interrupted before completion.

;Usage:

    status = NXinitgroupdir (file_id)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|}

### NXgetnextentry

Implements a directory search facility on the current group level. The
first call initializes the search and returns information on the first
data item in the list. Subsequent calls yield information about the
remaining items. If the item is a group, its name and class is returned.
If it is a data set, its name and type is returned with a class of
“SDS.”

;Usage:

    status = NXgetnextentry (file_id, name, class, data_type)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! | Output Arguments | name | char \* | Name of NeXus data item
(group or set) |- |   | class | char \* | Class of NeXus group |- |   |
data\_type | int \* | Type of data set (see list of valid data types) |}

### NXgetattrinfo

Returns the number of attributes in the current data set.

;Usage:

    status = NXgetattrinfo (file_id, attr_number)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! | Output Arguments | attr\_number | int \* | Number of attributes
in the current data set |}

### NXinitattrdir

Initializes attribute searches of the currently open data set. This is
required to reset searches using NXgetnextattr that may have been
interrupted before completion.

;Usage:

    status = NXinitattrdir (file_id)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|}

### NXgetnextattr

Implements a search facility of the attributes of the currently open
data set. The first call initializes the search and returns information
on the first attribute in the list. Subsequent calls yield information
about the remaining attributes. This routine returns global attributes
if no data set is open.

;Usage:

    status = NXgetnextattr (file_id, attr_name, length, type)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! | Output Arguments | attr\_name | char \* | Name of next attribute
|- |   | length | int \* | Length of next attribute |- |   | type | int
\* | Type of next attribute (see list of valid data types) |}

### NXgetgroupID

Returns the identifier of the currently open group as an NXlink
structure.

;Usage:

    status = NXgetgroupID (file_id, group_id)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! | Output Arguments | group\_id | NXlink \* | Identifier of NeXus
group |}

### NXgetdataID

Gets the identifier of the currently open data set as an NXlink
structure. Returns NX\_ERROR if there is no open data set.

;Usage:

    status = NXgetdataID (file_id, data_id)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! | Output Arguments | data\_id | NXlink \* | Identifier of NeXus
data set |}

### NXmakelink

Links a data item (group or set) to a NeXus group. Returns NX\_ERROR if
the current group level is the root level, since no data item can be
linked here.

;Usage:

    status = NXmakelink (file_id, link)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! | Output Arguments | link | NXlink \* | Identifier of linked group
|}
