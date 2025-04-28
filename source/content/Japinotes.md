---
title: Japinotes
permalink: Japinotes.html
layout: wiki
---
Japi notes
==========

The NeXus API for Java
======================

Introduction
------------

NeXus is a proposal for a common file format for neutron and X-ray
scattering. NeXus uses HDF as its physical file format. At the last
NOBUGS conference a strong need for a Java-API to NeXus files was
expressed. Version 1.0 of this Java API has now (October 2000) become
available. As recoding the HDF library in Java was no option the Java
API for NeXus (jnexus) was implemented through the Java Native Methods
Interface (JNI). This has the consequence that the Java API for NeXus
cannot be used in applets as the security restrictions for applets
prohibit downloading of shared libraries and local file access. Applets
can use a NeXus Data Server in order to access NeXus files in readonly
mode.

Acknowledgement
---------------

This implementation uses classes and native methods from NCSA's Java HDF
Interface project. Basically all conversions from native types to Java
types is done through code from the NCSA HDF group. Without this code
the implementation of this API would have taken much longer. See NCSA's
copyright for more information.

Installation
------------

### Requirements

For the binary distribution only a JDK1.1 compatible Java runtime is
required. Suitable runtime environments for Solaris, Linux and Windows32
can be downloaded from Sun's Java homepage. This website also holds
pointers to Java runtime systems for other platforms. Jnexus has not
been tested with Java 2 but should work with it.

In order to compile the Java API for NeXus the following components are
required:

-   A Java Development Kit 1.1 or better. For downloads see above.
-   A C compiler for your platform.
-   The HDF libraries version 4.1r3 or better. Can be downloaded from
    NCSA's HDF homepage.
-   A complete copy of the latest NAPI sources (including jnexus
    sources).

### Installation under Windows32 (Windows NT, Windows 95, 98, ME)

1.  Copy the HDF DLL's (\*413m.dll) and the file jnexus.dll to a
    directory in your path. For instance C:\\Windows\\system32.
2.  Copy the jnexus.jar to the place where you usually keep library jar
    files.

### Installation under Unix

Two files are needed: the jnexus.so shared library and the jnexus.jar
file holding the required Java class. Copy them wherever you like and
see below for instructions how to run programs using jnexus.

Running Programs with the NeXus API for Java
--------------------------------------------

In order to successfully run a program with jnexus the Java runtime
systems needs to locate two items:

-   The shared library implementing the native methods.
-   The nexus.jar file in order to find the Java classes.

### Locating the shared library

Of course the method for locating a shared library differ between
systems. Under Windows32 systems the best method is to copy the
jnexus.dll and the HDF-libarary DLL's into a directory in your path. The
HDF DLL's have to go there anyway.

On a unix system the problem can be solved in three different ways:

-   Make your system administrator copy the jnexus.so file into the
    systems default shared library directory (usually /usr/sbin).
-   Put the jnexus.so file wherever you see fit and set the
    LD\_LIBRARY\_PATH environment variable to point to the directory of
    your choice.
-   Specify the full pathname of the jnexus shared library on the java
    command line with the
    -Dneutron.nexus.JNEXUSLIB=full-path-2-shared-library option.

### Locating jnexus.jar

This is easier: just add the the full pathname to jnexus.jar to the
classpath when starting java. Examples

A unix example shell script:

