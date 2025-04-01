---
title: NXbrowse
permalink: NXbrowse.html
layout: wiki
---
NXbrowse
========

NXbrowse is a terminal browser that provides a simple command-line
interface to view the contents of NeXus files. Datasets within the NeXus
file can be dumped to an ASCII file.

If you have any questions/comments/bug reports email [Ray
Osborn](mailto:ROsborn@anl.gov).

Usage
-----

A simple terminal browser written in ISO C (replacing the earlier
version in Fortran 90). When compiled and linked with the NeXus API, it
can be run interactively to list the directories of each group within a
NeXus file. If used from a terminal (and installed in the default PATH
\[u\*\*x\] or defined as a symbol \[VMS\]), type

    nxbrowse <file_name>

If no file name is given, the user is prompted for the file to be
opened. NXbrowse then lists the global attributes and prompts for
further commands. The following commands may be given in upper or lower
case (although the group and data names are case sensitive) :

<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Command</p></th>
<th><p>Command Definition</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>dir</p></td>
<td><p>List the contents of the currently open group.</p></td>
</tr>
<tr class="even">
<td><p>open <group></p></td>
<td><p>Open the specified group.</p></td>
</tr>
<tr class="odd">
<td><p>read &lt;data[i,j,...]&gt;</p></td>
<td><p>Read the contents of the specified data set. If no array indices are specified, the first three elements of the data set are output along with all its attributes. If an array index is specified, only that element is output. Note that the order of the array indices follows the C-convention (the last index is the most-rapidly varying).</p></td>
</tr>
<tr class="even">
<td><p>dump <data> <file></p></td>
<td><p>Write the entire contents of the specified data set to the specified ASCII file.</p></td>
</tr>
<tr class="odd">
<td><p>byteaschar</p></td>
<td><p>Toggle the output format for NX_INT8 and NX_UINT8 variables. By default, they are output as integers, but after giving this command, they are printed as character strings.</p></td>
</tr>
<tr class="even">
<td><p>close</p></td>
<td><p>Close the currently open group. At the root level of the NeXus file, this command is ignored.</p></td>
</tr>
<tr class="odd">
<td><p>exit, quit</p></td>
<td><p>Exit the program.</p></td>
</tr>
<tr class="even">
<td><p>help</p></td>
<td><p>List the available commands.</p></td>
</tr>
</tbody>
</table>

Installation
------------

NXbrowse is now installed as part of the standard NeXus installation.
See the [NeXus Downloads section] (Application_Program_Interface.html#Downloads "wikilink") for more
details.

If you encounter any bugs, please report them using the 
[NeXus bugzilla] (Application_Program_Interface.html#Reporting_Bugs_in_the_NeXus_API "wikilink").
