---
title: NIACdoc
permalink: NIACdoc.html
layout: wiki
---
NIACdoc
=======

NIAC Decisions regarding Documentation
--------------------------------------

This section records NIAC decisions on the topic of NeXus documentation,
WWW-site and such.

NIAC 2003: Until an appropriate format can be determined, instrument
definitions and base classes will be stored in metaDTD format.

NIAC 2004: Decision to use NeXus meta-DTD instead of XML schema for base
classes and instrument definitions

NIAC 2005: The documenation will consist of five documents: 1. Technical
Reference - describes the metaDTD, base classes and definitions 2. NeXus
API Reference 3. User Reference 4. Plan to testing and releasing the
NeXus API 5. Example files and code

NIAC 2006: Move the entrire NeXus WWW-site to MediaWiki

NIAC 2006: move to nexusformat.org and a new WWW-service, abandon
european NeXus mirror at lns00.psi.ch and original site at Argonne.

NIAC 2007: Separate repository for base classes and definitions

NIAC 2007: Move to subversion from CVS

NIAC 2007: Move NeXus mailing lists from anl.gov to
lists.nexusformat.org

NIAC 2007HMI: Redirect WWW-server to nexusformat.org

NIAC 2007HMI: Move metaDTD to schema: NeXus 3.0 will be schema based

NIAC 2008: move to application rather then instrument definitions

NIAC 2008: docbook as the primary format for the NeXus manual.
Everything else to be generated from this master

NIAC 2008: wiki to be kept as discussion forum

NIAC 2008??: somewhere after NIAC 2008 the decision was taken to move to
NXDL and nxvalidate.

NIAC 2010: Documentation to go under the GNU FDL, example code under the
LGPL licence

NIAC 2012??: obviously we decided in some stage to provide the
documentation in Restructured Text and use sphinx for generating
documents. This, however, I either missed or was not properly recorded.

NIAC 2024:  [issue 1472](https://github.com/nexusformat/definitions/issues/1472>) was created in *definitions* repo to Harmonize the NeXus web pages so that the Wiki would look and feel like the [NeXus manual](https://manual.nexusformat.org/user_manual.html).
1. [Issue 11](https://github.com/nexusformat/wiki/issues/11) in the [wiki repository](https://github.com/nexusformat/wiki) was created to address this.
2. Wiki now built with sphinx.
3. Wiki documents will be kept as markdown files and sphinx will translate to html during build.
4. NeXus logos in wiki linked from [NIAC repository](https://github.com/nexusformat/NIAC)
