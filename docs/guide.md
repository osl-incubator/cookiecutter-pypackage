# Guide

## Build System

There are several build system options available to development of Python
packages. SciCookie support the following:

- [**Poetry**](https://python-poetry.org/) (default): It's a Python package
  manager that streamlines dependency management and package distribution. It
  provides a simple and intuitive syntax for defining project dependencies and
  allows you to easily create and manage virtual environments for your projects.
  With Poetry, you can easily install, update, and remove dependencies, and it
  automatically handles conflicts and resolution between packages. Additionally,
  Poetry provides a comprehensive toolset for packaging and publishing your
  projects to PyPI, including support for building source distributions and
  wheel packages, as well as generating and uploading documentation. Overall,
  Poetry simplifies the development and distribution of Python projects, making
  it a popular tool for many Python developers.

- [**Flit**](https://flit.pypa.io): It's a Python package and a lightweight tool
  for creating and distributing Python packages. It automates the processes
  involved in packaging and submitting a project to PyPI, and provides a
  straightforward interface for managing a project's dependencies. With just a
  few  commands, you can use Flit to quickly create source distributions and
  wheel packages and submit them to PyPI.

- [**meson-python**](https://meson-python.readthedocs.io/en/latest/index.html):
  It's a Python build backend built on top of the *Meson* build-system.
  It enables you to use Meson for your Python packages. With
  meson-python, you can easily define project dependencies, specify
  build options, generate configuration files and build scripts, among
  other things. Meson-python is primarily focused on improving speed and
  ease of use compared to other build systems. It is designed to be fast
  and scalable, making it suitable for both small and large projects.

- [**Setuptools**](https://setuptools.pypa.io/en/latest/): It's a package that
  facilitates the distribution and installation of Python packages. Setuptools
  provides a way to define metadata about your project, such as its name,
  version, dependencies, and other details. It also provides functionality for
  building and distributing packages, creating distribution archives, and
  installing packages with their dependencies.  _"It helps developers to easily
  share reusable code (in the form of a library) and programs (e.g., CLI/GUI
  tools implemented in Python), that can be installed with pip and uploaded to
  PyPI."_

- [**PDM**](https://pdm.fming.dev/): It's a modern Python package and
  dependency manager supporting the latest PEP standards. But it is more
  than a package manager. It boosts your development workflow in various
  aspects. It has very powerful features, including easy and fast
  dependency resolution, especially for large binary distributions, a
  PEP 517 compilation backend, PEP 621 project metadata, a flexible and
  powerful plugin system. It also offers, among other things, versatile
  user scripting, PyPI integration and version management.

The idea behind the options in SciCookie is that you can choose from some of the
most popular system compilers to suit your needs and preferences for developing
Python packages. If you think we should add more options, you can submit your
suggestion as a issue at
https://github.com/osl-incubator/scicookie/issues/new/choose.
 
## Test Library

There are several test library options available to development of Python packages. SciCookie support the following:

-  [**Pytest**](https://docs.pytest.org/en/): is a popular testing framework for Python. It simplifies the process of writing and running tests by providing a concise syntax and powerful features. With Pytest, you can automatically discover and collect test cases, use fixtures for test setup and resource management, and write test functions with assert statements to check expected outcomes. It offers various options for test execution, including running specific tests, parallel execution, and generating test reports. Pytest also has a thriving ecosystem of plugins that extend its capabilities, such as code coverage analysis and test parameterization. Overall, Pytest is widely adopted for its simplicity, flexibility, and community support, making it an effective tool for ensuring the quality and reliability of Python code. You can check documentation [here](https://docs.pytest.org/en/)

- [**Hypothesis**](https://hypothesis.readthedocs.io/): is a property-based testing library for Python. It focuses on generating diverse input data and exploring different scenarios to thoroughly test code. Instead of relying on specific examples, Hypothesis allows you to define general properties that your code should satisfy. It automatically generates random inputs, including edge cases, to uncover potential bugs and unexpected behaviors. Hypothesis integrates well with popular testing frameworks like Pytest and promotes comprehensive testing to improve code reliability. You can check documentation [here](https://hypothesis.readthedocs.io/)
