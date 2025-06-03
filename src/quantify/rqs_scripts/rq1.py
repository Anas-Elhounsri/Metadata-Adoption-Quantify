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
    "contributors": {"count": 0, "files": []},
    "license": {"count": 0},
    "codemeta.json": {"count": 0, "files": []},
    "zenodo.json": {"count": 0, "files": []},
    "identifier_extract": {"count": 0, "extracted_values": []},
    "None": {"count": 0}
}

def rq1(directory, temp_dir, missing_key, output_file, output_directory, slice_level=2):

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
                        all_keys_missing = False

            if 'readme_url' in data and 'readme_url' not in missing_categories:
                result['readme_url']['count'] += 1
                all_keys_missing = False

            if 'contributors' in data and 'contributors' not in missing_categories:
                result['contributors']['count'] += 1
                result["contributors"]['files'].append(file_name)
                all_keys_missing = False
            
            if 'license' in data and 'license' not in missing_categories:
                result['license']['count'] += 1
                all_keys_missing = False

            if 'identifier' in data and 'identifier' not in missing_categories:
                for identifier in data["identifier"]:
                    doi_value = identifier.get("result", {}).get("value", "")

                    if doi_value.startswith("https://doi.org/") and "10.5281/zenodo." in doi_value:
                        extracted_part = doi_value.split("https://doi.org/")[-1]
                        result["identifier_extract"]["count"] += 1
                        result["identifier_extract"]["extracted_values"].append(extracted_part)
                        break
                    
                    elif doi_value.startswith("https://zenodo.org/badge/latestdoi/"):
                        extracted_part = doi_value.split("https://zenodo.org/badge/latestdoi/")[-1]
                        result["identifier_extract"]["count"] += 1
                        result["identifier_extract"]["extracted_values"].append(doi_value)
                        break

            if all_keys_missing:
                result['None']['count'] += 1

    packages = ["setup.cfg", "setup.py", "Cargo.toml", "pom.xml", "bower.json", "package.json",
                     "composer.json", "DESCRIPTION.txt", "package.json", "Project.toml", '"nombre".cabal.',
                       '"nombre".gemspec']
    package_files = []
    authors_files = []
    codemeta_files = []

    for root, dirs, files in os.walk(temp_dir):
        
        relative_root = os.path.relpath(root, temp_dir)
        depth = len(relative_root.split(os.sep))

        if "codemeta.json" in files:
            codemeta_path = os.path.join(root, "codemeta.json")
            codemeta_files.append(codemeta_path)

        if ".zenodo.json" in files and depth == 2:
            zenodo_path = os.path.join(root, ".zenodo.json")
            result["zenodo.json"]["count"] += 1
            result["zenodo.json"]["files"].append(zenodo_path)

        if "AUTHORS" in files:
            authors_path = os.path.join(root, "AUTHORS")
            authors_files.append(authors_path)

        for package in packages:
            if package in files:
                package_path = os.path.join(root, package)
                package_files.append(package_path)
                break
        
        unique_packages = {}
        for package_path in package_files:
            relative_root = os.path.relpath(os.path.dirname(package_path), temp_dir)
            sliced_path = os.sep.join(relative_root.split(os.sep)[:slice_level])

            if sliced_path not in unique_packages:
                unique_packages[sliced_path] = package_path

        result["package"]["files"] = list(unique_packages.values())
        result["package"]["count"] = len(unique_packages)

    unique_codemeta = {}
    for codemeta_path in codemeta_files:
        relative_root = os.path.relpath(os.path.dirname(codemeta_path), temp_dir)
        sliced_path = os.sep.join(relative_root.split(os.sep)[:slice_level])

        if sliced_path not in unique_codemeta:
            unique_codemeta[sliced_path] = codemeta_path
    
    result["codemeta.json"]["files"] = list(unique_codemeta.values())
    result["codemeta.json"]["count"] = len(unique_codemeta)
    
    unique_authors = {}
    for authors_path in authors_files:
        relative_root = os.path.relpath(os.path.dirname(authors_path), temp_dir)
        sliced_path = os.sep.join(relative_root.split(os.sep)[:slice_level])

        if sliced_path not in unique_authors:
            unique_authors[sliced_path] = authors_path

    result["authors"]["files"] = list(unique_authors.values())
    result["authors"]["count"] = len(unique_authors)

    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, output_file)
    with open(output_path, 'w') as outfile:
        json.dump(result, outfile, indent=4)
    
    print("Successfully extracted the necessary information!")

def main():
    directory = input("Please input the directory where the SOMEF outputs are: ")
    temp_dir = input("Please input the base directory (e.g., temp_analysis/escape2020): ")
    missing_key = "somef_missing_categories"
    output_file = input("Please name your output file: ")
    output_directory = input("Please input your output directory: ")

    rq1(directory, temp_dir, missing_key, output_file, output_directory)

if __name__ == "__main__":
    main()
