"""File_Founder: Created by Amir Mohammad Tavallali Nia!

You can refer to this link to see my games and apps:
https://t.me/A_M_T_N134
"""

from pathlib import Path
import shutil

folder = input("Enter the folder to scan: ")
destination_name = input("Enter the destination folder name: ")
cmd = input("Enter the command: ")
script_folder = Path(__file__).parent
destination_folder = script_folder / destination_name

def read_names(names_file):
    with open(names_file, "r", encoding="utf-8") as file:
        names = set()
        for line in file:
            name = line.strip()
            if name:
                names.add(name)
    return names

def process_item(item, names, cmd):
    names.remove(item.stem)
    if cmd == "copy":
        copy(item, destination_folder)
    elif cmd == "move":
        move(item, destination_folder)
    elif cmd == "remove":
        remove(item)

def show_missing_names(names):
    if names:
        print("\nThese names were not found:")
        for name in names:
            print(name)
    else:
        print("\nAll names were found.")

def scan(folder):
    folder = Path(folder)
    if not folder.exists():
        print(f"{folder} does not exist!")
        return
    names_file = script_folder / "names.txt"
    if not names_file.exists():
        print(f"{names_file} does not exist!")
        return
    if cmd not in ("copy", "move", "remove"):
        print("Invalid command!")
        return
    destination_folder.mkdir(exist_ok=True)
    names = read_names(names_file)
    for item in folder.rglob("*"):
        if item.stem in names:
            process_item(item, names, cmd)
    show_missing_names(names)

def copy(files, folder):
    if files.is_dir():
        shutil.copytree(files, folder / files.name, dirs_exist_ok=True)
    else:
        shutil.copy(files, folder)

def move(files, folder):
    shutil.move(files, folder)

def remove(files):
    if files.is_dir():
        shutil.rmtree(files)
    else:
        files.unlink()

if __name__ == "__main__":
    print("File Founder! Created by Amir Mohammad Tavallali Nia!")
    scan(folder)
