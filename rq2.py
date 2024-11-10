import json
import requests
import os
import time


"""
This script is for answering RQ1
"""
SWH_API_ENDPOINT = "https://archive.softwareheritage.org/api/1/origin/"

TOKEN1 = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhMTMxYTQ1My1hM2IyLTQwMTUtODQ2Ny05MzAyZjk3MTFkOGEifQ.eyJpYXQiOjE3MzA2NDkxMDksImp0aSI6Ijk0MmFiMGUyLWRlM2EtNDQ2ZS1hZGM3LWRhYjFjNGYwMjA2YyIsImlzcyI6Imh0dHBzOi8vYXV0aC5zb2Z0d2FyZWhlcml0YWdlLm9yZy9hdXRoL3JlYWxtcy9Tb2Z0d2FyZUhlcml0YWdlIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLnNvZnR3YXJlaGVyaXRhZ2Uub3JnL2F1dGgvcmVhbG1zL1NvZnR3YXJlSGVyaXRhZ2UiLCJzdWIiOiJmMjdlYmRmMC03YTQzLTQ4YTktODQ0Zi1kZjUwMmNmZjk2NDYiLCJ0eXAiOiJPZmZsaW5lIiwiYXpwIjoic3doLXdlYiIsInNlc3Npb25fc3RhdGUiOiI0NjYyOTI2MS03Yzk2LTRlODYtYTU0ZS1iYzEwM2UwMTZjZGIiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVtYWlsIn0.fc8QNoudDxFwm8MIOn2z9KqDlGHYxehMsNTCMZYiWAU"
TOKEN2 = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhMTMxYTQ1My1hM2IyLTQwMTUtODQ2Ny05MzAyZjk3MTFkOGEifQ.eyJpYXQiOjE3MzA2NzM5NDIsImp0aSI6IjMyZmFlYjNkLWM2MzUtNGZjYy04MjRmLTU0NDRlZGY3Y2MyMSIsImlzcyI6Imh0dHBzOi8vYXV0aC5zb2Z0d2FyZWhlcml0YWdlLm9yZy9hdXRoL3JlYWxtcy9Tb2Z0d2FyZUhlcml0YWdlIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLnNvZnR3YXJlaGVyaXRhZ2Uub3JnL2F1dGgvcmVhbG1zL1NvZnR3YXJlSGVyaXRhZ2UiLCJzdWIiOiJmMjdlYmRmMC03YTQzLTQ4YTktODQ0Zi1kZjUwMmNmZjk2NDYiLCJ0eXAiOiJPZmZsaW5lIiwiYXpwIjoic3doLXdlYiIsInNlc3Npb25fc3RhdGUiOiI0NjYyOTI2MS03Yzk2LTRlODYtYTU0ZS1iYzEwM2UwMTZjZGIiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVtYWlsIn0.gH570Eq4ehrFhz5gIUGa-UOrGtymBzky5oh92fYZwis"
TOKEN3 = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhMTMxYTQ1My1hM2IyLTQwMTUtODQ2Ny05MzAyZjk3MTFkOGEifQ.eyJpYXQiOjE3MzA2NDkxMjIsImp0aSI6Ijg2Yzc1OGQzLWFkNDgtNGNhZi05NTk1LWQ4YjI0MTViMjMxYiIsImlzcyI6Imh0dHBzOi8vYXV0aC5zb2Z0d2FyZWhlcml0YWdlLm9yZy9hdXRoL3JlYWxtcy9Tb2Z0d2FyZUhlcml0YWdlIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLnNvZnR3YXJlaGVyaXRhZ2Uub3JnL2F1dGgvcmVhbG1zL1NvZnR3YXJlSGVyaXRhZ2UiLCJzdWIiOiJmMjdlYmRmMC03YTQzLTQ4YTktODQ0Zi1kZjUwMmNmZjk2NDYiLCJ0eXAiOiJPZmZsaW5lIiwiYXpwIjoic3doLXdlYiIsInNlc3Npb25fc3RhdGUiOiI0NjYyOTI2MS03Yzk2LTRlODYtYTU0ZS1iYzEwM2UwMTZjZGIiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVtYWlsIn0.KSwBdW0gnmNQ8_UkMsWmZsEH2MAwbo_8qW3Xof_3Gos"
TOKEN4 = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhMTMxYTQ1My1hM2IyLTQwMTUtODQ2Ny05MzAyZjk3MTFkOGEifQ.eyJpYXQiOjE3MzA2NzM5MzIsImp0aSI6IjU3OGI0MjdkLWI2ZGQtNDFhNS04MGVhLTRiNWVlZDk4NzIxMCIsImlzcyI6Imh0dHBzOi8vYXV0aC5zb2Z0d2FyZWhlcml0YWdlLm9yZy9hdXRoL3JlYWxtcy9Tb2Z0d2FyZUhlcml0YWdlIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLnNvZnR3YXJlaGVyaXRhZ2Uub3JnL2F1dGgvcmVhbG1zL1NvZnR3YXJlSGVyaXRhZ2UiLCJzdWIiOiJmMjdlYmRmMC03YTQzLTQ4YTktODQ0Zi1kZjUwMmNmZjk2NDYiLCJ0eXAiOiJPZmZsaW5lIiwiYXpwIjoic3doLXdlYiIsInNlc3Npb25fc3RhdGUiOiI0NjYyOTI2MS03Yzk2LTRlODYtYTU0ZS1iYzEwM2UwMTZjZGIiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVtYWlsIn0.aNAEG3zusvUrQkvSMcy0aIS2k35c-Qp1HxPj_xkhJPo"
TOKEN5 = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhMTMxYTQ1My1hM2IyLTQwMTUtODQ2Ny05MzAyZjk3MTFkOGEifQ.eyJpYXQiOjE3MzA2NzM5MzcsImp0aSI6ImJkNWFhMzQ1LTkwYWQtNDQ2MC1iMzE1LTQxM2YxM2VmYmNmMCIsImlzcyI6Imh0dHBzOi8vYXV0aC5zb2Z0d2FyZWhlcml0YWdlLm9yZy9hdXRoL3JlYWxtcy9Tb2Z0d2FyZUhlcml0YWdlIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLnNvZnR3YXJlaGVyaXRhZ2Uub3JnL2F1dGgvcmVhbG1zL1NvZnR3YXJlSGVyaXRhZ2UiLCJzdWIiOiJmMjdlYmRmMC03YTQzLTQ4YTktODQ0Zi1kZjUwMmNmZjk2NDYiLCJ0eXAiOiJPZmZsaW5lIiwiYXpwIjoic3doLXdlYiIsInNlc3Npb25fc3RhdGUiOiI0NjYyOTI2MS03Yzk2LTRlODYtYTU0ZS1iYzEwM2UwMTZjZGIiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVtYWlsIn0.Wol0KP_mzbS62JUT_t48OTLisEitLUuVVMKvP2FSpkU"
TOKEN6 = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhMTMxYTQ1My1hM2IyLTQwMTUtODQ2Ny05MzAyZjk3MTFkOGEifQ.eyJpYXQiOjE3MzA2NzM5NTAsImp0aSI6IjAxOWFhMjM2LWQ3YjktNDY0NC04MDJhLWU3NzMzMWM3ZWUyYyIsImlzcyI6Imh0dHBzOi8vYXV0aC5zb2Z0d2FyZWhlcml0YWdlLm9yZy9hdXRoL3JlYWxtcy9Tb2Z0d2FyZUhlcml0YWdlIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLnNvZnR3YXJlaGVyaXRhZ2Uub3JnL2F1dGgvcmVhbG1zL1NvZnR3YXJlSGVyaXRhZ2UiLCJzdWIiOiJmMjdlYmRmMC03YTQzLTQ4YTktODQ0Zi1kZjUwMmNmZjk2NDYiLCJ0eXAiOiJPZmZsaW5lIiwiYXpwIjoic3doLXdlYiIsInNlc3Npb25fc3RhdGUiOiI0NjYyOTI2MS03Yzk2LTRlODYtYTU0ZS1iYzEwM2UwMTZjZGIiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVtYWlsIn0.4XU8wte6vhPYfl9WO8WpyJz3Hv9CmNkireKFZ3gqEDw"
TOKEN7 = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhMTMxYTQ1My1hM2IyLTQwMTUtODQ2Ny05MzAyZjk3MTFkOGEifQ.eyJpYXQiOjE3MzA2NzM5NTksImp0aSI6IjI1NzY0MzZkLWIxYzQtNDRmMS05MjE3LTRiNGVkNTYzZDc5ZSIsImlzcyI6Imh0dHBzOi8vYXV0aC5zb2Z0d2FyZWhlcml0YWdlLm9yZy9hdXRoL3JlYWxtcy9Tb2Z0d2FyZUhlcml0YWdlIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLnNvZnR3YXJlaGVyaXRhZ2Uub3JnL2F1dGgvcmVhbG1zL1NvZnR3YXJlSGVyaXRhZ2UiLCJzdWIiOiJmMjdlYmRmMC03YTQzLTQ4YTktODQ0Zi1kZjUwMmNmZjk2NDYiLCJ0eXAiOiJPZmZsaW5lIiwiYXpwIjoic3doLXdlYiIsInNlc3Npb25fc3RhdGUiOiI0NjYyOTI2MS03Yzk2LTRlODYtYTU0ZS1iYzEwM2UwMTZjZGIiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVtYWlsIn0.fI-_h_MO69DCSQakrQsGN4UCWCG2UQRhPSt9U43HaEQ"
TOKEN8 = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhMTMxYTQ1My1hM2IyLTQwMTUtODQ2Ny05MzAyZjk3MTFkOGEifQ.eyJpYXQiOjE3MzA2NzU3NzgsImp0aSI6ImZhYTdhZDRlLTgzOGItNDRkMS1iY2M1LWY2OWMwZWU4MmRhNyIsImlzcyI6Imh0dHBzOi8vYXV0aC5zb2Z0d2FyZWhlcml0YWdlLm9yZy9hdXRoL3JlYWxtcy9Tb2Z0d2FyZUhlcml0YWdlIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLnNvZnR3YXJlaGVyaXRhZ2Uub3JnL2F1dGgvcmVhbG1zL1NvZnR3YXJlSGVyaXRhZ2UiLCJzdWIiOiJmMjdlYmRmMC03YTQzLTQ4YTktODQ0Zi1kZjUwMmNmZjk2NDYiLCJ0eXAiOiJPZmZsaW5lIiwiYXpwIjoic3doLXdlYiIsInNlc3Npb25fc3RhdGUiOiI0NjYyOTI2MS03Yzk2LTRlODYtYTU0ZS1iYzEwM2UwMTZjZGIiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVtYWlsIn0.5dNhUyE1V2mixgtKG0htVeeViy-Hil5HBTT4f95R7N0"

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

