import tkinter as tk
from tkinter import filedialog
import time
# from some_module import check_malicious


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Add label to prompt user to select a text file or enter plain text
        self.input_label = tk.Label(
            self, text="Enter the text to check or select a file to check:")
        self.input_label.pack()

        # Add text box for user to enter plain text
        self.text_box = tk.Text(self, height=10)
        self.text_box.pack()

        # Add button to select a file
        self.select_file_button = tk.Button(
            self, text="Select File", command=self.select_file)
        self.select_file_button.pack()

        # Add button to check if text is malicious
        self.check_button = tk.Button(
            self, text="Check", command=self.check_text)
        self.check_button.pack()

        # Add label to display result
        self.result_label = tk.Label(self, text="")

    def select_file(self):
        # Allow user to select a file and load its contents into the text box
        file_path = filedialog.askopenfilename()
        with open(file_path, "r") as f:
            self.text_box.delete("1.0", "end")
            self.text_box.insert("end", f.read())

    def check_text(self):
        # Disable the check button to prevent multiple clicks
        self.check_button.configure(state="disabled")

        # Show loading wheel animation
        self.loading_animation = tk.Label(
            self, text="Checking...", font=("Arial", 16))
        self.loading_animation.pack()

        # Get the text from the text box
        text = self.text_box.get("1.0", "end-1c")

        # Call the function to check if text is malicious
        is_malicious = "malicious"  # check_malicious(text)

        # Remove the loading animation and show the result
        self.loading_animation.pack_forget()
        if is_malicious:
            self.result_label.configure(text="The text is malicious.")
        else:
            self.result_label.configure(text="The text is not malicious.")

        self.result_label.pack()

        # Enable the check button again
        self.check_button.configure(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
