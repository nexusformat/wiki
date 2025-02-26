================
Group Attributes
================

### Group Attributes Implementation
At the last NIAC meeting we decided that group attributes shall be
implemented for NAPI-4.0. I now looked into this. As recent versions
of HDF4 now also support group attributes, the implementation is not a
big problem. However there is one issue: The most logical approach
would be to modify NXputattr, NXgetattr, NXgetnextattr etc. to do
group attributes. But this changes the way the NeXus-API works in a
subtle and incompatible way: Now the NeXus-API writes a file global
attribute when no dataset is open. After the change, file global
attributes would only be written at root level, else group attributes
would be written when no dataset is open. This can break older code.
Or we can keep the way the API works and introduce a new set of
functions for handling group attributes.

So we have two choices:

- Use the existing NX attribute functions and introduce a subtle version incompatibility

- Define new functions for group attributes. I am in favour of the first solution because it prevents API-bloat. But what does everyone else think? Mark Koennecke, January, 6, 2006 Decided: february, 3, 2006,we go with the incompatible change
