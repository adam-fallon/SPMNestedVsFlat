import os
import random

# Create main directory and sub-directory for sources
if not os.path.exists('Flat'):
    os.mkdir('Flat')
if not os.path.exists('Flat/Sources'):
    os.mkdir('Flat/Sources')
if not os.path.exists('Flat/Tests'):
    os.mkdir('Flat/Tests')

# Dictionary to hold dependencies
dependencies = {}

for i in range(0, 250):
    current_module = f"Module{i}"
    os.mkdir(f"Flat/Sources/{current_module}")
    os.mkdir(f"Flat/Tests/{current_module}Tests")

    struct_name = f"File{i}"

    with open(f"Flat/Sources/{current_module}/file{i}.swift", "w") as f:
        f.write(f"struct {struct_name} {{\n")
        f.write(f"    // Implementation\n")
        f.write(f"}}\n")
    
    with open(f"Flat/Tests/{current_module}Tests/file{i}.swift", "w") as f:
        if i > 1:
            f.write("import Mocks")
        f.write(f"struct {struct_name}Test {{\n")
        f.write(f"    // Implementation\n")
        f.write(f"}}\n")
    
    for submodule in ["Sources", "Interface", "Mocks", "Other"]:
        os.mkdir(f"Flat/Sources/{current_module}/{submodule}")
        with open(f"Flat/Sources/{current_module}/{submodule}/file{i}_{submodule}.swift", "w") as f:

            f.write(f"struct {struct_name}_{submodule} {{\n")
            f.write(f"    // Implementation\n")
            f.write(f"}}\n")

if not os.path.exists('Flat/Sources/Mocks'):
    os.mkdir('Flat/Sources/Mocks')

# Generate Package.swift
with open("Flat/Package.swift", "w") as f:
    f.write("// swift-tools-version:5.3\n")
    f.write("import PackageDescription\n")
    f.write("\n")
    f.write("let package = Package(\n")
    f.write("    name: \"Flat\",\n")
    f.write("    products: [\n")
    f.write("        .library(name: \"Flat\", targets: [\"Module1\"])  // Example: first module as main product\n")
    f.write("    ],\n")
    f.write("    dependencies: [],\n")
    f.write("    targets: [\n")
    f.write(f"        .target(name: \"Mocks\", dependencies: []),\n")
    for i in range(0, 250):
        f.write(f"        .target(name: \"Module{i}\", dependencies: []),\n")
        f.write(f"        .testTarget(name: \"Module{i}Tests\", dependencies: [\"Mocks\"]),\n")
    f.write("    ]\n")
    f.write(")\n")
