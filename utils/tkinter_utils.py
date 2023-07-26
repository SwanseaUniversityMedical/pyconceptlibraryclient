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
