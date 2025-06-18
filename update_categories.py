import json
import os

# Define the category translations
category_translations = {
    "Warm-up/activation": "Разминка/активация (Warm-up/activation)",
    "Main exercises": "Основные упражнения (Main exercises)",
    "Balance/Proprioception": "Баланс/Проприоцепция (Balance/Proprioception)",
    "Cool-down/stretching": "Заминка/Растяжка (Cool-down/Stretching)",
    "Cool-down/Stretching": "Заминка/Растяжка (Cool-down/Stretching)"
}

def update_categories_in_file(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Track if any changes were made
    changes_made = False
    
    # Update categories in the data structure
    if 'exercise_routines' in data:  # First file format
        for exercise in data['exercise_routines']:
            if exercise['category'] in category_translations:
                exercise['category'] = category_translations[exercise['category']]
                changes_made = True
    else:  # Second file format
        for section in ['warm_up_activation', 'main_exercises', 'balance_proprioception', 'cool_down_stretching']:
            if section in data:
                for exercise in data[section]:
                    if 'category' in exercise and exercise['category'] in category_translations:
                        exercise['category'] = category_translations[exercise['category']]
                        changes_made = True
    
    # Write back to file if changes were made
    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated categories in {os.path.basename(file_path)}")
    else:
        print(f"No category updates needed in {os.path.basename(file_path)}")

# Update both files
files = [
    "/Users/timnik/Library/CloudStorage/GoogleDrive-timofnii@gmail.com/My Drive/Fitness Kids App/exercise_routines_Manus.json",
    "/Users/timnik/Library/CloudStorage/GoogleDrive-timofnii@gmail.com/My Drive/Fitness Kids App/Exercises_Claud Opus.json"
]

for file_path in files:
    if os.path.exists(file_path):
        update_categories_in_file(file_path)
    else:
        print(f"File not found: {file_path}")
