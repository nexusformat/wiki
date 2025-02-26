==============
NXnet Proposal
==============

The motivation for NeXus is to allow the exchange of data between programs, instruments, establishments, and branches of
science where the neutron, muon, and X-ray technologies are the common theme. Recently, the NeXus community has been
greatly (and crucially) occupied with choosing what data to store in a file and how it should be described in a common
fashion. This proposal tackles a complementary facet of the broader problem: namely, the exchange of the data files
themselves between the programs, operating systems, instruments, and establishments.

Most scientists doing experiments on instruments at different establishments will have experienced the joy of trying to
copy data off a variety of different computer systems, often being forced to network a laptop machine at the last minute,
write a CD or floppy disk before racing to catch a flight, manually select and copy files one at a time via FTP, and/or
negotiate a firewall to get at their data. If very lucky, maybe they have been able to download data from a conveniently
set-up website, where remembering the password has been the only problem.

If this state of affairs wasn’t bad enough, there are things that are even harder to do than read your data. For example,
you might want to send a few calibration files and sample setup notes to a remote site ready for an experiment. This
would normally be seen as folly unless you have a trusted colleague already on-site to help you receive and look after
the files. And what if you’ve forgotten a file you needed on arrival? Wouldn’t it be nice if you could do a bit of data
reduction on-site and then continue at home, all the time saving the reduced files in the same directory as the raw data
(and with no need to copy the data locally)? And then permit a colleague to access a few of the files from their own
laptop while at home (by setting permissions like you do on a local Unix NFS file system or Windows share)?

There is really very little reason why we should accept such a desperate state of affairs. With the help of the UK’s
e-Science Centre, we have been experimenting with the San Diego Supercomputing Centre’s SRB (Storage Resource Broker)
for several months now. This provides, at a minimum, a very credible and functional globally distributable file system.

The proposal is in three parts:

1. **Adopt SRB for Experimentation**

We adopt SRB as a working system on which to experiment with building a global integrated network for sharing neutron,
 muon, and X-ray data between our establishments and our users. We do this pragmatically (like we have done with HDF)
 because it currently seems to do the job, and support is what standards like this need to develop.

2. **Standardize Data Organization and Location**

More fundamentally, we extend our remit of defining and organizing data types within the NeXus file to also giving
 some sort of standardization to the organization and location of data within a global file system. Quite simply, this
 just avoids things being lost by everyone storing things under different names and in different places (for example, a
 naming convention for raw files).

3. **Define Meta-Data for Enhanced Searchability**

Even more fundamentally, we spend some effort defining the sort of meta-data which we might associate with each file
 (possibly not contained in the NeXus file itself). This meta-data would enable a data-portal-style search engine, just
 like a super data-Google, to quickly find relevant data by searching throughout this global file system. Some of this
 sort of work is already underway, but some sort of standardization of the type and contents of this metadata is very
 close to the sort of standardization we are aiming at with the NeXus file contents and would greatly ease the ability
 to search and find relevant information.

The sheer usability of this particular system, especially for quite a young technology, is staggering. This is not
something to be planning for next year or the year after; it’s something to be using now—and then planning how to build
a data storage and access strategy around it.

NeXus has taken a long time to grow to the point where we are able to agree on the most difficult issue of what is
common within our data files. This is because it’s a really difficult job. Taking some responsibility for (2) and (3)
in particular is a lot less work but is something best tackled early.

Chris Moreton-Smith
