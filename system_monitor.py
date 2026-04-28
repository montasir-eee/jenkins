import os
import datetime
import subprocess

def header():
    print("=" * 40)
    print("SYSTEM MONITOR REPORT")
    print("Current Date:", datetime.datetime.now().strftime("%Y-%m-%d"))
    print("Current Time:", datetime.datetime.now().strftime("%H:%M:%S"))
    print("Full Timestamp:", datetime.datetime.now())
    print("=" * 40)

def run_command(command, title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)
    
    result = subprocess.getoutput(command)
    print(result)

def main():
    header()

    # CPU / Process info
    run_command("top -b -n 1 | head -n 15", "🔥 CPU & Memory Usage")

    # Disk usage
    run_command("df -h", "💽 Disk Usage")

    # Memory usage
    run_command("free -h", "🧠 Memory Usage")

    print("\nDone.")

if __name__ == "__main__":
    main()
