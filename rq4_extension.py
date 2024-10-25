import os
import json

"""
This script is for answering RQ4*
"""

result = {
    "citation": {"bib": 0, "cff": 0, "readme": 0},
    "None": {"count": 0}
}

def rq4_ext(directory, missing_key, output_file, output_directory):

    for file_name in os.listdir(directory):
        if file_name.startswith("output_") and file_name.endswith(".json"):
            file_path = os.path.join(directory, file_name)
            
            with open(file_path, 'r') as file:
                data = json.load(file)
    
            missing_categories = data.get(missing_key, [])

            citation_missing = True

            if 'citation' in data and 'citation' not in missing_categories:
                
                for citation in data["citation"]:
                    format_value = citation.get("result", {}).get("format")
                    
                    if format_value == "bibtex":
                        result["citation"]["bib"] += 1
                        print(f"Found bibtex in {file_name}")

                    elif format_value == "cff":
                        result["citation"]["cff"] += 1
                        print(f"Found cff in {file_name}")

                    elif citation.get("result", {}).get("original_header"):
                        result["citation"]["readme"] += 1
                        print(f"Found original_header in {file_name}")

            if citation_missing:
                result['None']['count'] += 1

    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, output_file)
    with open(output_file, 'w') as outfile:
        json.dump(result, outfile, indent=4)
    
    print("Successfully extracted the necessary information!")

directory = input("Please put the directory: ")
missing_key = "somef_missing_categories"
output_file = input("Please name your output file: ")
output_directory = input("Please input your output directory: ")

rq4_ext(directory, missing_key, output_file, output_directory)
