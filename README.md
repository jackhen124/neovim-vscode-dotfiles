# Neovim VsCode Dotfiles

The purpose of this project is to store all the configuration files I use to customize my development experience in VSCode.
It also provides scripts to automatically update the files.

This is intended to be used with the [VSCode Neovim](vscode:extension/asvetliakov.vscode-neovim) extension

### Dependencies to use configuration files
- [neovim](https://neovim.io/)
- [VSCode Neovim](vscode:extension/asvetliakov.vscode-neovim)

# Automatic Update Scripts
### Dependencies
- [python](https://www.python.org/downloads/)

### configure file paths
before running scripts, make sure the filepaths are configured correctly in user.config.json.
user.config.json determines what file paths the scripts will expect user settings
on linux, neovim-config-local-path should default to "~/.config/"

### Scripts
run scripts from the root directory of this repo

```bash
python3 copy_user_files.py
```
- Copy the user configs from the filesystem and write them to this repo

```bash
python3 overwrite_user.py
```
- Copy the configs from this repo and write them to the local user configs be used. 
**WARNING** your old user settings will be lost