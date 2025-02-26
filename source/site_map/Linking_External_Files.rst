======================
Linking External Files
======================

This discussion is on how to access external files from within a given NeXus
files. This defeats one guiding principle of NeXus: to have everything
in one file, somewhat. However, having everything in one file can mean
replicating large time-of-flight empty can or vanadium datasets in each
data file. In such cases it would be nice to access transparently an
external file holding such data. This page discusses some of the
implementation issues of such a scheme.

**Storing External File Information Somehow**

the information that an external file has to be
accessed must be stored within the parent NeXus file. Given the feature
set of NeXus, I suggest storing this information as an attribute of a
NeXus object. It would be sensible to restrict this attribute to NeXus
groups only. As the name of the attribute, I suggest \**mount*\*
following the example of HDF-5. The data content of this attribute
should be a URL pointing to the requested file. This not only follows
the fashion of the day but also gives a lot of freedom to implement
various file access strategies and even file formats. As it might be
necessary to specify alternative locations for a given external file, I
suggest allowing multiple URLs separated by :: It must be :: because a
single colon can be part of a valid URL.

**Implementing External File**

Access At The NAPI Level Various issues have to be addressed when
implementing external file access. The most important one is how to
transparently navigate the file hierarchy resulting from external
linking. In order to handle this, I suggest changing NXhandle. Currently
NXhandle maps to a pNexusFunction structure. Navigating the file
hierarchy becomes possible when NXhandle is modified to become a stack
of pNexusFunction structures. All functions in napi.c would need to be
changed to access the bottom element of this stack. NXopengroup would
then be modified to check for the mount attribute. If the mount
attribute is found, NXopengroup would open the file specified in the URL
and push the new pNexusFunction onto the stack. Likewise NXclosegroup
has to check if it is leaving a mounted file and if this is the case,
has to close the file and to pop the expired pNexusFunction structure
from the stack. If we choose to implement external linking on datasets
too a similar scheme would have to be implemented for NXopendata and
NXclosedata.

**Actually Accessing The External File**

This section is about schemes for actually opening an external file as specified by a
URL. Accessing an external NeXus file within the same file system is the
easiest case: just open the path! It becomes moderately more complex
when accessing NeXus files which are available through the http or ftp
series of protocols. In that case, I suggest downloading such a file
through a suitable library and accessing it in the cache area. Such a
copy and access method would also help minimise the download of possibly
large files as a cache lookup can be implemented to precede an actual
download. A good library to choose for http and ftp style downloads
might be cURL. A drawback of such a solution (or any general URL
solution) is that another meta data API would be required in order to
keep such information as usernames, passwords and possibly proxy
servers. The degree of implementation complexity increases when we wish
to support general URL schemes or wish to support files not in a
supported NeXus physical file format. In such cases, a means would be
needed to dynamically add URL handlers to the NeXus-API. However, if we
restrict ourselves to the copy, cache and access scheme outlined above,
another easily implemented option is to call external utility programs
for downloading files into the cache. This solution will appeal to the
unix crowd (including the Macs who are also unix), but might leave the
utility deprived Windows users in a tight spot. The most ambitious
implementation would be to allow loading both file format and URL
handlers dynamically into the NeXus-API. Both are possible but will
cause stability and maintainance problems due to the reliance on many
shared libraries. ### Summary And Open Issues Summing it up,
implementing external linking is definitely possible and implementable
within a reasonable amount of time. Group attributes would have to be
implemented first though. Open questions include:

- Do we restrict external linking to groups?

- Is the suggested path to an implementation acceptable? There might be others.

- Which level do we implement?

- Local NeXus files only?

- Download, cache, access through a library included with the NeXus-API? Which library then?

- cURL?

- Download and cache delegated to external programs?

- Dynamically loadable URL Handlers?

- Dynamically loadable physical file format handlers?

- Your question here! My two cents worth of opinion: shared libraries always
    annoy me, I like big statically built things, especially as disk space
    is cheap these days. I would implement a local disk access version first
    in order to get the mechanics right, followed by a version implementing
    the download, cache and access NeXus files scheme using cURL. Both
    versions would restrict external linking to groups.

Decisions NIAC 2006, ILL, February 2006
---------------------------------------

- mount becomes napimount

- NXinquirefile, which file we are actually

- nxdir expanded to print and copy dependencies

- Files are searched in NX\\_LOAD\\_PATH

- getenv becomes napigetenv in order to address platform problems with getenv

- External linking will only implement local linking first.

- If network linking is implemented, the use of libcurl is preferred.

- network linking is deferred, may be indefinitly
