==========
Quickstart
==========


Pymaker is a very simple tool to learn; as of now, it only
has three functions you can possibly use! Learning it is very
easy.

Pymaker by default runs the makefile titled Makefile.py. You should
put all your functions in that file. As for the actual file, it's pretty
simple! Here's an example file:

.. code:: python

   from pymaker import command, r

   @command
   def start():
        r("echo Hello, World!")

You can run this file by running ``pymaker start``. ``r`` is basically a wrapper
around ``os.system`` or ``subprocess.call``, depending on whether you call it with
a string or a list. So this file might be similar to:

.. code:: make

   start:
        echo Hello, World!

You can also define dependencies as follows:

.. code:: python

   from pymaker import command, r

   @command
   def start():
        r("echo Hello, World!")

   @command(deps=['start'])
   def end():
        r("echo Goodbye, World!")

If you run this as ``pymaker end``, you will see ``Hello, World!`` then
``Goodbye, World``. You can also define command line arguments:

.. code:: python

   from pymaker import command, r, declare_argument

   declare_argument('-n', '--name', default='World')

   @command
   def greet(ns):   # The name of this argument **must** be ns
        r(['echo', 'Hello, ', ns.name])

If you run this as ``pymaker greet --name Bob``, the output will be ``Hello, Bob``.

See? So simple!
