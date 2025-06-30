import yaml

with open("manifests/demo/deployment.yaml") as f:
    doc = yaml.safe_load(f)

print(doc)

doc["spec"]["replicas"] += 1

with open("manifests/demo/deployment_scaled.yaml", "w") as f:
    yaml.safe_dump(doc, f, sort_keys=False)




