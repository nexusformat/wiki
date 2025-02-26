=========
Jnexustut
=========

The NeXus for Java API Tutorial
--------------------------------

This document explains in more detail how to program with the NeXus API for Java. The intended audience are Java programmers who do not know the C language NeXus API. This document will only explain how to deal with NeXus files. For a general description of NeXus, see the NeXus WWW-pages. For reference, see the jnexus API documentation. Another good source of information is the test driver source code for the NeXus API for Java. It is a more involved example of API usage, and it is documented!

Before doing anything with the NeXus for Java API, the necessary classes need to be imported. This is done with the statement:

.. code-block:: java

    import neutron.nexus.*;

at the head of your Java file. A NeXus programmer has to deal with the following five concepts:

### NeXus Files

    You should have guessed as much.

### Groups

    Groups are NeXus means of structuring data in a file. Groups can hold other groups or datasets. The filesystem analog to groups would be directories.

### SDS

    SDS are scientific datasets. This is an n-dimensional array of numbers stored in the file.

### Attributes

    Attributes are auxiliary information stored in the file. Two types of attributes are possible: global file-wide attributes and attributes linked to an SDS.

### Links

    For organizational reasons, it might be useful to refer to an SDS in more than one group. To avoid duplicating data, it is possible to link an SDS wherever you want. This concept is quite similar to a symbolic link in a Unix file system.

All these concepts will be explained in more detail below. A note about error handling: a ``NexusException`` is thrown whenever an error occurs. This implies that all code samples stated below should be included in a ``try-catch`` block, as shown here:

.. code-block:: java

    try {
        // some NeXus for Java calls.
    } catch (NexusException ne) {
        // analyze and treat the error
    }

For brevity and clarity, this will be left out in the following text.

### NeXus Files

A NeXus file is opened by:

.. code-block:: java

    NexusFile nf = new NexusFile(name, NexusFile.NXACC_CREATE);

The first parameter to the constructor is, of course, the file name. The second parameter is the access code valid for the file. Three access codes are supported:

- **NXACC_CREATE**: For creating a new NeXus file.
- **NXACC_RDWR**: For opening an existing NeXus file for modification or for appending.
- **NXACC_READ**: Open a file for reading only.

Please note that for all further examples, the name ``nf`` is assumed for the ``NexusFile`` object.

Closing files is accomplished through the ``finalize`` method. This should be called automatically by the Java garbage collector, but it is safer to explicitly call this method when done with a file:

.. code-block:: java

    nf.finalize();

Sometimes it is necessary to flush all buffered data to disk before doing, for instance, something else in a program to prevent data loss. This can be done with the ``flush`` method:

.. code-block:: java

    nf.flush();

``flush`` has the side effect of closing all open SDS.

### Groups

A group (or vGroup) is the NeXus equivalent of a directory. Like a directory hierarchy, a hierarchy of groups can be built in a NeXus file. Unlike directory names, NeXus group names consist of two strings: the ``groupname`` and the ``groupclass``. Both strings are needed to address a NeXus group.

The API provides functions for all necessary operations on groups. The first is group creation:

.. code-block:: java

    nf.makegroup(name, nxclass);

This corresponds to a ``mkdir`` in a Unix filesystem.

To use a group, we need a means of traversing the group hierarchy. For this, the methods:

.. code-block:: java

    nf.opengroup(name, nxclass);
    nf.closegroup();

are provided. ``opengroup`` corresponds to a ``cd name,class`` and steps into the group ``name`` with class ``nxclass``. ``closegroup`` corresponds to ``cd ..`` and steps one group lower in the group hierarchy.

NeXus is self-describing. A method is needed to find out about the contents of the current group:

.. code-block:: java

    Hashtable ha = nf.groupdir();

The ``Hashtable`` returned contains pairs of ``name, class`` as entries. For datasets, the class name is set to ``SDS``. See the following code snippet as an example of how to print the contents of a NeXus group:

.. code-block:: java

    Hashtable h = nf.groupdir();
    Enumeration e = h.keys();
    System.out.println("Found in Group");
    while (e.hasMoreElements()) {
        String vname = (String) e.nextElement();
        String vclass = (String) h.get(vname);
        System.out.println("Item: " + vname + " class: " + vclass);
    }

### SDS

SDS are scientific datasets used to store n-dimensional arrays of data in various number types in a NeXus file. The following number types are allowed in NeXus files:

- **NexusFile.NX_INT8**
- **NexusFile.NX_UINT8**
- **NexusFile.NX_CHAR**
- **NexusFile.NX_INT16**
- **NexusFile.NX_UINT16**
- **NexusFile.NX_INT32**
- **NexusFile.NX_UINT32**
- **NexusFile.NX_FLOAT32**
- **NexusFile.NX_FLOAT64**

These types are defined as constants in ``NexusFile.java``.

When creating a new file, a means is needed for creating a new SDS in the NeXus file. An SDS is fully characterized by its name, its number type (from the list above), the number of dimensions it has (its rank), and its size in each dimension. With this information, an SDS can be created:

.. code-block:: java

    nf.makedata(name, type, rank, iDim);

Here, ``iDim`` is an integer array holding the size of the dataset in each dimension. A specialty of NeXus (and HDF) is that the first dimension can be unlimited. Simply set the dimension to 0. Data can then be appended in consecutive steps along this dimension. Please note that ``makedata`` does not automatically open the SDS. Before writing data to it, a call to ``opendata`` is required.

To write and read SDS data, methods such as ``putdata`` and ``getdata`` are used. Here is an example:

.. code-block:: java

    // Example data
    int iData[][] = new int[3][10];

    // Write it
    nf.putdata(iData);

    // Read it
    nf.getdata(iData);

The handling of strings and subsets, compression options, and other specific operations on SDS are described similarly.

### Attributes

Attributes are auxiliary information stored in a NeXus file. They can be global (file-level) or specific to an SDS. Attributes are managed with methods like ``putattr``, ``getattr``, and ``attrdir``. Examples for writing and reading attributes are:

.. code-block:: java

    // Writing an attribute
    nf.putattr(name, data, type);

    // Reading an attribute
    nf.getattr(name, data, args);

### Linking

Linking an SDS into more than one group requires some precautions. First, internal information needed for linking must be retrieved while the SDS is still open:

.. code-block:: java

    NXlink nl = nf.getdataID();

Then, after navigating to the appropriate place for the link in the group hierarchy, the link can be created:

.. code-block:: java

    nf.makelink(nl);

This covers the core aspects of using the NeXus API for Java.
