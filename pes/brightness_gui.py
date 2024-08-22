#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import os

# Define the path to the brightness file
BRIGHTNESS_FILE = '/sys/class/backlight/intel_backlight/brightness'
MAX_BRIGHTNESS_FILE = '/sys/class/backlight/intel_backlight/max_brightness'

def read_brightness():
    """Read the current brightness value from the file."""
    try:
        with open(BRIGHTNESS_FILE, 'r') as file:
            return int(file.read().strip())
    except IOError as e:
        messagebox.showerror("Error", f"Unable to read brightness: {e}")
        return 0

def read_max_brightness():
    """Read the maximum brightness value from the file."""
    try:
        with open(MAX_BRIGHTNESS_FILE, 'r') as file:
            return int(file.read().strip())
    except IOError as e:
        messagebox.showerror("Error", f"Unable to read max brightness: {e}")
        return 100

def set_brightness(value):
    """Set the brightness to the specified value."""
    try:
        with open(BRIGHTNESS_FILE, 'w') as file:
            file.write(str(int(value)))
    except IOError as e:
        messagebox.showerror("Error", f"Unable to set brightness: {e}")

def update_brightness(value):
    """Update the brightness based on the slider value."""
    set_brightness(value)

# Create the main application window
root = tk.Tk()
root.title("Brightness Controller")

# Read the current and maximum brightness levels
current_brightness = read_brightness()
max_brightness = read_max_brightness()

# Create a label for the slider
label = tk.Label(root, text="Adjust Brightness")
label.pack(pady=10)

# Create a slider to adjust the brightness
slider = tk.Scale(root, from_=20, to=max_brightness, orient=tk.HORIZONTAL, length=300, command=update_brightness)
slider.set(current_brightness)
slider.pack(pady=20)

# Start the GUI event loop
root.mainloop()

