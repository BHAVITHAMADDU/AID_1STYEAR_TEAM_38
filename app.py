import tkinter as tk
from tkinter import font, colorchooser

# Function to update font and label text
def update_font():
    # Get user options
    user_text = text_entry.get()
    weight = "bold" if bold_var.get() else "normal"
    slant = "italic" if italic_var.get() else "roman"
    size = int(size_var.get())
    color = color_var.get()

    # Update label with user input and styles
    new_font = font.Font(family="Arial", size=size, weight=weight, slant=slant)
    label.config(text=user_text, font=new_font, fg=color)

# Function to choose font color
def choose_color():
    chosen_color = colorchooser.askcolor(title="Choose Font Color")[1]
    if chosen_color:
        color_var.set(chosen_color)

# Function to choose background color
def choose_bg_color():
    chosen_bg = colorchooser.askcolor(title="Choose Background Color")[1]
    if chosen_bg:
        root.config(bg=chosen_bg)
        label.config(bg=chosen_bg)
        title_label.config(bg=chosen_bg)
        for widget in [bold_cb, italic_cb, size_label, color_label, text_label]:
            widget.config(bg=chosen_bg)

# Main window setup
root = tk.Tk()
root.title("Font Style Demo")
root.geometry("500x550")
root.config(bg="#D8E9F0")  # default background color

# Title
title_label = tk.Label(root, text="FONT STYLE DEMO", bg="#D8E9F0", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# User text input
text_label = tk.Label(root, text="Enter Your Text:", bg="#D8E9F0", font=("Arial", 12))
text_label.pack()
text_entry = tk.Entry(root, width=30, font=("Arial", 12))
text_entry.insert(0, "Type something here...")
text_entry.pack(pady=5)

# Bold and Italic Checkbuttons
bold_var = tk.BooleanVar()
italic_var = tk.BooleanVar()
bold_cb = tk.Checkbutton(root, text="Bold", variable=bold_var, bg="#D8E9F0", font=("Arial", 12))
italic_cb = tk.Checkbutton(root, text="Italic", variable=italic_var, bg="#D8E9F0", font=("Arial", 12))
bold_cb.pack()
italic_cb.pack()

# Font size input
size_label = tk.Label(root, text="Font Size:", bg="#D8E9F0", font=("Arial", 12))
size_label.pack(pady=5)
size_var = tk.StringVar(value="20")
size_entry = tk.Entry(root, textvariable=size_var, width=5, font=("Arial", 12))
size_entry.pack()

# Font color selector
color_label = tk.Label(root, text="Font Color:", bg="#D8E9F0", font=("Arial", 12))
color_label.pack(pady=5)
color_var = tk.StringVar(value="black")
color_button = tk.Button(root, text="Choose Font Color", command=choose_color, bg="#C0E6F5", font=("Arial", 12))
color_button.pack()

# Background color selector
bg_button = tk.Button(root, text="Choose Background Color", command=choose_bg_color, bg="#B4D6C1", font=("Arial", 12))
bg_button.pack(pady=10)

# Apply button
apply_button = tk.Button(root, text="Apply Style", command=update_font, bg="#79A3B1", fg="white", font=("Arial", 12, "bold"))
apply_button.pack(pady=20)

# Label to display user text
label = tk.Label(root, text="", bg="#D8E9F0", font=("Arial", 20))
label.pack(pady=20)

root.mainloop()