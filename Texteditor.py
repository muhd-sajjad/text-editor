from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.simpledialog import askstring

# Create the main window
window = Tk()
window.title("Untitled - Unsaved")  # Set initial window title

# Create a Text widget
editor = Text(window, width=60, height=20)
editor.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Create a Scrollbar
scrollbar = Scrollbar(window, orient=VERTICAL, command=editor.yview)
scrollbar.grid(row=0, column=2, sticky="ns")

# Link the scrollbar to the Text widget
editor.config(yscrollcommand=scrollbar.set)

# Initialize variable to track save status
saved = False

# Define the save function
def save(event=None):
    global saved
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = editor.get(1.0, END)
        output_file.write(text)
    window.title(f"{filepath.split('/')[-1]} - Saved")  # Update window title
    saved = True

# Create the Save button
save_button = Button(window, text='Save', font=('Arial', 12), command=save, bg='white')
save_button.grid(row=1, column=0, padx=(10,5), pady=10)  # Added padding

# Define the replace function
def replace(event=None):
    find_text = askstring("Find", "Enter text to find:")
    if find_text:
        replace_text = askstring("Replace", "Enter text to replace:")
        if replace_text:
            content = editor.get(1.0, END)
            replaced_content = content.replace(find_text, replace_text)
            editor.delete(1.0, END)
            editor.insert(1.0, replaced_content)

# Create the Replace button
replace_button = Button(window, text='Replace', font=('Arial', 12), command=replace, bg='white')
replace_button.grid(row=1, column=1, padx=(5,10), pady=10)  # Added padding

# Bind keyboard shortcuts
window.bind("<Control-s>", save)  # Ctrl+S to save
window.bind("<Control-r>", replace)  # Ctrl+R to replace

# Configure row and column weights to make them expandable
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Start the main event loop
window.mainloop()
