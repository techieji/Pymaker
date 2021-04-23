.. Pymaker documentation master file, created by
   sphinx-quickstart on Fri Apr 23 08:39:35 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pymaker's documentation!
===================================

.. toctree::
   quickstart
   api
   :maxdepth: 2
   :caption: Contents:

Pymaker, the better alternative to make.

.. note::

   Because I don't own the package name ``Pymaker``, to install, you
   run ``pip install py-maker``

.. code:: python

   from pymaker import command, r

   @command
   def start():
        r('echo Hello, World!')

.. code:: bash

   $ pymaker start
   Pymaker: echo Hello, World!
   Hello, World!

Pymaker allows you to use your knowledge of Python in order to
define and run repetitive commands.

Although Pymaker is not as intellegent as GNU Make yet, Pymaker
allows you to take advantage of Python, which is already a major
power boost. In the future, support for C compilers and Python
might be available. To see the available features, see the :ref:`quickstart`.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
