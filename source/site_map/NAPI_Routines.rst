=============
NAPI Routines
=============

OUT OF DATE
-----------
This page is now out of date and has been replaced by `[Doxygen generated documentation] <https://manual.nexusformat.org/doxygen/html-c/>`__

General Initialization and Shutdown
-----------------------------------

NXopen
======

    Opens the NeXus file, and creates and initializes the NeXus file structure.
    The returned handle is a pointer to this structure.

    **Usage:**

    .. code-block:: c

        status = NXopen(file_name, access_method, file_id);

    **Input Arguments**

        - file_name: *char \***
          Name of NeXus file to be opened.

        - access_method: *int*
          File Access options:

          - ``NXACC_READ``:   Read only

          - ``NXACC_RDWR``:   Read and write access

          - ``NXACC_CREATE``:   Create (HDF4) file

          - ``NXACC_CREATE4``:   Create HDF4 file

          - ``NXACC_CREATE5``:   Create HDF5 file

          - ``NXACC_CREATEXML``:   Create XML file

    **Output Arguments**

        - file_id: *NXhandle \***
          Identifier of the NeXus file.


NXclose
=======

    Closes NeXus file and deletes all associated data structures from memory.

    **Usage:**

    .. code-block:: c

        status = NXclose (file_id)

    **Input Arguments**
        - file_id
        - NXhandle *
        - Identifier of NeXus file

NXmakegroup
===========

    Creates a NeXus group at the current level in the group hierarchy, defining its name and class. This does not open the new group automatically.

    **Usage:**

    .. code-block:: c

        status = NXmakegroup (file_id, group_name, group_class)

    **Input Arguments**

            file_id       NXhandle  Identifier of NeXus file
            group_name    char *    Name of NeXus group
            group_class   char *    Class of NeXus group


NXopengroup
===========

    Opens an existing NeXus group for input and output of data.

    **Usage:**

    .. code-block:: c

        status = NXopengroup (file_id, group_name, group_class)

    **Input Arguments**

            file_id       NXhandle  Identifier of NeXus file
            group_name    char *    Name of NeXus group
            group_class   char *    Class of NeXus group


NXopenpath
==========

    Opens a NeXus group or dataset from a path string. The NeXus item must exist for NXopenpath to work correctly. The path string for NXopenpath has the same form as a unix path string: /group1/group/group2/dataset. Both absolute and relative path are supported.

    **Usage:**

    .. code-block:: c

        status = NXopenpath(file_id, path_string)

    **Input Arguments**

            file_id       NXhandle  Identifier of NeXus file
            path_string   char *    path to dataset or group in NeXus file


NXopengrouppath
===============

    Opens a NeXus group from a path string. This function is subtly different from NXopenpath in that it only opens the path to the last group; it does not open datasets. The NeXus item must exist for NXopengrouppath to work correctly. The path string for NXopengrouppath has the same form as a unix path string: /group1/group/group2/dataset. Both absolute and relative path are supported.

    **Usage:**

    .. code-block:: c

        status = NXopengrouppath(file_id, path_string)

    **Input Arguments**

        file_id       NXhandle  Identifier of NeXus file
        path_string   char *    path to dataset or group in NeXus file

NXclosegroup
============

    Closes the currently open group. If this group is a top-level group (i.e. with class NXentry), no groups are left open. Otherwise, the next group up in the hierarchy (i.e. the group containing the currently open group) is left open.

    **Usage:**

    .. code-block:: c

        status = NXclosegroup (file_id)

    **Input Arguments**

        file_id       NXhandle  Identifier of NeXus file

NXmakedata
==========

    Creates a new NeXus data set with the specified name, type, rank, and dimensions.

    **Usage:**

    .. code-block:: c

        status = NXmakedata (file_id, data_name, data_type, rank, dimensions[])

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **data_name** (char \*):
      Name of NeXus data set.

    - **data_type** (int):
      Data Type:

      - ``NX_CHAR``:  Character string

      - ``NX_FLOAT32``:  4-byte real

      - ``NX_FLOAT64``:  8-byte real

      - ``NX_INT8``:  1-byte integer

      - ``NX_UINT8``:   unsigned 1-byte integer

      - ``NX_INT16``:   2-byte integer

      - ``NX_UINT16``:   unsigned 2-byte integer

      - ``NX_INT32``:   4-byte integer

      - ``NX_UINT32``:   unsigned 4-byte integer

    - **rank** (int):
      Rank of data.

    - **dimensions** (int[]):
      Dimensions of data. The array is of size 'rank'.


