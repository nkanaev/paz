paz
===

**paz** is a small, versatile library for path string manipulation.
It's primary purpose is to simplify path & file management operations
by wrapping built-in modules like ``os``, ``os.path``, ``shutil``
in a concise, pythonic api.

usage
-----

.. code:: python

    from paz import p

    image_dir = p('/home/username/pics')
    for image_file in image_dir.walk('*.jpg', type='file'):
        image_file.move('{basepath}_backup.{ext}')

The same code without ``paz``:

.. code:: python

    import os
    import shutil

    for root, dirs, files in os.walk('/home/username/pics'):
        for file in files:
            if file.endswith('.png'):
                basename = os.path.splitext(file)[0]
                src_path = os.path.join(root, file)
                dst_path = os.path.join(root, basename + '_backup.png')
                shutil.move(src_path, dst_path)

docs
----

The library provides only one function - ``paz.p``.
It returns a subclass of ``str``/``bytes``, depending on the input,
which can be manipulated like a regular string.
On top of that, an instance provides a few commonly used operations:

* file system information: ``owner``, ``group``, ``is_dir``, ``is_file``,
  ``is_link``, ``exists``, ``type``, ``last_accessed``, ``last_modified``
* path parts extraction: ``filename``, ``basename``, ``ext``, ``dirname``,
  ``basepath``, ``path``, ``fullpath``
* utility operations: ``copy()``, ``move()``, ``chown()``, ``chmod()``, ``hash()``
* path string manipulation: ``pathmap()`` & readable path joins (ex.: ``image_dir / 'wallpapers'``)

``pathmap``, ``copy`` & ``move`` support substituting path parts between ``{`` and ``}``
with the corresponding values. The full diagram of path parts is provided below:

.. code:: text

    /home/username/pics/portrait-of-madame-x.png

    └────────┬────────┘ └─────────┬────────┘ └┬┘
          dirname              basename      ext
                        └───────────┬──────────┘
                                filename
    └───────────────────┬──────────────────┘
                    basepath
    └──────────────────────┬───────────────────┘
                         path


tests
-----

.. image:: https://travis-ci.org/nkanaev/paz.svg?branch=master
    :target: https://travis-ci.org/nkanaev/paz
