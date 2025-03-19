import os
import json

def update_json_files(base_file, directory):
    
    # Recursively update nested JSON
    def update_nested_json(base, target):
        updated = False
        for key, value in base.items():
            # If key not in target, or it's a dictionary but not equivalent to base[key]
            if key not in target or (isinstance(value, dict) and target[key] != value):
                if isinstance(value, dict) and key in target:
                    # If it's a nested dictionary, recursively update
                    updated = update_nested_json(value, target[key]) or updated
                else:
                    # Add or update the key
                    target[key] = value
                    updated = True
        return updated

    # Load the base file (en.json)
    with open(os.path.join(directory, base_file), 'r',  encoding='utf-8') as file:
        base_data = json.load(file)

    # Get all JSON files in the directory except the base file
    json_files = [f for f in os.listdir(directory) if f.endswith('.json') and f != base_file]

    print('Found ' + str(len(json_files)) + ' JSON files')
    missing_fields = {}

    # Process each JSON file
    for file in json_files:
        print('Processing file: ' + file)
        try:
            with open(os.path.join(directory, file), 'r',  encoding='utf-8') as f:
                data = json.load(f)

            # Compare and update nested JSON
            if update_nested_json(base_data, data):
                # Save the updated JSON file if there were updates
                with open(os.path.join(directory, file), 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                    print('Updated file: ' + file)
                missing_fields[file] = {k: base_data[k] for k in base_data if k not in data}
            else:
                print('No updates needed for file: ' + file)

        except (json.JSONDecodeError, IOError):
            print('Error processing file: ' + file)
            continue

    return missing_fields


missing_fields = update_json_files('en.json', './res/')
print(missing_fields.keys())
