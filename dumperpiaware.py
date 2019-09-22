#!/usr/bin/env python3
import json
import time

import requests


def main():
    while True:
        url = 'http://192.168.0.129:8080/data/aircraft.json'
        r = requests.get(url)
        url = '' # Create a Google Cloud function and update this URL with that value
        payload = {'name': 'piawareaircraft', 'data': r.json()}
        r = requests.post(url, json=json.dumps(payload))
        time.sleep(10)


if __name__ == "__main__":
    """
    Run this script on your raspberrypi
    """
    main()
