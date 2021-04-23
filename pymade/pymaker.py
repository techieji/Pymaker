"Pymaker, the better `make`"
__version__ = '0.0.1'

from importlib import import_module
from inspect import signature
from pathlib import Path
from pymaker.settings import cli_args
import argparse
import os
import subprocess
import sys
import pickle

from doc import doc

@doc
def r(s):
    if type(s) is list:
        print("Pymaker: " + " ".join(s))
        return subprocess.call(s)
    else:
        print("Pymaker: " + s)
        return os.system(s)

@doc
class RecursiveDefinitionError(Exception):
    pass

@doc
def declare_argument(*args, **kwargs):
    cli_args.append((args, kwargs))

@doc
def command(command, deps):
    def dec(fn):
        fn.command = command if type(command) is str else fn.__name__
        fn.deps = deps
        fn.help = fn.__doc__
        if 'ns' in signature(fn).parameters:
            fn.needs_namespace = True
        else:
            fn.needs_namespace = False
        return fn
    if callable(command):
        return dec(command)
    else:
        return dec

@doc
def build_direc(filename):
    sys.path.insert(0, os.getcwd())
    module = import_module('.'.join(filename.split('.')[:-1]))
    return dict((fn.command, fn) for fn in module.__dict__.values() if callable(fn) and hasattr(fn, 'command'))

@doc
def call_command(command, direc, ns):
    fn = direc[command]
    if command in fn.deps:
        raise RecursiveDefinitionError(f"{fn.__name__}'s dependencies include {fn.__name__} itself.")
    for x in fn.deps:
        call_command(x, direc, ns)
    if fn.needs_namespace:
        fn(ns)
    else:
        fn()

@doc
def make_help_message(direc):
    result = f"The command to run from the Makefile. This can be one of these elements: {', '.join(direc.keys())}.\n"
    for x in direc.values():
        if x.help:
            result += ' - ' + f'{x.command}: {x.help}' + '\n'
    return result

@doc
def main(filename="Makefile.py"):
    direc = build_direc(filename)
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="Pymaker, the better `make`",
    )
    parser.add_argument(
        "command", 
        default=None, 
        choices=direc.keys(),
        help=make_help_message(direc)
    )
    for x, y in cli_args:
        parser.add_argument(*x, **y)
    args = parser.parse_args()
    call_command(args.command, direc, args)

if __name__ == '__main__':
    main()
