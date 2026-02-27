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

## Origin Story: 

I saw that there was a video about vibe coding a Markdown Viewer from Google, and wanted to see if I could replicate it—without even WATCHING the video. 

1) I handed the URL to Gemini, and had it generate a summary of the transcript as a Markdown file outlining the project. 

2) I put that file in a folder, opened VS Code and Gemini CLI, and told it to build the project from the description in that Markdown summary of the video. 

 3) In 90 seconds, I had a version that could render Markdown in the Terminal—but no colors. Gemini eventually gave up ("If this does not work, I have exhausted all my diagnostic capabilities and I will not be able to solve this problem."). 

4) Claude Code spotted the error in one conversational turn, though. There was some wrangling between the paging system, less, and rich on my system, but Claude crushed those bugs and it just worked. 

I wrote 0 lines of code, <300 words of English, and copy/pasted some bash commands for testing. That's all. 

"The future is already here—it's just not evenly distributed." -- William Gibson

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
