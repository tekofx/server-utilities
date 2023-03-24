#!/bin/bash

# Update ClamAV database
sudo freshclam

# Scan the system and save the result to a file
sudo clamscan -r / --log=scan_result.txt

# Send the result via Gotify
curl -X POST "http://192.168.0.2:1000/message?token=AH.xceQ4FK49wow" \
    -F "title=ClamAV Scan Result" \
    -F "message=$(cat scan_result.txt)" \
    -F "priority=5"
