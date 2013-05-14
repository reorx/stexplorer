SongTaste Explorer
==================

Simple Qt based GUI tool for downloading songs from SongTaste_

.. _SongTaste: http://songtaste.com/


Screenshots
-----------

Windows
+++++++

.. image:: screenshot_windows.png

Kubuntu
+++++++

.. image:: screenshot_kubuntu.png


Build
-----

Download and unpack **pyinstaller** to gui/pyinstaller-2.0 folder, then execute:

::

    $ cd gui
    $ make build


TODO
----

* exe freeze (with more detailed options like icon)

* writing to file while receiving, not after receiving

* wrong url handling

* show parsed song information

* menu

* store settings

* output logs to file
