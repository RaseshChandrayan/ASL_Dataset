import tkinter as tk
import subprocess
import os
import signal

def start_detection():
    global process
    # Start the realtimedetection.py script
    process = subprocess.Popen(["python", "realtimedetection.py"])

def stop_detection():
    global process
    # Stop the realtimedetection.py script by sending SIGTERM signal
    if process:
        process.terminate()

def close_gui():
    global process
    # Stop the realtimedetection.py script if running
    if process:
        process.terminate()
    # Close the GUI
    print("Closing GUI")
    root.destroy()

root = tk.Tk()
root.title("Hand Detection Control")

process = None

# Create buttons
start_button = tk.Button(root, text="Start Detection", command=start_detection)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Detection", command=stop_detection)
stop_button.pack(pady=10)

close_button = tk.Button(root, text="Close", command=close_gui)
close_button.pack(pady=10)

root.mainloop()
