import yaml, glob, os

def update_img(path, old_tag="old", new_tag="new"):
    changed = False
    with open(path) as f:
        docs = list(yaml.safe_load_all(f))
    for doc in docs:
        try:
            containers = doc["spec"]["template"]["spec"]["containers"]
            for c in containers:
                if c["name"] == "web" and c["image"].endswith(":"+old_tag):
                    c["image"] = c["image"].rsplit(":", 1)[0] + ":" + new_tag
                    changed = True
        except (TypeError, KeyError):
            continue
    if changed:
        with open(path, "w") as f:
            yaml.safe_dump_all(docs, f, sort_keys=False)
        print("OK", path)

for yml in glob.iglob("manifests/**/*.y*ml", recursive=True):
    update_img(yml)

