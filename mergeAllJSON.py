import json
import glob
import os

# Get the current working directory (same as the Python script's directory)
current_dir = os.path.dirname(os.path.abspath(__file__))

# List all JSON files in the directory following the naming pattern
json_files = glob.glob(os.path.join(current_dir, 'allDocuments0*.json'))

combined_data = []

for file in json_files:
    with open(file, 'r', encoding='utf-8') as f:
        file_data = json.load(f)
        if 'data' in file_data:
            combined_data.extend(file_data['data'])  # Assuming 'data' is a list of objects
        else:
            print(f"No 'data' key found in {file}")

# Save the combined data into a new JSON file
combined_file_path = os.path.join(current_dir, 'combinedAll.json')
with open(combined_file_path, 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)

print(f"Combined JSON data saved to {combined_file_path}")
