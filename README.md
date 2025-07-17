# macOS Screenshot Tool

A simple screenshot utility for macOS that leverages the native `screencapture` command for area and full-screen captures.

## Features

- Select an area of the screen to capture using the native macOS interface
- Capture the entire screen
- Screenshots are saved directly to your Desktop with a timestamped filename
- No external dependencies required

## Requirements

- macOS
- Python 3 (with tkinter, included by default)

## Usage

1. Clone or download this repository.
2. Open Terminal and navigate to the project directory.
3. Run the tool:
   ```bash
   python3 screenshot_tool.py
   ```
4. Use the GUI to select either "Select Area" or "Full Screen".

## Notes

- This tool is designed for macOS only.
- Screenshots are saved to your Desktop.
- The tool uses the built-in `screencapture` command for reliability and native experience. 