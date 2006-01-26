---
title: Linking External Files
permalink: Linking_External_Files/
layout: wiki
---

Linkinge External Files
-----------------------

This discussion is on how to access external files from within a given
NeXus files. This defeats one guiding principle of NeXus: to have
everything in one file, somewhat. However, having everything in one file
can mean replicating large time-of-flight empty can or vanadium datasets
in each data file. In such cases it would be nice to access
transparently an external file holding such data. This page discusses
some of the implementation issues of such a scheme.

### Storing External File Information

Somehow the information that an external file has to be accessed must be
stored within the parent NeXus file. Given the feauture set of NeXus I
suggest to store this information as an attribute to a NeXus object. It
would be sensible to restrict this attribute to NeXus groups only. As a
name of the attribute I suggest **mount** following the example of
HDF-5. The data content of this attribute should be an URL pointing to
the requested file. This not only follows the fashion of the day but
also gives a lot of freedom to implement various file access strategies
and even file formats. As it might be necessary to specify alternative
locations for a given external file, I suggest to allow multiple URLs
separated by :: It must be :: because a single colon can be part of a
valid URL.

### Implementing External File Access At The NAPI Level

Various issues have to be adressed when implementing external file
access. The most important one is how to transparently navigate the file
hierarchy resulting from external linking. In order to handle this I
suggest to change NXhandle. Currently NXhandle maps to a pNexusFunction
structure. Navigating the file hierarchy becomes possible when NXhandle
is modified to become a stack of pNexusFunction structures. All
functions in napi.c would need to be changed to access the bottom
element of this stack. NXopengroup would then be modified to check for
the mount attribute. If the mount attribute is found, NXopengroup would
open the file specified in the URL and push the new pNexusFunction onto
the stack. Likewise NXclosegroup has to check if it is leaving a mounted
file and if this is the case, has to close the file and to pop the
expired pNexusFunction structure from the stack. If we choose to
implement external linking on datasets too a similar scheme would have
to be implemented for NXopendata and NXclosedata.

### Actually Accessing The External File

This section is about schemes for actually opening an external file as
specified by a URL. Accessing an external NeXus file within the same
file system is the easiest case: just open the path! It becomes
moderatly more complex when accessing NeXus files which are available
through the http or ftp series of protocolls. In that case I suggest to
download such a file through a suitable library and access them on the
cache area. Such a copy and access method would also help minimise the
download of possibly large files as a cache lookup can implemented to
preceed an actual download. A good library to choose for http and ftp
style downloads might be [cURL](http://curl.haxx.se/).

The degree of implementation complexity increases when we wish to
support general URL schemes or wish to support files not in a supported
NeXus physical file format. In such cases a means would be needed to
dynamically add URL handlers to the NeXus-API.
