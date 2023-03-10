Auto re/upload and cross-seed script for use with qbittorrent

Created by Khak1s

This tool relies on Cross-Seed, Qbittorrent, Autobrr/RSS feeds, and L4G Upload-Assistant

In autobrr the catagories are configured to the same name that is used in Upload-Assistant in this script.


L4G Upload-Assistant:

Ensure that upload.py is executable using the command chmod +x upload.py


Cross-Seed:

1.Cross-seed must be set up in Daemon mode in order for this script to work.


Qbittorrent:

1. In the 'Run external program on torrent completion' section of qbittorrent: 

/path/to/cross-up.sh %F %L

This next section passes through the parameter from the command line by order.

%F is the content path
%L is the category for the torrents you want to reupload
%G is the tag of for the torrent used to identify the source
%N is the name of the torrent to allow for cross seeding

%F=$1
%L=$2
%G=$3
%N=$4

Cross-Up:

This script will be called when a torrent is downloaded and reaches 100% completion.
A category and a tag have to be defined for the torrent in question.

The category is used to verify that the torrent was intended to be sent to Cross-up

The tags are used to define the source of the torrent and what trackers should then be uploaded to.

The cross-seed.config will need to be setup in order for the script to function.

The path to the config fill will need to be defined in the cross-up.sh


TO-DO:

Allow for script to be called upon category change.
