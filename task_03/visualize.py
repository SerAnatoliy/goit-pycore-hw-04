from colorama import Fore, Style

def print_with_color(text,color=Fore.WHITE, style=Style.NORMAL):
    print(color+style+text+Style.RESET_ALL)

def visualize_directory(directory,margin=""):
    for item in directory.iterdir():
        if item.is_dir():
            print_with_color(margin +"   " "📁 " + item.name, color=Fore.BLUE)
            visualize_directory(item, margin + "  ")
        else:
            print_with_color(margin +"   " "📄 " + item.name, color=Fore.GREEN)