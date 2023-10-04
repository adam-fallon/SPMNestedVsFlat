# SPM Structure Test Bench

Test Bench to test;

1. Does having more folders slow down swift build down in comparison to less folders?  
2. Does having a target per module slow swift build down in comparison to less targets? 

# Running
1. `cd <TEST>` (i.e `cd FileIO`) 
2. `python3 -m virtualenv env`
3. `source env/bin/activate`
4. `pip install openpyxl`
5. `./run.sh`
6. `python compare.py`