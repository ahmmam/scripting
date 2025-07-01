#!/usr/bin/env python3
import subprocess,shlex,argparse,pathlib,sys

BACKUP_DIR = pathlib.Path('backups')
BACKUP_DIR.mkdir(exist_ok=True)

def backup(cmd):
    print(cmd)
    res = subprocess.run(shlex.split(cmd), check=True, capture_output=True)
    return res


def backup_source(path: pathlib.Path):
    base = path.name
    arch = BACKUP_DIR / f"{base}.tgz"
    snar = BACKUP_DIR / f"{base}.snar"
    cmd = f"tar --listed-incremental={snar} -czf {arch} {path}"
    backup(cmd)
    print(f"Archive {arch} → {arch.stat().st_size/1_048_576:.1f} MiB")


def read_source(src_file):
    for line in src_file.read_text().splitlines():
        p = pathlib.Path(line.strip())
        if p.exists():
            backup_source(p)


if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('sources', nargs='?', default='sources.txt', type=pathlib.Path)
    args = ap.parse_args()
    read_source(args.sources)
