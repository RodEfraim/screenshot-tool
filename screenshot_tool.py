#!/usr/bin/env python3
"""
Simple Screenshot Tool for macOS
Uses native macOS screenshot functionality
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import os
from datetime import datetime

class MacScreenshotTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("macOS Screenshot Tool")
        self.root.geometry("300x200")
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
            text="Click a button to use native macOS screenshot",
            font=('Arial', 10),
            justify='center'
        )
        instructions.pack(pady=(0, 30))
        
        # Buttons frame
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # Select Area button
        self.select_btn = tk.Button(
            button_frame,
            text="Select Area",
            command=self.select_area,
            font=('Arial', 12),
            padx=20,
            pady=10
        )
        self.select_btn.pack(side='left', padx=10)
        
        # Full Screen button
        self.fullscreen_btn = tk.Button(
            button_frame,
            text="Full Screen",
            command=self.full_screen,
            font=('Arial', 12),
            padx=20,
            pady=10
        )
        self.fullscreen_btn.pack(side='left', padx=10)
        
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
            subprocess.run(['screencapture', full_path], check=True)
            messagebox.showinfo("Success", f"Screenshot saved to Desktop:\n{filename}")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to capture screenshot.")
        except FileNotFoundError:
            messagebox.showerror("Error", "screencapture not found. This tool requires macOS.")
        
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