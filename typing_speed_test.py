import tkinter as tk
import time
import random

# Sample text list
TEXTS = [
    "The quick brown fox jumps over the lazy dog",
    "Typing speed tests help improve accuracy",
    "Python is a great language for building GUI apps",
    "Tkinter is simple yet powerful for beginners"
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        self.start_time = None
        self.selected_text = random.choice(TEXTS)

        tk.Label(root, text="Typing Speed Tester",font=("Arial", 24, "bold")).pack(pady=10)

        self.text_label = tk.Label(root, text=self.selected_text,font=("Arial", 14), wraplength=650).pack(pady=20)
       

        self.text_box = tk.Text(root, height=5, width=70, font=("Arial", 14))
        self.text_box.pack()
        self.text_box.bind("<KeyPress>", self.start_timer)

        self.result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
        self.result_label.pack(pady=15)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Done", font=("Arial", 14),
                  command=self.calculate_speed).grid(row=0, column=0, padx=10)

        tk.Button(btn_frame, text="Reset", font=("Arial", 14),
                  command=self.reset_test).grid(row=0, column=1, padx=10)

    def start_timer(self, event):
        if self.start_time is None:        # Timer starts on first keypress
            self.start_time = time.time()
            
            

    def calculate_speed(self):
        if self.start_time is None:
            self.result_label.config(text="Start typing first!")
            return

        total_time = time.time() - self.start_time
        typed_text = self.text_box.get("1.0", tk.END).strip()

        words = typed_text.split()
        word_count = len(words)

        wpm = round((word_count / total_time) * 60)

        accuracy = self.calculate_accuracy(typed_text)

        self.result_label.config(
            text=f"WPM: {wpm}   |   Accuracy: {accuracy}%"
        )

    def calculate_accuracy(self, typed):
        original_words = self.selected_text.split()
        typed_words = typed.split()

        correct = 0

        for o, t in zip(original_words, typed_words):
            if o == t:
                correct += 1

        if len(original_words) == 0:
            return 0

        return round((correct / len(original_words)) * 100)

    def reset_test(self):
        self.start_time = None
        self.text_box.delete("1.0", tk.END)
        self.selected_text = random.choice(TEXTS)
        self.text_label.config(text=self.selected_text)
        self.result_label.config(text="")


# Run the app
root = tk.Tk()
TypingSpeedTest(root)
root.mainloop()
