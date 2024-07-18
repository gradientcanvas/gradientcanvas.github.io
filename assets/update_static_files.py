import subprocess
import os
import json

with open('record.json') as f:
    example_dict = json.load(f)

for canvas in example_dict:
    url = canvas['url']
    timestamp = canvas['timestamp']
    timestamp = timestamp.replace(":", "-")
    timestamp = timestamp.replace(" ", "_")
    timestamp = timestamp.replace(".", "-")
    subprocess.run(['wget', url, '-O', f"./img/gallery/{timestamp}.png"])
    
