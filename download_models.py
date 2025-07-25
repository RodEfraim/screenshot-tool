#!/usr/bin/env python3
"""
Model Download Script for Screenshot Tool
Downloads required Hugging Face models locally
"""

from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch

def download_blip2():
    """Download BLIP-2 model and processor"""
    print("Downloading BLIP-2 model and processor...")
    print("This may take several minutes depending on your internet connection...")
    
    try:
        # Download processor
        print("Downloading processor...")
        processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
        print("✓ Processor downloaded successfully")
        
        # Download model
        print("Downloading model (this is the large file, ~6GB)...")
        model = Blip2ForConditionalGeneration.from_pretrained(
            "Salesforce/blip2-opt-2.7b",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        print("✓ Model downloaded successfully")
        
        print("\n🎉 All models downloaded successfully!")
        print("You can now run your screenshot tool.")
        
    except Exception as e:
        print(f"❌ Error downloading models: {str(e)}")
        print("Please check your internet connection and try again.")

if __name__ == "__main__":
    print("=== Model Download Script ===")
    download_blip2()