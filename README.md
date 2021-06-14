# fzf-dirhistory

A small Python package that keeps a history of recently visited directories. It
is primarily intended for use by FZF to quickly jump to previous locations.

## Installation
```bash
pip3 install --user fzf-dirhistory
```

## Usage (with Bash)
Add this to your `.bashrc` to log directories as you visit them:
```bash
PROMPT_COMMAND='python3 -m fzfdirhist log "$(pwd)"'
```

Then add this function to call FZF with the history file as input:
```bash
fdh() {
  local dir=$(python3 -m fzfdirhist show | fzf --height=40% --reverse +m)
  cd "$dir"
}
```

Calling `fdh` will jump to the selected location. You may want to map that
function (here to `ALT-H` denoted by `\eh`):
```bash
bind '"\eh": "\C-k\C-u fdh\n"'
```

## Configuration
The `DIR_HISTORY_FILE` environment variable points to the history file (by
default `~/.dirhistory`):
```bash
export DIR_HISTORY_FILE="~/.fzf_dirhistory"
```

The `DIR_HISTORY_SIZE` environment variable sets the history maximum size (by
default `100`):
```bash
export DIR_HISTORY_SIZE=200
```

## License
[GNU Lesser General Public License v2.1](https://github.com/ojroques/fzf-dirhistory/blob/main/LICENSE)
