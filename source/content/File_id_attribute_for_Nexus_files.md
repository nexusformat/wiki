---
title: File id attribute for Nexus files
permalink: File_id_attribute_for_Nexus_files.html
layout: wiki
---
File id attribute for Nexus files
=================================

In its current definition of `NXroot` no attribute is provided to hold a
unique ID for a file. Though there is one for the filename, this might
not be unique and can change over time. Several facilities are planning
to store files on large storage systems to which access is provided not
only via a file system but also via web applications. The latter ones
typically rely on a database holding an index of the files on the
storage. In such cases a file on the storage system is typically
associated with an ID which acts as a primary key for the file.
Currently this ID is only stored in the database. Thus if the names or
locations of files on the storage system change there is no way to
rebuild the map between IDs and files.

I thus suggest to add an attribute `file_id` to the `NXroot` class which
allows facilities to store such a unique key for a file directly to the
Nexus file. The other ID values available are related to a particular
instance of `NXentry` and are thus not feasible to identify a file. In
particular if several instances of `NXentry` are stored in a single file
(this would make sense for archiving purposes as tape libraries can
usually handle large files much better than very small ones).

    NXroot (base class, version 1.0)
      @NX_class
      @file_time
      @file_name
      @file_update_time
      @NeXus_version
      @HDF_version
      @HDF5_Version
      @XML_version
      @creator
      @file_id 
      NXentry

The `file_id` attribute should be of type `NX_CHAR`.
