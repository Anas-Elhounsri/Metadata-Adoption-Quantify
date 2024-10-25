import os
import json
import re

result = {
    "description": {"count_short": 0, "count_long": 0},
    "license": {
        "spdx": {"count": 0, "licenses": []},
        "no_spdx": {"count": 0, "licenses": []}
    },
    "installation": {"count": 0},
    "requirements": {"count": 0},
    "download": {"count": 0},
    "documentation": {"count": 0},
    "authors_id": {"count": 0, "files": []}
}

identifiers_pattern = re.compile(r'(ORCID|ID-HAL|ID-REF|GPG key|VIAF|ISNI)', re.IGNORECASE)

def check_authors_identifiers(authors_file_path):
    with open(authors_file_path, 'r') as authors_file:
        authors_content = authors_file.readlines()

    all_identified = True
    for line in authors_content:
        if not identifiers_pattern.search(line):
            all_identified = False
            break

    return all_identified


def process_authors_files(temp_analysis_directory):
    for root, dirs, files in os.walk(temp_analysis_directory):
        for file_name in files:
            if file_name == "AUTHORS":
                authors_file_path = os.path.join(root, file_name)
                if check_authors_identifiers(authors_file_path):
                    result["authors_id"]["count"] += 1
                    result["authors_id"]["files"].append(authors_file_path)

def process_json_files(json_files_directory):
    for root, dirs, files in os.walk(json_files_directory):
        for file_name in files:
            if file_name.startswith("output_") and file_name.endswith(".json"):
                file_path = os.path.join(root, file_name)

                with open(file_path, 'r') as file:
                    data = json.load(file)

                license_found = False
                if "license" in data:
                    for license_entry in data["license"]:
                        license_result = license_entry.get("result", {})
                        license_name = license_result.get("name", "Unknown License")
                        spdx_id = license_result.get("spdx_id")

                        if spdx_id:
                            result["license"]["spdx"]["count"] += 1
                            result["license"]["spdx"]["licenses"].append({"file": file_name, "name": license_name, "spdx_id": spdx_id})
                            license_found = True
                            break

                    if not license_found:
                        result["license"]["no_spdx"]["count"] += 1
                        result["license"]["no_spdx"]["licenses"].append({"file": file_name, "name": license_name})

                if "installation" in data and "installation" not in data.get("somef_missing_categories", []):
                    result["installation"]["count"] += 1

                if "requirements" in data and "installation" not in data.get("somef_missing_categories", []):
                    result["requirements"]["count"] += 1

                if "download" in data and "installation" not in data.get("somef_missing_categories", []):
                    result["download"]["count"] += 1

                if "documentation" in data and "documentation" not in data.get("somef_missing_categories", []):
                    result["documentation"]["count"] += 1

                if "description" in data and "description" not in data.get("somef_missing_categories", []):
                    for desc_entry in data["description"]:
                        if desc_entry.get("technique") == "GitHub_API":
                            result["description"]["count_short"] += 1
                        if "README.md" in desc_entry.get("source", ""):
                            result["description"]["count_long"] += 1
                            break

temp_analysis_directory = input("Enter the temp_analysis directory: ")

json_files_directory = input("Enter the directory containing JSON files: ")

process_authors_files(temp_analysis_directory)

process_json_files(json_files_directory)

output_file = input("Enter the output filename: ")
output_directory = input("Enter the output directory: ")
os.makedirs(output_directory, exist_ok=True)

with open(os.path.join(output_directory, output_file), 'w') as f:
    json.dump(result, f, indent=4)

print(f"Results saved to {os.path.join(output_directory, output_file)}")