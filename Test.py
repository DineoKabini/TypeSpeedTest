import tkinter as tk
from tkinter import messagebox
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sample_text = (
            "The quick brown fox jumps over the lazy dog. This sentence is often used to test typing speed and keyboard functionality because it contains every letter in the English alphabet. Practice regularly to improve your typing accuracy and speed significantly"
        )

        self.text_label = tk.Label(root, text=self.sample_text, wraplength=400)
        self.text_label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.calculate_speed)

        self.start_button = tk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Test", command=self.stop_test)
        self.stop_button.pack(pady=5)

        self.time_label = tk.Label(root, text="Time: 0 seconds")
        self.time_label.pack(pady=10)

        self.start_time = None
        self.end_time = None

    def start_test(self):
        self.start_time = time.time()
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.time_label.config(text="Time: 0 seconds")
        self.root.after(1000, self.update_timer)

    def update_timer(self):
        if self.start_time:
            elapsed_time = int(time.time() - self.start_time)
            self.time_label.config(text=f"Time: {elapsed_time} seconds")
            self.root.after(1000, self.update_timer)

    def stop_test(self):
        if self.start_time:
            self.end_time = time.time()
            self.calculate_speed(None)

    def calculate_speed(self, event):
        if not self.start_time:
            messagebox.showwarning("Warning", "Please start the test first!")
            return

        elapsed_time = self.end_time - self.start_time if self.end_time else time.time() - self.start_time
        typed_text = self.entry.get()
        word_count = len(typed_text.split())

        words_per_minute = (word_count / elapsed_time) * 60

        messagebox.showinfo("Typing Speed", f"Your typing speed is {words_per_minute:.2f} words per minute.")

        self.start_time = None
        self.end_time = None
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
