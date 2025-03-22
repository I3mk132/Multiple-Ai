import tkinter as tk
from tkinter import font

def show_all_fonts():
    root = tk.Tk()
    root.title("Tkinter Fonts Showcase")

    all_fonts = font.families()

    for i, font_name in enumerate(all_fonts):
        try:
            # Create a label with the current font
            label = tk.Label(root, text=font_name, font=(font_name, 8))
            
            # Calculate row and column dynamically
            row = i // 5
            col = i % 20
            
            label.grid(row=row, column=col, padx=1, pady=1)
        except tk.TclError:
            # Skip fonts that cannot be loaded
            pass

    root.mainloop()

if __name__ == "__main__":
    show_all_fonts()