---
title: NAPI Utility Routines
permalink: NAPI_Utility_Routines.html
layout: wiki
---
NAPI Utility Routines
=====================

### NXUwriteglobals

Writes the global attributes defined in the NeXus standard. Note that
NeXus\_version, file\_name and file\_time are written automatically by
the NeXus API. The attribute arguments are optional, so the F90 keyword
syntax can be used for all of them, *e.g.*,

    status = NXUwriteglobals (file_id, user="Joe Bloggs", email="JB@some.where")

;Usage:

    status = NXUwriteglobals (file_id, user, affiliation, address, phone, fax, email)

|- ! rowspan=“7” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | user | character(len=\*) | Name of user |-
| affiliation | character(len=\*) | User's affiliation |- | address |
character(len=\*) | User's address |- | phone | character(len=\*) |
User's telephone number |- | fax | character(len=\*) | User's fax number
|- | email | character(len=\*) | User's email address |}

### NXUwritegroup

Creates a NeXus group leaving it open for subsequent data output.

;Usage:

    status = NXUwritegroup (file_id, group_name, group_class)

|- ! rowspan=“3” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | group\_name | character(len=\*) | Name of
group |- | group\_class | character(len=\*) | Class of group |}

### NXUwritedata

Creates, opens and writes a NeXus data set in the current group. “data”
can be a scalar value, or a one-, two-, or three-dimensional array. If
higher dimensions are required, use the core API (see NXputdata).
“units”, “data\_start” and “data\_size” are optional parameters. If you
want the data set to be compressed, set default compression parameters
in NXUsetcompress.

;Usage:

    status = NXUwritedata (file_id, data_name, data, units, data_start, data_size)

|- ! rowspan=“7”| Input Arguments |- | file\_id | type(NXhandle) |
Identifier of NeXus file |- | data\_name | character(len=\*) | Name of
data set |- | data | integer  
integer(:)  
integer(:,:)  
integer(:,:,:)  
real  
real(:)  
real(:,:)  
real(:,:,:)  
character(len=\*) | Data values |- | units | character(len=\*) | Data
units (optional) |- | start | integer(:) | Starting indices of data slab
(optional) |- | size | integer(:) | Length of each dimension of data
slab (optional) |}

### NXUreaddata

Opens and reads a NeXus data set in the current group. “data” can be a
scalar value, or a one-, two-, or three-dimensional array. If higher
dimensions are required, use the core API (see NXgetdata). “units”,
“data\_start” and “data\_size” are optional parameters.

;Usage:

    status = NXUreaddata (file_id, data_name, data, units, data_start, data_size)

|- ! rowspan=“4” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | data\_name | character(len=\*) | Name of
data set |- | start | integer(:) | Starting indices of data slab
(optional) |- | size | integer(:) | Length of each dimension of data
slab (optional) |- ! rowspan=“2” | Output Arguments | data | integer  
integer(:)  
integer(:,:)  
integer(:,:,:)  
real  
real(:)  
real(:,:)  
real(:,:,:)  
character(len=\*) | Data values |- | units | character(len=\*) | Data
units (optional) |}

### NXUwritehistogram

Creates, opens and writes a one dimensional NeXus data item with units.
The input “data” are assumed to be histogram bin boundaries, and the
stored data contains the histogram centers, i.e. the stored array has a
dimension one less than the “data”. The “histogram\_offset” attribute is
automatically set to half the width of the first bin, which allows the
regeneration of the bin boundaries by NXUreadhistogram.

;Usage:

    status = NXUwritehistogram (file_id, data_name, data, units)

|- ! rowspan=“4” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | data\_name | character(len=\*) | Name of
histogram |- | data | real(:), pointer | Histogram bin boundaries |- |
units | character(len=\*) | Data units (optional) |}

### NXUreadhistogram

Opens and reads a one dimensional real data set in the current group.
The data are assumed to be histogram bin boundaries, which are stored in
NeXus files as bin centers with the first bin offset defined as the
attribute “histogram\_offset”, i.e. the returned array has a dimension
one greater than the stored array (see NXUwritehistogram). If the
“histogram\_offset” attribute is not present, it is assumed that the
first bin width equals the separation of the first two bin centers.

;Usage:

    status = NXUreadhistogram (file_id, data_name, data, units)

|- ! rowspan=“2” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | data\_name | character(len=\*) | Name of
histogram |- ! rowspan=“2” | Output Arguments | data | real(:), pointer
| Histogram bin boundaries |- | units | character(len=\*) | Data units
(optional) |}

### NXUsetcompress

