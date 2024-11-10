import os
import json
import re

result = {
    "description": {"count_short": 0, "count_long": 0},
    "no_description": {"count":0},
    "license": {
        "spdx": {"count": 0, "licenses": []},
        "no_spdx": {"count": 0, "licenses": []},
        "no_license":{"count": 0}
    },
    "installation": {"count": 0},
    "requirements": {"count": 0},
    "download": {"count": 0},
    "documentation": {"count": 0}
    #"authors_id": {"count": 0, "files": [], "ORCID_count": 0}
}

# identifiers_pattern = re.compile(r'(ORCID|ID-HAL|ID-REF|GPG key|VIAF|ISNI)', re.IGNORECASE)
# orcid_pattern = re.compile(r'\bhttps?://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]\b', re.IGNORECASE)

# def check_authors_identifiers(authors_file_path):
#     try:
#         with open(authors_file_path, 'r', encoding='utf-8', errors='ignore') as authors_file:
#             authors_content = authors_file.readlines()
#     except UnicodeDecodeError as e:
#         print(f"UnicodeDecodeError reading {authors_file_path}: {e}")
#         return False, False 

#     identified = False
#     orcid_found = False

#     for line in authors_content:

#         if identifiers_pattern.search(line):
#             identified = True

#         if orcid_pattern.search(line):
#             orcid_found = True
#             break

#     return identified, orcid_found

# def process_authors_files(temp_analysis_directory):
#     for root, dirs, files in os.walk(temp_analysis_directory):
#         for file_name in files:
#             if file_name == "AUTHORS":
#                 authors_file_path = os.path.join(root, file_name)
#                 identifier_found, orcid_found = check_authors_identifiers(authors_file_path)

#                 if identifier_found:
#                     result["authors_id"]["count"] += 1
#                     result["authors_id"]["files"].append(authors_file_path)

#                 if orcid_found:
#                     result["authors_id"]["ORCID_count"] += 1
#                     print(f"Found ORCID in {authors_file_path}")
#                     break

def process_json_files(json_files_directory):
    for root, dirs, files in os.walk(json_files_directory):
        for file_name in files:
            if file_name.startswith("output_") and file_name.endswith(".json"):
                file_path = os.path.join(root, file_name)

                with open(file_path, 'r') as file:
                    data = json.load(file)

                spdx_found = False
                # if "license" in data.get("somef_missing_categories", []):
                #     result["no_license"]["count"] += 1

                if "license" in data:
                    for license_entry in data["license"]:
                        license_result = license_entry.get("result", {})
                        license_name = license_result.get("name", "Unknown License")
                        spdx_id = license_result.get("spdx_id")

                        if spdx_id:
                            result["license"]["spdx"]["count"] += 1
                            result["license"]["spdx"]["licenses"].append({"file": file_name, "name": license_name, "spdx_id": spdx_id})
                            spdx_found = True
                            break


                    if not spdx_found:
                        result["license"]["no_spdx"]["count"] += 1
                        result["license"]["no_spdx"]["licenses"].append({"file": file_name, "name": license_name})
                
                else:
                    result["license"]["no_license"]["count"] += 1

                if "installation" in data and "installation" not in data.get("somef_missing_categories", []):
                    for tech_type in data["installation"]:
                        if tech_type.get("technique") != "supervised_classification":
                            result["installation"]["count"] += 1
                            print("Found installation!")
                            break

                if "requirements" in data and "installation" not in data.get("somef_missing_categories", []):
                    result["requirements"]["count"] += 1

                if "download" in data and "installation" not in data.get("somef_missing_categories", []):
                    result["download"]["count"] += 1

                if "documentation" in data and "documentation" not in data.get("somef_missing_categories", []):
                    result["documentation"]["count"] += 1

                if "description" in data.get("somef_missing_categories", []):
                    result["no_description"]["count"] += 1

                elif "description" in data:
                    for desc_entry in data["description"]:
                        if desc_entry.get("technique") == "GitHub_API":
                            result["description"]["count_short"] += 1

                        if "README.md" in desc_entry.get("source", ""):
                            result["description"]["count_long"] += 1
                            break

#temp_analysis_directory = input("Enter the temp_analysis directory: ")

json_files_directory = input("Enter the directory containing JSON files: ")

# process_authors_files(temp_analysis_directory)

process_json_files(json_files_directory)

output_file = input("Enter the output filename: ")
output_directory = input("Enter the output directory: ")
os.makedirs(output_directory, exist_ok=True)

with open(os.path.join(output_directory, output_file), 'w') as f:
    json.dump(result, f, indent=4)

print(f"Results saved to {os.path.join(output_directory, output_file)}")