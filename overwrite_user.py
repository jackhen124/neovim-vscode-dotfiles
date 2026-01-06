import shutil
from pathlib import Path
from file_helper import get_vscode_paths, get_user_neovim_path, get_dotfiles_neovim_path

print("Updating this repo from from Local VSCode config...")

# Get and validate all VSCode paths
vscode_paths = get_vscode_paths()

# Copy VSCode files
shutil.copy2(vscode_paths['dotfiles_vscode_keybindings_path'],
             vscode_paths['user_vscode_keybindings'])
shutil.copy2(vscode_paths['dotfiles_vscode_settings_path'],
             vscode_paths['user_vscode_settings'])
print("Copied settings.json and keybindings.json from user VSCode config.")

# Copy the neovim files
shutil.copytree(get_user_neovim_path(), get_dotfiles_neovim_path(),
                dirs_exist_ok=True)