NXcompmakedata
==============

    Creates a new NeXus data set with the specified name, type, rank, and dimensions, compressed using the specified protocol.

    **Usage:**

    .. code-block:: c

        status = NXcompmakedata (file_id, data_name, data_type, rank, dimensions[], compress_type, bufsize[])

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **data_name** (char \*):
      Name of NeXus data set.

    - **data_type** (int):
      Data Type:

      - ``NX_CHAR``:  Character string

      - ``NX_FLOAT32``:  4-byte real

      - ``NX_FLOAT64``:  8-byte real

      - ``NX_INT8``:  1-byte integer

      - ``NX_UINT8``:   unsigned 1-byte integer

      - ``NX_INT16``:   2-byte integer

      - ``NX_UINT16``:   unsigned 2-byte integer

      - ``NX_INT32``:   4-byte integer

      - ``NX_UINT32``:   unsigned 4-byte integer

    - **rank** (int):
      Rank of data.

    - **dimensions** (int[]):
      Dimensions of data. The array is of size 'rank'.

    - **compress_type** (int):
      Compression algorithm:

      - ``NX_COMP_LZW``:   GZIP

      - ``NX_COMP_HUF``:   Skipping Huffman

      - ``NX_COMP_RLE``:   Run Length Encoding

    - **bufsize** (int[]):
      The typical buffer size for writing.

NXopendata
===========

    Opens an existing NeXus data set for further processing i.e. reading and writing data or attributes, defining compression algorithms, and obtaining data set information.

    **Usage:**

    .. code-block:: c

        status = NXopendata (file_id, data_name)

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **data_name** (char \*):
      Name of NeXus data set


NXcompress
==========

    Defines a compression algorithm for subsequent calls to NXputdata.
    This routine is now deprecated; please use `NXcompmakedata` instead.

    **Usage:**

    .. code-block:: c

        status = NXcompress (file_id, compress_type)

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **compress_type** (int):
      Compression algorithm:

      - ``NX_COMP_LZW``:   GZIP

      - ``NX_COMP_HUF``:   Skipping Huffman

      - ``NX_COMP_RLE``:   Run Length Encoding


NXclosedata
===========

    Ends access to the currently active data set.

    **Usage:**

    .. code-block:: c

        status = NXclosedata (file_id)

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.


NXsetnumberformat
=================

    Sets the number format when writing to ASCII files.
    When serializing NeXus files to ASCII-XML files, a format for printing numbers is required.
    The NeXus-API has reasonable defaults for this. However, with this function, a desired format can be chosen for special cases.
    Please note that calls to this function will be silently ignored for the binary NeXus formats HDF-4 and HDF-5.

    **Usage:**

    .. code-block:: c

        status = NXsetnumberformat(file_id, data_type, format_string)

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **data_type** (int):
      The NeXus data type for which to change the print format:

      - ``NX_CHAR``:  Character string

      - ``NX_FLOAT32``:  4-byte real

      - ``NX_FLOAT64``:  8-byte real

      - ``NX_INT8``:  1-byte integer

      - ``NX_UINT8``:   unsigned 1-byte integer

      - ``NX_INT16``:   2-byte integer

      - ``NX_UINT16``:   unsigned 2-byte integer

      - ``NX_INT32``:   4-byte integer

      - ``NX_UINT32``:   unsigned 4-byte integer

    - **format_string** (char \*):
      An ANSI-C language style format string.


Reading and Writing
-------------------

NXgetdata
=========

    Reads data values from the currently open data set.
    Please note that memory overwrite occurs if the caller has not allocated enough memory to hold all the data available.
    Call ``NXgetinfo`` to determine the required dimension sizes.
    The data set must have been opened by ``NXopendata``.

    **Usage:**

    .. code-block:: c

        status = NXgetdata (file_id, data)

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    **Output Arguments:**

    - **data** (void \*):
      Data values.


NXgetslab
=========

    Reads a subset of the data in the current data set specifying the starting indices and size of each dimension.
    The caller is responsible for allocating enough memory for the data.

    **Usage:**

    .. code-block:: c

        status = NXgetslab (file_id, data, start[], size[])

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **start[]** (int):
      Indices of starting values in each dimension.

    - **size[]** (int):
      Length of slab in each dimension.

    **Output Arguments:**

    - **data** (void \*):
      Data values.


