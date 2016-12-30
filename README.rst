Python Project Template
=======================

This is a free to use Python project template for Python 2.7-3.7
that I use for all of my open source Python projects.
Hope that it's also useful to others! :)

How to use this template
------------------------

Change to the directory you want your project to be in::

    $ cd ~/Desktop

Install the `cookiecutter <https://github.com/audreyr/cookiecutter>`_ module via pip::

    $ python -m pip install cookiecutter
    
Then run cookiecutter to get the latest version of the template.
It'll ask you a few questions like your Github user name, repo name, etc::

    $ cookiecutter gh:SethMichaelLarson/python_project_template
    
Do a quick look at all ``.rst`` files to make sure the number of underlines is correct for titles. :)
And voila! Ready to be commited as your initial commit!

After this commit, you should sign up for the following services and set their permissions on Github:

* `Travis CI <https://travis-ci.org/>`_
* `AppVeyor <https://ci.appveyor.com/projects>`_
* `PyUp <https://pyup.io/>`_
* `Codecov <https://codecov.io/gh>`_
* `CodeClimate <https://codeclimate.com>`_
* `Readthedocs <https://readthedocs.org/>`_
* `Mention Bot <https://github.com/facebook/mention-bot>`_

And you should be ready to go! Happy committing!

Be sure to change the licenses everywhere if you're using something besides MIT and the year on the Copyright.
All of my Python projects are MIT, that's why I use it as a default. :)

Questions / Suggestions
-----------------------

If you've got a question or a suggestion just create an issue in the Github issue tracker.

License
-------
This template is licensed under CC0-1.0.
