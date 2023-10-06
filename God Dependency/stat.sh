#!/bin/bash

echo "Targets"
echo "---"
echo -e "Nested:\t$(grep -o 'target(' Nested/Package.swift | wc -l)"
echo -e "Flat:\t$(grep -o 'target(' Flat/Package.swift | wc -l)"
echo -e "Nested Tests:\t$(grep -o 'testTarget(' Nested/Package.swift | wc -l)"
echo -e "Flat Tests:\t$(grep -o 'testTarget(' Flat/Package.swift | wc -l)"
echo "---"

total_dirs_Nested=$(find Nested/Sources -type d | wc -l)
total_files_Nested=$(find Nested/Sources -type f | wc -l)
total_dirs_Flat=$(find Flat/Sources -type d | wc -l)
total_files_Flat=$(find Flat/Sources -type f | wc -l)

echo -e "\nFiles"
echo "---"
echo -e "Nested:\t$total_files_Nested"
echo -e "Flat:\t$total_files_Flat"
echo "---"

echo -e "\nDirectories"
echo "---"
echo -e "Nested:\t$total_dirs_Nested"
echo -e "Flat:\t$total_dirs_Flat"
echo "---"