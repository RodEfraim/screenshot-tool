#!/usr/bin/env python3
"""
macOS Screenshot Tool with LLM Integration
Uses native macOS screenshot functionality and sends to HuggingFace
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import os
from datetime import datetime

from transformers import Blip2Processor, Blip2ForConditionalGeneration
from PIL import Image
import torch

import pytesseract

import gc
import torch
import psutil  # Add this import

def check_memory():
    """Monitor memory usage"""
    if torch.cuda.is_available():
        print(f"GPU Memory: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")

class MacScreenshotTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("macOS Screenshot Tool with LLM")
        self.root.geometry("350x350")
        self.root.resizable(False, False)
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main user interface"""
        # Main frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="macOS Screenshot Tool", 
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=(0, 20))
        
        # Instructions
        instructions = tk.Label(
            main_frame,
            text="Take a screenshot and analyze with AI or OCR",
            font=('Arial', 10),
            justify='center'
        )
        instructions.pack(pady=(0, 30))
        
        # Top row buttons frame
        top_button_frame = tk.Frame(main_frame)
        top_button_frame.pack(pady=10)
        
        # Select Area button
        self.select_btn = tk.Button(
            top_button_frame,
            text="Select Area",
            command=self.select_area,
            font=('Arial', 12),
            padx=20,
            pady=10
        )
        self.select_btn.pack(side='left', padx=10)
        
        # Full Screen button
        self.fullscreen_btn = tk.Button(
            top_button_frame,
            text="Full Screen",
            command=self.full_screen,
            font=('Arial', 12),
            padx=20,
            pady=10
        )
        self.fullscreen_btn.pack(side='left', padx=10)
        
        # Bottom row buttons frame
        bottom_button_frame = tk.Frame(main_frame)
        bottom_button_frame.pack(pady=10)
        
        # Send to LLM button
        self.llm_btn = tk.Button(
            bottom_button_frame,
            text="Send to AI",
            command=self.send_to_llm,
            font=('Arial', 12),
            padx=20,
            pady=10,
            bg='lightblue'
        )
        self.llm_btn.pack(side='left', padx=10)

        # OCR button
        self.ocr_btn = tk.Button(
            bottom_button_frame,
            text="Extract Text (OCR)",
            command=self.extract_text_from_image,
            font=('Arial', 12),
            padx=20,
            pady=10,
            bg='lightgreen'
        )
        self.ocr_btn.pack(side='left', padx=10)
        
    def select_area(self):
        """Use native macOS area selection"""
        try:
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            desktop_path = os.path.expanduser("~/Desktop")
            full_path = os.path.join(desktop_path, filename)
            
            # Use screencapture with -i (interactive) and specify output file
            subprocess.run(['screencapture', '-i', full_path])
            
            # Check if file was created
            if os.path.exists(full_path):
                self.latest_screenshot = full_path
                messagebox.showinfo("Success", f"Screenshot saved to Desktop:\n{filename}")
            else:
                messagebox.showinfo("Info", "Screenshot cancelled or no area selected.")
                
        except FileNotFoundError:
            messagebox.showerror("Error", "screencapture not found. This tool requires macOS.")
        except Exception as e:
            messagebox.showerror("Error", f"Screenshot failed: {str(e)}")
            
    def full_screen(self):
        """Use native macOS full screen capture"""
        try:
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            desktop_path = os.path.expanduser("~/Desktop")
            full_path = os.path.join(desktop_path, filename)
            
            # Use macOS built-in screenshot
            subprocess.run(['screencapture', full_path])
            
            # Check if file was created
            if os.path.exists(full_path):
                self.latest_screenshot = full_path
                messagebox.showinfo("Success", f"Screenshot saved to Desktop:\n{filename}")
            else:
                messagebox.showerror("Error", "Failed to capture screenshot.")
                
        except FileNotFoundError:
            messagebox.showerror("Error", "screencapture not found. This tool requires macOS.")
        except Exception as e:
            messagebox.showerror("Error", f"Screenshot failed: {str(e)}")
    
    def send_to_llm(self):
        """Run BLIP-2 locally to describe the latest screenshot."""
        if not hasattr(self, 'latest_screenshot') or not os.path.exists(self.latest_screenshot):
            messagebox.showerror("Error", "No screenshot available. Please take a screenshot first.")
            return

        try:
            # Load model and processor (no force_download)
            processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
            model = Blip2ForConditionalGeneration.from_pretrained(
                "Salesforce/blip2-opt-2.7b",
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
            )
            device = "cuda" if torch.cuda.is_available() else "cpu"
            model.to(device)

            print("device: ", device)

            # Load the screenshot
            image = Image.open(self.latest_screenshot).convert("RGB")
            prompt = "Describe this image in detail."

            # Prepare inputs and run model
            # TODO: SEE IF TAKING OUT the text=prompt parameter makes it work
            # inputs = processor(images=image, text=prompt, return_tensors="pt").to(device)
            inputs = processor(images=image, return_tensors="pt").to(device)

            out = model.generate(**inputs)
            result = processor.decode(out[0], skip_special_tokens=True)

            messagebox.showinfo("AI Response", f"AI says: {result}")

        except FileNotFoundError:
            messagebox.showerror("Error", "Model not found. Please run 'python download_models.py' first to download the required models.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run BLIP-2 locally: {str(e)}")
        
    def extract_text_from_image(self):
        """Extract text from clean screenshots using Tesseract OCR"""
        if not hasattr(self, 'latest_screenshot') or not os.path.exists(self.latest_screenshot):
            messagebox.showerror("Error", "No screenshot available. Please take a screenshot first.")
            return

        try:
            loading_window = tk.Toplevel(self.root)
            loading_window.title("OCR Processing")
            loading_window.geometry("250x100")
            loading_label = tk.Label(loading_window, text="Extracting text from image...")
            loading_label.pack(expand=True)
            loading_window.update()

            # Extract text using Tesseract
            custom_config = r'--oem 3 --psm 6'
            
            extracted_text = pytesseract.image_to_string(
                self.latest_screenshot, 
                config=custom_config
            )
            
            # Clean up the text
            cleaned_text = extracted_text.strip()
            
            # Remove excessive whitespace
            cleaned_text = ' '.join(cleaned_text.split())
            
            loading_window.destroy()
            
            if cleaned_text:
                # Show OCR results and ask if user wants CodeLlama analysis
                result = messagebox.askyesno(
                    "OCR Results", 
                    f"Extracted text:\n\n{cleaned_text}\n\nWould you like to analyze this code with CodeLlama?"
                )
                
                if result:
                    self.analyze_code_with_codellama(cleaned_text)
            else:
                messagebox.showinfo("OCR Results", "No text found in the image.")
                
        except Exception as e:
            if 'loading_window' in locals():
                loading_window.destroy()
            messagebox.showerror("Error", f"OCR failed: {str(e)}")
        
    def analyze_code_with_codellama(self, cleaned_text):
        """Analyze Leetcode-style questions using CodeLlama-13B-Instruct with memory management"""
        try:
            # Check memory before starting
            print("=== Memory before loading model ===")
            check_memory()
            
            # Show loading message
            loading_window = tk.Toplevel(self.root)
            loading_window.title("CodeLlama Analysis")
            loading_window.geometry("300x120")
            loading_label = tk.Label(loading_window, text="Loading CodeLlama model...\nThis may take 30-60 seconds on first run.")
            loading_label.pack(expand=True)
            loading_window.update()

            # Memory cleanup before loading
            import gc
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                torch.cuda.synchronize()

            # Load CodeLlama model and tokenizer
            from transformers import AutoTokenizer, AutoModelForCausalLM
            
            print("=== Loading model ===")
            tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-13B-Instruct-hf")
            model = AutoModelForCausalLM.from_pretrained(
                "codellama/CodeLlama-13B-Instruct-hf",
                torch_dtype=torch.float32 if torch.cuda.is_available() else torch.float32,
                # device_map="auto",
                device_map="cpu",
                low_cpu_mem_usage=True,  # Reduce memory usage
                offload_folder="offload"  # Offload to disk if needed
            )

            # Check memory after loading
            print("=== Memory after loading model ===")
            check_memory()

            # Memory cleanup after loading
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

            # Update loading message
            loading_label.config(text="Analyzing problem with CodeLlama...\nThis may take a minute.")
            loading_window.update()

            # Create prompt
            prompt = f"""<s>[INST] Analyze this Leetcode problem and provide a solution approach:

{cleaned_text}

Give me:
1. What the problem asks for
2. The algorithm approach

Keep it concise and actionable. [/INST]"""

            # Generate response with memory management
            inputs = tokenizer(prompt, return_tensors="pt")
            inputs = inputs.to(model.device)
            
            # Check memory before generation
            print("=== Memory before generation ===")
            check_memory()
            
            # Memory cleanup before generation
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=128,
                    temperature=0.5,
                    do_sample=False,
                    pad_token_id=tokenizer.eos_token_id,
                    #eos_token_id=tokenizer.eos_token_id,
                    #repetition_penalty=1.1,
                    #early_stopping=True
                )
            
            # Check memory after generation
            print("=== Memory after generation ===")
            check_memory()
            
            # Memory cleanup after generation
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            response = response[len(prompt):].strip()
            
            # Clear model from memory
            del model
            del tokenizer
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            
            # Check memory after cleanup
            print("=== Memory after cleanup ===")
            check_memory()
            
            loading_window.destroy()
            messagebox.showinfo("CodeLlama Problem Analysis", f"CodeLlama Analysis:\n\n{response}")
            
        except Exception as e:
            if 'loading_window' in locals():
                loading_window.destroy()
            # Memory cleanup on error
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            print("=== Memory after error ===")
            check_memory()
            messagebox.showerror("Error", f"CodeLlama analysis failed: {str(e)}")
        
    def run(self):
        """Start the application"""
        self.root.mainloop()

def main():
    """Main function"""
    try:
        app = MacScreenshotTool()
        app.run()
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Application failed to start: {str(e)}")

if __name__ == "__main__":
    main() 