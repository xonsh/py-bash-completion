==================
py-bash-completion
==================
A package that provides python interface for bash completion

Usage example
*************
.. code-block:: python

    from bash_completion import bash_completions

    def get_completions(line):
        split = line.split()
        if len(split) > 1 and not line.endswith(' '):
            prefix = split[-1]
            begidx = len(line.rsplit(prefix)[0])
        else:
            prefix = ''
            begidx = len(line)

        endidx = len(line)
        return bash_completions(prefix, line, begidx, endidx)

    In [1]: get_completions('git s')
    Out[1]:
    ({'shortlog',
    'show',
    'show-branch',
    'stage',
    'stash',
    'status',
    'submodule',
    'subtree'},
    1)
