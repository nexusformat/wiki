---
title: Object Oriented Interface
permalink: Object_Oriented_Interface.html
layout: wiki
---
Object Oriented Interface
=========================

For object oriented languages (C++, Java, and Python) it would be good
if there were a common object oriented way of working with NeXus files.
This page is set up for determining the public methods of a “NeXusFile”
object.

    class NeXusFile{
    public:
      enum access(READ=NXACC_READ, WRITE=NXACC_CREATE, WRITE_HDF4=NXACC_CREATE4, 
                          WRITE_HDF5=NXACC_CREATE5, READ_WRITE=NXACC_RDWR);
      enum compress(COMP_LZW=NX_COMP_LZW,COMP_HUF=NX_COMP_HUF,COMP_RLE=NX_COMP_RLE,COMP_NONE);

      // constructor, default mode is read
      NeXusFile(std::string &filename, const access mode=READ);

      // opens the specified absolute path in the file. the path is 
      // a '/' delimited list of the names to open. If any portion of 
      //the path does not exist an exception will be thrown.
      void openPath(const std::string &path);
      
      // creates and opens a group. this throws an exception when fails
      void make_group(const std::string &name, const std::string &class);

      // creates and opens a data. this throws an exception when fails
      void make_data(const std::string &name, const std::string &type, const std::vector<int> 
                               &dimensions, const compress comp_type=COMP_NONE);
    };

[Peter Peterson] (Pfpeterson.html "wikilink"), SNS

Conclusion
----------

01/2015 This is now obsolete. Implementations in C++ and python are
available.
