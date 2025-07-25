# Quick Start: macOS Screenshot Tool with AI Integration

## 🚀 Get Started in 4 Steps

### 1. Prerequisites
- **macOS** (required for screenshot functionality)
- **Python 3.7+** with tkinter
- **~2GB free disk space** (for AI models)

### 2. Setup Environment
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Download AI Models
```bash
# Download required AI models (~2GB, may take several minutes)
python download_models.py
```

### 4. Run the Application
```bash
python screenshot_tool.py
```

## 🎯 Key Features
- ✅ **Screenshot Capture**: Native macOS area selection and full-screen capture
- ✅ **AI Image Analysis**: Local AI models describe what's in your screenshots
- ✅ **Privacy-First**: All processing happens on your machine
- ✅ **Offline Capable**: Works without internet after initial setup
- ✅ **GPU Acceleration**: Automatically uses GPU if available

## 📱 How to Use

### Take Screenshots
- **Select Area**: Click button → drag to select → screenshot saved to Desktop
- **Full Screen**: Click button → entire screen captured → saved to Desktop

### Analyze with AI
- Click **"Send Latest Screenshot to LLM"** 
- AI will describe what it sees in the image
- No data sent to external servers

## 🔧 Troubleshooting

### Model Download Issues
```bash
rm -rf ~/.cache/huggingface
python download_models.py
```

### NumPy Compatibility
```bash
pip install "numpy<2"
```

### Tkinter Issues
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

That's it! Your AI-powered screenshot tool is ready to use. 