def check_swh_presence(github_url, token):

    headers = {"Authorization": f"Bearer {token}"}
    full_url = f"{SWH_API_ENDPOINT}{github_url}/get/"

    while True:
        
        try:
            response = requests.get(full_url, headers=headers)
            print(f"Processing {full_url} - Status: {response.status_code}")
            
            if response.status_code == 200:
                return True
            
            elif response.status_code == 404:
                return False
            
            #elif response.status_code == 429:
                #print("Rate limit reached. Waiting for reset...")
                #time.sleep(3600) 

            else:
                print(f"Unexpected status code: {response.status_code}")
                return False
                
        except requests.RequestException as e:
            print(f"Error checking URL {github_url}: {e}")
            return False

def rq2(input_file, token, temp_dir, output_file, output_directory):

    try:
        with open(input_file, 'r') as file:
            repositories = json.load(file)
        print(f"Loaded {len(repositories)} repositories from {input_file}")

    except Exception as e:
        print(f"Could not open {input_file}: {e}")
        return

    for repo in repositories:
        github_url = repo.get("github_url")

        if github_url:

            in_swh = check_swh_presence(github_url, token)
            result["results"].append({
                "github_link": github_url,
                "in_swh": in_swh
            })
            
            if in_swh:
                result["summary"]["count_in_swh"] += 1
                print(f"{github_url} is available on SWH")
            else:
                result["summary"]["count_not_in_swh"] += 1
        else:
            print(f"No 'github_url' found in entry: {repo}")

    print(f"Processed repositories. In SWH: {result['summary']['count_in_swh']}, Not in SWH: {result['summary']['count_not_in_swh']}")

    # url_pattern = re.compile(re.escape(SWH_API_ENDPOINT))
    # for root, dirs, files in os.walk(temp_dir):
    #     if "README.md" in files:
    #         readme_path = os.path.join(root, "README.md")
    #         try:
    #             with open(readme_path, "r") as file:
    #                 content = file.read()
                
    #             if url_pattern.search(content):
    #                 result["links_swh"]["count"] += 1
    #                 result["links_swh"]["files"].append(readme_path)
    #                 print(f"Found a link to SWH in {readme_path}")

    #         except UnicodeDecodeError as e:
    #             print(f"Could not read {readme_path} due to encoding issues: {e}")
    #             break
    #         # else:
    #         #     print(f"URL not found in {readme_path}.")

    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, output_file)

    with open(output_path, 'w') as f:
        json.dump(result, f, indent=4)
    print(f"Results saved to {output_path}")
    print("Final output data:", result)

input_file = input("Enter the name of the JSON file with GitHub links (in the same directory): ")
token = input("Enter TOKEN 1-8:")

if token == "TOKEN1":
    token = TOKEN1
elif token == "TOKEN2":
    token = TOKEN2
elif token == "TOKEN3":
    token = TOKEN3
elif token == "TOKEN4":
    token = TOKEN4
elif token == "TOKEN5":
    token = TOKEN5
elif token == "TOKEN6":
    token = TOKEN6
elif token == "TOKEN7":
    token = TOKEN7
elif token == "TOKEN8":
    token = TOKEN8
    
temp_dir = input("Please input the base directory (e.g., temp_analysis/escape2020): ")
output_file = input("Please input the name of the output file: ")
output_directory = input("Enter the output directory: ")

rq2(input_file, token, temp_dir, output_file, output_directory)
