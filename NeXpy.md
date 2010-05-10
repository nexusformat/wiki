---
title: NeXpy
permalink: NeXpy/
layout: wiki
---

NeXpy provides a high-level Python interface to NeXus data contained
within a simple GUI. It is designed to provide an intuitive interactive
toolbox allowing users both to access existing NeXus files and to create
new NeXus-conforming data structures without expert knowledge of the
file format.

Installation
------------

NeXpy is in the early stages of development, and so there has been no
stable release yet. However, it is available for testing purposes only.
To check out the latest version from the
[Mercurial](http://mercurial.selenic.com/) repository and install the
NeXpy package to the standard Python site-packages directory,:

`> hg clone `[`http://mercurial.mcs.anl.gov/repos/nexpy`](http://mercurial.mcs.anl.gov/repos/nexpy)  
`> cd nexpy`  
`> python setup.py install`  
`> nexpy`  

This assumes that the standard Python script directory is in your
default path.

The source code can also be viewed on the [NeXpy Trac
Server](http://trac.mcs.anl.gov/projects/nexpy/).

GUI Shell
---------

![NeXpy|center|800px](Nexpy.png "fig:NeXpy|center|800px") There are a
number of useful features available when running NeXpy within the GUI
shell.

1.  Data can be loaded with the <File:Open> menu item using a standard
    file browser window.
2.  All current NeXus data trees are easy to inspect in the pane on the
    upper left side. Hovering over a data item produces a tooltip
    containing a list of all the item's children.
3.  The root level of all newly created groups are automatically
    displayed in the tree.
4.  Any changes to data sets in the scripting window will be reflected
    within the tree pane, including the creation of new NXroot, NXentry,
    or NXdata groups.
5.  NXdata and NXmonitor plots can be displayed by right-clicking and
    choosing 'Plot'.
6.  Axis limits are set by a series of slider bars.
7.  The scripting shell provides convenient autocompletion, and
    automatically displays function docstrings as a tooltip when you
    open the function parentheses.

### Planned Enhancements

-   Plotting projections along any axis by dragging and right-clicking
    the plots.
-   Editing data items in the tree within an editor pane.
-   Fitting data with predefined and user-supplied functions.
