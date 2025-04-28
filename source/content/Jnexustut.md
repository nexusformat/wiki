---
title: Jnexustut
permalink: Jnexustut.html
layout: wiki
---
Jnexustut
=========

The NeXus for Java API Tutorial

This document explains in more detail how to program with the NeXus API
for Java. The intended audience are Java programmers who do not know the
C language NeXus API. This document will only explain how to deal with
NeXus files. For a general description of NeXus see the NeXus WWW-pages.
For reference,see the jnexus API documentation. Another good source of
information is the test driver source code for the NeXus API for Java.
It is a more involved example of API usage. And it is documented!

Before doing anything with the NeXus for Java API the necessary classes
need to be imported. This is done with the statement: import
neutron.nexus.\*; at the head of your Java file. A NeXus programmer has
to deal with the following five concepts:

NeXus Files

`   You should have guessed as much. `

Groups

`   Groups are NeXus means of structuring data in a file. Groups can hold other groups or datsets. The filesystem analogon to groups would be directories. `

SDS

`   SDS are scientific datasets. This is a n-dimensional array of numbers stored in the file. `

Attributes

`   Attributes is auxiliary information stored in the file. Two types of attributes are possible: global file wide attributes and attributes linked to a SDS. `

Links

`   For organisational reasons it might be useful to refer a SDS in more then one group. But it should be avoided to duplicate data. In order to avoid this it is possible to link SDS wherever you want. This concept is quite similar to a symbolic link in a unix file system. `

All these concepts will be explained in more detail below. A note about
error handling: A NexusException is thrown whenever an error occurs.
This implies that all code samples stated below should be included in a
try-catch block looking like this:

`   try{`  
`     // some NeXus for Java calls.`  
`   }catch(NexusException ne) {`  
`      // analyze and treat the error`  
`   }`

For brevity and clarity this will be left out in the following text.

NeXus Files

A Nexus File is opened by: NexusFile nf = new NexusFile(name,
NexusFile.NXACC\_CREATE); The first parameter to the constructor is of
course the name. The second parameter is the access code valid for the
file: Three access codes are supported:

NXACC\_CREATE

`   For creating a new NeXus file. `

NXACC\_RDWR

`   For opening an existing NeXus file for modification or for appending. `

NXACC\_READ

`   Open a file for reading only. `

Please note that for all further examples, the name nf is assumed for
the NexusFile object.

Closing files is accomplished through the finalize method. This should
be called automatically by the Java garbage collector but it is safer to
explicitly call this method when done with a file. nf.finalize() does
the trick.

Sometimes it is necessary to flush all buffered data to disk before
doing for instance something else in a program in order to prevent data
loss. This can be done with the flush method: nf.flush(); flush has the
side effect of closing all open SDS.

Groups

A group (or vGroup) is the NeXus equivalent of a directory. Alike to a
directory hierarchy, a hierarchy of groups can be built in a NeXus file.
In contrast to directory names however, NeXus group names consist of two
strings: the groupname and the groupclass. Both strings are needed in
order to address a NeXus group. There are API functions for all
necessary operations on groups. The first one is group creation:
nf.makegroup(name, nxclass); This corresponds to a mkdir in a unix
filesystem.

In order to use a group we need a means of traversing the group
hierarchy. For this the methods: nf.opengroup(name,nxclass); and
nf.closegroup(); are provided. opengroup corresponds to a cd name,class
and steps into the group name with class nxclass. closegroup corresponds
to cd .. and steps one group lower in the group hierarchy.

NeXus is self describing. Clearly a method is needed to find out about
the contents of the current group. For this the method: Hashtable ha =
nf.groupdir(); is used. The hashtable returned contains pairs of name,
class as entries. For datasets the class name is set to SDS. See the
following code snippet as an example how to print the contents of a
NeXus group:

`        Hashtable h = nf.groupdir();`  
`        e = h.keys();`  
`        System.out.println(`“`Found`` ``in`` ``Group`”`);`  
`        while(e.hasMoreElements())`  
`    {`  
`           vname = (String)e.nextElement();`  
`           vclass = (String)h.get(vname);`  
`           System.out.println("     Item: " + vname + " class: " + vclass);`  
`        }`

SDS SDS are scientific dataset. They are used to store n-dimensional
arrays of data in a variety of number types in a NeXus file. The
following number types are allowed in NeXus files:

`   NexusFile.NX_INT8:`  
`   NexusFile.NX_UINT8:`  
`       NexusFile.NX_CHAR:`  
`   NexusFile.NX_INT16:`  
`   NexusFile.NX_UINT16:`  
`   NexusFile.NX_INT32:`  
`   NexusFile.NX_UINT32:`  
`   NexusFile.NX_FLOAT32:`  
`   NexusFile.NX_FLOAT64:`

I think the names are self describing. These types are defined as
constants in NexusFile.java.

When creating a new file a means is needed for creating a new SDS in the
NeXus file. A SDS is fully characterized by its name, its number type
(out of the list above), the number of dimensions it has (its rank) and
its size in each dimension. With this information a SDS can be created:
nf.makedata(name,type,rank,iDim); with iDim being an integer array
holding the size of the dataset in each dimension. A speciality of NeXus
(and HDF) is that the first dimension can be unlimited. Simpy set the
dimension 0. Then data can be appended in consecutive steps along this
dimension. Please note, that makedata does not automatically open the
SDS. Before writing data to it, a call to opendata is required.

