{{cookiecutter.module_display_name}}
=======

.. image:: https://img.shields.io/travis/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/master.svg
    :target: https://travis-ci.org/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}
    :alt: Linux and MacOS Build Status
.. image:: https://img.shields.io/appveyor/ci/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/master.svg
    :target: https://ci.appveyor.com/project/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}
    :alt: Windows Build Status
.. image:: https://img.shields.io/codecov/c/github/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/master.svg
    :target: https://codecov.io/gh/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}
    :alt: Test Suite Coverage
.. image:: https://img.shields.io/codeclimate/github/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}.svg
    :target: https://codeclimate.com/github/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}
    :alt: Code Health
.. image:: https://readthedocs.org/projects/{{cookiecutter.module_name}}/badge/?version=latest
    :target: http://{{cookiecutter.module_name}}.readthedocs.io
    :alt: Documentation Build Status
.. image:: https://pyup.io/repos/github/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/shield.svg
     :target: https://pyup.io/repos/github/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}
     :alt: Dependency Versions
.. image:: https://img.shields.io/pypi/v/{{cookiecutter.module_name}}.svg
    :target: https://pypi.python.org/pypi/{{cookiecutter.module_name}}
    :alt: PyPI Version
.. image:: https://img.shields.io/badge/say-thanks-ff69b4.svg
    :target: https://saythanks.io/to/{{cookiecutter.github_name}}
    :alt: Say Thanks to the Maintainers

{{cookiecutter.module_description}}

Getting Started with {{cookiecutter.module_display_name}}
----------------------------

{{cookiecutter.module_display_name}} is available on PyPI can be installed with `pip <https://pip.pypa.io>`_.::

    $ python -m pip install {{cookiecutter.module_name}}

To install the latest development version from `Github <https://github.com/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}>`_::

    $ python -m pip install git+git://github.com/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}.git


If your current Python installation doesn't have pip available, try `get-pip.py <bootstrap.pypa.io>`_

After installing {{cookiecutter.module_display_name}} you can use it like any other Python module.
Here's a very simple example:

.. code-block:: python

    import {{cookiecutter.module_name}}
    # Fill this section in with the common use-case.

API Reference
-------------

The `API Reference on readthedocs.io <http://{{cookiecutter.module_name}}.readthedocs.io>`_ provides API-level documentation.

Support / Report Issues
-----------------------

All support requests and issue reports should be
`filed on Github as an issue <https://github.com/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/issues>`_.
Make sure to follow the template so your request may be as handled as quickly as possible.
Please respect contributors by not using personal contacts for support requests.

Contributing
------------

We happily welcome contributions, please see `our guide for Contributors <http://{{cookiecutter.module_name}}.readthedocs.io/en/latest/contributing.html>`_ for the best places to start and help.

License
-------

{{cookiecutter.github_repo}} is made available under the MIT License. For more details, see `LICENSE.txt <https://github.com/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/blob/master/LICENSE.txt>`_.
