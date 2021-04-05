import json
from jsonschema import validate


def load_config(config, schema):
    return validate_config(json.load(open(config, "r")), json.load(open(schema, "r")))


def validate_config(config, schema):
    validate(config, schema)
    return config
