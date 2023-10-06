import os
import random

# Create main directory and sub-directory for sources
if not os.path.exists('Nested'):
    os.mkdir('Nested')
if not os.path.exists('Nested/Sources'):
    os.mkdir('Nested/Sources')

for i in range(0, 250):
    current_module = f"Module{i}"
    os.mkdir(f"Nested/Sources/{current_module}")

    struct_name = f"File{i}"
    
    for submodule in ["Interface", "Mocks", "Sources", "Tests"]:
        os.mkdir(f"Nested/Sources/{current_module}/{submodule}")
        with open(f"Nested/Sources/{current_module}/{submodule}/file{i}_{submodule}.swift", "w") as f:
            if submodule == "Tests":
                f.write(f"import {struct_name}_Mocks \n")    
            f.write(f"struct {struct_name}_{submodule} {{\n")
            f.write(f"    // Implementation\n")
            f.write(f"}}\n")

# Generate Package.swift
with open("Nested/Package.swift", "w") as f:
    f.write("// swift-tools-version:5.3\n")
    f.write("import PackageDescription\n")
    f.write("\n")
    f.write("let package = Package(\n")
    f.write("    name: \"Nested\",\n")
    f.write("    products: [\n")
    f.write("        .library(name: \"Nested\", targets: [\"Module0_Interface\"])  // Just have a module as main product\n")
    f.write("    ],\n")
    f.write("    dependencies: [],\n")
    f.write("    targets: [\n")
    for i in range(0, 250):
        for submodule in ["Interface", "Mocks", "Sources", "Tests"]:
            if submodule == "Tests":
                f.write(f"        .target(name: \"Module{i}_{submodule}\", dependencies: [Module{i}_Mocks], path: \"Sources/Module{i}/{submodule}/\"),\n")        
            else:
                f.write(f"        .target(name: \"Module{i}_{submodule}\", dependencies: [], path: \"Sources/Module{i}/{submodule}/\"),\n")
    f.write("    ]\n")
    f.write(")\n")
