import argparse
from importlib import import_module
import os
import subprocess
import sys

def r(s):
    if type(s) is list:
        print("Pymaker: " + " ".join(s))
        return subprocess.call(s)
    else:
        print("Pymaker: " + s)
        return os.system(s)

class RecursiveDefinitionError(Exception):
    pass

def command(command=None, deps=[]):
    def dec(fn):
        fn.command = command if type(command) is str else fn.__name__
        fn.deps = deps
        return fn
    if callable(command):
        return dec(command)
    else:
        return dec

def build_direc(filename):
    module = import_module('.'.join(filename.split('.')[:-1]))
    return dict((fn.command, fn) for fn in module.__dict__.values() if callable(fn) and hasattr(fn, 'command'))

def call_command(command, direc):
    fn = direc[command]
    if command in fn.deps:
        raise RecursiveDefinitionError(f"{fn.__name__}'s dependencies include {fn.__name__} itself.")
    for x in fn.deps:
        call_command(x, direc)
    fn()

def main():
    parser = argparse.ArgumentParser(description="Pymake, the better alternative to `make`")
    parser.add_argument("command", help="The command to run from the Makefile", default=None)
    parser.add_argument("-f", "--file", help="The makefile (default: Makefile.py)", default="Make.py")
    parser.add_argument("-t", "--targets", help="Display commands", action="store_true")
    args = parser.parse_args()
    direc = build_direc(args.file)
    if args.targets:
        print("\n".join(direc.keys()))
        sys.exit(0)
    call_command(args.command, direc)

if __name__ == '__main__':
    main()
