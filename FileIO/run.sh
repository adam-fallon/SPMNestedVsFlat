#!/bin/sh

set -euo pipefail

rm -rf Nested;
rm -rf Flat;

python3 generate_nested.py && python3 generate_flat.py

sh stat.sh