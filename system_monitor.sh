#!/bin/bash

echo "==============================="
echo "SYSTEM MONITOR REPORT"
echo "Current Date: $(date '+%Y-%m-%d')"
echo "Current Time: $(date '+%H:%M:%S')"
echo "Full Timestamp: $(date)"
echo "==============================="

echo ""
echo "🔥 Top CPU & Memory processes (snapshot)"
top -b -n 1 | head -n 15

echo ""
echo "==============================="
echo "Disk Usage"
df -h

echo ""
echo "==============================="
echo "Memory Usage"
free -h

echo ""
echo "==============================="
echo "Uptime"
uptime

echo ""
echo "Done."
