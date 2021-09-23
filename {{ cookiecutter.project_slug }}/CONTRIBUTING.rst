.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

TODO

Submit Feedback
~~~~~~~~~~~~~~~

TODO

Get Started!
------------

TODO

Pull Request Guidelines
-----------------------

TODO

Deploying
---------

A reminder for the maintainers on how to deploy.

**If this is the first release, register the package on PyPI.**

.. code-block:: bash

   python setup.py register

Then, visit PyPI to make sure it registered.

**For all releases**

1. Make sure all your changes (including an entry in CHANGELOG.rst) are committed on a secondary branch.
2. Make sure that all Pull Request checks and tests pass
3. Once the PR is merged, checkout master branch

Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

This will trigger a GitHub workflow that will handle deploying to PyPI.

Finally, edit the release on GitHub (https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/releases).
Paste the release notes into the release's release page, and come up with a title for the release.
