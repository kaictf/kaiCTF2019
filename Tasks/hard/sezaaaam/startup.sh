#!/usr/bin/bash

# Delete already existing folders
rm -rf levels
rm -rf nginx-dirs

# Make scripts executable
chmod +x create_dir.sh
chmod +x create_level.sh

# Create level passwords
./create_level.sh

# Create random directories and put flag into one of the largest paths
./create_dir.sh | tee flag_path

# Create nginx configuration
python3 prepare_nginx.py

# Start container
docker-compose restart
docker-compose up -d