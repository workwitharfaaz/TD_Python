import socket
import threading
import tkinter as tk
from tkinter import scrolledtext


class ClientApp:

    def __init__(self, root, host="127.0.0.1", port=12345):
        self.root = root
        self.root.title("Python Socket Chat - CLIENT")
        self.root.geometry("400x500")

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.chat_display = scrolledtext.ScrolledText(
            root, state="disabled", wrap=tk.WORD
        )
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.msg_entry = tk.Entry(root)
        self.msg_entry.pack(
            padx=10, pady=(0, 5), fill=tk.X, side=tk.LEFT, expand=True
        )
        self.msg_entry.bind("<Return>", lambda event: self.send_message())

        self.send_btn = tk.Button(
            root, text="Send", command=self.send_message, state=tk.DISABLED
        )
        self.send_btn.pack(padx=(0, 10), pady=(0, 5), side=tk.RIGHT)

        self.connect_to_server(host, port)

    def display_message(self, sender, text):
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, f"{sender}: {text}\n")
        self.chat_display.config(state="disabled")
        self.chat_display.yview(tk.END)

    def connect_to_server(self, host, port):
        try:
            self.client_socket.connect((host, port))
            self.display_message("System", f"Connected to server {host}:{port}")
            self.send_btn.config(state=tk.NORMAL)

            threading.Thread(
                target=self.receive_messages, daemon=True
            ).start()
        except Exception as e:
            self.display_message("System", f"Could not connect to server: {e}")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                if not message:
                    break
                self.display_message("Server", message)
            except ConnectionResetError:
                break

        self.display_message("System", "Disconnected from server.")
        self.send_btn.config(state=tk.DISABLED)

    def send_message(self):
        msg = self.msg_entry.get().strip()
        if msg:
            try:
                self.client_socket.send(msg.encode("utf-8"))
                self.display_message("Client (You)", msg)
                self.msg_entry.delete(0, tk.END)
            except Exception as e:
                self.display_message("System", f"Error sending message: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ClientApp(root)
    root.mainloop()