#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Go to src
cd src

# Run the script
python insta_automation_script.py ../photos/astronaut.jpg "Your caption here" "https://your-link.com"
