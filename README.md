# ARCHIVED

This package is no longer maintained as a standalone bash completion package.

For an up-to-date version of `bash_completion.py` you can visit https://github.com/xonsh/xonsh/blob/main/xonsh/completers/bash_completion.py


# py-bash-completion
A package that provides python interface for bash completion

## Usage example
In the simplest case, we can just complete from the end of the line using, `bash_complete_line()`:

``` python
from bash_completion import bash_complete_line

In [1]: bash_complete_line('git s', return_line=True)
Out[1]:
{'git shortlog',
'git show',
'git show-branch',
'git stage',
'git stash',
'git status',
'git submodule',
'git subtree'}
```


However, there is also a lower-level API that more closely matches the actual Bash completion
interface, for those who need it!

``` python
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
```


You may also use this as a simple command line utility:

``` sh
$ python -m bash_completion "ls --s"
ls --show-control-chars
ls --si
ls --size
ls --sort
ls --sort=
```

