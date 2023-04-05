# Cookiecutter Python Package

**Cookiecutter-python** is a template developed by [Open Science Labs](https://opensciencelabs.org/) that creates projects from project templates and is based on [Cookiecutter](https://github.com/cookiecutter/cookiecutter) command-line utility  . It serves as a boilerplate which can be used by beginners as well as full fledged developers to simplify the project creation process and save considerable amount of time.
Cookiecutter enables projects with an initial layout that includes recommended tools, workflows, and project structure. 

Cookiecutter also offers other features that can enhance the workflow of the development process.Features such as *automatic documentation generation, automated testing,* and *project-specific configuration* are part of this. Overall, Cookiecutter is an efficient tool that gives users the ability to effortlessly create consistent, high-quality projects.

Open Science Labs Scientific Python cookiecutter  template is primarily based on the **PyOpenSci** recommendations who is actively conducting research to determine the tools, libraries, best practices, and workflows utilized by significant scientific Python groups. As a result, this template offers to authors a starting point for their project that adheres with industry standards and can be adjusted to meet particular project requirements


[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template
for a Python package.

  - GitHub repo: <https://github.com/osl-incubator/cookiecutter-python/>
  - Free software: BSD license

## Features

  - Allows package slug (use `_` instead of `-`)
  - Licenses supported: MIT, BSD 3 Clause, ISC License, Apache Software License 2.0, and GPL 3
  - Documentation engines: mkdocs, sphinx, jupyter-boook
  - Test library: pytest
  - Auto format code tool: blue, and black
  - Initial integration with git
  - Support to conda (as base environment) and poetry as packaging and dependency management
  - Support to pre-commit
  - CI with github actions
  - Release workflow with semantic release and github actions

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this
requires Cookiecutter 1.4.0 or higher):

```bash
pip install -U cookiecutter
```

or, using conda/mamba:

```bash
mamba create -n cookiecutter cookiecutter
conda activate cookiecutter
```

Go to a desired folder to create your new project, for example:

```bash
cd ~/dev/my-python-projects
```

Generate a Python package project:

```bash
cookiecutter https://github.com/osl-incubator/cookiecutter-python.git
```

or, using ssh:

```bash
cookiecutter git@github.com:osl-incubator/cookiecutter-python.git
```

## Development

For testing your changes locally, you can run:

```bash
make test-template
```
