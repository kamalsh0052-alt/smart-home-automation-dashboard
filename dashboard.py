import tkinter as tk

# Main window
root = tk.Tk()
root.title("Smart Home Automation")
root.geometry("800x550")
root.configure(bg="#101820")


# Functions
def toggle_light():
    if light_button["text"] == "OFF":
        light_button.config(text="ON", bg="green")
        light_status.config(text="Light is ON")
    else:
        light_button.config(text="OFF", bg="red")
        light_status.config(text="Light is OFF")


def toggle_fan():
    if fan_button["text"] == "OFF":
        fan_button.config(text="ON", bg="green")
        fan_status.config(text="Fan is ON")
    else:
        fan_button.config(text="OFF", bg="red")
        fan_status.config(text="Fan is OFF")


def toggle_ac():
    if ac_button["text"] == "OFF":
        ac_button.config(text="ON", bg="green")
        ac_status.config(text="AC is ON")
    else:
        ac_button.config(text="OFF", bg="red")
        ac_status.config(text="AC is OFF")


# Heading
title = tk.Label(
    root,
    text="🏠 SMART HOME AUTOMATION",
    font=("Arial", 24, "bold"),
    bg="#101820",
    fg="white"
)
title.pack(pady=25)

subtitle = tk.Label(
    root,
    text="Home Control Dashboard",
    font=("Arial", 14),
    bg="#101820",
    fg="lightgray"
)
subtitle.pack()


# Device frame
device_frame = tk.Frame(root, bg="#101820")
device_frame.pack(pady=35)


# LIGHT
light_frame = tk.Frame(device_frame, bg="#1E2A35", padx=25, pady=20)
light_frame.grid(row=0, column=0, padx=15)

tk.Label(
    light_frame,
    text="💡 LIGHT",
    font=("Arial", 16, "bold"),
    bg="#1E2A35",
    fg="white"
).pack()

light_button = tk.Button(
    light_frame,
    text="OFF",
    width=10,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    command=toggle_light
)
light_button.pack(pady=10)

light_status = tk.Label(
    light_frame,
    text="Light is OFF",
    bg="#1E2A35",
    fg="white"
)
light_status.pack()


# FAN
fan_frame = tk.Frame(device_frame, bg="#1E2A35", padx=25, pady=20)
fan_frame.grid(row=0, column=1, padx=15)

tk.Label(
    fan_frame,
    text="🌀 FAN",
    font=("Arial", 16, "bold"),
    bg="#1E2A35",
    fg="white"
).pack()

fan_button = tk.Button(
    fan_frame,
    text="OFF",
    width=10,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    command=toggle_fan
)
fan_button.pack(pady=10)

fan_status = tk.Label(
    fan_frame,
    text="Fan is OFF",
    bg="#1E2A35",
    fg="white"
)
fan_status.pack()


# AC
ac_frame = tk.Frame(device_frame, bg="#1E2A35", padx=25, pady=20)
ac_frame.grid(row=0, column=2, padx=15)

tk.Label(
    ac_frame,
    text="❄️ AC",
    font=("Arial", 16, "bold"),
    bg="#1E2A35",
    fg="white"
).pack()

ac_button = tk.Button(
    ac_frame,
    text="OFF",
    width=10,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    command=toggle_ac
)
ac_button.pack(pady=10)

ac_status = tk.Label(
    ac_frame,
    text="AC is OFF",
    bg="#1E2A35",
    fg="white"
)
ac_status.pack()


# Temperature
temperature = tk.Label(
    root,
    text="🌡 Temperature: 27°C",
    font=("Arial", 16, "bold"),
    bg="#101820",
    fg="white"
)
temperature.pack(pady=15)


# System status
system = tk.Label(
    root,
    text="📡 System Status: CONNECTED",
    font=("Arial", 14, "bold"),
    bg="#101820",
    fg="lightgreen"
)
system.pack(pady=10)


# Run application
root.mainloop()