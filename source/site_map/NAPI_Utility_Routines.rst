=====================
NAPI Utility Routines
=====================

NXUwriteglobals
===============

    Writes the global attributes defined in the NeXus standard. Note that ``NeXus_version``, ``file_name``
    and ``file_time`` are written automatically by the NeXus API. The
    attribute arguments are optional, so the Fortran 90 keyword syntax can be used
    for all of them, *e.g.*, ``status = NXUwriteglobals (file_id, user="Joe
    Bloggs", email="JB@some.where")``.

    **Usage:**

    .. code-block:: fortran

        status = NXUwriteglobals (file_id, user, affiliation, address, phone, fax, email)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **user** (type: ``character(len=*)``):
      Name of user.

    - **affiliation** (type: ``character(len=*)``):
      User's affiliation.

    - **address** (type: ``character(len=*)``):
      User's address.

    - **phone** (type: ``character(len=*)``):
      User's telephone number.

    - **fax** (type: ``character(len=*)``):
      User's fax number.

    - **email** (type: ``character(len=*)``):
      User's email address.

NXUwritegroup
=============

    Creates a NeXus group leaving it open for subsequent data output.

    **Usage:**

    .. code-block:: fortran

        status = NXUwritegroup (file_id, group_name, group_class)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **group_name** (type: ``character(len=*)``):
      Name of group.

    - **group_class** (type: ``character(len=*)``):
      Class of group.


NXUwritedata
============

    Creates, opens and writes a NeXus data set in the current group. Data can be a scalar value, or a one-, two-, or three-dimensional array. If higher dimensions are required, use the core API (see ``NXputdata``). ``units``, ``data_start``, and ``data_size`` are optional parameters. If you want the data set to be compressed, set default compression parameters in ``NXUsetcompress``.

    **Usage:**

    .. code-block:: c

        status = NXUwritedata (file_id, data_name, data, units, data_start, data_size)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **data_name** (type: ``character(len=*)``):
      Name of data set.

    - **data** (type:
      ``integer(:)``, ``integer(:,:)``, ``integer(:,:,:)``,
      ``real``, ``real(:)``, ``real(:,:)``, ``real(:,:,:)``,
      ``character(len=*)``):
      Data values.

    - **units** (type: ``character(len=*)``, optional):
      Data units.

    - **start** (type: ``integer(:)``, optional):
      Starting indices of data slab.

    - **size** (type: ``integer(:)``, optional):
      Length of each dimension of data slab.


NXUreaddata
===========

    Opens and reads a NeXus data set in the current group. Data can be a scalar value, or a one-, two-, or three-dimensional array. If higher dimensions are required, use the core API (see ``NXgetdata``). ``units``, ``data_start``, and ``data_size`` are optional parameters.

    **Usage:**

    .. code-block:: c

        status = NXUreaddata(file_id, data_name, data, units, data_start, data_size)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **data_name** (type: ``character(len=*)``):
      Name of data set.

    - **start** (type: ``integer(:)``, optional):
      Starting indices of data slab.

    - **size** (type: ``integer(:)``, optional):
      Length of each dimension of data slab.

    **Output Arguments:**

    - **data** (type:
      ``integer(:)``, ``integer(:,:)``, ``integer(:,:,:)``,
      ``real``, ``real(:)``, ``real(:,:)``, ``real(:,:,:)``,
      ``character(len=*)``):
      Data values.

    - **units** (type: ``character(len=*)``, optional):
      Data units.

NXUwritehistogram
=================

    Creates, opens, and writes a one-dimensional NeXus data item with units. The input data are assumed to be histogram bin boundaries, and the stored data contains the histogram centers, i.e., the stored array has a dimension one less than the data. The ``histogram_offset`` attribute is automatically set to half the width of the first bin, which allows the regeneration of the bin boundaries by ``NXUreadhistogram``.

    **Usage:**

    .. code-block:: c

        status = NXUwritehistogram(file_id, data_name, data, units)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **data_name** (type: ``character(len=*)``):
      Name of histogram.

    - **data** (type: ``real(:), pointer``):
      Histogram bin boundaries.

    - **units** (type: ``character(len=*)``, optional):
      Data units.


NXUreadhistogram
================

    Opens and reads a one-dimensional real data set in the current group. The data are assumed to be histogram bin boundaries, which are stored in NeXus files as bin centers with the first bin offset defined as the attribute ``histogram_offset``, i.e., the returned array has a dimension one greater than the stored array (see ``NXUwritehistogram``). If the ``histogram_offset`` attribute is not present, it is assumed that the first bin width equals the separation of the first two bin centers.

    **Usage:**

    .. code-block:: c

        status = NXUreadhistogram (file_id, data_name, data, units)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **data_name** (type: ``character(len=*)``):
      Name of histogram.

    **Output Arguments:**

    - **data** (type: ``real(:), pointer``):
      Histogram bin boundaries.

    - **units** (type: ``character(len=*)``, optional):
      Data units.


NXUsetcompress
==============

    Sets the compression type to be used in subsequent calls to ``NXUwritedata``. The second parameter, which is optional, sets the minimum number of elements in a data set before any compression is performed. This is to prevent inefficient compression of small data sets. The default value is 100.

    **Usage:**

    .. code-block:: c

        status = NXUsetcompress (file_id, compress_type, compress_size)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **compress_type** (type: ``integer``):
      Compression algorithm. Options include:
      - ``NX_COMP_LZW``: GZIP
      - ``NX_COMP_HUF``: Skipping Huffman
      - ``NX_COMP_RLE``: Run Length Encoding
      - ``NX_COMP_NONE``: No compression

    - **compress_size** (type: ``integer``):
      Minimum number of elements in data set before compression is attempted.

NXUfindgroup
=============

    Finds if the NeXus group exists in the current group and returns its class. The returned status is ``NX_EOD`` if the group is not found.

    **Usage:**

    .. code-block:: c

        status = NXUfindgroup (file_id, group_name, group_class)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **group_name** (type: ``character(len=*)``):
      Name of group.

    **Output Arguments:**

    - **group_class** (type: ``character(len=*)``):
      Class of group.

NXUfindclass
=============

    Finds if a NeXus group of the requested class exists in the current group and returns its name. ``find_index`` is used when there is more than one group of the required class; ``find_index = 3`` returns the name of the third group found. The returned status is ``NX_EOD`` if no such group is found.

    **Usage:**

    .. code-block:: c

        status = NXUfindclass (file_id, group_class, group_name, find_index)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **group_class** (type: ``character(len=*)``):
      Requested class.

    - **find_index** (type: ``integer``):
      Search index.

    **Output Arguments:**

    - **group_name** (type: ``character(len=*)``):
      Name of the group with that class.

NXUfinddata
============

    Finds if a NeXus data set of the requested name exists in the current group. The returned status is ``NX_EOD`` if the data set is not found.

    **Usage:**

    .. code-block:: c

        status = NXUfinddata (file_id, data_name)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **data_name** (type: ``character(len=*)``):
      Requested data set.

NXUfindattr
============

    Finds if a NeXus attribute of the current data set exists. The returned status is ``NX_EOD`` if the attribute is not found.

    **Usage:**

    .. code-block:: c

        status = NXUfindattr (file_id, attr_name)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **attr_name** (type: ``character(len=*)``):
      Requested attribute name.

NXUfindsignal
=============

    Finds the NeXus data set in the current group with the required signal attribute, and returns its name, rank, type, and dimensions. The returned status is ``NX_EOD`` if the signal data set is not found.

    **Usage:**

    .. code-block:: c

        status = NXUfindsignal (file_id, signal, data_name, data_rank, data_type, data_dimensions)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **signal** (type: ``integer``):
      Required value of signal attribute.

    **Output Arguments:**

    - **data_name** (type: ``character(len=*)``):
      Data set with the required signal attribute.

    - **data_rank** (type: ``integer``):
      Rank of the data set.

    - **data_type** (type: ``integer``):
      Type of the data set (see list of valid data types).

    - **data_dimensions** (type: ``integer(:)``):
      Dimensions of the data set.


NXUfindaxis
============

    Finds the NeXus data set in the current group with the required axis and primary attributes, and returns its name, rank, type, and dimensions. Note that the axis data set should be one-dimensional. The returned status is ``NX_EOD`` if the axis data set is not found.

    **Usage:**

    .. code-block:: c

        status = NXUfindaxis (file_id, axis, primary, data_name, data_rank, data_type, data_dimensions)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **axis** (type: ``integer``):
      Required value of axis attribute.

    - **primary** (type: ``integer``):
      Required value of primary attribute.

    **Output Arguments:**

    - **data_name** (type: ``character(len=*)``):
      Data set with the required axis attribute.

    - **data_rank** (type: ``integer``):
      Rank of the data set.

    - **data_type** (type: ``integer``):
      Type of the data set (see list of valid data types).

    - **data_dimensions** (type: ``integer(:)``):
      Dimensions of the data set.

NXUfindlink
============

    Finds another group to which the currently open data set is linked and leaves it open for getting associated data. ``group_id`` stores the ID of the original group to enable a subsequent return (see ``NXUresumelink``). ``group_class`` is an optional argument that restricts the search to the specified group class. The returned status is ``NX_EOD`` if the group is not found.

    **Usage:**

    .. code-block:: c

        status = NXUfindlink (file_id, group_id, group_class)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **group_class** (type: ``character(len=*)``):
      Group classes to be searched.

    **Output Arguments:**

    - **group_id** (type: ``NXlink``):
      ID of the current group.

NXUresumelink
==============

    Returns to the original group from which an ``NXUfindlink`` call was issued.

    **Usage:**

    .. code-block:: c

        status = NXUresumelink (file_id, group_id)

    **Input Arguments:**

    - **file_id** (type: ``NXhandle``):
      Identifier of NeXus file.

    - **group_id** (type: ``NXlink``):
      ID of the original group.

