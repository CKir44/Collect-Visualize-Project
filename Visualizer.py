import json
import pandas as pd

# Load the JSON file
with open("data_capture.json", "r") as f:
    data = json.load(f)

# Extract Timestamps
timestamps = [entry["timestamp"] for entry in data]

# System Usage DataFrame
system_usage = pd.DataFrame({
    "timestamp": timestamps,
    "cpu_usage": [entry["system_usage"]["cpu_usage"] for entry in data],
    "memory_total": [entry["system_usage"]["memory"]["total"] for entry in data],
    "memory_used": [entry["system_usage"]["memory"]["used"] for entry in data],
    "memory_free": [entry["system_usage"]["memory"]["free"] for entry in data],
    "disk_total": [entry["system_usage"]["disk_usage"]["total"] for entry in data],
    "disk_used": [entry["system_usage"]["disk_usage"]["used"] for entry in data],
    "disk_free": [entry["system_usage"]["disk_usage"]["free"] for entry in data],
    "disk_percent": [entry["system_usage"]["disk_usage"]["percent"] for entry in data],
    "uptime": [entry["system_usage"]["uptime"] for entry in data]
})

# User Activity DataFrame
user_activity = pd.DataFrame({
    "timestamp": timestamps,
    "active_sessions": [entry["user_activity"]["active_sessions"] for entry in data],
    "command_history": [entry["user_activity"]["command_history"] for entry in data]
})

# Network Activity DataFrame
network_activity = pd.DataFrame({
    "timestamp": timestamps,
    "connected_ips": [entry["network_activity"]["connected_ips"] for entry in data],
    "open_connections": [entry["network_activity"]["open_connections"] for entry in data],
    "bytes_sent": [entry["network_activity"]["bandwidth_usage"]["bytes_sent"] for entry in data],
    "bytes_recv": [entry["network_activity"]["bandwidth_usage"]["bytes_recv"] for entry in data],
    "packets_sent": [entry["network_activity"]["bandwidth_usage"]["packets_sent"] for entry in data],
    "packets_recv": [entry["network_activity"]["bandwidth_usage"]["packets_recv"] for entry in data]
})

# File System Details DataFrame
file_system_details = pd.DataFrame({
    "timestamp": timestamps,
    "largest_files": [entry["file_system_details"]["largest_files"] for entry in data],
    "photo_count": [entry["file_system_details"]["photo_count"] for entry in data],
    "video_count": [entry["file_system_details"]["video_count"] for entry in data]
})

# Save to CSV for Power BI
system_usage.to_csv("system_usage.csv", index=False)
user_activity.to_csv("user_activity.csv", index=False)
network_activity.to_csv("network_activity.csv", index=False)
file_system_details.to_csv("file_system_details.csv", index=False)

print("Data successfully processed and saved to CSV files!")
