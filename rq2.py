import json
import requests
import os
import re

"""
This script is for answering RQ1
"""
SWH_API_ENDPOINT = "https://archive.softwareheritage.org/api/1/origin/"

result = {
        "results": [],
        "summary": {
            "count_in_swh": 0,
            "count_not_in_swh": 0
        },
        "links_swh": {
            "count": 0,
            "files": []
        }
    }

def check_swh_presence(github_url):
    try:
        response = requests.get(f"{SWH_API_ENDPOINT}{github_url}/get/")
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking URL {github_url}: {e}")
        return False

def process_repositories(input_file, temp_dir, output_file, output_directory):

    try:
        with open(input_file, 'r') as file:
            repositories = json.load(file)
        print(f"Loaded {len(repositories)} repositories from {input_file}")

    except Exception as e:
        print(f"Could not open {input_file}: {e}")
        return

    for repo in repositories:
        github_url = repo.get("githublink")

        if github_url:
            in_swh = check_swh_presence(github_url)
            result["results"].append({
                "githublink": github_url,
                "in_swh": in_swh
            })
            
            if in_swh:
                result["summary"]["count_in_swh"] += 1
            else:
                result["summary"]["count_not_in_swh"] += 1
        else:
            print(f"No 'github_url' found in entry: {repo}")

    print(f"Processed repositories. In SWH: {result['summary']['count_in_swh']}, Not in SWH: {result['summary']['count_not_in_swh']}")

    url_pattern = re.compile(re.escape(SWH_API_ENDPOINT))
    for root, dirs, files in os.walk(temp_dir):
        if "README.md" in files:
            readme_path = os.path.join(root, "README.md")
            with open(readme_path, "r") as file:
                content = file.read()
            
            if url_pattern.search(content):
                result["links_swh"]["count"] += 1
                result["links_swh"]["files"].append(readme_path)
                print(f"Found a link to SWH in {readme_path}")
            # else:
            #     print(f"URL not found in {readme_path}.")

    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, output_file)

    with open(output_path, 'w') as f:
        json.dump(result, f, indent=4)
    print(f"Results saved to {output_path}")
    print("Final output data:", result)

input_file = input("Enter the name of the JSON file with GitHub links (in the same directory): ")
temp_dir = input("Please input the base directory (e.g., temp_analysis/escape2020): ")
output_file = input("Please input the name of the output file: ")
output_directory = input("Enter the output directory: ")

process_repositories(input_file, temp_dir, output_file, output_directory)
