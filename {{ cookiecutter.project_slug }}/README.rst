{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/build/badge.svg?branch=master
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3Abuild
        :alt: Build Status

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/gh-pages/badge.svg?branch=master
        :target: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/
        :alt: Docs

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug | replace("_", "-") }}/branch/master/graph/badge.svg?token=REMOVE_OR_REPLACE_ME
        :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :alt: Codecov

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug | replace("_", "-") }}
        :target: https://pypi.org/project/{{ cookiecutter.project_slug | replace("_", "-") }}
        :alt: PyPI

.. image:: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/releases
        :alt: Symantic Versions

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black
        :alt: Code style: black


{{ cookiecutter.project_short_description }}

TODOs once project is created
==============================

- [ ] Register project on `test.pypi.org <https://test.pypi.org/account/register/>`_ and
    `pypi.org <https://pypi.org/account/register/>`_.
- [ ] Add project to Codecov account
- [ ] Add the following secrets to the repo:

  - ``GITHUB_TOKEN``

    - From Settings > Developer Settings > `Tokens <https://github.com/settings/tokens>`_ > Personal Access Tokens

  - ``CODECOV_TOKEN``

    - `Activate a repository <https://app.codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings>`_
    - `Add the repository <https://codecov.io/gh/{{ cookiecutter.github_username }}/+>`_ to your \[Codecov\] account
    - Token will be displayed in the "Upload Token" field
    - If the repo is private, you will need to append the "Graphing Token" to the codecov-badge link above

  - ``PYPI_USER`` and ``PYPI_PASSWORD``

- [ ] Configure ``gh-pages``

  - Go to the settings tab > github pages section
  - Select ``gh-pages`` as the branch to host your docs
  - Choose ``docs/build/html`` as the directory containing your docs
  - You should now see ``github-pages`` under the environments in the sidebar.
    Click on it and select 'View deployment' this will take you to your ready-made website.
    If it says 404, just give it 2 minutes and retry.



Template Repo Details
=====================
- Github workflows to perform CI/CD tasks:

  - Run code quality, test coverage, and security checks on Pull Requests and commits to master branch

  - Auto-publish documentation to `GitHub Pages <https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/>`_

  - Auto-publish new releases to PyPI once a new tag is pushed to the remote repository::

        $ git checkout master
        $ git pull origin --force
        $ bump2version patch # possible: major / minor / patch
        $ git push
        $ git push --tags

- Code coverage report comments on Pull Requests, provided by Codecov

- Isolated test environments provided by ``tox``

  .. list-table::
     :widths: 25 25 50
     :header-rows: 1

     * - Environment Name
       - Invocation
       - Purpose
     * - ``py``
       - ``tox -e py``
       - Runs ``pytest`` with ``pytest-cov`` for testing functionality and code coverage
     * - ``format``
       - ``tox -e format``
       - Formats the project's code using ``black`` and ``isort``
     * - ``black``
       - ``tox -e black``
       - Checks that the project's code is properly formatted according to ``black``'s opinionated specifications
     * - ``isort``
       - ``tox -e isort``
       - Checks that import statements are in the proper order and uniform across the project
     * - ``check-manifest``
       - ``tox -e check-manifest``
       - Check that ``MANIFEST.in`` has the appropriate settings
     * - ``pyroma``
       - ``tox -e pyroma``
       - Determine package friendliness
     * - ``flake8``
       - ``tox -e flake8``
       - Check adherence to pep8 styling using ``flake8``
     * - ``pylint``
       - ``tox -e pylint``
       - Check adherence to pep8 styling using ``pylint``
     * - ``mypy``
       - ``tox -e mypy``
       - Check that static typing has been added across the project
     * - ``doc8``
       - ``tox -e doc8``
       - Check the validity, style, and uniformity of the RST files in the project docs
     * - ``docstr-coverage``
       - ``tox -e docstr-coverage``
       - Check that all modules, classes, and functions contain proper docstrings
     * - ``security``
       - ``tox -e security``
       - Check for any potential security issues with the package code
     * - ``docs-create``
       - ``tox -e docs-create``
       - (Re-)creates fresh ``sphinx-apidoc`` stubs
     * - ``docs-build``
       - ``tox -e docs-build``
       - Builds the static html files based on the .rst files in ``source/``
     * - ``bumpversion``
       - ``tox -e bumpversion``
       - Used to create a new release, updating the version in relavent files and tagging the most-recent commit
     * - ``test-release``
       - ``tox -e test-release``
       - Release the newest version of the code to the test PyPI site

Project structure::

    {{ cookiecutter.project_slug }}
    ├── .github
    │   └── workflows
    │       ├── build.yml
    │       ├── gh-pages.yml
    │       └── release.yml
    ├── docs
    │   └── source
    │       └── conf.py
    ├── src
    │   └── {{ cookiecutter.project_slug }}
    │       ├── __init__.py
    │       └── replace_me.py
    ├── tests
    │   ├── __init__.py
    │   └── test_{{ cookiecutter.project_slug }}.py
    ├── .editorconfig
    ├── .gitignore
    ├── CHANGELOG.rst
    ├── codecov.yml
    ├── CONTRIBUTING.rst
    ├── MANIFEST.in
    ├── pyproject.toml
    ├── README.rst
    ├── requirements.txt
    ├── requirements_dev.txt
    ├── setup.cfg
    ├── setup.py
    └── tox.ini
