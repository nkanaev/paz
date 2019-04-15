paz
===

**paz** is a simple path manipulation library, which wraps `os.path` & `shutil` modules.


usage
-----

.. code:: python

    from paz import p

    p('/path/to/any/file.ext')


    # *p* is a subclass of *str* and can be manipulated like a regular string:

    p('images/lenna.png').split('/')  # returns: ['images', 'lenna.png']


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
