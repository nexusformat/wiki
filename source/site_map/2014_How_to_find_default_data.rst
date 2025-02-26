=============================
2014 How to Find Default Data
=============================

*Written for [NIAC2014 Meeting](NIAC2014_Meeting.html "wikilink").*

One of the [motivations](https://manual.nexusformat.org/motivations.html) for NeXus is
[simple plotting](https://manual.nexusformat.org/motivations.html#simpleplotting). The [procedure to find the default
data to be plotted](https://manual.nexusformat.org/datarules.html#find-plottable-data) is convoluted. In some cases
(e.g., files with multiple NXentry and/or NXdata groups), it is not certain which data will be found.

This proposal introduces a new and simpler mechanism to manage (both set and determine) the path to the default data.
The intent is to preserve backward compatibility while making this mechanism the standard way for new data files to
identify the default data to be plotted.

Proposal
--------

It is proposed to add a deterministic method to identify the default data for visualization in a data file. This is
expected to become the preferred method moving forward:

- Add a **default_NXentry** attribute to the root of the file that specifies which NXentry is the default. The value is the name of the NXentry group.
- Add a **default_NXdata** attribute to each NXentry that specifies which NXdata is the default. The value is the name of the NXdata group.
- Add a **signal** attribute to each NXdata that specifies which dataset is the default. The value is the name of the dataset to be plotted.

These default attributes describe only child elements, not child/object, ../object, or other hierarchy. The procedure
to identify the default data to be plotted is straightforward: starting from any NeXus file, NXentry, or NXdata, follow
the chain as described.

Conclusion
----------

Ratified in a slightly modified form at NIAC 2014. See the `[NIAC 2014 Minutes] <../niac/NIAC2014_Meeting.html#minutes>`__.

### Summary of Modifications:

- Add a **default** attribute to the root of the file to specify which NXentry is the default. This resolves ambiguity when more than one NXentry exists. The value is the name of the NXentry group.
- Add a **default** attribute to each NXentry to specify which NXdata is the default. This resolves ambiguity when more than one NXdata exists. The value is the name of the NXdata group.
- Add a **signal** attribute to each NXdata to specify which dataset is the default. The value is the name of the dataset to be plotted.
