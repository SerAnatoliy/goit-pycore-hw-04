import sys
from pathlib import Path
from colorama import Fore
from visualize import visualize_directory,print_with_color


if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Please provide the folder path as a command-line argument.")
        sys.exit(1)

    folder_path=sys.argv[1]

    folder=Path(folder_path)
    if not folder.is_dir():
        print(f"The specified path '{folder_path}' is not a valid folder.")
        sys.exit(1)

    print_with_color("📦 " + folder.name + "/", color=Fore.BLUE)

    visualize_directory(folder)