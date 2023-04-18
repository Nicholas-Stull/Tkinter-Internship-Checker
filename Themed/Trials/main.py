"""
Example script for testing the Azure ttk theme
Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""


import tkinter as tk
from tkinter import ttk


class  InternshipChecker(ttk.Frame, object):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # First Name
        self.fname = ttk.Entry(self.widgets_frame)
        self.fname.insert(0, "First Name:")
        self.fname.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")
        # Last Name
        self.lname = ttk.Entry(self.widgets_frame)
        self.lname.insert(0, "Last Name:")
        self.lname.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ew")
        # Major
        self.major = ttk.Entry(self.widgets_frame)
        self.major.insert(0, "Major:")
        self.major.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="ew")
        # Credits
        self.credits = ttk.Entry(self.widgets_frame)
        self.credits.insert(0, "Credits:")
        self.credits.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="ew")
        # Button
        self.button = ttk.Button(
        self.widgets_frame, text="Check Eligibility", command=self.check_eligibility)
        self.button.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="ew")
        #label
        self.results = ttk.Label()
        self.results.grid(row=5, column=0, pady=10, columnspan=2)

        




    def check_eligibility(self):
        try:
            # Retrieve values from entries
            first_name = self.fname.get()
            last_name = self.lname.get()
            major = self.major.get()
            credits = int(self.credits.get())

            # Check eligibility based on criteria
            if credits >= 125 and major.lower() == "it":
                message = f"Congratulations {first_name} {last_name}, you are eligible for an internship!\nThe Minimum credits for the internship is 125"
            else:
                message = f"Sorry {first_name} {last_name}, you are not eligible for an internship.\nThe Minimum credits for the internship is 125"

            # Display result
            self.results.config(text=message)

        except ValueError:
            # Handle ValueError if credits is not an integer
            self.results.config(text="Credits must be an integer.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Internship Checker")

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = InternshipChecker(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) -
                      (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) -
                      (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()


