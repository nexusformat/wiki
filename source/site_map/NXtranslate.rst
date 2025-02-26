===========
NXtranslate
===========

NNXtranslate - the anything to NeXus converter
----------------------------------------------

NXtranslate is an extensible console-based tool that allows creating
NeXus files from information stored in other places. The program works
by parsing a translation file, which describes the structure of the
resulting file, and libraries that understand different file formats,
databases, etc., to retrieve information and put it into the resulting
NeXus file. NXtranslate was designed with "plugins" in mind to read from
new formats as needed.

If you have any questions/comments/bug reports, email Peter Peterson
<petersonpf@ornl.gov>. Also, email if you want to be notified of
test (alpha/beta) releases.

**News:**
October 1, 2004: The NXtranslate web page is published. The current version of NXtranslate is v0.1.1.
v0.2.0 is in progress and can be obtained by emailing <petersonpf@ornl.gov>.

**Downloads:**
Source: The manual `NXtranslate.pdf`

- `NXtranslate-v0.1.1.tar.gz`
- `NXtranslate-v0.1.0.tar.gz`

**Prerequisites:**
- C++ compiler
- NeXus libraries

**Installation:**
*Unix/Linux/Irix/MacOSX:*
Unpack the tarball, enter the directory, and type:

.. code-block:: bash

   ./configure;make;make test;make install
    make;make test;make install.


The resulting binary, nxtranslate, will be in /usr/local/bin/.

**Un-installing:**

Remove the file nxtranslate.

The installation process did not modify the registry or other system
settings in any way. *' Frequently Asked Questions (FAQ)*'

Q: What do you mean by “anything to NeXus”?

A: Because NXtranslate is extensible it can get information from more
places as new retrievers are written. Since there is no inherent
limitation on what retrievers are written, the information can be from
anything.
