"""Test Azure Pipelines YAML files."""

import json
import sys

import yaml

from jsonschema import validate

print(sys.argv)
args = 3
if len(sys.argv) != args:
    raise Exception(
        "Usage: python test_azure_pipelines.py <schema_file> <yaml_file>"
    )

schema_file = sys.argv[1]
yaml_file = sys.argv[2]

with open(schema_file, "r") as f:
    schema = json.load(f)

with open(yaml_file, "r") as f:
    yaml_data = yaml.safe_load(f)


validate(instance=yaml_data, schema=schema)
print(
    "The file {} is valid according to the schema {}.".format(
        yaml_file, schema_file
    )
)