NXgetattr
=========

    Reads attribute values associated with the currently open data set.
    The attribute is defined by its name.
    Attributes are meta-data; data that provides information on the associated data set such as units, long names, etc.
    If no data set is open, it looks for a global attribute (i.e., attributes of the NeXus file).
    The caller is responsible for allocating enough memory for the attribute values.
    Only the first 'length' bytes of the attribute are read to prevent memory overwrite.

    **Usage:**

    .. code-block:: c

        status = NXgetattr (file_id, attr_name, value, length, type)

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **attr_name** (char \*):
      Name of attribute.

    - **length** (int \*):
      Length of buffer for storing attribute data.

    - **type** (int \*):
      Attribute Data Type:

      - ``NX_CHAR``: Character string

      - ``NX_FLOAT32``: 4-byte real

      - ``NX_FLOAT64``: 8-byte real

      - ``NX_INT8``: 1-byte integer

      - ``NX_UINT8``: Unsigned 1-byte integer

      - ``NX_INT16``: 2-byte integer

      - ``NX_UINT16``: Unsigned 2-byte integer

      - ``NX_INT32``: 4-byte integer

      - ``NX_UINT32``: Unsigned 4-byte integer

    **Output Arguments:**

    - **value** (void \*):
      Value of attribute.

    - **length** (int \*):
      Actual length of attribute data.


NXputdata
=========

    Writes data into the specified data set.

    **Usage:**

    .. code-block:: c

        status = NXputdata (file_id, data[])

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **data** (void \*):
      Data values.


NXputslab
=========

    Writes a subset of a multidimensional data array, specified by the starting indices and size of each dimension, into the currently open dataset.

    **Usage:**

    .. code-block:: c

        status = NXputslab (file_id, data, start[], size[])

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **data** (void \*):
      Data values.

    - **start[]** (int):
      Indices of starting values in each dimension.

    - **size[]** (int):
      Length of slab in each dimension.


NXputattr
=========

    Writes an attribute of the currently open data set.
    If no data set is open, a global attribute is generated.
    The attribute has both a name and a value.

    **Usage:**

    .. code-block:: c

        status = NXputattr (file_id, attr_name, value, length, type)

    **Return Value:**

    - **status** (int):
      Error status.

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **attr_name** (char \*):
      Name of attribute.

    - **value** (void \*):
      Value of attribute.

    - **length** (int):
      Length of data.

    - **type** (int):
      Data Type:

      - ``NX_CHAR``: Character string

      - ``NX_FLOAT32``: 4-byte real

      - ``NX_FLOAT64``: 8-byte real

      - ``NX_INT8``: 1-byte integer

      - ``NX_UINT8``: Unsigned 1-byte integer

      - ``NX_INT16``: 2-byte integer

      - ``NX_UINT16``: Unsigned 2-byte integer

      - ``NX_INT32``: 4-byte integer

      - ``NX_UINT32``: Unsigned 4-byte integer


NXflush
========

    Flushes all data to the NeXus file. Since this command closes and reopens the file, a new file handle is returned. The command leaves the program in the same state, i.e., with the same group and/or data set open.

    **Usage:**

    .. code-block:: c

        status = NXflush (file_id)

    **Input & Output Arguments:**

    - **file_id** (NXhandle \*):
      Identifier of NeXus file


Meta-Data Routines
------------------

NXgetinfo
=========

    Gets the rank, dimensions, and data type of the currently open data set.

    **Usage:**

    .. code-block:: c

       status = NXgetinfo(file_id, rank, dimensions[], data_type)

    **Return Value:**

     **status** (int):
     Error status.

    **Input Arguments**

     **file_id** (NXhandle):
     Identifier of NeXus file.

    **Output Arguments:**

     **rank** (int*):
     Rank of data.

     **dimensions** (int[]):
     Dimensions of data.

     **data_type** (int*):
     Data Type:

     - ``NX_CHAR``: Character string

     - ``NX_FLOAT32``: 4-byte real

     - ``NX_FLOAT64``: 8-byte real

     - ``NX_INT8``: 1-byte integer

     - ``NX_UINT8``: Unsigned 1-byte integer

     - ``NX_INT16``: 2-byte integer

     - ``NX_UINT16``: Unsigned 2-byte integer

     - ``NX_INT32``: 4-byte integer

     - ``NX_UINT32``: Unsigned 4-byte integer



