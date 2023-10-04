import os
import random

# Create main directory and sub-directory for sources
if not os.path.exists('Nested'):
    os.mkdir('Nested')
if not os.path.exists('Nested/Sources'):
    os.mkdir('Nested/Sources')

# Dictionary to hold dependencies
dependencies = {}

for i in range(0, 250):
    current_module = f"Module{i}"
    os.mkdir(f"Nested/Sources/{current_module}")

    # Generate random dependencies
    if i > 1:
        possible_deps = random.randint(0, min(2, i-1))
        dependencies[current_module] = random.sample(range(1, i), possible_deps)
        dependencies[current_module] = [f"Module{x}_Interface" for x in dependencies[current_module] if x != i]  # No self-dependency
    else:
        dependencies[current_module] = []

    import_statements = "\n".join([f"import {dep}" for dep in dependencies[current_module]])
    struct_name = f"File{i}"
    
    for submodule in ["Interface", "Mocks", "Other"]:
        os.mkdir(f"Nested/Sources/{current_module}/{submodule}")
        with open(f"Nested/Sources/{current_module}/{submodule}/file{i}_{submodule}.swift", "w") as f:
            f.write(f"{import_statements}\n" if import_statements else "")
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
        dep_str = ", ".join([f"\"{x}\"" for x in dependencies[f"Module{i}"]])
        for submodule in ["Interface", "Mocks", "Other"]:
            f.write(f"        .target(name: \"Module{i}_{submodule}\", dependencies: [{dep_str}], path: \"Sources/Module{i}/{submodule}/\"),\n")        
    f.write("    ]\n")
    f.write(")\n")
