#!/bin/bash

# Cross-Up an auto reupload and cross-seed script for use with qbittorrent created by khak1s
# This tool relies on cross-seed Autobrr/RSS feeds, and L4G Upload-Assistant
#
#
#Cross-seed must be set up in Daemon mode in order for this script to work
#This goes into the 'Run external program on torrent completion' section of qbittorrent:
#/path/to/crossup.sh "%F" "%L" "%N"
#This next section passes through the parameter from the command line by order.
#
# %F is the content path
# %L is the catagory for the torrents you want to reupload
# %N is the name of the torrent to allow for cross seeding
#
#%F=$1
#%L=$2
#%N=$3

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
