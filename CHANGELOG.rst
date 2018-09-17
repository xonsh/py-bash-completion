=============================
py-bash-completion Change Log
=============================

.. current developments

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




