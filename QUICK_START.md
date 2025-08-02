# Quick Start: macOS Screenshot Tool with AI Integration

## 🚀 Get Started in 5 Steps

### 1. Prerequisites
- **macOS** (required for screenshot functionality)
- **Python 3.7+** with tkinter
- **~2GB free disk space** (for AI models)

### 2. Install Tesseract OCR
```bash
brew install tesseract
```

### 3. Setup Environment
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Download AI Models
```bash
# Download required AI models (~2GB, may take several minutes)
python download_models.py
```

### 5. Run the Application
```bash
python screenshot_tool.py
```

## 🎯 Key Features
- ✅ **Screenshot Capture**: Native macOS area selection and full-screen capture
- ✅ **AI Image Analysis**: Local AI models describe what's in your screenshots
- ✅ **Text Extraction (OCR)**: Extract text from screenshots using Tesseract
- ✅ **No Internet Required**: All AI processing happens locally on your machine
- ✅ **Cross-Platform AI**: Works with both CPU and GPU (CUDA) for optimal performance

## 📱 How to Use

### Take Screenshots
- **Select Area**: Click button → drag to select → screenshot saved to Desktop
- **Full Screen**: Click button → entire screen captured → saved to Desktop

### Analyze with AI
- Click **"Send Latest Screenshot to LLM"** 
- AI will describe what it sees in the image
- No data sent to external servers

### Extract Text (OCR)
- Click **"Extract Text (OCR)"**
- Tesseract will extract all text from the screenshot
- Perfect for clean screenshots with printed text

## 🔧 Troubleshooting

### Tesseract Installation Issues
If `brew install tesseract` fails:
```bash
# Update Homebrew first
brew update
brew install tesseract
```

### Model Download Issues
If you get errors downloading models:
```bash
rm -rf ~/.cache/huggingface
python download_models.py
```

### NumPy Compatibility
If you see NumPy compatibility warnings:
```bash
pip install "numpy<2"
```

### Tkinter Issues
If you get `_tkinter` errors, install Python with Tkinter support:
```bash
brew install python-tk@3.10
```

## ⚡ Performance Tips
- **GPU Users**: Models will automatically use CUDA for faster processing
- **CPU Users**: Processing will be slower but still functional
- **First Run**: AI analysis may take 10-30 seconds to load models

## 🔒 Privacy & Security
- **Local Processing**: All AI analysis happens on your machine
- **No Data Upload**: Screenshots never leave your computer
- **Offline Capable**: Works without internet connection
- **Text Extraction**: OCR processing is completely local

## 🔗 Dependencies
- **Tesseract**: OCR engine for text extraction
- **transformers**: Hugging Face model loading and inference
- **torch**: PyTorch for AI model execution
- **Pillow**: Image processing
- **pytesseract**: Python wrapper for Tesseract

That's it! Your AI-powered screenshot tool with OCR is ready to use. 