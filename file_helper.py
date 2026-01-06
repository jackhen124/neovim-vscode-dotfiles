import json
import sys
from pathlib import Path


root_dir = Path(__file__).parent

# "dotfiles" is used to refer to the copied config files stored in this repo
# "user" is used to refer to the working config files on the user's machine
# Each key represents a path that is in common between the dotfiles and user configs
VSCODE_SETTINGS_CONTAINER_KEY = 'vscode_settings_container_path'
VSCODE_KEYBINDINGS_KEY = 'vscode_keybindings'
VSCODE_SETTINGS_KEY = 'vscode_settings'
# This key represents the folder that contains the 'nvim' folder
NEOVIM_NVIM_CONTAINER_KEY = 'neovim_nvim_container_path'
NEOVIM_NVIM_KEY = 'neovim_nvim_path'


dotfiles_path = root_dir / 'dotfiles'
dotfiles_vscode_path = dotfiles_path / 'vscode'
dotfiles_vscode_keybindings_path = dotfiles_vscode_path / 'keybindings.json'
dotfiles_vscode_settings_path = dotfiles_vscode_path / 'settings.json'


dotfiles_paths = {
    VSCODE_SETTINGS_CONTAINER_KEY: dotfiles_vscode_path,
    VSCODE_KEYBINDINGS_KEY: dotfiles_vscode_keybindings_path,
    VSCODE_SETTINGS_KEY: dotfiles_vscode_settings_path,
    NEOVIM_NVIM_CONTAINER_KEY: dotfiles_path,
    NEOVIM_NVIM_KEY: dotfiles_path / 'nvim'
}

# User paths


def assert_path_exists(path, description):
    """Check if a path exists, exit with error if it doesn't."""
    if not path.exists():
        sys.exit(f"Error: {description} not found at {path}")


def load_user_config():
    """Load JSON configuration file."""
    user_config_path = root_dir / 'user.config.json'
    assert_path_exists(user_config_path, "user config file")
    with open(user_config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


user_config = load_user_config()


def get_value_from_user_config(key):
    """Use key to get and validate the corresponding path from user config."""
    user_config_path = user_config[key]
    user_config_dir = Path(user_config_path).expanduser()

    assert_path_exists(user_config_dir, f"user {key} directory")
    return user_config_dir


def get_user_paths():
    """Get and validate all user config paths."""
    user_vscode_path = get_value_from_user_config(
        VSCODE_SETTINGS_CONTAINER_KEY)

    user_nvim_container = get_value_from_user_config(
        NEOVIM_NVIM_CONTAINER_KEY)
    user_paths = {
        VSCODE_KEYBINDINGS_KEY: user_vscode_path / 'keybindings.json',
        VSCODE_SETTINGS_KEY: user_vscode_path / 'settings.json',
        NEOVIM_NVIM_CONTAINER_KEY: user_nvim_container,
        NEOVIM_NVIM_KEY: user_nvim_container / 'nvim'
    }

    for key, path in user_paths.items():
        assert_path_exists(path, f"user {key} path")

    return user_paths
