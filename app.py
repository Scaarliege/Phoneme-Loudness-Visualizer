import tkinter as tk
from tkinter import messagebox
from phoneme_utils import get_phonetic, extract_phonemes, get_loudness_data
from plot_utils import plot_loudness

class DictionaryApp:
    def __init__(self, master):
        self.master = master
        master.title("Phoneme Loudness Dictionary")
        
        self.label = tk.Label(master, text="Enter English word(s):")
        self.label.pack(pady=5)
        
        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=5)
        
        self.submit_button = tk.Button(master, text="Submit", command=self.process_input)
        self.submit_button.pack(pady=5)
        
        self.quit_button = tk.Button(master, text="Exit", command=master.quit)
        self.quit_button.pack(pady=5)

    def process_input(self):
        inp = self.entry.get().strip()
        if inp.lower() == "exit":
            self.master.quit()
            return
        
        words = inp.split()
        for word in words:
            phonetic, error = get_phonetic(word)
            if error:
                messagebox.showerror("Error", error)
            else:
                phonemes = extract_phonemes(phonetic)
                x, y = get_loudness_data(phonemes)
                plot_loudness(x, y, word)

if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()