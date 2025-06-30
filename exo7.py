from jinja2 import Environment, FileSystemLoader
import yaml, os, pathlib

env = Environment(loader=FileSystemLoader("."), autoescape=False)
tpl = env.get_template("deployment.j2")

vars_by_env = yaml.safe_load(open("values.yaml"))

for env_name, values in vars_by_env.items():
    out_dir = pathlib.Path("build")/env_name
    out_dir.mkdir(parents=True, exist_ok=True)
    rendered = tpl.render(**values)
    (out_dir/"deployment.yaml").write_text(rendered)

