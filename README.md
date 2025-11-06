# mdview

A terminal-based Markdown viewer with syntax highlighting and pagination.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- 🎨 **Syntax highlighting** for code blocks using Pygments
- 📄 **Pagination** with `less` for easy navigation
- 🌈 **Color support** for headers, lists, blockquotes, and links
- ⚡ **Fast** - renders markdown instantly
- 🔧 **Simple** - single Python script, minimal dependencies

## Installation

### Prerequisites

- Python 3.9+
- `less` (usually pre-installed on macOS/Linux)

### Install from source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/markdown-viewer.git
cd markdown-viewer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make the script executable:
```bash
chmod +x mdview.py
```

4. Create a symlink (optional, for system-wide access):
```bash
ln -sf $(pwd)/mdview.py ~/bin/mdview
```

## Usage

```bash
# View a markdown file
mdview README.md

# View with absolute path
mdview ~/Documents/notes.md

# View with relative path
mdview ../other-project/docs.md

# Get help
mdview --help
```

## How It Works

mdview uses the [Rich](https://github.com/Textualize/rich) library to render Markdown with ANSI color codes, then pipes the output through `less` for pagination. The key insight was setting the `LESS` environment variable to `-R -X -F` to enable color support in the pager.

## Troubleshooting

**Seeing raw ANSI escape codes (like `ESC[1m`) instead of colors?**

This is a known issue when `less` doesn't have the `-R` flag enabled. The script sets this automatically, but if you're experiencing issues, see [Learnings.md](Learnings.md) for:

- Complete debugging journey and solution
- Why `console.pager(styles=True)` alone doesn't work
- How to fix pager color issues system-wide
- Discussion on containerization and deployment options

[Learnings.md](Learnings.md) contains the full technical breakdown of the color rendering problem and its solution.

## Requirements

- `rich` - Terminal rendering library

## License

MIT

## Acknowledgments

- Built with [Rich](https://github.com/Textualize/rich) by Textualize
- Developed with assistance from Claude Code (Anthropic)
