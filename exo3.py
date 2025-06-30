from ruamel.yaml import YAML
from pathlib import Path
from copy import deepcopy

yaml = YAML()
def deep_merge(a, b):
    for k, v in b.items():
        if isinstance(v, dict) and k in a:
            deep_merge(a[k], v)
        else:
            a[k] = deepcopy(v)

base = yaml.load(Path("manifests/demo/deployment.yaml"))
overlay = yaml.load(Path("manifests/demo/overlay.yaml"))

deep_merge(base, overlay)

with open("manifests/demo/deployment_merged.yaml", "w") as f:
    yaml.dump(base, f)


