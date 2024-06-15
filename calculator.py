import tkinter as tk
from tkinter import ttk

# Define the iPhone theme colors
bg_color = '#000000'          # Background color
fg_color = '#ffffff'          # Foreground (text) color
button_bg_color = '#EFEEED'   # Button background color
button_fg_color = '#000000'   # Button text color
highlight_color = '#f09a36'   # Highlight color for '=' button
operator_color = '#ff9500'    # Color for operator buttons

# Define button specific colors
row1_bg_color = '#373736'
row1_fg_color = '#FFFFFF'
row1_hover_bg_color = '#C7C7C4'
row1_hover_fg_color = '#FFFFFF'
col4_bg_color = '#f09a36'
col4_fg_color = '#EFEEED'

# Define a function named 'click' that takes an event as an argument
def click(event):
    text = event.widget.text
    if text == "=":
        try:
            result = str(eval(screen.get().replace('x', '*')))  # Replace 'x' with '*' for multiplication
            screen_var.set(result)            # Set the result in the screen_var
        except Exception as e:
            screen_var.set("Error")           # If an error occurs, display 'Error'
    elif text == "AC":
        screen_var.set("")                    # If the text on the button is 'AC', clear the entry widget
    elif text == '+/-':
        current = screen_var.get()
        if current:
            if current[0] == '-':
                screen_var.set(current[1:])
            else:
                screen_var.set('-' + current)
    elif text == '%':
        try:
            current = screen_var.get()
            if current:
                result = str(float(current) / 100)
                screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == '←':
        current = screen_var.get()
        if current:
            screen_var.set(current[:-1])
    else:
        screen_var.set(screen_var.get() + text)  # Append the button text to the current text in the entry widget

def on_enter(event):
    button = event.widget
    if button.text in ['AC', '+/-', '%', '←']:
        button.itemconfig(button.oval_id, fill=row1_hover_bg_color)
    else:
        button.itemconfig(button.oval_id, fill='#4b4b4b')

def on_leave(event):
    button = event.widget
    text = button.text
    if text in ['=', '+', '-', 'x', '/']:
        button.itemconfig(button.oval_id, fill=col4_bg_color)
    elif text == '=':
        button.itemconfig(button.oval_id, fill=highlight_color)
    elif text in ['AC', '+/-', '%', '←']:
        button.itemconfig(button.oval_id, fill=row1_bg_color)
    else:
        button.itemconfig(button.oval_id, fill=button_bg_color)

# Function to create a round button
def create_round_button(frame, text, bg, fg, command, row, col, padx=0, pady=0):
    button = tk.Canvas(frame, width=80, height=80, bg=bg_color, highlightthickness=0)
    button.grid(row=row, column=col, padx=padx, pady=pady, sticky='nsew')
    oval_id = button.create_oval(5, 5, 75, 75, fill=bg, outline=bg)
    text_id = button.create_text(40, 40, text=text, fill=fg, font='Roboto 36 bold')
    button.bind("<Button-1>", command)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.text = text  # Store the text in the button for reference
    button.oval_id = oval_id  # Store the oval ID for hover effect
    return button

# Create the main window of the application
root = tk.Tk()
root.title("Calculator")
root.configure(bg=bg_color)
root.geometry("320x500")  # iPhone size

# Entry Widget
# Create a StringVar to hold the text for the entry widget
screen_var = tk.StringVar()
# Create an entry widget for the calculator display
screen = tk.Entry(root, textvar=screen_var, font='System 40 bold', fg=fg_color, bg=bg_color, borderwidth=0, justify='right', highlightthickness=0)
# Add the entry widget to the main window with padding
screen.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10, padx=10)

# Create a frame to hold the calculator buttons
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(expand=True, fill=tk.BOTH)

buttons = [
    'AC', '+/-', '%', '←',
    '7', '8', '9', '/',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Initialize row and column variables for button placement
row, col = 0, 0

# Create a loop to add buttons
for button in buttons:
    if row == 0:
        btn_bg = row1_bg_color
        btn_fg = row1_fg_color
    elif col == 3:
        btn_bg = col4_bg_color
        btn_fg = col4_fg_color
    else:
        btn_bg = button_bg_color
        btn_fg = button_fg_color
    
    btn = create_round_button(button_frame, button, btn_bg, btn_fg, click, row, col)
    
    # Layout positioning
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure the grid layout of the button_frame so that all columns and rows have equal weight and expand evenly when the window is resized
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
for i in range(5):  # We have 5 rows, including the row for entry widget
    button_frame.grid_rowconfigure(i, weight=1)

root.mainloop()
