# fzf-dirhistory

A small Python package that keeps a history of recently visited directories. It
is primarily intended for use by FZF to quickly jump to previous locations.

## Installation
```bash
pip3 install --user fzf-dirhistory
```

## Usage (with Bash)
Add this to your `.bashrc`:
```bash
PROMPT_COMMAND='python3 -m fzfdirhist log $(pwd)'
```

Then add this function to call FZF with the history file as input:
```bash
__fzf_dirhistory__() {
  local cmd=$(python3 -m fzfdirhist show | fzf --height=40% --reverse +m | while read -r item; do printf "%q " "$item"; done && echo)
  READLINE_LINE="${READLINE_LINE:0:$READLINE_POINT}$cmd${READLINE_LINE:$READLINE_POINT}"
  READLINE_POINT=$(( READLINE_POINT + ${#cmd} ))
}
```

Calling `__fzf_dirhistory__` will insert the selected entry into the command
line. You may want to map that function (here to `ALT-H`):
```bash
bind -m emacs-standard -x '"\eh": __fzf_dirhistory__'
bind -m vi-command -x '"\eh": __fzf_dirhistory__'
bind -m vi-insert -x '"\eh": __fzf_dirhistory__'
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
