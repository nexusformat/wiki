=====================
NeXus CIF Integration
=====================

NeXus CIF Integration
=====================

At August 22, 2013, some members of the NIAC will meet with representatives of the CIF community and the IUCR in order to discuss a possible merger or collaboration between NeXus and CIF. This wiki page is meant as a forum to discuss the NIAC's position towards this integration. The initial reaction was quite positive.

Some Issues and Differences
===========================

- NeXus addresses a far greater range of techniques and instrumentation than CIF does.

- NeXus is about hierarchical data storage and arrays.

- CIF so far prefers tables and ASCII.

- CIF (or Herbert) are very concerned about getting data out of files into relational databases. The NeXus position as of now is to store the necessary information in a NeXus file and have databases populated by external scanners. Thus, NeXus makes no assumptions about database structures.

- Both CIF and NeXus have dictionaries of documented names. In many cases, the dictionaries overlap.

- NeXus is based on HDF-5 and NXDL, CIF on the star ASCII file format and DDL as a dictionary description language. There are many versions of DDL.

- CIF's ASCII file format is hitting a limit when storing raw data from modern high-speed detectors. Or sometimes even when storing atom positions for huge protein structures.

- Herbert has demonstrated that it is possible to map CIF into NeXus. There are issues but no real showstoppers.

- DECTRIS is pushing the PX community towards HDF/NeXus through the use of NeXus as the format for the upcoming EIGER series of detectors.

Questions
=========

- How can CIF and NeXus interoperate and integrate?

- Is CIF ready to expand towards a more general data format?

- How are the NeXus and CIF dictionaries to be integrated? Or are they to be integrated?

- How will the new integrated file format be used? I assume for deposition of data with IUCR journals.

- What exactly is the interest of the CIF community to collaborate with NeXus?

- Which CIF concepts would need to be included into NeXus to make it work?

- How does CIF solve the issue: we provide for everything, but in most cases really need only 20-30 data items? This is the problem NeXus solves with application definitions.

The NIAC's Interest
===================

- NeXus has always tried to be inclusive: it is no use having a standard if everyone has their own one!

- Recognition by the IUCR would be a selling point for NeXus and helpful.

- Increased interoperability: Interoperability is the raison d'etre of NeXus.

- Ideal world: use CIF, HDF5, and NeXus tools on all files.

To Discuss
==========

- Anything to add to the statements above?

- NeXus tries to be inclusive: how far are we prepared to change? Presumably, this can only be answered after the meeting when we can see more clearly what the merger means. It is also crystal clear that any changes to NeXus for a CIF merger need proper process: discussion and voting.

CIF-NeXus Presentation
----------------------

The draft for the NeXus CIF presentation can be downloaded here: [CIFNeXus.pdf](pdfs/CIFNexus.pdf "wikilink"). May be we get a chance to discuss this on the next Telco. Details of how NeXus and CDF might be mapped are contained on the [ConcordanceDiscussion](ConcordanceDiscussion.html "wikilink") page.

Conclusion
----------

01/2015: A NXmx application definition has been designed together with COMCIFS. The application definition was tested at Diamond and it works. This NXmx application definition together with a few changes to NeXus to make it work were ratified at NIAC 2014.
