#!/bin/bash

URL="http://192.168.0.2:1000/message?token=AH.xceQ4FK49wow"

if test "$(checkupdates | wc -l)" != 0; then
	curl "${URL}" -F "title=Updates" -F "message=New updates" -F "priority=5"
fi
