import yaml, glob, collections

kinds = collections.Counter()
for path in glob.iglob("manifests/**/*.y*ml", recursive=True):
    with open(path) as f:
        for doc in yaml.safe_load_all(f):
            k = doc.get("kind")
            if k in {"Deployment","StatefulSet","DaemonSet","Job"}:
                kinds[k] += 1

print("\nInventaire:")
for k, n in kinds.items():
    print(f"  {k:<12}: {n}")

