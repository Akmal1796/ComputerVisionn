import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def read_file():
    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("CSV Files", "*.csv"), ("Text Files", "*.txt"), ("Excel Files", "*.xlsx")]
    )
    if not file_path:
        return

    try:
        if file_path.endswith(".csv"):
            data = pd.read_csv(file_path)
        elif file_path.endswith(".txt"):
            with open(file_path, "r") as file:
                data = file.read()
        elif file_path.endswith(".xlsx"):
            data = pd.read_excel(file_path)
        else:
            messagebox.showerror("Error", "Unsupported file format")
            return

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, data)
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {str(e)}")


# GUI Setup
root = tk.Tk()
root.title("File Reader")

tk.Button(root, text="Open File", command=read_file).pack(pady=10)
output_text = tk.Text(root, wrap="word", height=20, width=80)
output_text.pack(padx=10, pady=10)

root.mainloop()
