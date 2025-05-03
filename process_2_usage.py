import re
from collections import defaultdict

LOG_FILE = "logfile.txt"

def parse_log_for_pid2(filename):
    usage_by_pid = defaultdict(float)

    pattern = re.compile(r'PID-(\d+),\s*([\d\.]+)(?:s)?')

    with open(filename, "r") as f:
        for line in f:
            for pid, time_str in pattern.findall(line):
                usage_by_pid[pid] += float(time_str)

    return usage_by_pid

def main():
    usage_by_pid = parse_log_for_pid2(LOG_FILE)
    total_time = sum(usage_by_pid.values())
    pid2_time = usage_by_pid.get("2", 0.0)

    if total_time == 0:
        print("No usage data found.")
    else:
        percent = (pid2_time / total_time) * 100
        print(f"PID-2 CPU Usage: {percent:.2f}%")

if __name__ == "__main__":
    main()
