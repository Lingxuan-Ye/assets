#!/usr/bin/env bash

# this script must be executed top level directory of 'assets'

python ./scripts/run.py $@

# exit prompt
echo
read -p 'Press any key to exit...' -n 1
