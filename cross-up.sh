#!/bin/bash

source config.cfg

exec >> $logfile 2>&1

echo $(date -u)
echo ""
echo "Starting L4G Upload Assistant for " "$3" " at filepath" "$1"
echo ""

if [ "$2" == "$cat" ]; then
     python3 $l4g $1 -ua -tk $trackers --anon
     curl -XPOST $csurl --data-urlencode "name=$3"
else
     echo "unknown error"

fi
