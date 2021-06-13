import sys
from .fzfdirhist import log_dir, show_history


def usage():
    print("Usage: python3 -m fzfdirhist <help|log|show> [dir]")


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3 or sys.argv[1] == "help":
        usage()
        return

    if sys.argv[1] == "log":
        if len(sys.argv) != 3:
            usage()
        else:
            log_dir(sys.argv[2])
        return

    if sys.argv[1] == "show":
        show_history()
        return

    usage()


main()
