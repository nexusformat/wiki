---
title: NAPI Routines
permalink: NAPI_Routines.html
layout: wiki
---
NAPI Routines
=============

OUT OF DATE
-----------

This page is now out of date and has been replaced by [Doxygen generated
documentation](https://manual.nexusformat.org/doxygen/html-c/)

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

### NXopenpath

Opens a NeXus group or dataset from a path string. The NeXus item must
exist for NXopenpath to work correctly. The path string for NXopenpath
has the same form as a unix path string: /group1/group/group2/dataset.
Both absolute and relative path are supported.

;Usage:

    status = NXopenpath(file_id, path_string)

|- | rowspan=“3” | Input Arguments | file\_id | NXhandle |Identifier of
NeXus file |- | path\_string | char\* | path to dataset or group in
NeXus file |}

### NXopengrouppath

Opens a NeXus group from a path string. This function is subtly
different from NXopenpath in that it only opens the path to the last
group; it does not open datasets. The NeXus item must exist for
NXopengrouppath to work correctly. The path string for NXopengrouppath
has the same form as a unix path string: /group1/group/group2/dataset.
Both absolute and relative path are supported.

;Usage:

    status = NXopengrouppath(file_id, path_string)

|- | rowspan=“3” | Input Arguments | file\_id | NXhandle |Identifier of
NeXus file |- | path\_string | char\* | path to dataset or group in
NeXus file |}

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
data\_type | int |

Data Type:NX\_CHAR - Character string  
NX\_FLOAT32 - 4-byte real

NX\_FLOAT64 - 8-byte real

NX\_INT8 - 1-byte integer

NX\_UINT8 - unsigned 1-byte integer

NX\_INT16 - 2-byte integer

NX\_UINT16 - unsigned 2-byte integer

NX\_INT32 - 4-byte integer

NX\_UINT32 - unsigned 4-byte integer

|- | rank | int | Rank of data |- | dimensions | int\[\] | Dimensions of
data. The array is of size 'rank' |}

### NXcompmakedata

Creates a new NeXus data set with the specified name, type, rank and
dimensions, compressed using the specified protocol.

;Usage:

    status = NXcompmakedata (file_id, data_name, data_type, rank, dimensions[], compress_type, bufsize[])

|- ! rowspan=“7” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | data\_name | char \* | Name of NeXus data set |- |
data\_type | int |

Data Type:NX\_CHAR - Character string  
NX\_FLOAT32 - 4-byte real

NX\_FLOAT64 - 8-byte real

NX\_INT8 - 1-byte integer

NX\_UINT8 - unsigned 1-byte integer

NX\_INT16 - 2-byte integer

NX\_UINT16 - unsigned 2-byte integer

NX\_INT32 - 4-byte integer

NX\_UINT32 - unsigned 4-byte integer

|- | rank | int | Rank of data |- | dimensions | int\[\] | Dimensions of
data. The array is of size 'rank' |- | compress\_type | int |

Compression algorithm:NX\_COMP\_LZW - GZIP  
NX\_COMP\_HUF - Skipping Huffman

NX\_COMP\_RLE - Run Length Encoding

|- | bufsize | int\[\] | The typical buffersize for writing. |} The
buffersize requires further explanation. HDF-5 compresses data in
chunks. And the buffersize is this chunksize. If data is written in one
go with a NXputdata, this is the dimensions of the data. If data is
written in slabs, this is the preferred size of the slabs. Please note,
that this has only a performance impact when writing, it is no show
stopper. Please note that HDF-4 does not support compression on data
sets written in slabs: If you want compression with HDF-4, data must be
written with one call to NXputdata. Compression is ignored for XML-NeXus
files.

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
|- |}

### NXsetnumberformat

Sets the number format when writing to ASCII files. When serializing
NeXus file to ASCII-XML files a format for printing numbers is required.
The NeXus-API has reasonable defaults for this. However, with this
function a desired format can be choosen for special cases. Please note
that calls to this function will be silently ignored for the binary
NeXus formats HDF-4 and HDF-5.

;Usage:

    status = NXsetnumberformat(file_id,data_type,format_string

|- ! rowspan=“3” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- |data\_type | int | The NeXus data type for which to
change the print format.

Data Type:NX\_CHAR - Character string  
NX\_FLOAT32 - 4-byte real

NX\_FLOAT64 - 8-byte real

NX\_INT8 - 1-byte integer

NX\_UINT8 - unsigned 1-byte integer

NX\_INT16 - 2-byte integer

NX\_UINT16 - unsigned 2-byte integer

NX\_INT32 - 4-byte integer

NX\_UINT32 - unsigned 4-byte integer

|- | format\_string | char\* | A ANSI-C language style format string |-
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

|- ! rowspan=“3” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | start\[\] | int | Indices of starting values in each
dimension |- | size\[\] | int | Length of slab in each dimension |- ! |
Output Arguments | data | void \* | Data values |}

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

