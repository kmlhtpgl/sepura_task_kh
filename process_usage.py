import re
from collections import defaultdict

LOG_FILE = "logfile.txt"

def parse_log(filename):
    usage_by_pid = defaultdict(float)
    # This regex will find every "PID-<n>,<number>" in the line,
    # whether or not that number is followed by "s"
    pattern = re.compile(r'PID-(\d+),\s*([\d\.]+)(?:s)?')

    with open(filename, "r") as f:
        for line in f:
            for pid, time_str in pattern.findall(line):
                usage_by_pid[pid] += float(time_str)

    return usage_by_pid

def main():
    usage_by_pid = parse_log(LOG_FILE)
    if not usage_by_pid:
        print("No PID usage data found in the log.")
        return

    total = sum(usage_by_pid.values())

    # Let the user pick which PID to report on
    print("PIDs found:", ", ".join(sorted(usage_by_pid.keys())))
    choice = input("Enter the PID number you want to calculate (e.g. 1, 2, 3): ").strip()

    if choice not in usage_by_pid:
        print(f"PID-{choice} not found.")
        return

    pid_usage = usage_by_pid[choice]
    percent = (pid_usage / total) * 100
    print(f"Process-{choice} (PID-{choice}) CPU Usage: {percent:.2f}%")

if __name__ == "__main__":
    main()
