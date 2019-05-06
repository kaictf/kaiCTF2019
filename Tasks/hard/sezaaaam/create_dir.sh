#!/usr/bin/bash

# Maximum Number of levels
LEVELS=3
# Number of folders on each level
DIR_PER_LEVEL=10

# First parameter - deep of current level
# Second parameter - parent directory

function create_dirs_on_level {

# Identify current level of deep
CUR_LEVEL=$1
NEXT_LEVEL=$((CUR_LEVEL+1))


#echo Currently at $CUR_LEVEL

# If not reached the end of the recurrent
if [ $NEXT_LEVEL -lt $LEVELS  ]
then

    for i in $(seq $DIR_PER_LEVEL) ;
    do
        d=$RANDOM
        mkdir -p $2/$d

        create_dirs_on_level $NEXT_LEVEL $2/$d
    done;



else
    echo $2/$d
    return
fi

}

mkdir nginx-dirs

create_dirs_on_level 0 nginx-dirs

