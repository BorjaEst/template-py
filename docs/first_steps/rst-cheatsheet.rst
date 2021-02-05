.. role:: small

ReStructuredText Cheatsheet
==============================

Highlights
-------------------------------

- *emphasis*
- **strong emphasis**
- `interpreted text`
- ``inline literals``


Links
-------------------------------

- standalone hyperlinks (http://www.python.org)
- external hyperlinks (Python_)
- internal cross-references (example_)
- footnote references ([1]_)
- citation references ([CIT2002]_)
- `inline internal target`_

.. _Python: http://www.python.org
.. _example:


References
------------------------------

- This is the target of an _`inline internal target`.

.. [CIT2002] Just like a footnote, except the label is textual.
.. [1] A footnote contains body elements, consistently indented by at least 3 spaces.


Lists
-------------------------------

- This is a bullet list.
- Bullets can be "*", "+", or "-".

1. This is an enumerated list.
2. Enumerators may be arabic numbers, letters, or roman
   numerals.

:what: Field lists map field names to field bodies, like
       database records.  They are often part of an extension
       syntax.
:how: The field marker is a colon, the field name, and a
      colon.

      The field body may contain one or more body elements,
      indented relative to the field marker.


Command line options
-------------------------------

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            DOS/VMS-style options too


Literal blocks
-------------------------------

Literal blocks are either indented or line-prefix-quoted blocks,
and indicated with a double-colon ("::") at the end of the
preceding paragraph (right here -->)::

    if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None




Block quotes
-------------------------------

Block quotes consist of indented body elements:

    This theory, that is mine, is mine.

    -- Anne Elk (Miss)


Doctest blocks
-------------------------------

>>> print 'Python-specific usage examples; begun with ">>>"'
Python-specific usage examples; begun with ">>>"
>>> print '(cut and pasted from interactive Python sessions)'
(cut and pasted from interactive Python sessions)


Two syntaxes for tables
-------------------------------

Grid tables; complete, but complex and verbose:

+------------------------+------------+----------+
| Header row, column 1   | Header 2   | Header 3 |
+========================+============+==========+
| body row 1, column 1   | column 2   | column 3 |
+------------------------+------------+----------+
| body row 2             | Cells may span        |
+------------------------+-----------------------+

Simple tables; easy and compact, but limited:

====================  ==========  ==========
Header row, column 1  Header 2    Header 3
====================  ==========  ==========
body row 1, column 1  column 2    column 3
body row 2            Cells may span columns
====================  ======================


