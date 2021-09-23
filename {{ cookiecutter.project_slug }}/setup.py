"""Install file that uses setuptools. Installation command: ``python setup.py install``"""
from pathlib import Path
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.rst").read_text(encoding="utf-8")
# Get the requirements from requirements.txt
requirements = (here / "requirements.txt").read_text(encoding="utf-8")

setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    description=
    "{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    project_urls={
        "Documentation":  "https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}",
        "Source": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
        "Issue Tracker": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues"
    },
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    keywords="{{ cookiecutter.project_slug }}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"{{ cookiecutter.project_slug }}": ["py.typed"]},
    include_package_data=True,
    python_requires=">=3.6,<4.0",
    install_requires=requirements,
    test_suite="tests",
    tests_require=["pytest"],
    extras_require={
        # pip install daap-reporting[tests]
        "tests": ["pytest", "pytest-cov"],
        # pip install daap-reporting[docs]
        "docs": ["Sphinx", "sphinx-rtd-theme"],
    }
)
