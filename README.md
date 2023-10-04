# SPM Structure Test Bench

Test Bench to test;

1. Does having more folders slow down swift build down in comparison to less folders?  
2. Does having a target per module slow swift build down in comparison to less targets? 

## Before Running
1. `python3 -m virtualenv env`
2. `source env/bin/activate`
3. `pip install openpyxl`

# Running
1. `./run.sh`

## Compare
Run `compare.py` to generate an Excel sheet showing the difference in running a `swift build` between the two packages.