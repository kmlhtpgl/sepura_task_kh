import re
from collections import defaultdict

LOG_FILE = "logfile.txt"

def parse_log(filename):
    usage_by_pid = defaultdict(float)

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 3:
                pid_match = re.search(r'PID-(\d+)', parts[1])
                time_match = re.search(r'(\d+\.\d+)s', parts[2])
                if pid_match and time_match:
                    pid = pid_match.group(1)
                    time_used = float(time_match.group(1))
                    usage_by_pid[pid] += time_used

    return usage_by_pid

def main():
    usage_by_pid = parse_log(LOG_FILE)
    total = sum(usage_by_pid.values())
    pid2 = usage_by_pid.get("2", 0.0)

    if total == 0:
        print("No usage data found.")
    else:
        percent = (pid2 / total) * 100
        print(f"Process-2 (PID-2) CPU Usage: {percent:.2f}%")

if __name__ == "__main__":
    main()
