"""
Task 04 - Simple Keylogger (Educational & Limited Scope)
Internship: Prodigy InfoTech - Cyber Security

IMPORTANT:
- This program ONLY logs keys typed inside its own window.
- It does NOT log system-wide keystrokes.
- It is meant for learning how keystroke logging works in a safe, ethical way.
"""

import tkinter as tk
from datetime import datetime

LOG_FILE = "key_log.txt"


def log_to_file(text: str) -> None:
    """Append text to a log file with timestamp."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)


def on_key_press(event):
    """
    This function is called every time a key is pressed
    inside the text box.
    """
    key = event.keysym      # symbolic name like 'a', 'Return', 'BackSpace'
    char = event.char       # actual character like 'a', '\n', etc.

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Build a readable representation of the key
    if char and char.isprintable():
        display_key = char
    else:
        # Special keys like Enter, Backspace, etc.
        display_key = f"<{key}>"

    log_line = f"[{timestamp}] {display_key}\n"

    # Show in the log area on screen
    log_area.insert(tk.END, log_line)
    log_area.see(tk.END)  # auto-scroll

    # Save to file
    log_to_file(log_line)


def clear_log():
    """Clear the on-screen log area (file remains)."""
    log_area.delete("1.0", tk.END)


def main():
    global log_area

    root = tk.Tk()
    root.title("Simple Keylogger (Educational Task 04)")
    root.geometry("600x400")

    # Instruction label
    tk.Label(
        root,
        text="Type in the box below. Every key press will be logged to key_log.txt",
        font=("Arial", 10)
    ).pack(pady=5)

    # Text input area where user types
    input_box = tk.Text(root, height=5)
    input_box.pack(fill=tk.X, padx=10, pady=5)

    # Bind key press events in this text box
    input_box.bind("<KeyPress>", on_key_press)

    # Log display area (read-only-ish)
    tk.Label(root, text="Logged Keystrokes:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
    log_area = tk.Text(root, height=10)
    log_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # Button to clear only on-screen log
    tk.Button(root, text="Clear Display", command=clear_log).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()