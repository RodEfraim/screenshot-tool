# macOS Screenshot Tool with AI Integration

A macOS screenshot utility that captures screenshots and uses local AI models to describe what's in the images.

## Features

- **Screenshot Capture**: Select an area or capture the entire screen using native macOS `screencapture`
- **AI Image Analysis**: Uses local Hugging Face models to describe screenshots
- **No Internet Required**: All AI processing happens locally on your machine
- **Cross-Platform AI**: Works with both CPU and GPU (CUDA) for optimal performance

## Requirements

- **macOS** (for screenshot functionality)
- **Python 3.7+** (with tkinter)
- **Sufficient disk space** (~2GB for AI models)
- **Optional**: CUDA-capable GPU for faster AI processing

## Installation

1. **Clone or download this repository**

2. **Install Tesseract OCR** (required for text extraction):
   ```bash
   brew install tesseract
   ```

3. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Download AI models** (required for AI features):
   ```bash
   python download_models.py
   ```
   *Note: This downloads ~2GB of AI models and may take several minutes*

## Usage

1. **Run the application**:
   ```bash
   python screenshot_tool.py
   ```

2. **Take a screenshot**:
   - Click "Select Area" to capture a specific portion
   - Click "Full Screen" to capture the entire screen
   - Screenshots are automatically saved to your Desktop

3. **Analyze with AI**:
   - Click "Send Latest Screenshot to LLM" to get an AI description
   - The AI will describe what it sees in the image

## Project Structure

```
SnippetToChatGPT/
├── screenshot_tool.py      # Main application
├── download_models.py      # AI model downloader
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── venv/                  # Virtual environment
```

## AI Models Used

- **BLIP Image Captioning**: Automatically generates descriptions of screenshots
- **Local Processing**: No data sent to external servers
- **Privacy-First**: All processing happens on your local machine

## Troubleshooting

### Model Download Issues
If you get errors downloading models:
```bash
rm -rf ~/.cache/huggingface
python download_models.py
```

### NumPy Version Conflicts
If you see NumPy compatibility warnings:
```bash
pip install "numpy<2"
```

### Tkinter Issues
If you get `_tkinter` errors, install Python with Tkinter support:
```bash
brew install python-tk@3.10
```

## Dependencies

- `transformers`: Hugging Face model loading and inference
- `torch`: PyTorch for AI model execution
- `Pillow`: Image processing
- `tkinter`: GUI framework (built-in with Python)

## Notes

- Screenshots are saved to your Desktop with timestamped filenames
- AI models are downloaded once and cached locally
- The tool works offline after initial model download
- GPU acceleration is automatically detected and used if available

## License

This project is open source and available under the MIT License. 