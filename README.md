# SPM Nested v Flat structure

Creates two SPM Packages, Nested + Flat.

Nested creates a module per subsystem; { Interface, Mocks, Other } while Flat creates 1 module that has all of those things under 1 folder.

## Before Running
1. `python3 -m virtualenv env`
2. `source env/bin/activate`
3. `pip install openpyxl`

## Flat
Flat has a flatter structure, with numerous files per module, but only 1 target

So;
```
> Module0
    Interface.swift
    Mock.swift
    Other.swift
    ...
```

Run `generate_flat.py` to create this Package

## Nested
Nested has nested Modules, with lots of folders - each with their own target in Package.swift

So;
```
> Module0
    > Interface
        Interface.swift
    > Mocks
        Mocks.swift
    > Other
        Other.swift
```

Run `generate_nested.py` to create this Package

## Compare
Run `compare.py` to generate an Excel sheet showing the difference in running a `swift build` between the two packages.