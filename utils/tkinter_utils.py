import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import yaml
import api


class LoginWindow:
    def __init__(self, is_public: bool) -> None:
        self.user = None
        self.password = None
        self.is_public = is_public
        self.baseurl = None
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry("500x300")
        self.window.eval("tk::PlaceWindow . center")
        self.window.eval(f"tk::PlaceWindow {str(self.window)} center")

    def start(self):
        url_values: list = [api.Path.BASEURL_LOCAL.value, api.Path.BASEURL_PROD.value]

        self.clicked = tk.StringVar()
        self.clicked.set("Pick the URL")
        drop = tk.OptionMenu(self.window, self.clicked, *url_values)
        drop.pack(pady=10)

        # Wait until a value is set to self.url_value
        self.window.wait_variable(self.clicked)
        self.baseurl = self.clicked.get().strip()

        if not self.is_public:
            username_label = tk.Label(self.window, text="Username")
            username_label.pack(pady=5)
            username_entry = tk.Entry(self.window)
            username_entry.pack(pady=5)

            password_label = tk.Label(self.window, text="Password")
            password_label.pack(pady=5)
            password_entry = tk.Entry(self.window, show="*")
            password_entry.pack(pady=5)

            login_button = tk.Button(
                self.window,
                text="Login & Connect",
                command=lambda: self.store_credentials(username_entry, password_entry),
            )
            login_button.pack(pady=5)
        else:
            connect_button = tk.Button(
                self.window,
                text="Connect",
                command=lambda: self.ack(),
            )
            connect_button.pack(pady=10)
        self.window.mainloop()

    def ack(self):
        ack_label = tk.Label(
            self.window, text="Connected! You may close this window.", fg="green"
        )
        ack_label.pack()

    def store_credentials(self, username_entry, password_entry):
        user = username_entry.get()
        password = password_entry.get()
        if user and password:
            self.user = username_entry.get()
            self.password = password_entry.get()
            self.ack()
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
        self.window = tk.Tk()
        self.window.title("File Picker")
        self.window.geometry("500x300")
        self.window.eval("tk::PlaceWindow . center")
        self.window.eval(f"tk::PlaceWindow {str(self.window)} center")
        self.file_path = None

    def open_file_picker(self):
        self.file_path = filedialog.askopenfilename()
        print("Selected file:", self.file_path)
        if self.file_path:
            self.window.destroy()

    def upload_file(self):
        file_picker_button = tk.Button(
            self.window, text="Select File", command=lambda: self.open_file_picker()
        )
        file_picker_button.pack(pady=20)

        self.window.mainloop()

        return self.file_path
