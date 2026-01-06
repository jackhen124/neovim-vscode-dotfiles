import os
import shutil
from pathlib import Path
from file_helper import *

print("Updating this repo from from Local files config...")


def initialize_dotfiles_directory():
    """Create empty dotfiles directory structure."""
    if dotfiles_path.exists():
        shutil.rmtree(dotfiles_path)
    os.mkdir(dotfiles_path)
    os.mkdir(dotfiles_paths[VSCODE_SETTINGS_CONTAINER_KEY])
    os.mkdir(dotfiles_paths[NEOVIM_NVIM_KEY])


initialize_dotfiles_directory()
user_paths = get_user_paths()

# Copy VSCode files
shutil.copy2(user_paths[VSCODE_SETTINGS_KEY],
             dotfiles_paths[VSCODE_SETTINGS_KEY])
shutil.copy2(user_paths[VSCODE_KEYBINDINGS_KEY],
             dotfiles_paths[VSCODE_KEYBINDINGS_KEY])
print("Copied settings.json and keybindings.json from user VSCode config.")

# Copy the neovim files
shutil.copytree(user_paths[NEOVIM_NVIM_KEY],
                dotfiles_paths[NEOVIM_NVIM_KEY],
                dirs_exist_ok=True)
