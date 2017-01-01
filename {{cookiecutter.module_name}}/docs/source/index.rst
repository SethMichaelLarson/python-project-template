{{cookiecutter.module_display_name}}
=====================

.. toctree::
    :hidden:
    :maxdepth: 2

    api_reference/index
    changelog
    contributing
    about

{{cookiecutter.module_description}}

Getting Started with {{cookiecutter.module_display_name}}
----------------------------

{{cookiecutter.module_display_name}} is available on PyPI can be installed with `pip <https://pip.pypa.io>`_.::

    $ python -m pip install {{cookiecutter.module_name}}

To install the latest development version from `Github <https://github.com/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}>`_::

    $ python -m pip install git+git://github.com/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}.git


If your current Python installation doesn't have pip available, try `get-pip.py <bootstrap.pypa.io>`_

After installing {{cookiecutter.module_display_name}} you can use it like any other Python module.
Here's a very simple demonstration of scheduling a single job on a farm.

.. code-block:: python

    import {{cookiecutter.module_name}}
    # Fill this section in with the common use-case.

API Reference
-------------

The :doc:`api_reference/index` documentation provides API-level documentation.

Support / Report Issues
-----------------------

All support requests and issue reports should be
`filed on Github as an issue <https://github.com/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/issues>`_.
Make sure to follow the template so your request may be as handled as quickly as possible.
Please respect contributors by not using personal contacts for support requests.

Contributing
------------

We happily welcome contributions, please see :doc:`contributing` for details.

License
-------

{{cookiecutter.module_name}} is made available under the MIT License. For more details, see :doc:`about`.
