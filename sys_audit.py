#!/usr/bin/env python3
import psutil, json, time, datetime, argparse, pathlib


def audit(limit, duration):
    psutil.cpu_percent(None);
    time.sleep(duration);
    cpu = psutil.cpu_percent(None)
    
    process = [
                {
                    'pid': p.pid,
                    'name': p.info['name'],
                    'ram_mb': round(p.info['memory_info'].rss/1_048_576, 1)
                }
                for p in psutil.process_iter(['name', 'memory_info']) 
                    if p.info['memory_info'].rss/1_048_576 > limit 
            ]

    return { 'timestamp': datetime.datetime.now().isoformat(), 'cpu_percent': cpu, 'processes': process }


if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--limite', type=int, default=300)
    ap.add_argument('--duree', type=int, default=30)
    args = ap.parse_args()
    rpt = audit(args.limite, args.duree)
    report = pathlib.Path(f'audit_{datetime.date.today()}.json')
    report.write_text(json.dumps(rpt, indent=2))
    print('Report →', report)
    print(report)
