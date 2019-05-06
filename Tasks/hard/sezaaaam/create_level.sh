#!/usr/bin/bash

LEVELS=10
PASSFILE="10-million-password-list-top-10000.txt"

# Folder to store passwords
mkdir levels

# Enumerate over all levels
for r in $(seq $LEVELS);
do
    PASS=$(shuf -n 1 $PASSFILE)
    USER=$PASS

    #echo $PASS $USER

    htpasswd -bc levels/level$r $USER $PASS

    #echo "htpasswd -c levels/level$r $USER $PASS"

done;
