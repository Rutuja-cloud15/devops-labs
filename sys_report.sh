#!/bin/bash 

echo "=== HELLO! STARTING SYSTEM HEALTH CHECK ==="
echo "Where am I right now?"
pwd

echo "What files are in this folder?"
ls

echo "What is my local network doing?"
ss -tuln

echo "=== HEALTH CHECK COMPLETE==="

