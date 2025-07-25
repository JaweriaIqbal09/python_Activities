import time
import os

# Step 1: Ask how many files the user wants to analyze
try:
    total_files = int(input("How many Python files do you want to analyze? "))
except ValueError:
    print("❌ Invalid number. Please enter an integer.")
    exit()

file_names = []
print("\n Now enter the names of those Python files (e.g., script.py):")

folder = "D:\\PYTHON\\introductory"
for i in range(total_files):
    name = input(f"File {i+1} of {total_files}: ").strip()
    if not name.endswith(".py"):
        name += ".py"
    full_path = os.path.join(folder, name)
    file_names.append(full_path)
min_time = None
max_time = None
fastest_file = ""
slowest_file = ""

print("\n📊 File Analysis:\n")

# Step 2: Analyze each file
for file_name in file_names:
    if not os.path.isfile(file_name):
        print(f"⚠ File not found: {file_name}\n")
        continue

    print(f" Analyzing: {file_name} ...")

    try:
        start_time = time.time()

        with open(file_name, "r", encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()

        loc = 0  # Count lines of code
        for line in lines:
            stripped = line.strip()
            if stripped == "" or stripped.startswith("#"):
                continue
            loc += 1

        end_time = time.time()
        time_taken = end_time - start_time

        print(f" LOC (Lines of Code): {loc}")
        print(f" Time Taken: {time_taken:.4f} seconds\n")

        if min_time is None or time_taken < min_time:
            min_time = time_taken
            fastest_file = file_name

        if max_time is None or time_taken > max_time:
            max_time = time_taken
            slowest_file = file_name

    except Exception as e:
        print(f"❌ Error reading {file_name}: {e}\n")

# Step 3: Summary
print("Summary:\n")
if fastest_file:
    print(f"🚀 Fastest File: {fastest_file} ({min_time:.4f} seconds)")
if slowest_file:
    print(f"🐌 Slowest File: {slowest_file} ({max_time:.4f} seconds)")

if fastest_file and slowest_file and fastest_file != slowest_file:
    print(" Observation: Larger or more complex files generally took more time, but not always.\n")
else:
    print(" Observation: All files took similar time or only one valid file was analyzed.\n")
