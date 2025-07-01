#!/usr/bin/env python3
from pathlib import Path;
from datetime import datetime,timedelta; 
import argparse

def purge(root:Path,days:int):
    cut=datetime.now()-timedelta(days=days); freed=0

    for f in root.rglob('*.log*'):
        if datetime.fromtimestamp(f.stat().st_mtime)<cut:
            size=f.stat().st_size; 
            f.unlink(); 
            freed+=size
            print(f'Removed {f} ({size/1_048_576:.1f} MiB)')
    
    print(f'Total freed: {freed/1_048_576:.2f} MiB')

if __name__=='__main__':
    ap=argparse.ArgumentParser();
    ap.add_argument('--root',type=Path,default='sample_logs/myapp')
    ap.add_argument('--days',type=int,default=15);
    args=ap.parse_args();
    purge(args.root,args.days)
