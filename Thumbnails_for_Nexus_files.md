---
title: Thumbnails for Nexus files
permalink: Thumbnails_for_Nexus_files/
layout: wiki
---

Thumbnails that a file browser (or even a web browser) can use to render
a Nexus file shall be stored in an instance of NXnote directly below
NXentry

    entry:NXentry
      thumbnail:NXnote
        data:NX_BINARY
        type:NX_CHAR
        description:NX_CHAR

The data field contains the binary data of the thumbail image. The image
type is determined by the type field. We currently recommend the image
to be stored as PNG. The description field can be used to store
provenance data which may show up as a tool-tip when the mouse pointer
hovers over the files icon.

Topics for discussion
---------------------

-   should it go to NXroot or NXentry?
-   restrict the image type to PNG or leave this open?
-   shall we restrict the size of the thumbnail image?

Windows for instance uses 96x96 jpeg images.
