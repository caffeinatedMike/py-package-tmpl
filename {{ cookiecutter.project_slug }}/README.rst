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

# TODO once project is created

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

- [ ] Configure gh-pages

  - Go to the settings tab > github pages section
  - Select ``gh-pages`` as the branch to host your docs
  - Choose docs/build/html as the directory containing your docs
  - You should now see github-pages under the environments in the sidebar.
    Click on it and select 'View deployment' this will take you to your ready-made website.
    If it says 404, just give it 2 minutes and retry.



Template Repo Details
=====================
- Github workflows to handle code checks and publishing documentation on github pages