Sets the compression type to be used in subsequent calls to
NXUwritedata. The second parameter, which is optional, sets the minimum
number of elements in a data set before any compression is performed.
This is to prevent inefficient compression of small data sets. The
default value is 100.

;Usage:

    status = NXUsetcompress (file_id, compress_type, compress_size)

|- ! rowspan=“3” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | compress\_type | integer |

Compression algorithm:NX\_COMP\_LZW - GZIP  
NX\_COMP\_HUF - Skipping Huffman

NX\_COMP\_RLE - Run Length Encoding

NX\_COMP\_NONE - No compression

|- | compress\_size | integer | Minimum number of elements in data set
before data compression is attempted. |}

### NXUfindgroup

Finds if NeXus group exists in the current group and returns its class.
The returned status is NX\_EOD if the group is not found.

;Usage:

    status = NXUfindgroup (file_id, group_name, group_class)

|- ! rowspan=“2” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | group\_name | character(len=\*) | Name of
group |- ! | Output Arguments | group\_class | character(len=\*) | Class
of group |}

### NXUfindclass

Finds if a NeXus group of the requested class exists in the current
group and returns its name. “find\_index” is used when there is more
than one group of the required class; find\_index = 3 returns the name
of the third group found. The returned status is NX\_EOD if no such
group is found.

;Usage:

    status = NXUfindclass (file_id, group_class, group_name, find_index)

|- ! rowspan=“3” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | group\_class | character(len=\*) |
Requested class |- | find\_index | integer | Search index |- ! | Output
Arguments | group\_name | character(len=\*) | Name of group with that
class |}

### NXUfinddata

Finds if a NeXus data set of the requested name exists in the current
group. The returned status is NX\_EOD if the data set is not found.

;Usage:

    status = NXUfinddata (file_id, data_name)

|- ! rowspan=“2” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | data\_name | character(len=\*) | Requested
data set |}

### NXUfindattr

Finds if a NeXus attribute of the current data set exists. The returned
status is NX\_EOD if the attribute is not found.

;Usage:

    status = NXUfindattr (file_id, attr_name)

|- ! rowspan=“2” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | attr\_name | character(len=\*) | Requested
attribute name |}

### NXUfindsignal

Finds the NeXus data set in the current group with the required signal
attribute, and returns its name, rank, type and dimensions. The returned
status is NX\_EOD if the signal data set is not found.

;Usage:

    status = NXUfindsignal (file_id, signal, data_name, data_rank, data_type, data_dimensions)

|- ! rowspan=“2” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | signal | integer | Required value of
signal attribute |- ! rowspan=“4” | Output Arguments | data\_name |
character(len=\*) | Data set with required signal attribute |- |
data\_rank | integer | Rank of data set |- | data\_type | integer | Type
of data set (see list of valid data types) |- | data\_dimensions |
integer(:) | Dimensions of data set |}

### NXUfindaxis

Finds the NeXus data set in the current group with the required axis and
primary attributes, and returns its name, rank, type and dimensions.
Note that the axis data set should be one-dimensional. The returned
status is NX\_EOD if the axis data set is not found.

;Usage:

    status = NXUfindaxis (file_id, axis, primary, data_name, data_rank, data_type, data_dimensions)

|- ! rowspan=“3” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | axis | integer | Required value of axis
attribute |- | primary | integer | Required value of primary attribute
|- ! rowspan=“4” | Output Arguments | data\_name | character(len=\*) |
Data set with required signal attribute |- | data\_rank | integer | Rank
of data set |- | data\_type | integer | Type of data set (see list of
valid data types) |- | data\_dimensions | integer(:) | Dimensions of
data set |}

### NXUfindlink

Finds another group to which the currently open data set is linked and
leaves it open for getting associated data. “group\_id” stores the ID of
the original group to enable a subsequent return (see NXUresumelink).
“group\_class” is an optional argument which restricts the search to the
specified group class. The returned status is NX\_EOD if the group is
not found.

;Usage:

    status = NXUfindlink (file_id, group_id, group_class)

|- ! rowspan=“2” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | group\_class | character(len=\*) | Group
classes to be searched. |- ! | Output Arguments | group\_id |
type(NXlink) | ID of current group. |}

### NXUresumelink

Returns to the original group from which an NXfindlink call was issued.

;Usage:

    status = NXUresumelink (file_id, group_id)

|- ! rowspan=“2” | Input Arguments | file\_id | type(NXhandle) |
Identifier of NeXus file |- | group\_id | type(NXlink) | ID of original
group |}
