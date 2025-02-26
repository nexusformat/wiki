========================================================================
How to avoid name clashes during future extensions of the Nexus standard
========================================================================

The current standard allows users to use any name they want for fields and groups within base
classes. This can cause troubles for future extensions of the standard. Consider the simple case
where a user has chosen a name for a field within a base class which is not used by the current
standard. What will happen when the NIAC decides 3 years later that this name will be used for a
new standard field in the same base class. There are three possible approaches to avoid this
problem:

- every user defined field must start with a particular prefix
- use strong typing not only for groups but also for fields
- store all non-standard fields in an instance of NXcollection

Each of these approaches has its pros and cons which should be discussed in this article.
Question: I readily agree that there is a potential problem. But what does it tell us that we
needed 20 years to discover it? MK

Prefixes for user defined names
-------------------------------

The most obvious way would be to add a prefix to a field in order to distinguish standard- from
user-defined fields. For instance we could require users to prefix their own fields with `user__`
so a user defined angle would have a name like user__tth

Pros:
* easy to implement -- a paragraph in the documentation would suffice

Cons:
* it is virtually impossible to force users to stick to this convention
* every field name must be parsed before we can tell whether it is a standard or a user defined field
* users hardly ever read a manual that careful to recognize such a convention

Strong typing for fields
------------------------

A type could be added to each field by adding an attribute like *NX_class* for groups. Indeed we
could reuse *NX_class* for fields. Such an approach might makes names entirely arbitrary as we
search for fields by type rather than by name (as we are doing it for groups).

Pros:

Cons:
- We break heavily with NeXus: the dictionary is part of NeXus
- All searches would need to be for type. Types which are encoded in attributes. This becomes only practical with a special tool. Do we like special tools? Given our limited resources to maintain them?

Using of NXcollection
---------------------

The third approach is to make more extensive use of *NXcollection*. Every field or group which
is not defined by the standard will be stored in an instance of *NXcollection*.

Pros:
* like the prefix approach this is easy to do - just add a section in the documentation
* no need to invent new concepts as *NXcollection* already exists
* could use *NXcollection* as a kind of staging area for future class extensions

Cons:
* add an additional hierarchy to the Nexus tree
* need to define standard name for instances of *NXcollection* to avoid future name clashes with the collection instance itself
