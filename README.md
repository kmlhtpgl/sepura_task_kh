# 🧠 CPU Usage Analyzer – Log Parsing Tools

This repository contains two Python scripts designed to analyze CPU usage from a `logfile.txt` based on process IDs (PIDs). These tools are helpful for understanding how much CPU time specific processes consume.

---

## 📁 Files Included

- `pid2_usage_analyzer.py` – Focuses specifically on CPU usage by **PID-2**
- `interactive_pid_analyzer.py` – Interactive tool that lets you choose any PID dynamically

---

## 🔧 Prerequisites

- Python 3.x
- A log file named `logfile.txt` in the same directory  
  (Format must include lines like: `timestamp, PID-3, 0.456s`)

---

## 📄 Log File Format Example


Example log line:

[TIMESTAMP], PID-[X], [CPU TIME]s, [SESSION ID]

Example:
2025-04-22  14:32:31.429, PID-2,0.675s,G6kVdT1jNw

## PID-2 Usage

## How It Works

The script:
1. Reads each line from the log file.
2. Extracts the process ID and CPU usage time.
3. Sums up the CPU time per process.
4. Calculates PID-2's share as a percentage of total usage.

## How to Use

1. Save your log file as logfile.txt and place it in the same directory as the script.

2. Save the script as process_2_usage.py in the same folder.

3. Open a terminal or command prompt and navigate to the folder.

4. Run the script:
```bash
    python process_usage.py
```

## Output

Process-2 (PID-2) CPU Usage: 81.02%


## Interactive PID Analyzer

## How It Works

1. The script welcomes you and describes its purpose.

2. You enter the PID you're interested in (e.g., 3).

3. If the PID exists in the log, it shows the usage percentage.

4. If not, it prompts you to try again.

5. Ends with a thank you message.

## How to Use

Run the script:
```bash
    python process_usage.py
```

## Output

📊 Welcome to the CPU Usage Analyzer!
This tool helps you calculate CPU time usage by process ID (PID).

👉 Please enter the PID you want to analyze (e.g., 2): 3

✅ Process-3 (PID-3) CPU Usage: 41.87%

🙌 Thank you for using the CPU Usage Analyzer!

## Notes
- Time values like 0.567s are parsed as 0.567 (float) for computation.

- If no valid lines are found in the log, a warning message appears.

# License
This project is for educational or interview demonstration purposes. No license restrictions.

## Author
Developed by Kemal Hatipoglu – feel free to contribute or adapt for your own use cases!


---

Would you like me to include this in a downloadable `.md` file for you?
