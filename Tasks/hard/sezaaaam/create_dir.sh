#!/usr/bin/bash

# Maximum Number of levels
LEVELS=10
# Number of folders on each level
DIR_PER_LEVEL=10

FLAG="kaiCTF{6a4b909aee1a838bda249e1a3434e60e}"



# First parameter - deep of current level
# Second parameter - parent directory
function create_dirs_on_level {

# Identify current level of deep
CUR_LEVEL=$1
NEXT_LEVEL=$((CUR_LEVEL+1))


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
    #FOR DEBUG ONLY
    #echo $2/$d
    return
fi

}

# Make folder to store temporary results
mkdir nginx-dirs

# Execute recursively
create_dirs_on_level 0 nginx-dirs


# Insert flag
deepest_folder=$(find nginx-dirs -type d -links 2 -prune | awk '{print length, $0}' | sort -n | cut -d " " -f2- | tail -n1)

touch $deepest_folder/flag

echo $FLAG > $deepest_folder/flag
echo Flag is on $deepest_folder/flag
