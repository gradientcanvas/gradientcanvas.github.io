import subprocess
import os
import json

# Dictionary containing the URL and the timestamps
with open('record.json') as f:
    example_dict = json.load(f)


# The name of the file to save the image as
# output_filename = 'downloaded_image.png'

#Remove all existing .png files in the directory
# directory = "TODO"
# for filename in os.listdir(directory):
#     if filename.endswith(".png"):
#         os.remove(os.path.join(directory, filename))


# Using subprocess to run the wget command
for canvas in example_dict:
    url = canvas['url']
    timestamp = canvas['timestamp']
    subprocess.run(['wget', url, '-O', f"{timestamp}.png"])
    