|- ! rowspan=“4” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | attr\_name | char \* | Name of attribute |- | length |
int \* | Length of buffer for storing attribute data |- | type | int \*
|

Attribute Data Type:NX\_CHAR - Character string  
NX\_FLOAT32 - 4-byte real

NX\_FLOAT64 - 8-byte real

NX\_INT8 - 1-byte integer

NX\_UINT8 - unsigned 1-byte integer

NX\_INT16 - 2-byte integer

NX\_UINT16 - unsigned 2-byte integer

NX\_INT32 - 4-byte integer

NX\_UINT32 - unsigned 4-byte integer

|- ! rowspan=“2” | Output Arguments | value | void \* | Value of
attribute |- | length | int \* | Actual length of attribute data |}

### NXputdata

Writes data into the specified data set.

;Usage:

    status = NXputdata (file_id, data[])

|- ! rowspan=“2” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | data | void \* | Data values |}

### NXputslab

Writes a subset of a multidimensional data array, specified by the
starting indices and size of each dimension, into the currently open
dataset.

;Usage:

    status = NXputslab (file_id, data, start[], size[])

|- ! rowspan=“4” | Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | data | void \* | Data values |- | start\[\] | int |
Indices of starting values in each dimension |- | size\[\] | int |
Length of slab in each dimension |}

### NXputattr

Writes an attribute of the currently open data set. If no data set is
open, a global attribute is generated. The attribute has both a name and
a value.

;Usage:

    status = NXputattr (file_id, attr_name, value, length, type)

|- ! | Return Value | status | int | Error status |- ! rowspan=“5” |
Input Arguments | file\_id | NXhandle | Identifier of NeXus file |- |
attr\_name | char \* | Name of attribute |- | value | void \* | Value of
attribute |- | length | int | Length of data |- | type | int |

Data Type:NX\_CHAR - Character string  
NX\_FLOAT32 - 4-byte real

NX\_FLOAT64 - 8-byte real

NX\_INT8 - 1-byte integer

NX\_UINT8 - unsigned 1-byte integer

NX\_INT16 - 2-byte integer

NX\_UINT16 - unsigned 2-byte integer

NX\_INT32 - 4-byte integer

NX\_UINT32 - unsigned 4-byte integer

|}

### NXflush

Flushes all data to the NeXus file. Since this command closes and
reopens the file, a new file handle is returned. The command leaves the
program in the same state, i.e. with the same group and/or data set
open.

;Usage:

    status = NXflush (file_id)

|- ! | Input & Output Argument | file\_id | NXhandle \* | Identifier of
NeXus file |}

Meta-Data Routines
------------------

### NXgetinfo

Gets the rank, dimensions and data type of the currently open data set.

;Usage:

    status = NXgetinfo (file_id, rank, dimensions[], data_type)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! rowspan=“3” | Output Arguments | rank | int \* | Rank of data |- |
dimensions | int\[\] | Dimensions of data |- | data\_type | int \* |

Data Type:NX\_CHAR - Character string  
NX\_FLOAT32 - 4-byte real

NX\_FLOAT64 - 8-byte real

NX\_INT8 - 1-byte integer

NX\_UINT8 - unsigned 1-byte integer

NX\_INT16 - 2-byte integer

NX\_UINT16 - unsigned 2-byte integer

NX\_INT32 - 4-byte integer

NX\_UINT32 - unsigned 4-byte integer

|}

### NXgetgroupinfo

Returns the number of items in the current group, and the name and class
of the current group.

;Usage:

    status = NXgetgroupinfo (file_id, item_number, group_name, group_class)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! rowspan=“3” | Output Arguments | item\_number | int \* | Number of
NeXus data items in the current group |- | group\_name | char \* | Name
of currently open NeXus group |- | group\_class | char \* | Class of
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
|- ! rowspan=“3” | Output Arguments | name | char \* | Name of NeXus
data item (group or set) |- | class | char \* | Class of NeXus group
(“SDS” for a data item) |- | data\_type | int \* |

Data Type:NX\_CHAR - Character string  
NX\_FLOAT32 - 4-byte real

NX\_FLOAT64 - 8-byte real

