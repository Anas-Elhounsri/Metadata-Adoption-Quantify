import json
import os
from collections import defaultdict

# This is the script for extracting languages
directory = input("Input the directory: ")
output_file = input("Input the file output: ")
language_count = defaultdict(int)

for file_name in os.listdir(directory):

    if file_name.startswith('output_') and file_name.endswith('.json'):
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)

            if 'programming_languages' in data:

                for lang in data['programming_languages']:

                    language = lang['result']['name']
                    language_count[language] += 1

sorted_language_count = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

for language, count in sorted_language_count:
    print(f"{language}: {count}")

with open(output_file, 'w') as json_file:
    json.dump(dict(sorted_language_count), json_file, indent=4)

print(f"Results saved to {output_file}")