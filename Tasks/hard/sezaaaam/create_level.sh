#!/usr/bin/bash

LEVELS=10
PASSFILE="data/10-million-password-list-top-10000.txt"

# Folder to store passwords
mkdir levels

# Enumerate over all levels
for r in $(seq $LEVELS);
do
    PASS=$(shuf -n 1 $PASSFILE | tr -d "\r\n" | cut -f1)
    USER=$PASS

    htpasswd -bc levels/level$r $USER $PASS;

done;
