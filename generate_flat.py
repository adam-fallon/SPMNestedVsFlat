import os
import random

# Create main directory and sub-directory for sources
if not os.path.exists('Flat'):
    os.mkdir('Flat')
if not os.path.exists('Flat/Sources'):
    os.mkdir('Flat/Sources')

# Dictionary to hold dependencies
dependencies = {}

for i in range(0, 250):
    current_module = f"Module{i}"
    os.mkdir(f"Flat/Sources/{current_module}")

    # Generate random dependencies
    if i > 1:
        possible_deps = random.randint(0, min(2, i-1))
        dependencies[current_module] = random.sample(range(1, i), possible_deps)
        dependencies[current_module] = [f"Module{x}" for x in dependencies[current_module] if x != i]  # No self-dependency
    else:
        dependencies[current_module] = []

    import_statements = "\n".join([f"import {dep}" for dep in dependencies[current_module]])
    struct_name = f"File{i}"

    with open(f"Flat/Sources/{current_module}/file{i}.swift", "w") as f:
        f.write(f"{import_statements}\n" if import_statements else "")
        f.write(f"struct {struct_name} {{\n")
        f.write(f"    // Implementation\n")
        f.write(f"}}\n")

    for submodule in ["Interface", "Mocks", "Other"]:
        with open(f"Flat/Sources/{current_module}/file{i}_{submodule}.swift", "w") as f:
            f.write(f"{import_statements}\n" if import_statements else "")
            f.write(f"struct {struct_name}_{submodule} {{\n")
            f.write(f"    // Implementation\n")
            f.write(f"}}\n")

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
    for i in range(0, 250):
        dep_str = ", ".join([f"\"{x}\"" for x in dependencies[f"Module{i}"]])
        f.write(f"        .target(name: \"Module{i}\", dependencies: [{dep_str}]),\n")
    f.write("    ]\n")
    f.write(")\n")
