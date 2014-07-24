---
title: How to avoid name clashes during future extensions of the Nexus standard
permalink: How_to_avoid_name_clashes_during_future_extensions_of_the_Nexus_standard/
layout: wiki
---

The Problem
===========

The current standard allows users to use any name they want for fields
and groups within base classes. This can cause troubles for future
extensions of the standard. Consider the simple case where a user has
chosen a name for a field within a base class which is not used by the
current standard. What will happen when the NIAC decides 3 years later
that this name will be used for a new standard field in the same base
class. This is in particular problematic if the new field has an
entirely different semantics as the one the user had in mind when he
created its own field.

There are three possible approaches to avoid this problem

-   every user defined field must start with a particular prefix
-   use strong typing not only for groups but also for fields
-   store all non-standard fields in an instance of NXcollection

Each of these approaches has its pros and cons which should be discussed
in this article.
