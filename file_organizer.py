import os
import shutil
import argparse

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css']
}

def organize_files(source_folder):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    dest = os.path.join(source_folder, folder)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest, filename))
                    moved = True
                    break

            if not moved:
                other = os.path.join(source_folder, 'Others')
                os.makedirs(other, exist_ok=True)
                shutil.move(file_path, os.path.join(other, filename))

    print("Files organized successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a folder.")
    parser.add_argument("folder", help="Folder to organize")
    args = parser.parse_args()
    organize_files(args.folder)
