#!/bin/bash

echo "Targets"
echo "---"
echo -e "Nested:\t$(grep -o 'target(' Nested/Package.swift | wc -l)"
echo -e "Flat:\t$(grep -o 'target(' Flat/Package.swift | wc -l)"
echo "---"

total_dirs_nested=$(find Nested/Sources -type d | wc -l)
total_files_nested=$(find Nested/Sources -type f | wc -l)
total_dirs_flat=$(find Flat/Sources -type d | wc -l)
total_files_flat=$(find Flat/Sources -type f | wc -l)

echo -e "\nFiles"
echo "---"
echo -e "Nested:\t$total_files_nested"
echo -e "Flat:\t$total_files_flat"
echo "---"

echo -e "\nDirectories"
echo "---"
echo -e "Nested:\t$total_dirs_nested"
echo -e "Flat:\t$total_dirs_flat"
echo "---"