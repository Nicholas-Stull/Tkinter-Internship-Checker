import tkinter as tk
from tkinter import ttk


class InternshipChecker(ttk.Frame, object):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=6, column=0, padx=10, pady=(30, 10), sticky="nsew", rowspan=6
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # First Name Label
        self.fname_label = ttk.Label(self.widgets_frame, text="First Name:",)
        self.fname_label.grid(row=0, column=0, padx=5,
                              pady=(0, 10), sticky="ew")
        # First Name Entry
        self.fname = ttk.Entry(self.widgets_frame)
        self.fname.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="ew")
# --------------------------------------------------------------------
        # Last Name Label
        self.lname_label = ttk.Label(self.widgets_frame, text="Last Name:")
        self.lname_label.grid(row=1, column=0, padx=5,
                              pady=(0, 10), sticky="ew")
        # Last Name Entry
        self.lname = ttk.Entry(self.widgets_frame)
        self.lname.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")
# --------------------------------------------------------------------
        # Major Label
        self.major_label = ttk.Label(self.widgets_frame, text="Major:")
        self.major_label.grid(row=2, column=0, padx=5,
                              pady=(0, 10), sticky="ew")
        # Major Entry
        self.major = ttk.Entry(self.widgets_frame)
        self.major.grid(row=2, column=1, padx=5, pady=(0, 10), sticky="ew")
# --------------------------------------------------------------------
        # Credits Label
        self.credits_label = ttk.Label(self.widgets_frame, text="Credits:")
        self.credits_label.grid(row=3, column=0, padx=5,
                                pady=(0, 10), sticky="ew")
        # Credits Entry
        self.credits = ttk.Entry(self.widgets_frame)
        self.credits.grid(row=3, column=1, padx=5, pady=(0, 10), sticky="ew")
# --------------------------------------------------------------------
        # Button
        self.button = ttk.Button(
            self.widgets_frame, text="Check Eligibility", command=self.check_eligibility)
        self.button.grid(row=4, column=0, columnspan=2,
                         padx=5, pady=(0, 10), sticky="ew")
# --------------------------------------------------------------------
        # label
        self.results = ttk.Label(wraplength=340)
        self.results.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="ew")
# --------------------------------------------------------------------

    def check_eligibility(self):
        try:
            # Retrieve values from entries
            first_name = self.fname.get().upper
            last_name = self.lname.get().upper
            major = self.major.get()
            credits = int(self.credits.get())

            # Check eligibility based on criteria
            if credits >= 125 and major.lower() == "it":
                message = f"Congratulations {first_name} {last_name}.\nYou are eligible for an internship!\nThe Minimum credits for the internship is 125"
            else:
                message = f"Sorry {first_name} {last_name}.\nYou are not eligible for an internship.\nThe Minimum credits for the internship is 125"

            # Display result
            self.results.config(text=message)

        except ValueError:
            # Handle ValueError if credits is not an integer
            self.results.config(text="Credits must be an integer.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Internship Checker")
    # root.geometry("400x400")

    # Simply set the theme
    #root.tk.call("source", "azure.tcl")
    #root.tk.call("set_theme", "dark")

    app = InternshipChecker(root)
    app.grid(row=0, column=0, sticky="nsew")

    # Set a minsize for the window, and place it in the middle

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) -
                      (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) -
                      (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()
