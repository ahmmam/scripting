import json
from jsonschema import Draft202012Validator

with open("schema.json") as f:
    schema = json.load(f)
with open("config.json") as f:
    data = json.load(f)

validator = Draft202012Validator(schema)
errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

if errors:
    for err in errors:
        print(f"Erreur: {'/'.join(map(str, err.path))} -> {err.message}")
else:
    print("Config valide.")