NX\_INT8 - 1-byte integer

NX\_UINT8 - unsigned 1-byte integer

NX\_INT16 - 2-byte integer

NX\_UINT16 - unsigned 2-byte integer

NX\_INT32 - 4-byte integer

NX\_UINT32 - unsigned 4-byte integer

|}

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

    status = NXgetnextattr (file_id, attr_name, length, attr_type)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- ! rowspan=“3” | Output Arguments | attr\_name | char \* | Name of
next attribute |- | length | int \* | Length of next attribute |- |
attr\_type | int \* |

Data type of next attribute:NX\_CHAR - Character string  
NX\_FLOAT32 - 4-byte real

NX\_FLOAT64 - 8-byte real

NX\_INT8 - 1-byte integer

NX\_UINT8 - unsigned 1-byte integer

NX\_INT16 - 2-byte integer

NX\_UINT16 - unsigned 2-byte integer

NX\_INT32 - 4-byte integer

NX\_UINT32 - unsigned 4-byte integer

|}

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

### NXsameID

Tests if two data items are the same, i.e. one is linked to the other.

;Usage:

    status = NXsameID (file_id, link1, link2)

|- ! rowspan=“3”| Input Arguments | file\_id | NXhandle | Identifier of
NeXus file |- | link1 | NXlink \* | Identifier of first item |- | link2
| NXlink \* | Indentifier of second item |- |}

### NXopensourcegroup

Opens the group from which a linked dataset was linked. This is useful
for accessing auxiliary information related to the dataset. This works
only if the linked dataset is currently open.

;Usage:

    status = NXopensourcegroup (file_id)

|- ! | Input Arguments | file\_id | NXhandle | Identifier of NeXus file
|- |}

Memory Allocation
-----------------

### NXmalloc

Allocates memory to the specified data pointer according to the specifed
data type, rank and dimensions.

;Usage:

    status = NXmalloc (void** data, int rank, int dimensions[], int datatype)

|- ! | Output Arguments | data | void \*\* | Data pointer |- !
rowspan=“3” | Input Arguments | rank | int | Rank of data |- |
dimensions | int\[\] | Dimensions of data |- | datatype | int |

Data Type:NX\_CHAR - Character string  
NX\_FLOAT32 - 4-byte real

NX\_FLOAT64 - 8-byte real

NX\_INT8 - 1-byte integer

NX\_UINT8 - unsigned 1-byte integer

NX\_INT16 - 2-byte integer

NX\_UINT16 - unsigned 2-byte integer

NX\_INT32 - 4-byte integer

NX\_UINT32 - unsigned 4-byte integer

|}

### NXfree

Frees memory allocated to the specified data pointer.

;Usage:

    status = NXfree (data)

|- ! | Input Arguments | data | void \*\* | Pointer to the allocated
memory |}

External Linking
----------------

### NXinquirefile

Queries which file is really active.

;Usage:

    status = NXinquirefile(handle,filename, filenameLength);

|- ! rowspan=“2” | Input Arguments | handle | NXhandle | handle to a
currently open NeXus file. |- | filenameLength | int | length of
filename buffer |- ! |Output Arguments | filename | char\* | buffer to
receive filename |}

### NXlinkexternal

Links an external file. This happens by creating a group which points to
an external file. Navigating into such a group automatically opens the
external file.

;Usage:

    status = NXlinkexternal(handle,name, nxclass, nxurl);

|- ! rowspan=“4” | Input Arguments | handle | NXhandle | handle to a
currently open NeXus file. |- | name | NXname | The name of the group to
link the file to. |- | nxclass | NXname | The NeXus class of the group
to which the external file is to be linked. |- | nxurl | NXURL | An URL
of a format which the NeXus-API understands. The only URL format so far
is: nxfile://path-to-file\#path-to-group-in-file. This consistes of two
parts: The file path and a path to a group in the file which is to be
mapped into the source file. |}

### NXisexternalgroup

Tests in the group is an external group. If not, NX\_ERROR is returned.
If yes, NX\_OK is returned and the URL of the external file is copied
into nxurl.

;Usage:

    status = NXisexternalgroup(handle,name, nxclass, nxurl,nxurllen);

|- ! rowspan=“4” | Input Arguments | handle | NXhandle | handle to a
currently open NeXus file. |- | name | NXname | The name of the group to
test. |- | nxclass | NXname | The NeXus class of the group to test. |- |
nxurllen | int | length of the nxurl buffer |- ! rowspan=“4” | Output
Arguments | nxurl | char \* | buffer to copy the URL, too. |}
