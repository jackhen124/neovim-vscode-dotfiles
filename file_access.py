import json
import sys
from pathlib import Path


def load_config(config_file_path):
    """Load JSON configuration file."""
    with open(config_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def check_path_exists(path, description):
    """Check if a path exists, exit with error if it doesn't."""
    if not path.exists():
        sys.exit(f"Error: {description} not found at {path}")


def get_vscode_paths(script_dir, config):
    """Get and validate all VSCode related paths."""
    dotfiles_path = script_dir / 'dotfiles'
    dotfiles_vscode_path = dotfiles_path / 'vscode'

    # Expand user paths
    user_vscode_path = config['vscode-config-local-path']
    user_vscode_dir = Path(user_vscode_path).expanduser()
    dotfiles_vscode_dir = dotfiles_vscode_path.expanduser()

    # Define file paths
    dotfiles_vscode_settings_path = dotfiles_vscode_path / 'vscode-settings.json'
    dotfiles_vscode_keybindings_path = dotfiles_vscode_path / 'vscode-keybindings.json'
    user_vscode_settings = user_vscode_dir / 'settings.json'
    user_vscode_keybindings = user_vscode_dir / 'keybindings.json'

    # Validate paths exist
    check_path_exists(dotfiles_vscode_dir, "dotfiles vscode directory")
    check_path_exists(dotfiles_vscode_settings_path,
                      "dotfiles vscode settings.json")
    check_path_exists(dotfiles_vscode_keybindings_path,
                      "dotfiles vscode keybindings.json")
    check_path_exists(user_vscode_settings, "user vscode settings.json")
    check_path_exists(user_vscode_keybindings, "user vscode keybindings.json")

    return {
        'dotfiles_vscode_dir': dotfiles_vscode_dir,
        'dotfiles_vscode_settings_path': dotfiles_vscode_settings_path,
        'dotfiles_vscode_keybindings_path': dotfiles_vscode_keybindings_path,
        'user_vscode_dir': user_vscode_dir,
        'user_vscode_settings': user_vscode_settings,
        'user_vscode_keybindings': user_vscode_keybindings,
    }
