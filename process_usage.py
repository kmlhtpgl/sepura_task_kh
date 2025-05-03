import re
from collections import defaultdict

LOG_FILE = "logfile.txt"

def parse_log(filename):
    usage_by_pid = defaultdict(float)

    pattern = re.compile(r'PID-(\d+),\s*([\d\.]+)(?:s)?')

    with open(filename, "r") as f:
        for line in f:
            for pid, time_str in pattern.findall(line):
                usage_by_pid[pid] += float(time_str)

    return usage_by_pid

def main():
    print("📊 Welcome to the CPU Usage Analyzer!")
    print("This tool helps you calculate CPU time usage by process ID (PID).\n")

    usage_by_pid = parse_log(LOG_FILE)
    total = sum(usage_by_pid.values())

    if total == 0:
        print("No usage data found in the log file.")
        return

    while True:
        pid_input = input("👉 Please enter the PID you want to analyze (e.g., 2): ").strip()
        if pid_input in usage_by_pid:
            usage = usage_by_pid[pid_input]
            percent = (usage / total) * 100
            print(f"\n✅ Process-{pid_input} (PID-{pid_input}) CPU Usage: {percent:.2f}%\n")
            print("🙌 Thank you for using the CPU Usage Analyzer!")
            break
        else:
            print(f"❌ PID-{pid_input} not found in the log data. Please try again.\n")

if __name__ == "__main__":
    main()
