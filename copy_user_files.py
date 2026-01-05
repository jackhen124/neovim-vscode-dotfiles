import shutil
from pathlib import Path
from file_access import load_config, get_vscode_paths

print("Updating this repo from from Local VSCode config...")

# Get the directory where this script is located
script_dir = Path(__file__).parent

# Load config from script directory
user_config_file = script_dir / 'user.config.json'
loaded_user_config = load_config(user_config_file)

# Get and validate all VSCode paths
vscode_paths = get_vscode_paths(script_dir, loaded_user_config)

# Copy VSCode files
shutil.copy2(vscode_paths['user_vscode_settings'],
             vscode_paths['dotfiles_vscode_settings_path'])
shutil.copy2(vscode_paths['user_vscode_keybindings'],
             vscode_paths['dotfiles_vscode_keybindings_path'])
print("Copied settings.json and keybindings.json from user VSCode config.")
