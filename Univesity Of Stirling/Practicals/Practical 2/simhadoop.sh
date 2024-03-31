#!/usr/bin/env bash

cat coffee.txt | ./mapper.py | sort | ./reducer.py > results.txt