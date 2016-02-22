# range-glob
Produce glob patterns for numeric ranges

Usage
-----
::

    from range_glob import glob_for_range

    glob_for_range(12, 34)

generates
::

    "{1[2-9],2[0-9],3[0-4]}"


Based on: https://github.com/dimka665/range-regex