NXgetgroupinfo
==============

    Returns the number of items in the current group, and the name and class of the current group.

    **Usage:**

    .. code-block:: c

        status = NXgetgroupinfo (file_id, item_number, group_name, group_class)

    **Return Value:**

        status        int       Error status

    **Input Arguments**

        file_id       NXhandle  Identifier of NeXus file

    **Output Arguments:**

        item_number   int*      Number of NeXus data items in the current group
        group_name    char*     Name of currently open NeXus group
        group_class   char*     Class of currently open NeXus group

NXinitgroupdir
==============

    Initializes directory searches of the currently open group. This is required to reset searches using NXgetnextentry that may have been interrupted before completion.

    **Usage:**

    .. code-block:: c

        status = NXinitgroupdir (file_id)

    **Return Value:**

        status        int       Error status

    **Input Arguments**

        file_id       NXhandle  Identifier of NeXus file


NXgetnextentry
==============

    Implements a directory search facility on the current group level. The first call initializes the search and returns information on the first data item in the list. Subsequent calls yield information about the remaining items. If the item is a group, its name and class is returned. If it is a data set, its name and type is returned with a class of SDS.

    **Usage:**

    .. code-block:: c

        status = NXgetnextentry (file_id, name, class, data_type)

    **Return Value:**

    - **status** (int):
      Error status.

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    **Output Arguments:**

    - **name** (char \*):
      Name of NeXus data item (group or set).

    - **class** (char \*):
      Class of NeXus group (SDS for a data item).

    - **data_type** (int \*):
      Data Type:

      - ``NX_CHAR``: Character string

      - ``NX_FLOAT32``: 4-byte real

      - ``NX_FLOAT64``: 8-byte real

      - ``NX_INT8``: 1-byte integer

      - ``NX_UINT8``: Unsigned 1-byte integer

      - ``NX_INT16``: 2-byte integer

      - ``NX_UINT16``: Unsigned 2-byte integer

      - ``NX_INT32``: 4-byte integer

      - ``NX_UINT32``: Unsigned 4-byte integer



NXgetattrinfo
=============

    Returns the number of attributes in the current data set.

    **Usage:**

    .. code-block:: c

        status = NXgetattrinfo (file_id, attr_number)

    **Return Value:**

        status        int       Error status

    **Input Arguments**

        file_id       NXhandle  Identifier of NeXus file

    **Output Arguments:**

        attr_number   int *     Number of attributes in the current data set


NXinitattrdir
=============

    Initializes attribute searches of the currently open data set. This is required to reset searches using NXgetnextattr that may have been interrupted before completion.

    **Usage:**

    .. code-block:: c

        status = NXinitattrdir (file_id)

    **Input Arguments**

        file_id       NXhandle  Identifier of NeXus file


NXgetnextattr
=============

    Implements a search facility of the attributes of the currently open data set. The first call initializes the search and returns information on the first attribute in the list. Subsequent calls yield information about the remaining attributes. This routine returns global attributes if no data set is open.

    **Usage:**

    .. code-block:: c

        status = NXgetnextattr (file_id, attr_name, length, attr_type)

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    **Output Arguments:**

    - **attr_name** (char \*):
      Name of next attribute.

    - **length** (int \*):
      Length of next attribute.

    - **attr_type** (int \*):
      Data type of next attribute:

      - ``NX_CHAR``: Character string

      - ``NX_FLOAT32``: 4-byte real

      - ``NX_FLOAT64``: 8-byte real

      - ``NX_INT8``: 1-byte integer

      - ``NX_UINT8``: Unsigned 1-byte integer

      - ``NX_INT16``: 2-byte integer

      - ``NX_UINT16``: Unsigned 2-byte integer

      - ``NX_INT32``: 4-byte integer

      - ``NX_UINT32``: Unsigned 4-byte integer



NXgetgroupID
============

    Returns the identifier of the currently open group as an NXlink structure.

    **Usage:**

    .. code-block:: c

        status = NXgetgroupID (file_id, group_id)

    **Input Arguments**

        file_id    NXhandle  Identifier of NeXus file

    **Output Arguments:**

        group_id   NXlink    Identifier of NeXus group


