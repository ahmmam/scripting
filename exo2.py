import json, yaml

def yaml_to_json(src, dst):
    with open(src) as f:
        data = yaml.safe_load(f)
    with open(dst, "w") as f:
        json.dump(data, f, indent=2)

def json_to_yaml(src, dst):
    with open(src) as f:
        data = json.load(f)
    with open(dst, "w") as f:
        yaml.safe_dump(data, f, sort_keys=False)


yaml_to_json("manifests/demo/deployment.yaml", "manifests/demo/deployment.json")
json_to_yaml("manifests/demo/deployment.json", "manifests/demo/deployment_roundtrip.yaml")


