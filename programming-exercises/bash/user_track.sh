#!/bin/bash

# Define log file location
LOG_FILE="/var/log/user_activity.log"

# Function to track command history
track_commands() {
    echo "Tracking commands run by users..." >> $LOG_FILE
    history -a  # Append the current session's history to the history file
    cat ~/.bash_history >> $LOG_FILE  # Log the user's command history
    echo "Commands logged at $(date)" >> $LOG_FILE
}

# Function to track login and logout times
track_login_logout() {
    echo "Tracking login/logout times..." >> $LOG_FILE
    last -F >> $LOG_FILE  # Use `last` to show all login/logout times
    echo "Login/logout times logged at $(date)" >> $LOG_FILE
}

# Function to track file activity
track_file_activity() {
    echo "Tracking file access/modification..." >> $LOG_FILE
    # Use the `auditd` system service (if installed) to monitor file access/modification
    ausearch -m execve -ts recent >> $LOG_FILE  # Search for commands that have been executed
    echo "File activity logged at $(date)" >> $LOG_FILE
}

# Main script execution
echo "User Activity Tracker started at $(date)" >> $LOG_FILE

# Call the tracking functions
track_commands
track_login_logout
track_file_activity

echo "User Activity Tracker finished at $(date)" >> $LOG_FILE

exit 0
