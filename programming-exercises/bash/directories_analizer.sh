#!/bin/bash

# Define the directories to check (you can change these)
DIRECTORIES=("/home/usuario" "/var" "/etc" "/opt")

# Check if the user has specified a directory or use default ones
if [ ! -z "$1" ]; then
    DIRECTORIES=("$1")
fi

# Function to analyze disk usage in a directory
analyze_usage() {
    local dir=$1
    echo "Analyzing disk usage for: $dir"
    
    # Get the top 10 largest directories and files (sorted by size)
    du -ah $dir 2>/dev/null | sort -rh | head -n 10
}

# Function to find large files over a specific size (e.g., 100MB)
find_large_files() {
    local size_limit="100M"  # Change this to your desired size
    echo "Searching for files larger than $size_limit..."
    
    # Find and list large files
    find / -type f -size +$size_limit 2>/dev/null
}

# Main script execution
echo "Disk Usage Analyzer - Started at $(date)"

# Loop through each directory and analyze its disk usage
for dir in "${DIRECTORIES[@]}"; do
    analyze_usage $dir
done

# Optionally find large files (over 100MB)
find_large_files

echo "Disk Usage Analyzer - Finished at $(date)"
exit 0
