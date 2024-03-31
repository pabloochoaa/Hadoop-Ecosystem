#!/usr/bin/env bash

cat r5.txt | ./mapper.py > mapout.txt
sort mapout.txt | ./combiner.py > comout.txt 
sort comout.txt | ./reducer.py > results.txt