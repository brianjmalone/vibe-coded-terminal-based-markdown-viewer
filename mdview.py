#!/usr/bin/env python3
import argparse
import os
import sys
from rich.console import Console
from rich.markdown import Markdown

def main():
    parser = argparse.ArgumentParser(description="View Markdown files in the terminal.")
    parser.add_argument("FILE_PATH", help="Path to the Markdown file to view.")
    args = parser.parse_args()

    # Set LESS environment variable to enable ANSI color codes
    # -R: interpret ANSI color escape sequences
    # -X: don't clear screen on exit
    # -F: quit if output fits on one screen
    os.environ['LESS'] = '-R -X -F'

    console = Console()

    try:
        with open(args.FILE_PATH, "r", encoding="utf-8-sig") as f:
            markdown_content = f.read()

        md = Markdown(markdown_content, code_theme="monokai")

        # Check if output is going to a terminal
        if sys.stdout.isatty():
            # Use pager only in interactive mode
            with console.pager(styles=True):
                console.print(md)
        else:
            # Just print if output is being redirected
            console.print(md)

    except FileNotFoundError:
        console.print(f"[red]Error:[/red] File not found: {args.FILE_PATH}")
    except Exception as e:
        console.print(f"[red]An unexpected error occurred:[/red] {e}")

if __name__ == "__main__":
    main()
