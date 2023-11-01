Cross-Up an auto reupload and cross-seed script for use with qbittorrent
This tool relies on cross-seed, Autobrr/RSS feeds, and L4G Upload-Assistant


Cross-seed must be set up in Daemon mode in order for this script to work.

Configure qbittorrent it have the 'Run external program on torrent completion' section include:
/path/to/crossup.py "%F" "%L" "%N"

This next section passes through the parameter from the command line by order.

%F is the content path
 
%L is the category for the torrents you want to reupload
 
%N is the name of the torrent to allow for cross seeding

%F=$1
%L=$2
%N=$3

Cross-Up:

This script will be called when a torrent is downloaded and reaches 100% completion.
A category have to be defined in order for the script to be envoked.

The category is used to verify that the torrent was intended to be sent to Cross-up.

The config.cfg will need to be setup in order for the script to function.

TO-DO:

Allow for script to be called upon category change.
