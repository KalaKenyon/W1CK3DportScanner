import tkinter as tk
import socket

# Function to scan ports and update the UI
def scan_ports():
    target = target_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())

    open_ports.delete(1.0, tk.END)  # Clear previous results

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set timeout for the connection attempt
                result = s.connect_ex((target, port))
                if result == 0:
                    open_ports.insert(tk.END, f"Port {port} is open\n", "green")
                else:
                    open_ports.insert(tk.END, f"Port {port} is closed\n", "red")
        except Exception as e:
            open_ports.insert(tk.END, f"Error: {e}\n", "red")

# Create GUI window
root = tk.Tk()
root.title("W1CK3D Port Scanner")

# Create and pack widgets
target_label = tk.Label(root, text="Target IP:")
target_label.pack()

target_entry = tk.Entry(root)
target_entry.pack()

start_port_label = tk.Label(root, text="Start Port:")
start_port_label.pack()

start_port_entry = tk.Entry(root)
start_port_entry.pack()

end_port_label = tk.Label(root, text="End Port:")
end_port_label.pack()

end_port_entry = tk.Entry(root)
end_port_entry.pack()

scan_button = tk.Button(root, text="Scan Ports", command=scan_ports)
scan_button.pack(pady=10)

open_ports = tk.Text(root, wrap=tk.WORD)
open_ports.pack(expand=True, fill=tk.BOTH, pady=10, padx=10)

# Define tags for text color
open_ports.tag_config("green", foreground="green")
open_ports.tag_config("red", foreground="red")

# Run the GUI event loop
root.mainloop()
