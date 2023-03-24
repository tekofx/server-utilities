#!/bin/bash
URL="http://192.168.0.2:1000/message?token=AjSLYWb0gZn.C.m"

docker restart musicbot
docker restart furbot
curl "${URL}" -F "title=Furbot status" -F "message=Furbot has been restarted" -F "priority=5"
