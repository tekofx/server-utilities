#!/bin/bash
URL="http://192.168.0.2:1000/message?token=AH.xceQ4FK49wow"

response=400
echo $response

while [ $response -ne 200 ]
do
  response=$(curl --write-out '%{http_code}' --silent --output /dev/null "${URL}" -F "title=Startup" -F "message=Device started" -F "priority=5")
  sleep 30
done
