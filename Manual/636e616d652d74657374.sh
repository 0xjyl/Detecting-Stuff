#!/bin/bash

# cname dns request beaconing 

CNAME=ADD CNAME FROM DNS REC
COUNT=20
INTERVAL=60

echo "Requesting..."

for (( i=1; i<=COUNT; i++ ))
do 
	dig $CNAME CNAME +short
	sleep $INTERVAL
done

echo "Completed DNS queries" 