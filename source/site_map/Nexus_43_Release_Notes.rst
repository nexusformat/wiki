======================
Nexus 43 Release Notes
======================


4.3.0rc1
--------

Dowload the release candidate from the [NeXus download page](http://download.nexusformat.org/kits/nx43testing.shtml). Issues
reported with this release [can be found here](http://trac.nexusformat.org/code/query?status=new&status=assigned&status=reopened&status=closed&version=4.3.0-rc1&order=priority)
and results to testing on [NeXus\\_43\\_Testing](NeXus_43_Testing.html
"wikilink")

New Features
------------

- Links to external files via the NeXus external linking mechanism have now been enhanced to take advantage of native HDF5 external linking. Previously a nexus external file link was only visible to NeXus aware programs, and this will continue to be the case for XML and HDF4 based files. In the case of files created with the HDF5 underlying format, external file links will now be visible to any HDF5 (1.8.\\\*) aware program.

- HDF5 based files can now have multiple unlimited dimensions (previously only one was allowed)

- New API functions have been added to handle very large arrays. Most original NeXus functions had array dimensions of type int which restricted the maximum size of an array. New functions with a 64 suffix have been added which use int64\\_t rather than int

- existing functions continue to work as normal, so there is no need to update code unless you want to make use of the larger dimensions.

- A new python tree API has been added (note: need to add link for more finformation)

- A GUI java based NXvalidate program has now been added - The NeXus API now ensures thread safety, even if the underlying HDF/XML library is not built that way. The current approach would not allow any concurrency in writing, but HDF5 does not support this anyway at the moment.

- A new function NXreopen() has been added which will create additional NXhandle objects from an existing NXhandle, allowing you to have several NXhandle structures referring to the same file. This can give a large performance gain if you need to write to different parts of a file as separate threads can be created with their own NXhandles, thus removing the need to open and close data groups that can lead to unnecessary flushing to disk etc. - New application NXtraverse added

- TODO: other applications

- anything of note changed in NXtranslate, NXsummary etc?

Changed Features
----------------

- The HDF5 1.6.\\\* series libraries are no longer supported

- NeXus now requires 1.8.\\\* or higher. The 1.6.\\\* series is now very old and moving to 1.8.\\\* has allowed us to make use of new and improved features, such as native external file linking (see above)

System Requirements
-------------------

\**MXML XML Parsing Library*\* Version 2.2.2 or higher of mxml is required. Earlier versions have a bug and the XML API will not work. This package can be downloded
in [both source and binary rpm form](http://www.easysw.com/~mike/mxml/software.php) and is also available as part of [Fedora
Extras](http://fedoraproject.org/wiki/Extras/UsingExtras).

IMPORTANT NOTE: Debian also provides the mxml package, but it based on 2.0 and
will not work properly. \**Python Interface*\* You will need both the
numpy and ctypes modules to be available. These are provided in both the
Fedora and EPEL repositories. \**HDF5 Version*\* Only the HDF5-1.8.\\\*
series (and above) is now supported.

Building Notes
--------------

Known Issues
------------

Miscellaneous bug fixes
-----------------------

Upcoming Features
-----------------