Analog to a file in a filesystem a SDS must be opened before anything
can be done with it and closed when processing is finished. The
appropriate calls are: nf.opendata(name); and nf.closedata(); Please
note that all methods below this section require an openend SDS for
proper operation.

Once a SDS is open data can be read or written to it. Two means of data
transfer are provided: putdata, getdata write and read all the data in
one go, whereas putslab, getslab allows to write and read subsets of
data. There is a trick here though. Java is meant to be type safe. One
would think then that a data transfer method would be required for each
Java data type. In order to avoid this the data to transfer is passed
into the data transfer methods as type Object. Then the API proceeds to
analyze this object through the Java introspection API and converts the
data to a byte stream for writing through the native method call. This
is an elegant solution with one drawback: An array is needed at all
times. Even if only a single data value is written (or read) an array of
length one and an appropriate type is the required argument.

Writing and reading then looks like:

`     // example data`  
`     int iData[][] = new iData[3][10];`  
`     // write it`  
`     nf.putdata(iData);`  
`     // read it`  
`     nf.getdata(iData);`

Another issue are strings. Strings are first class objects in Java. HDF
(and NeXus) sees them as dumb arrays of bytes. Thus strings have to be
converted to and from bytes when reading string data. See a writing
example:

`       String ame = `“`Alle`` ``meine`` ``Entchen`”`;`  
`   nf.makedata(`“`string_data`”`,NexusFile.NX_CHAR,1,`  
`                          ame.length()+2);`  
`       nf.opendata(`“`string_data`”`);`  
`       nf.putdata(ame.getBytes());`

And reading:

`       byte bData[] = new byte[132];`  
`       nf.opendata(`“`string_data`”`);`  
`       nf.getdata(bData);`  
`       String string_data = new String(bData);`

The aforementioned holds for all strings written as SDS content or as an
attribute. SDS or vGroup names do not need this treatment.

When writing a subset of data two more arguments are needed: The first
is an integer array of size rank which holds the address in the dataset
where to start the transfer of the subset. The second is another integer
array of size rank which determines the size of the data subset to
transfer in each dimension. The methods then look like:

`     // example data`  
`     int iData[][] = new iData[3][10];`  
`     int iStart[2] = {0,0};`  
`     int iSize[2] = {3,10};`  
`     // write it`  
`     nf.putslab(iStart, iSize,iData);`  
`     // read it`  
`     nf.getdata(iStart, iSize,iData);`

This example is a bit contrieved in that it uses the subset API for
transfering the whole dataset.

NeXus and HDF support the compression and decompression of data on the
fly during transfer operations. The only thing which needs to be done is
to tell NeXus to compress the data before writing data. An example looks
like this:

`     float fData[][] = new float[100][1000];`  
`     int iDim[] = new int[2];`  
`     iDim[0] = 100;`  
`     iDim[1] = 1000;`

`      nf.makedata(`“`fData`”`,2,NexusFile.NX_FLOAT32,iDim);`  
`      nf.opendata(`“`fData`”`);`  
`      nf.compress(NexusFile.COMP_CODE_LZW);`  
`      nf.putdata(fData);`

Please note the sequence of calls. The parameter to compress is the
compression algorithm to use. Permitted values are:

NexusFile.NX\_COMP\_NONE

`   No compression `

NexusFile.NX\_COMP\_RLE

`   Run length encoding `

NexusFile.NX\_COMP\_LZW

`   gzip type compression `

NexusFile.NX\_COMP\_HUF

`   Huffman compression. `

Please note that transfers to compressed datasets have to be done
through the putdata, getdata routines, subset operations are not
supported with compression.

When dealing with an unknown NeXus file we might need to find out about
the characteristics of a SDS. This can be done with:
nf.getinfo(iDim,args); After this call iDim will hold the size of the
SDS in each dimension, args\[0\] will be the rank of the SDS and
args\[1\] the number type. Make sure that iDim is large enough to hold
all dimensions. Hint: 32 is the maximum number of dimensions supported
by HDF.

Attributes Attributes are auxiliary information stored in a NeXus file.
There are two variants: global attributes at file level and attributes
at SDS level. The attribute part of the API acts on global attributes if
no SDS is open and on SDS attributes if an SDS has been opened with
opendata(). Attributes can be written: nf.putattr(name,data,type); name
is a name, data is a one dimensional array of some data and type is the
of the data. The same data types as for SDS writing are supported.

Attributes can be read: nf.getattr(name, data, args); args\[0\] will
hold the length of the attribute array, args\[1\] its type. This must be
supplied as input. Proper values for these parameters can be inquired
trough the attribute directory method: Hashtable ha = nf.attrdir(); This
time the hashtable ha will hold pairs of attribute names and
AttributeEntry objects. These objects are small classes which hold the
length and type of the attribute. See an attribute printing example for
more information:

`        AttributeEntry atten;`  
`        String attname;`

`        Hashtable h = nf.attrdir();`  
`        Enumeration e = h.keys();`  
`        while(e.hasMoreElements())`  
`    {`  
`          attname = (String)e.nextElement();`  
`          atten = (AttributeEntry)h.get(attname);`  
`          System.out.println("Found global attribute: " + attname +`  
`            " type: "+ atten.type + " ,length: " + atten.length); `  
`        }`

Linking Linking a SDS into more then one group requires some
precautions. First some internal information needed for linking must be
retrieved while the SDS ist still open. The call: NXlink nl =
nf.getdataID(); does just that. Then, after moving to the appropriate
place for the link in the group hierarchy the call: nf.makelink(nl);
will actually install the link.
