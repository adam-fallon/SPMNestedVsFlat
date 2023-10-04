#!/bin/sh

set -euo pipefail

rm -rf Nested_250_Targets_300_Directories_250_Files;
rm -rf Flat_250_Targets_250_Directories_250_Files;

python3 generate_nested.py && python3 generate_flat.py

sh stat.sh