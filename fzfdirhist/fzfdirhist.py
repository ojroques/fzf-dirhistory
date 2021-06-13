from os import environ
from pathlib import Path

DIR_HISTORY_FILE = Path(environ.get("DIR_HISTORY_FILE",
                                    "~/.dir_history")).expanduser()
DIR_HISTORY_SIZE = int(environ.get("DIR_HISTORY_SIZE", "100"))


def log_dir(dir):
    if not Path.is_dir(Path(dir).expanduser()):
        return

    Path.touch(DIR_HISTORY_FILE, exist_ok=True)

    with open(DIR_HISTORY_FILE, "r+") as f:
        history = f.readlines()

        if history and history[-1].strip() == dir:
            return

        f.seek(0)
        start = 1 - DIR_HISTORY_SIZE if len(history) >= DIR_HISTORY_SIZE else 0

        for d in history[start:]:
            if d.strip() != dir:
                f.write(d)

        f.write(f"{dir}\n")
        f.truncate()


def show_history():
    if not Path.is_file(DIR_HISTORY_FILE):
        return

    with open(DIR_HISTORY_FILE, "r") as f:
        for d in reversed(f.readlines()):
            print(d, end="")
