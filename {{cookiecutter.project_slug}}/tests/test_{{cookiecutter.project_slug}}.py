"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest

#from {{cookiecutter.package_slug}} import {{ cookiecutter.package_slug }}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
# import requests
# return requests.get('https://github.com/osl-incubator/cookiecutter-python')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
