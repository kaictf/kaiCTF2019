#!/usr/bin/bash

LEVELS=10


DIR_PER_LEVEL=10

# First parameter - deep of current level
# Second parameter - parent directory

function create_dirs_on_level {

CUR_LEVEL=$1

# If not reached the end of the recurrent
if [ $CUR_LEVEL -lt $DIR_PER_LEVEL ]
then

    echo Currenlty at $2

    for i in {1..$LEVELS} ;
    do
        d=$RANDOM
        #mkdir -p $2/$d
        echo $2/$d
    done;

        for file in $2/$d ;
    do
        create_dirs_on_level $((CUR_LEVEL+1)) $file
    done;


fi


}


create_dirs_on_level 1 nginx-dirs

