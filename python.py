import tkinter as tk
from tkinter import colorchooser

def apply_styles():
    text = user_input.get()
    font_size = int(font_size_input.get())
    font_color = font_color_input.get()
    bg_color = bg_color_input.get()

    output_label.config(
        text=text,
        font=("Arial", font_size),
        fg=font_color,
        bg=bg_color
    )

def choose_font_color():
    color = colorchooser.askcolor(title="Choose Font Color")[1]
    font_color_input.delete(0, tk.END)
    font_color_input.insert(0, color)

def choose_bg_color():
    color = colorchooser.askcolor(title="Choose Background Color")[1]
    bg_color_input.delete(0, tk.END)
    bg_color_input.insert(0, color)

# Create main window
root = tk.Tk()
root.title("Font Style Customizer")
root.geometry("400x400")

# User input
tk.Label(root, text="Enter Text:").pack()
user_input = tk.Entry(root, width=30)
user_input.pack()

# Font size
tk.Label(root, text="Font Size:").pack()
font_size_input = tk.Entry(root, width=10)
font_size_input.insert(0, "16")
font_size_input.pack()

# Font color
tk.Label(root, text="Font Color:").pack()
font_color_input = tk.Entry(root, width=10)
font_color_input.insert(0, "#000000")
font_color_input.pack()
tk.Button(root, text="Choose Font Color", command=choose_font_color).pack()

# Background color
tk.Label(root, text="Background Color:").pack()
bg_color_input = tk.Entry(root, width=10)
bg_color_input.insert(0, "#ffffff")
bg_color_input.pack()
tk.Button(root, text="Choose Background Color", command=choose_bg_color).pack()

# Apply button
tk.Button(root, text="Apply Styles", command=apply_styles).pack(pady=10)

# Output label
output_label = tk.Label(root, text="Your styled text will appear here.", width=40, height=5)
output_label.pack(pady=20)

root.mainloop()