NXgetdataID
============

    Gets the identifier of the currently open data set as an NXlink structure. Returns NX_ERROR if there is no open data set.

    **Usage:**

    .. code-block:: c

        status = NXgetdataID (file_id, data_id)

    **Input Arguments**

        file_id    NXhandle  Identifier of NeXus file

    **Output Arguments:**

        data_id    NXlink    Identifier of NeXus data set


NXmakelink
==========

    Links a data item (group or set) to a NeXus group.
    Returns ``NX_ERROR`` if the current group level is the root level, since no data item can be linked here.

    **Usage:**

    .. code-block:: c

        status = NXmakelink (file_id, link)

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    **Output Arguments:**

    - **link** (NXlink \*):
      Identifier of linked group.


NXsameID
========

    Tests if two data items are the same, i.e., one is linked to the other.

    **Usage:**

    .. code-block:: c

        status = NXsameID (file_id, link1, link2)

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.

    - **link1** (NXlink \*):
      Identifier of first item.

    - **link2** (NXlink \*):
      Identifier of second item.


NXopensourcegroup
=================

    Opens the group from which a linked dataset was linked.
    This is useful for accessing auxiliary information related to the dataset.
    This works only if the linked dataset is currently open.

    **Usage:**

    .. code-block:: c

        status = NXopensourcegroup (file_id)

    **Input Arguments**

    - **file_id** (NXhandle):
      Identifier of NeXus file.


Memory Allocation
-----------------

NXmalloc
========

    Allocates memory to the specified data pointer according to the specified data type, rank, and dimensions.

    **Usage:**

    .. code-block:: c

        status = NXmalloc (void** data, int rank, int dimensions[], int datatype)

    **Output Arguments:**

    - **data** (void \*\*):
      Data pointer.

    **Input Arguments**

    - **rank** (int):
      Rank of data.

    - **dimensions** (int[]):
      Dimensions of data.

    - **datatype** (int):
      Data Type:
      - ``NX_CHAR``: Character string

      - ``NX_FLOAT32``: 4-byte real

      - ``NX_FLOAT64``: 8-byte real

      - ``NX_INT8``: 1-byte integer

      - ``NX_UINT8``: Unsigned 1-byte integer

      - ``NX_INT16``: 2-byte integer

      - ``NX_UINT16``: Unsigned 2-byte integer

      - ``NX_INT32``: 4-byte integer

      - ``NX_UINT32``: Unsigned 4-byte integer


NXfree
======

    Frees memory allocated to the specified data pointer.

    **Usage:**

    .. code-block:: c

        status = NXfree (data)

    **Input Arguments**

    - **data** (void \*\*):
      Pointer to the allocated memory.


NXinquirefile
=============

    Queries which file is really active.

    **Usage:**

    .. code-block:: c

        status = NXinquirefile(handle, filename, filenameLength)

    **Input Arguments**

    - **handle** (NXhandle):
      Handle to a currently open NeXus file.

    - **filenameLength** (int):
      Length of filename buffer.

    **Output Arguments:**

    - **filename** (char \*):
      Buffer to receive the filename.


NXlinkexternal
==============

    Links an external file. This happens by creating a group which points to an external file. Navigating into such a group automatically opens the external file.

    **Usage:**

    .. code-block:: c

        status = NXlinkexternal(handle, name, nxclass, nxurl)

    **Input Arguments**

    - **handle** (NXhandle):
      Handle to a currently open NeXus file.

    - **name** (NXname):
      The name of the group to link the file to.

    - **nxclass** (NXname):
      The NeXus class of the group to which the external file is to be linked.

    - **nxurl** (NXURL):
      An URL of a format understood by the NeXus-API. The only URL format so far is: ``nxfile://path-to-file#path-to-group-in-file``. This consists of two parts: the file path and a path to a group in the file to be mapped into the source file.


NXisexternalgroup
=================

    Tests if the group is an external group. If not, ``NX_ERROR`` is returned. If yes, ``NX_OK`` is returned and the URL of the external file is copied into `nxurl`.

    **Usage:**

    .. code-block:: c

        status = NXisexternalgroup(handle, name, nxclass, nxurl, nxurllen)

    **Input Arguments**

    - **handle** (NXhandle):
      Handle to a currently open NeXus file.

    - **name** (NXname):
      The name of the group to test.

    - **nxclass** (NXname):
      The NeXus class of the group to test.

    - **nxurllen** (int):
      Length of the `nxurl` buffer.

    **Output Arguments:**

    - **nxurl** (char \*):
      Buffer to copy the URL into.

