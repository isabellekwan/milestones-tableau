import json
import glob
import os

# Get the current working directory (same as the Python script's directory)
current_dir = os.path.dirname(os.path.abspath(__file__))

# List all JSON files in the directory following the naming pattern
json_files = glob.glob(os.path.join(current_dir, 'allDocuments*.json'))

merged_data = {}

for file in json_files:
    user_id = os.path.basename(file).replace('.json', '')  # Extract user ID from filename
    with open(file, 'r', encoding='utf-8') as f:
        try:
            file_data = json.load(f)
            
            if isinstance(file_data, list):
                for item in file_data:
                    if isinstance(item, dict) and 'data' in item:
                        data_attributes = item['data']
                        data_attributes['user_id'] = user_id  # Add user ID to data attributes
                        if user_id in merged_data:
                            merged_data[user_id].append(data_attributes)
                        else:
                            merged_data[user_id] = [data_attributes]
                    else:
                        print(f"No 'data' key found in one of the objects in {file}")
            elif isinstance(file_data, dict):
                if 'data' in file_data:
                    data_attributes = file_data['data']
                    data_attributes['user_id'] = user_id  # Add user ID to data attributes
                    if user_id in merged_data:
                        merged_data[user_id].append(data_attributes)
                    else:
                        merged_data[user_id] = [data_attributes]
                else:
                    print(f"No 'data' key found in the dictionary in {file}")
            else:
                print(f"File {file} contains an unexpected JSON structure.")
        
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {file}: {e}")

# Save the merged data into a new JSON file
combined_file_path = os.path.join(current_dir, 'combinedUser.json')
with open(combined_file_path, 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=4)

print(f"Merged JSON data saved to {combined_file_path}")
