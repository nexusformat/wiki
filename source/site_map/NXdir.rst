NXdir
=====

NXdir is a console based tool that allows inspecting the contents of a NeXus file.
It allows for directory-like listing of contents as well as printing out data. If you
have any questions/comments/bug reports, email Peter Peterson <petersonpf@ornl.gov>.

News
----

- May 7, 2004: New version of NXdir is v0.2.5. This version now supports NX_INT8
  and NX_UINT8 as well as fixes some bugs with reading integers from a NeXus file.
- Apr 15, 2004: New version of NXdir is v0.2.4. The added feature is writing out
  an NXdata to file (1D and 2D only for now). Let me know if the format should be changed.
- Mar 17, 2004: New version of NXdir is v0.2.3. This version provides more consistency
  between absolute and relative paths. It also allows for anchoring the path at both ends
  using a /.
- Mar 01, 2004: First public release of NXdir is v0.2.2 with Linux binary here.

Usage
-----

NXdir runs on the command line with a variety of arguments. Below is the online help
information (note that defaults can be changed during compilation).

About NXdir
------------

- `-h` / `--help`
- `--version`
- Node Selection:
  - `-p`
- Output Control:
  - `-o/+o`
  - `-l` / `--max-array [value]`
  - `-t` / `--tree-mode`
  - `--path-mode`
  - `--data-mode`
  - `--printline`
  - `--write-data`

Some common usages are:

- Print the online help:

**nxdir --help**

- List everything at the root level of the file: `nxdir lrcs3000.nxs`

- Find the user names in all of the files in the directory:
  `nxdir *.nxs -p NXuser/name -o`

- Find all the data in a file: `nxdir NPDF_E2_R0003000.nx.hdf -p NXdata`

- Print out how the entire file is organized: `nxdir trics058582002.hdf -p "*"` (The asterisk is in quotes so it is not expanded by the shell)

Downloads
---------

- NXdir-v0.2.5.tar.gz

- NXdir-v0.2.4.tar.gz

- NXdir-v0.2.3.tar.gz

- NXdir-v0.2.2.tar.gz

- CHANGES

Prerequisites
-------------

- C++ compiler

- NeXus libraries or

- Precompiled binary

Installation
------------

Binary: Some binaries can be found above. Download, rename to something you will remember (like nxdir), and move into your path.

Unix/Linux/Irix/MacOSX: Unpack the tarball, enter the directory, and type `make`. Copy the resulting binary `nxdir` into your path.

Un-installing
-------------

Remove the file `nxdir`. The installation process did not modify the registry or other system settings in any way.

Frequently Asked Questions (FAQ)
--------------------------------

**What is NXdir?**

NXdir is a console tool used for inspecting the contents of a NeXus file. It can print out the organization of the file as well as any data enclosed. It is intended to be a cross between the Unix tools `ls` and `grep`. It should help people writing scripts access NeXus files without having to compile in the NeXus API.

**The way NXdir prints arrays is hard to read, could you please change it?**

No, but a format easier for you to read can be added. Please send an example of a two-dimensional array in a format you like.