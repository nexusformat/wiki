---
title: SQA Process
permalink: SQA_Process/
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

This branch is then tagged to create the first beta distribution kit

    $svn cp -m "Creating 4.0beta1 tag" https://svn.nexusformat.org/code/branches/4.0  https://svn.nexusformat.org/code/tags/4.0beta1

A distribution kit is then created from this tag and placed on the nexus
web site for download and testing. A TRAC version tag “4.0beta1” is also
created for filinf bug reports against.

-   Fixes to defects found during the the 'Ready' stage are done in the
    `branch` and then merged back into the trunk. **this needs to be
    tested**

<!-- -->

    NEED TO DOCUMENT THE COMMAND

-   If needed, 4.0beta2 etc. tags are created and kits released

The developer can work on the 4.0 branch by checking it out directly
**this needs to be tested**

    svn co https://svn.nexusformat.org/code/branches/4.0 nexus-code-4.0branch

or using the switch command **this needs to be tested**

    svn switch https://svn.nexusformat.org/code/branches/4.0

-   Once all of the tickets in the 'Release' stage are completed the
    `branch` is tagged directly. Note that all changes to the branch
    should be merged back into the `trunk` by this time as well. **this
    needs to be tested**

<!-- -->

    $svn cp -m "Tagging 4.0" https://svn.nexusformat.org/code/branches/4.0 https://svn.nexusformat.org/code/tags/4.0.

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
another language is more appropriate.

### Supported Systems

**need to enumerate supported systems**

### List of tests

**Need to describe the tests run**
