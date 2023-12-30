#!/bin/bash

# List all processes with their PIDs and command names
# An alternative to the AppImage for those who want a pure bash script
ps -e -o pid=,comm= | while read -r proc_pid proc_name
do
    # Check if the environment file exists for the process
    if [ -f /proc/$proc_pid/environ ]; then
        # Attempt to get DRI_PRIME setting for the process
        gpu_usage=$(grep -az "DRI_PRIME" /proc/$proc_pid/environ)

        # If DRI_PRIME is set, display the process information
        if [ ! -z "$gpu_usage" ]; then
            # Display process name, PID, and GPU usage info
            echo "Process '${proc_name}' (ID ${proc_pid}) is using GPU: ${gpu_usage}"
        fi
    fi
done
