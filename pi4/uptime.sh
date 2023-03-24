#!/bin/bash
URL="http://192.168.0.2:1000/message?token=AH.xceQ4FK49wow"

uptime=$(awk '{print int($1/86400)}' /proc/uptime)

if ((uptime>7)); then
	curl "${URL}" -F "title=Uptime" -F "message=${uptime} days up. Reboot is recommended" -F "priority=5"
fi
