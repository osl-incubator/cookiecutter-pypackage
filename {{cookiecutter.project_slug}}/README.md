{% set is_open_source = cookiecutter.project_license != 'Other' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.project_license }}
* Documentation: https://{{ cookiecutter.project_slug }}.readthedocs.io.
{% endif %}

## Features

* TODO

## Credits

This package was created with Cookieninja and the `osl-incubator/cookiecutter-python` project template.
