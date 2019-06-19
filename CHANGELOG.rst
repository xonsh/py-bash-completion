=============================
py-bash-completion Change Log
=============================

.. current developments

v0.2.6
====================

**Fixed:**

* Fix completion which uses a subshell environment
* Fix for string index error in stripped prefix



v0.2.5
====================

**Fixed:**

* bash_completions to include special characters in lprefix

  Previously, glob expansion characters would not be included in lprefix for replacement

  .. code-block:: sh

    $ touch /tmp/abc
    $ python
    >>> from bash_completion import bash_completions
    >>>
    >>> def get_completions(line):
    ...     split = line.split()
    ...     if len(split) > 1 and not line.endswith(' '):
    ...         prefix = split[-1]
    ...         begidx = len(line.rsplit(prefix)[0])
    ...     else:
    ...         prefix = ''
    ...         begidx = len(line)
    ...     endidx = len(line)
    ...     return bash_completions(prefix, line, begidx, endidx)
    ...
    >>> get_completions('ls /tmp/a*')
    ({'/tmp/abc '}, 0)

  Now, lprefix begins at the first special character:

  .. code-block:: sh

    $ python
    >>> from bash_completion import bash_completions
    >>>
    >>> def get_completions(line):
    ...     split = line.split()
    ...     if len(split) > 1 and not line.endswith(' '):
    ...         prefix = split[-1]
    ...         begidx = len(line.rsplit(prefix)[0])
    ...     else:
    ...         prefix = ''
    ...         begidx = len(line)
    ...     endidx = len(line)
    ...     return bash_completions(prefix, line, begidx, endidx)
    ...
    >>> get_completions('ls /tmp/a*')
    ({'/tmp/abc '}, 7)




v0.2.4
====================

**Fixed:**

* If there are no files to source, a ``set()`` will no longer be inserted
  into the completion script.




v0.2.3
====================

**Fixed:**

* Fixed issue with incorrect strip lengths for prefixes with quotes in them
* Fixed bash script to also consider leading double quotes and not just single
  quotes
* `bash_completion` will not return negative prefix lengths for files that need
  to be string-escaped (files/folders with spaces in name)




v0.2.2
====================

**Fixed:**

* Fixed issue with completing quotes and spaces.




v0.2.1
====================

**Fixed:**

* Fixed extra comma in rever hook.




v0.2.0
====================

**Added:**

* New command line interface.


**Fixed:**

* Fixed whitespace deduplication issue.




