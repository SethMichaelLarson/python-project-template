Contributing
============

{{cookiecutter.module_display_name}} is a community-maintained project and happily accepts contributions.
Thank you for considering contributing. ❤️

Adding Features / Fixing Bugs
-----------------------------

#. `Check for open issues <https://github.com/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/issues>`_ or open
   a new issue to start a discussion around a new feature or a bug.  Issues labeled with
   *Contributor Friendly* are for issues that are great for new contributors that are
   new to the project or not as familiar with the codebase.

#. Fork the `{{cookiecutter.module_display_name}} repository on Github <https://github.com/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}>`_
   to start making changes.

#. Write a test which shows that the bug was fixed or that the feature works as expected.
   Make sure that all regression tests pass by running the tests as described below.

#. Send a Pull Request and bug maintainers until it gets merged and published.
   Mention bot will ping the maintainers that are best suited for reviewing the change.
   Make sure all steps in the Pull Request template are completed including adding
   documentation if necessary and adding yourself to ``CONTRIBUTORS.rst`` for non-trivial features.

#. If you need to make updates to your Pull Request, simply push to the same repository and branch
   that your Pull Request was filed under. There is no need to open a new Pull Request, our
   continuous integration services will pick up the updates.

Running the Test Suite
----------------------

Our test suite is based on `Tox <https://tox.readthedocs.io/en/latest/>`_ to allow
running from many different Python versions at once in addition to building docs
and running a style checker via `Flake8 <http://flake8.pycqa.org/en/latest/>`_.

To run our test suite, simply change your current working directory to the root
of the project and run the following command::

    $ tox
    [... install dependencies, build docs, run tests]
    docs: commands succeeded
    flake8: commands succeeded
    py27: commands succeeded
    py33: commands succeeded
    py34: commands succeeded
    py35: commands succeeded
    py36: commands succeeded

Note that unless you have a Python interpreter for 2.7 as well as 3.3-3.7 you may see failures
for all the interpreters you don't have.  If you don't have a Python 3.5 interpreter you will
not be able to run the flake8 check or build the docs as both require a Python 3.5 interpreter.

Our test suite is run against Travis CI as well as AppVeyor for each Pull Request.  Our codebase is
also monitored by Codecov for test suite coverage checks and CodeClimate to get automated code review
for both maintainers and contributors alike.
