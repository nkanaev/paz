paz123
===

**paz** is a small, versatile library for path string manipulation.

It is a wrapper around ``os``, ``os.path``, ``shutil`` and many other built-in modules,
which simplifies path management operations.

usage
-----

.. code:: python

    from paz import p

    image_dir = p('/Users/nkanaev/Pictures')
    for image_file in image_dir.find('*.jpg', type='file'):
        image_file.move('{basepath}_backup.{ext}')

The same code without ``paz``:

.. code:: python

    import os
    import shutil

    for root, dirs, files in os.walk('/Users/nkanaev/Pictures'):
        for file in files:
            if file.endswith('.png'):
                basename = os.path.splitext(file)[0]
                src_path = os.path.join(root, file)
                dst_path = os.path.join(root, basename + '_backup.png')
                shutil.move(src_path, dst_path)

docs
----

The library provides only one function - ``paz.p``.
It returns a subclass of ``str``/``bytes`` depending on the input,
which can be manipulated like a regular string.
On top of that,  provides a few commonly used operations:

* file system information: ``owner``, ``group``, ``is_dir``, ``is_file``,
  ``is_link``, ``exists``, ``type``, ``last_accessed``, ``last_modified``
* path parts extraction: ``filename``, ``basename``, ``ext``, ``dirname``, ``basepath``, ``path``, ``fullpath``
* utility operations: ``copy()``, ``move()``, ``chown()``, ``chmod()``, ``hash()``
* path string manipulation: ``pathmap()`` & readable path joins (ex.: ``image_dir / 'wallpapers'``)

The result is an object-oriented, "pythonic" object that makes
file-related operations easy without breaking the existing data types.

tests
-----

.. image:: https://travis-ci.org/nkanaev/paz.svg?branch=master
    :target: https://travis-ci.org/nkanaev/paz
