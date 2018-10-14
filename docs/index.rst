aiospread API Reference
=====================

`gspread <https://github.com/RainbowLegend/aiospread>`_ is an asynchronous Python client library for the `Google Sheets`_ API based off
of gspread by burnash.

.. _Google Sheets: https://docs.google.com/spreadsheets/

.. module:: gspread

.. contents:: :local:

Main Interface
--------------

.. autofunction:: authorize

.. autoclass:: aiospread.Client
   :members:

Models
------

The models represent common spreadsheet objects: :class:`a spreadsheet <Spreadsheet>`,
:class:`a worksheet <Worksheet>` and :class:`a cell <Cell>`.

.. note::

   The classes described below should not be instantiated by end-user. Their
   instances result from calling other objects' methods.

.. autoclass:: aiospread.models.Spreadsheet
   :members:
.. autoclass:: aiospread.models.Worksheet
   :members:
.. autoclass:: aiospread.models.Cell
   :members:

Utils
-----

.. automodule:: aiospread.utils
   :members: rowcol_to_a1, a1_to_rowcol

Exceptions
----------

.. autoexception:: aiospread.exceptions.GSpreadException
.. autoexception:: aiospread.exceptions.APIError

.. _github issue: https://github.com/RainbowLegend/aiospread/issues

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
