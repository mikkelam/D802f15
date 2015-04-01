#!/bin/bash

cat top_cpu.txt | cut -c 37-40 > log_cpu.txt & 
cat top_mem.txt | cut -c 41-49 > log_mem.txt & 
cat iotop_disk.txt | cut -c 19-26 > log_disk.txt &
