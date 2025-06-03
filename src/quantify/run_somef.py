import subprocess
import os
import json

def run_somef_on_links(json_file, output_dir, threshold, temp):
    os.makedirs(output_dir, exist_ok=True)
    
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    for i, entry in enumerate(data):
        link = entry.get('github_url')
        if link:
            print(f"Extracting: {link}")
            output_file = os.path.join(output_dir, f"output_{i+1}.json")
            command = f"somef describe -r {link} -o {output_file} -t {threshold} -kt {temp} -p -m"
            subprocess.run(command, shell=True)

json_file = input("Enter the json file: ")
print("You entered:", json_file)

output_dir = input("Enter the output directory: ")
print("You entered: ", output_dir)

threshold = input("Enter the threshold: ")
print("You have entered: ", threshold)

temp = input("Enter the the file where you will store the analysis files (e.g temp_analysis/sshoc): ")
print("You have entered: ", temp)

run_somef_on_links(json_file, output_dir, threshold, temp)