`#!/sbin/sh`  
`java -classpath /usr/lib/classes.zip:../jnexus.jar:. \`  
`   -Dneutron.nexus.JNEXUSLIB=../bin/du40/libjnexus.so TestJapi`  

A Windows 32 example batch file:

`set JL=-Dneutron.nexus.JNEXUSLIB=..\jnexus\bin\win32\jnexus.dll`  
`java -classpath C:\jdk1.1.5\lib\classes.zip;..\jnexus.jar;. %JL% TestJapi`

Programming with the NeXus API for Java.
----------------------------------------

note: for experienced NeXus API Programmers!

The NeXus C-API is good enough but for Java a few adaptions of the API
have been made in order to match the API better to the idioms used by
Java programmers. In order to understand the Java -API it is useful to
study the NeXus C-API because many methods work in the same way as their
C equivalents. A full API documentation is available in Java
documentation format. For full reference look especially at:

-   The interface NeXusFileInterface first. It gives an uncluttered view
    of the API.
-   The implementation NexusFile which gives more details about
    constructors and constants. However this documentation is
    interspersed with information about native methods which should not
    be called by an application programmer as they are not part of the
    standard and might change in future.

Some more general explanation will be given below.

### General Things

See the following code example for opening a file, opening a vGroup and
closing the file again in order to get a feeling for the API.

`    try{`  
`          NexusFile nf = new NexusFile(filename,`  
`                   NexusFile.NXACC_READ);`  
`          nf.opengroup(`“`entry1`”`,`“`NXentry`”`);`  
`          nf.finalize();`  
`    }catch(NexusException ne) {`  
`        // Something was wrong!`  
`    }`

Some notes on this little example:

-   Each NeXus file is represented by a NexusFile object which is
    created through the constructor.
-   The NexusFile object takes care of all file handles for you. So
    there is no need to pass in a handle anymore to each method as in
    the C language API.
-   All error handling is done through the Java exception handling
    mechanism. This saves all the code checking return values in the C
    language API. Most API functions return void.
-   Closing files is tricky. The Java garbage collector is supposed to
    call the finalize method for each object it decides to delete. In
    order to enable this mechanism, the NXclose function was replaced by
    the finalize method. In practice it seems not to be guranteed that
    the garbage collector calls the finalize method. It is safer to call
    finalize yourself in order to properly close a file. Multiple calls
    to the finalize method for the same object are safe and do no harm.

Data Writing and Reading
------------------------

Again a code sample which shows how this looks like:

`       int idata[][] = new idata[10][20];`  
`       int iDim[] = new int[2];`  
`       `  
`       // put some data into iData.......`  
`       `  
`       // write iData`  
`       iDim[0] = 10;`  
`       iDim[1] = 20;`  
`       nf.makedata(`“`idata`”`,NexusFile.NX_INT32,2,iDim);`  
`       nf.opendata(`“`idata`”`);`  
`       nf.putdata(idata);`  
`       `  
`       // read idata`  
`       nf.getdata(idata);`

The dataset is created as usual with makedata and opened with putdata.
The trick is in putdata. Java is meant to be type safe. One would think
then that a putdata method would be required for each Java data type. In
order to avoid this the data to write is passed into putdata as type
Object. Then the API proceeds to analyze this object through the Java
introspection API and convert the data to a byte stream for writing
through the native method call. This is an elegant solution with one
drawback: An array is needed at all times. Even if only a single data
value is written (or read) an array of length one and an appropriate
type is the required argument.

Another issue are strings. Strings are first class objects in Java. HDF
(and NeXus) sees them as dumb arrays of bytes. Thus strings have to be
converted to and from bytes when reading string data. See a writing
example:

`       String ame = `“`Alle`` ``meine`` ``Entchen`”`;`  
`       nf.makedata(`“`string_data`”`,NexusFile.NX_CHAR,`  
`               1,ame.length()+2);`  
`       nf.opendata(`“`string_data`”`);`  
`       nf.putdata(ame.getBytes());`

And reading:

`       byte bData[] = new byte[132];`  
`       nf.opendata(`“`string_data`”`);`  
`       nf.getdata(bData);`  
`       String string_data = new String(bData);`

The aforementioned holds for all strings written as SDS content or as an
attribute. SDS or vGroup names do not need this treatment.

### Inquiry Routines

Let us compare the C-API and Java-API signatures of the getinfo routine
or method:

`     /* C -API */`  
`     NXstatus NXgetinfo(NXhandle handle, int *rank, int iDim[], `  
`                        int *datatype);`  
`     // Java `  
`     void getinfo(int iDim[], int args[]);`

The problem is that Java passes arguments only by value, which means
they cannot be modified by the method. Only array arguments can be
modified. Thus args in the getinfo method holds the rank and datatype
information passed in separate items in the C-API version. For resolving
which one is which consult a debugger or the API-reference.

The attribute and vGroup search routines have been simplified using
Hashtables. The Hastable returned by groupdir() holds the name of the
item as a key and the classname or the string SDS as ths stored object
for the key. Thus the code for a vGroup search looks like this:

`        nf.opengroup(group,nxclass);`  
`        h = nf.groupdir();`  
`        e = h.keys();`  
`        System.out.println(`“`Found`` ``in`` ``vGroup`` ``entry:`”`);`  
`        while(e.hasMoreElements())`  
`        {`  
`           vname = (String)e.nextElement();`  
`           vclass = (String)h.get(vname);`  
`           System.out.println("     Item: " + vname + " class: " + vclass);`  
`        }`

For an attribute search both at global or SDS level the returned
Hashtable will hold the name as the key and a little class holding the
type and size information as value. Thus an attribute search looks like
this in the Java-API:

`        Hashtable h = nf.attrdir();`  
`        Enumeration e = h.keys();`  
`        while(e.hasMoreElements())`  
`        {`  
`          attname = (String)e.nextElement();`  
`          atten = (AttributeEntry)h.get(attname);`  
`          System.out.println("Found global attribute: " + attname +`  
`            " type: "+ atten.type + " ,length: " + atten.length); `  
`        }`

For more information about the usage of the API routines see the
reference or the NeXus C-API reference pages. Another good source of
information is the source code of the test program which exercises each
API routine. Limitations

Known Problems
--------------

These are a couple of known problems which you might run into:

Memory: As the Java API for NeXus has to convert between native and Java number types a copy of the data must be made in the process. This means that if you want to read or write 20MB of data your memory requirement will be 40MB! This can be reduced by using getslab/putslab for data transfers.  
Java.lang.OutOfMemoryException: By default the Java runtime has a ceiling of 16MB of memory use. This ceiling can be increased through the -mxXXm option to the Java runtime. An example: java -mx32m ..... starts the Java runtime with a memory ceiling of 32MB.  
DigitalUnix4.0D and LZW compression: An error occurs in the HDF library when trying to compress a dataset with COMP\_CODE\_LZW. This works just fine on other platforms and also when using the NeXus C language API. The reason for this is still an area for research.  
Maximum 8192 files open: The NeXus API for Java has a fixed buffer for file handles which allows only 8192 NeXus files to be open at the same time. If you ever hit this limit, increase the MAXHANDLE define in native/handle.h and recompile everything.  

Compiling the Java API for NeXus
--------------------------------

You will need a complete copy of the latest NAPI sources (including
jnexus sources). See other requirements under installation above.

For Windows32 a Microsoft Visual C++ 6.0 project file is supplied in the
jnexus/jnexus directory. Use this project file. You will need to adapt
the directory settings under Tools/Options/Directories for both include
and library directories in order to reflect the placement of the HDF
libraries and the jnexus source code in your directory hierarchy.
Hitting F7 after that should build the shared library. Hint: Only a
release build is possible with the HDF library binaries. If a debug
build is needed you have to recompile the HDF libraries yourself. For a
recompilation of the Java classes use the compilejava batch file in the
jnexus main directory.

For DigitalUnix4.0D and Redhat Linux 6.2 Makefiles are provided
(Makefile and Make.tux repectively). For these systems everything can be
build with make du40 of make -f make.tux respectively. If the Makefiles
do not work edit the directory paths in the configuration section to
match your installation. If you wish to compile on another unix system,
create a copy of one of the above mentioned Makefiles and edit the
configuration section in your copy to match your installation of java
and the HDF libraries. If you succeed in building the NeXus API for Java
on a new system, please put back modified sources into the CVS
repository and make your Makefile and the compiled shared library
available to the NAPI team in order to provide a new binary
distribution. Support

Author
------

I'm sure this software contains swarms of bugs. If you manage to find
one you may send requests either to the NAPI developer mailing list or
to Mark Könnecke who wrote the Java API for NeXus.

Author: Mark Könnecke Laboratory for Neutron Scattering Paul Scherrer
Institut CH-5232-Villigen-PSI Switzerland and the NeXus Design team.
Last Update: October, 19, 2000
