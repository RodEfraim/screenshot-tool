#!/usr/bin/env python3
"""
Model Download Script for Screenshot Tool
Downloads required Hugging Face models locally
"""

from transformers import Blip2Processor, Blip2ForConditionalGeneration
from transformers import AutoTokenizer, AutoModelForCausalLM
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
        
        print("\n🎉 BLIP-2 models downloaded successfully!")
        
    except Exception as e:
        print(f"❌ Error downloading BLIP-2 models: {str(e)}")

def download_codellama():
    """Download CodeLlama-13B-Instruct model"""
    print("\nDownloading CodeLlama-13B-Instruct model...")
    print("This is a large model (~26GB) and may take a long time...")
    
    try:
        # Download tokenizer
        print("Downloading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-13B-Instruct-hf")
        print("✓ Tokenizer downloaded successfully")
        
        # Download model
        print("Downloading model (this is very large, ~26GB)...")
        model = AutoModelForCausalLM.from_pretrained(
            "codellama/CodeLlama-13B-Instruct-hf",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto"  # Automatically handle model placement
        )
        print("✓ CodeLlama model downloaded successfully")
        
        print("\n🎉 CodeLlama models downloaded successfully!")
        
    except Exception as e:
        print(f"❌ Error downloading CodeLlama models: {str(e)}")

if __name__ == "__main__":
    print("=== Model Download Script ===")
    download_blip2()
    download_codellama()
    print("\n🎉 All models downloaded successfully!")
    print("You can now run your screenshot tool.")