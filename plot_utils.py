import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Toplevel

def plot_loudness(x, y, word):
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(range(len(x)), y, tick_label=x, color='skyblue')
    
    for i, bar in enumerate(bars):
        ax.text(bar.get_x() + bar.get_width()/2.0, bar.get_height() + 0.1,
                f'{x[i]}', ha='center', va='bottom')
    
    ax.set_title(f"Loudness of Phonemes in '{word}'")
    ax.set_xlabel("Phonemes (in order)")
    ax.set_ylabel("Loudness")
    ax.set_ylim(0, 6)
    ax.grid(True, axis='y', linestyle='--', alpha=0.6)
    
    plot_window = Toplevel()
    plot_window.title(f"Loudness Plot for '{word}'")
    
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.get_tk_widget().pack(fill='both', expand=True)
    
    plt.tight_layout()
    canvas.draw()