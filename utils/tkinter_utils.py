import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import yaml
from constants import Path


class LoginWindow:
    def __init__(self, is_public: bool) -> None:
        self.user = None
        self.password = None
        self.is_public = is_public
        self.baseurl = None

        window = tk.Tk()
        window.title("Login")
        window.geometry("500x300")
        window.eval("tk::PlaceWindow . center")
        window.eval(f"tk::PlaceWindow {str(window)} center")

        url_values: list = [Path.BASEURL_LOCAL.value, Path.BASEURL_PROD.value]

        self.clicked = tk.StringVar()
        self.clicked.set("Pick the URL")
        drop = tk.OptionMenu(window, self.clicked, *url_values)
        drop.pack(pady=20)

        # Wait until a value is set to self.url_value
        window.wait_variable(self.clicked)
        self.baseurl = self.clicked.get().strip()

        if not self.is_public:
            username_label = tk.Label(window, text="Username")
            username_label.pack(pady=10)
            username_entry = tk.Entry(window)
            username_entry.pack(pady=10)

            password_label = tk.Label(window, text="Password")
            password_label.pack(pady=10)
            password_entry = tk.Entry(window, show="*")
            password_entry.pack(pady=10)

            login_button = tk.Button(
                window,
                text="Login & Close This Window",
                command=lambda: self.store_credentials(
                    window, username_entry, password_entry
                ),
            )
            login_button.pack(pady=10)
            print(self.user)
            print(self.password)
            window.mainloop()
        else:
            connect_button = tk.Button(
                window,
                text="Connect & Close This Window",
                command=window.destroy,
            )
            connect_button.pack(pady=10)
            window.mainloop()

    def store_credentials(self, window, username_entry, password_entry):
        user = username_entry.get()
        password = password_entry.get()
        if user and password:
            print(user)
            print(password)
            self.user = username_entry.get()
            self.password = password_entry.get()
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
