#!/bin/bash
#source $(pwd)/venv/bin/activate &&
cd ../
source ./venv/bin/activate
cd executables && ./test1.py $@
