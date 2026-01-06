import shutil
from pathlib import Path
from file_helper import *

user_paths = validate_and_get_user_paths()
dotfiles_paths = get_dotfiles_paths()
assert_dotfiles_paths_exist()

# Confirm before proceeding
response = input(
    "This will cause changes to your system, and should be used carefully. Are you sure you want to continue? (y/n): ")
if response.lower() != 'y':
    print("Operation cancelled.")
    sys.exit()

print("Starting to overwrite user config files from dotfiles repo...")


# Copy VSCode files
shutil.copy2(
    dotfiles_paths[VSCODE_SETTINGS_KEY],
    user_paths[VSCODE_SETTINGS_KEY])
shutil.copy2(dotfiles_paths[VSCODE_KEYBINDINGS_KEY],
             user_paths[VSCODE_KEYBINDINGS_KEY])
print("Overwrote settings.json and keybindings.json for user VSCode config.")


# Copy the neovim files
shutil.copytree(dotfiles_paths[NEOVIM_NVIM_KEY],
                user_paths[NEOVIM_NVIM_KEY],
                dirs_exist_ok=True)
print("Overwrote user neovim config.")

print("Update complete.")
