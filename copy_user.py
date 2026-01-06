import shutil
from pathlib import Path
from file_helper import *

print("Updating this repo from from Local files config...")
# Get and validate all VSCode paths
user_paths = get_user_paths()
# Copy VSCode files
shutil.copy2(user_paths[VSCODE_SETTINGS_KEY],
             dotfiles_paths[VSCODE_SETTINGS_KEY])
shutil.copy2(user_paths[VSCODE_KEYBINDINGS_KEY],
             dotfiles_paths[VSCODE_KEYBINDINGS_KEY])
print("Copied settings.json and keybindings.json from user VSCode config.")

# Copy the neovim files

shutil.copytree(user_paths[NEOVIM_NVIM_KEY],
                dotfiles_paths[NEOVIM_NVIM_CONTAINER_KEY],
                dirs_exist_ok=True)
