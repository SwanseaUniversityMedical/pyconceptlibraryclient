import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import yaml


class LoginWindow:
    def __init__(self) -> None:
        self.user = None
        self.password = None
        self.username_entry = None
        self.password_entry = None

    def create_window(self):
        window = tk.Tk()
        window.title("Login")
        window.geometry("500x300")
        window.eval("tk::PlaceWindow . center")
        window.eval(f"tk::PlaceWindow {str(window)} center")
        return window

    def get_url_dropdown_field(self, window, url_values: list):
        self.clicked = tk.StringVar()
        self.clicked.set("Pick the URL")
        drop = tk.OptionMenu(window, self.clicked, *url_values)
        drop.pack(pady=20)

        # Wait until a value is set to self.url_value
        window.wait_variable(self.clicked)

        # Return the StringVar itself (optional, useful if you want to use it elsewhere)
        return self.clicked

    def get_username_field(self, window):
        username_label = tk.Label(window, text="Username")
        username_label.pack()
        self.username_entry = tk.Entry(window)
        self.username_entry.pack()
        return self.username_entry

    def get_password_field(self, window):
        password_label = tk.Label(window, text="Password")
        password_label.pack()
        self.password_entry = tk.Entry(window, show="*")
        self.password_entry.pack()
        return self.password_entry

    def get_login_button(self, window):
        login_button = tk.Button(
            window, text="Login", command=lambda: self.store_credentials(window)
        )
        login_button.pack()

    def get_connect_button(self, window):
        login_button = tk.Button(
            window, text="Connect", command=lambda: window.destroy()
        )
        login_button.pack()

    def store_credentials(self, window):
        user = self.username_entry
        password = self.password_entry
        if user and password:
            self.user = self.username_entry.get()
            self.password = self.password_entry.get()
            window.destroy()
        else:
            messagebox.showwarning(
                "Incomplete Credentials", "Please enter both username and password."
            )


class SaveFile:
    def __init__(self, content) -> None:
        self.content = content

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            filetypes=[("YAML files", "*.yaml or *.yml"), ("JSON files", "*.json")]
        )
        if not file_path:
            return
        with open(file_path, "w") as file:
            yaml.dump(
                self.content,
                file,
                default_flow_style=False,
                sort_keys=False,
            )


class OpenFile:
    def __init__(self) -> None:
        self.file_path = None

    def open_file_picker(self, window):
        self.file_path = filedialog.askopenfilename()
        print("Selected file:", self.file_path)
        if self.file_path:
            window.destroy()

    def upload_file(self):
        # GUI Setup
        app = tk.Tk()
        app.title("File Picker")

        # Get the screen width and height
        screen_width = app.winfo_screenwidth()
        screen_height = app.winfo_screenheight()

        # Calculate the center coordinates
        center_x = int((screen_width - 300) / 2)
        center_y = int((screen_height - 150) / 2)

        # Set the window size and position it in the center of the screen
        app.geometry(f"300x150+{center_x}+{center_y}")

        file_picker_button = tk.Button(
            app, text="Select File", command=lambda: self.open_file_picker(app)
        )
        file_picker_button.pack(pady=20)

        app.mainloop()

        return self.file_path
