# Process-2 CPU Usage Analyzer

This Python script analyzes a log file and calculates the percentage of CPU time used by **Process-2 (PID-2)**.

## Problem Description

You’re given a log file that records CPU usage for three processes (PID-1, PID-2, PID-3). Each line in the log includes:

- A timestamp  
- The process ID (e.g., PID-2)  
- The CPU time used in seconds (e.g., `0.675s`)  
- An identifier

Example log line:

[TIMESTAMP], PID-[X], [CPU TIME]s, [SESSION ID]

Example:
2025-04-22  14:32:31.429, PID-2,0.675s,G6kVdT1jNw


## How It Works

The script:
1. Reads each line from the log file.
2. Extracts the process ID and CPU usage time.
3. Sums up the CPU time per process.
4. Calculates PID-2's share as a percentage of total usage.

## Requirements

- Python 3 installed  
  You can check by running:
  ```bash
  python --version

## Project Structure
project-folder/
-logfile.txt          # Your log file
-process_usage.py     # The Python script
-README.md            # This readme file

## Output

Process-2 (PID-2) CPU Usage: 81.02%

