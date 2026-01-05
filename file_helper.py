import json
import sys
from pathlib import Path


root_dir = Path(__file__).parent


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


def get_vscode_paths():
    """Get and validate all VSCode related paths."""
    dotfiles_path = root_dir / 'dotfiles'
    dotfiles_vscode_path = dotfiles_path / 'vscode'

    # Expand user paths
    user_vscode_path = user_config['vscode-config-local-path']
    user_vscode_dir = Path(user_vscode_path).expanduser()
    dotfiles_vscode_dir = dotfiles_vscode_path.expanduser()

    # Define file paths
    dotfiles_vscode_settings_path = dotfiles_vscode_path / 'vscode-settings.json'
    dotfiles_vscode_keybindings_path = dotfiles_vscode_path / 'vscode-keybindings.json'
    user_vscode_settings = user_vscode_dir / 'settings.json'
    user_vscode_keybindings = user_vscode_dir / 'keybindings.json'

    # Validate paths exist
    assert_path_exists(dotfiles_vscode_dir, "dotfiles vscode directory")
    assert_path_exists(dotfiles_vscode_settings_path,
                       "dotfiles vscode settings.json")
    assert_path_exists(dotfiles_vscode_keybindings_path,
                       "dotfiles vscode keybindings.json")
    assert_path_exists(user_vscode_settings, "user vscode settings.json")
    assert_path_exists(user_vscode_keybindings, "user vscode keybindings.json")

    return {
        'dotfiles_vscode_dir': dotfiles_vscode_dir,
        'dotfiles_vscode_settings_path': dotfiles_vscode_settings_path,
        'dotfiles_vscode_keybindings_path': dotfiles_vscode_keybindings_path,
        'user_vscode_dir': user_vscode_dir,
        'user_vscode_settings': user_vscode_settings,
        'user_vscode_keybindings': user_vscode_keybindings,
    }


def get_user_neovim_path():
    """Get and validate the user's Neovim config path."""
    user_neovim_path = user_config['neovim-config-local-path']
    user_neovim_dir = Path(user_neovim_path).expanduser() / 'nvim'
    assert_path_exists(user_neovim_dir, "user neovim directory")
    return user_neovim_dir


def get_dotfiles_neovim_path():
    """Get and validate the dotfiles Neovim config path."""
    dotfiles_neovim_path = root_dir / 'dotfiles' / 'neovim'
    dotfiles_neovim_dir = dotfiles_neovim_path.expanduser()
    assert_path_exists(dotfiles_neovim_dir, "dotfiles neovim directory")
    return dotfiles_neovim_dir
