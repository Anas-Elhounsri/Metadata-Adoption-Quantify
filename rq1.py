import os
import json

"""
This script is for answering RQ1
"""
result = {
    "citation.cff": {"count": 0},
    "readme_url": {"count": 0},
    "package": {"count": 0, "files": []},
    "authors": {"count": 0, "files": []},
    "contributors": {"count": 0},
    "license": {"count": 0},
    "codemeta.json": {"count": 0, "files": []},
    "zenodo.json": {"count": 0, "files": []},
    "identifier_extract": {"count": 0, "extracted_values": []},
    "None": {"count": 0}
}

def rq1(directory, temp_dir, missing_key, output_file, output_directory):

    for file_name in os.listdir(directory):

        if file_name.startswith("output_") and file_name.endswith(".json"):
            file_path = os.path.join(directory, file_name)
            
            with open(file_path, 'r') as file:
                data = json.load(file)
            
            missing_categories = data.get(missing_key, [])
            all_keys_missing = True

            if 'citation' in data and 'citation' not in missing_categories:
                for citation in data["citation"]:
                    format_value = citation.get("result", {}).get("format")
                    if format_value == "cff":
                        result["citation.cff"]["count"] += 1
                        print(f"Found citation.cff in {file_name}")
                        all_keys_missing = False

            if 'readme_url' in data and 'readme_url' not in missing_categories:
                result['readme_url']['count'] += 1
                all_keys_missing = False

            if 'contributors' in data and 'contributors' not in missing_categories:
                result['contributors']['count'] += 1 
                all_keys_missing = False
            
            if 'license' in data and 'license' not in missing_categories:
                result['license']['count'] += 1
                all_keys_missing = False

            if 'identifier' in data and 'identifier' not in missing_categories:
                for identifier in data["identifier"]:
                    doi_value = identifier.get("result", {}).get("value", "")
                    
                    if doi_value.startswith("https://doi.org/"):
                        extracted_part = doi_value.split("https://doi.org/")[-1]
                        result["identifier_extract"]["count"] += 1
                        result["identifier_extract"]["extracted_values"].append(extracted_part)
                        print(f"Extracted '{extracted_part}' from {file_name}")
                        break

            if all_keys_missing:
                result['None']['count'] += 1

    packages = ["setup.cfg", "	setup.py", "Cargo.toml", "pom.xml", "bower.json", "package.json",
                     "composer.json", "DESCRIPTION.txt", "package.json", "	Project.toml", '"nombre".cabal.', '"nombre".gemspec']
    
    for root, dirs, files in os.walk(temp_dir):
        if "codemeta.json" in files:
            result["codemeta.json"]["count"] += 1
            result["codemeta.json"]["files"].append(os.path.join(root, "codemeta.json"))
            print(f"Found codemeta.json in {root}")

        if ".zenodo.json" in files:
            result["zenodo.json"]["count"] += 1
            result["zenodo.json"]["files"].append(os.path.join(root, "zenodo.json"))
            print(f"Found zenodo.json in {root}")

        if "AUTHORS" in files:
            result["authors"]["count"] += 1
            result["authors"]["files"].append(os.path.join(root, "AUTHORS"))
            print(f"Found AUTHORS in {root}")

        for package in packages:
            if package in files:
                result["package"]["count"] += 1
                result["package"]["files"].append(os.path.join(root, package))
                break

    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, output_file)
    with open(output_path, 'w') as outfile:
        json.dump(result, outfile, indent=4)
    
    print("Successfully extracted the necessary information!")

directory = input("Please input the directory where the SOMEF outputs are: ")
temp_dir = input("Please input the base directory (e.g., temp_analysis/escape2020): ")
missing_key = "somef_missing_categories"
output_file = input("Please name your output file: ")
output_directory = input("Please input your output directory: ")

rq1(directory, temp_dir, missing_key, output_file, output_directory)

