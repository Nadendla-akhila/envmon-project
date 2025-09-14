"""
Simple script to push sample sensor readings to the backend API for testing.
Usage: python scripts/ingest_sample.py --url http://localhost:8000 --api-key yourkey
"""
import argparse
import time
import random
import requests
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--url', default='http://localhost:8000')
parser.add_argument('--api-key', default=None)
parser.add_argument('--count', type=int, default=20)
parser.add_argument('--interval', type=float, default=0.2)
args = parser.parse_args()

headers = {}
if args.api_key:
    headers['x-api-key'] = args.api_key

for i in range(args.count):
    payload = {
        'sensor_id': f'sim-{i%3}',
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'pm25': max(0, random.gauss(40, 30)),
        'pm10': max(0, random.gauss(60, 40)),
        'temperature': random.uniform(15, 35),
        'humidity': random.uniform(20, 90)
    }
    try:
        r = requests.post(f"{args.url}/api/readings", json=payload, headers=headers, timeout=5)
        print(r.status_code, r.text)
    except Exception as e:
        print('failed', e)
    time.sleep(args.interval)
