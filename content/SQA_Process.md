---
title: SQA Process
permalink: SQA_Process.html
layout: wiki
---

Context
-------

This process is a living document that is intended to change over time.
Rather than try to follow 'best practices' from the beginning it was
decided to document current practices and modify them over time as
deficiencies are found. To this point the testing suite will be the main
tool for maintaining quality of the releases and will have additional
tests added as new features are added and defects are corrected.

Roles
-----

Release manager: Person in charge of determining what features are to be included in a version and when a milestone should be closed.  
Quality manager: Oversees the addition of individual tests coordinates tests being executed with the appropriate configuration on the appropriate systems.  
Developer: Works on individual changes.  

Milestone Conventions
---------------------

For each versioned release of the code there will be two milestones: one
associated with feature enhancement, and one with fixing defects
introduced by the new features. The following milestone names are
examples where the release version is '4.0'

4.0 Ready: The next set of features are defined. Known defects can also be added to this milestone.  
4.0 Release: Any defects discovered while testing the '4.0 Ready' milestone.  

Code Versioning
---------------

### Numbering Scheme

Versions are generically labeled as `major`.`minor`.`patch`.

-   The major number changes with big feature changes. While they won't
    always break backwards compatibility there is no guarantee.
-   The minor number changes with minor feature changes and bug fix
    releases.
-   The patch number will not be changed and will always be at '0'.

### Branches and Tags

This discussion assumes that the version in progress is '4.0'.

-   Day-to-day changes will be made to the `trunk` of the repository
    during the 'Ready' phase of development.
-   Once all of the tickets associated with the 'Ready' phase are closed
    a branch will be created from the trunk. **this needs to be tested**

<!-- -->

    $svn cp -m "Creating 4.0 branch" https://svn.nexusformat.org/code/trunk https://svn.nexusformat.org/code/branches/4.0

-   This branch is then tagged to create the first release candidate
    distribution kit

<!-- -->

    $svn cp -m "Creating 4.0rc1 tag" https://svn.nexusformat.org/code/branches/4.0  https://svn.nexusformat.org/code/tags/4.0rc1

-   A distribution kit is then created from this tag and placed on the
    [NeXus download site](http://download.nexusformat.org/kits/) for
    testing. An [IssueReporting](IssueReporting.html "wikilink") version tag
    “4.0rc1” is also created for filing bug reports against. If you wish
    to check out this version from subversion the command is

<!-- -->

    $svn co https://svn.nexusformat.org/code/tags/4.0rc1 nexus-4.0rc1

-   The developer should work and put fixes for the 'Ready' stage back
    onto the 4.0 branch and NOT onto the 4.0rc1 tag. This branch is
    obtained via

<!-- -->

    svn co https://svn.nexusformat.org/code/branches/4.0 nexus-4.0-branch

or using the switch command on an existing checked out area

    svn switch https://svn.nexusformat.org/code/branches/4.0

-   Fixes to the 4.0 branch that are relevant to the trunk should be
    merged back into the trunk. To do this you run a command similar to
    the following from a checked out trunk working copy area

<!-- -->

    svn merge -r first:last https://svn.nexusformat.org/code/branches/4.0

where first and last are the revision numbers for the range of changes
to be merged from the 4.0 branch into the local working copy. If the
merge is OK, commit them to the trunk with

    svn commit -m "Merge in branch 4.0 changes from reviosions first to last"

-   If needed, 4.0rc2 etc. tags are created and kits released from the
    4.0 branch
-   Once all of the tickets in the 'Release' stage are completed the
    `branch` is tagged again for final release. Note that all changes to
    the branch should be merged back into the `trunk` by this time as
    well. **this needs to be tested**

<!-- -->

    $svn cp -m "Tagging 4.0 final release" https://svn.nexusformat.org/code/branches/4.0 https://svn.nexusformat.org/code/tags/4.0.0

Testing
-------

The principle of testing is that automated testing will be used to find
the majority of defects in the code. This decision was made based on the
fact that The NeXus code is developed almost exclusively by volunteer
work. All tests that are applicable to a particular configuration will
be run using

    $make check
    $make distcheck

The second command will only be run on appropriate systems.

As new tests are needed they will be added to the code in python, unless
another language is more appropriate. Results of tests will be recorded
on [NeXus 4 Testing](NeXus_4_Testing.html "wikilink")

### Supported Systems

**need to enumerate supported systems**

### List of tests

Running a *make check* runs the NeXus test suite (testsuit.at) from the
“tests” directory, which does the following:

-   It writes a file using the C API, reads it back in using the C API
    and then compares the result with known correct output. This is done
    for all the bindings (HDF4, HDF5, XML) that are available and also
    for both the static and shared version of the NeXus library
-   If the Fortran 77 and 90 APIs are avilable, a similar test to above
    is performed with these
-   The NeXus file converter is tested by running up to the complete 3x3
    possible conversions
-   The NXbrowse utility is tested by reading an example file and
    checking the output again a known correct listing. This is again
    done for HDF4, HDF5, XML.
-   A very basic test is performed on the NXdir utility
-   If it has been built, a very basic test is also perfomed on the
    NXsummary application
