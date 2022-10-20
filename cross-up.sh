#!/bin/bash
. /path/to/cross-up.confg

exec >> $logfile 2>&1
upload=echo $trackers| sed "s/$3//g"

echo $(date -u)
echo ""
echo "Starting L4G Upload Assistant for" $1
echo ""

if [[ $2 == '$cat' ]] && [[ "$3" == 'BLU' ]]; then
     $l4g $1 -ua -tk $upload
     curl -XPOST $csurl --data-urlencode "name=%N"

 elif [[ $2 == 'reupload' ]] && [[ "$3" == "AITHER" ]]; then
     $l4g $1 -ua -tk $upload
     curl -XPOST $csurl --data-urlencode "name=%N"
fi