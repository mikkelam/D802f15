#!/bin/bash

sudo iotop -k -p0 -b -d 0.5 | grep --line-buffered READ: > iotop_disk.txt &
top -b -d 0.5 |grep --line-buffered Mem: > top_mem.txt &
top -b -d 0.5 | grep --line-buffered %Cpu > top_cpu.txt &
