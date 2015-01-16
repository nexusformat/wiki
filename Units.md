---
title: Units
permalink: Units/
layout: wiki
---

Some miscellaneous Units proposals
----------------------------------

[Paul Kienzle](Paul_Kienzle "wikilink") will propose a more coherent
specification of data units. It will be a response to the following set
of proposals.

The units of any stored data or metadata should be specified as an
attribute, unless they are dimensionless. The following conventions
should be adopted:

-   All units are written in singular form, without abbreviation.
-   There will be no spaces in units.
-   SI units will be used (e.g., metre, kilogram, second, ampere,
    kelvin), using the British English spellings (e.g., “metre”, not
    “meter”), but “angstrom” and “barn” are also allowed.
-   More complex units will be written with mathematical operators
    (+,-,/,^) and parentheses, with traditional operator precedence
    (e.g.,metre/second)
-   Prefixes are allowed, but will be separated from the unit using the
    appropriate mathematical operator (e.g., centi\*metre).

Update 1/2015
-------------

This went nowhere. Units in NeXus still follow the scheme as described
in the manual.
