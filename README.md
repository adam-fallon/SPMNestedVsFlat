# SPM Nested_250_Targets_300_Directories_250_Files v Flat_250_Targets_250_Directories_250_Files structure

Test bed for comparing;

- Nested_250_Targets_300_Directories_250_Files vs Flat_250_Targets_250_Directories_250_Files Targets.
- Target per submodule vs 1 module with all submodules inside.

## Before Running
1. `python3 -m virtualenv env`
2. `source env/bin/activate`
3. `pip install openpyxl`

# Running
1. `./run.sh`

## Compare
Run `compare.py` to generate an Excel sheet showing the difference in running a `swift build` between the two packages.