import tkinter as tk

def increment():
    current_value = int(label["text"])
    label["text"] = str(current_value + 1)

def decrement():
    current_value = int(label["text"])
    label["text"] = str(current_value - 1)
    
def reset():
    label["text"] = 0

# Create the main window
root = tk.Tk()
root.title("Counter App")

# Create a label to display the counter
label = tk.Label(root, text="0", font=("Helvetica", 50))
label.pack(pady=20)

# Create buttons to increment and decrement the counter
increment_button = tk.Button(root, text="Increment", command=increment)
decrement_button = tk.Button(root, text="Decrement", command=decrement)
reset_button = tk.Button(root, text="Reset", command=reset)

increment_button.pack()
decrement_button.pack()
reset_button.pack()

# Start the GUI main loop
root.mainloop()
