import os
import psutil
import json
import time
from datetime import datetime

def collect_system_usage():
    """
    Collect CPU, memory, uptime, and disk usage.
    """
    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory": {
            "total": psutil.virtual_memory().total,
            "used": psutil.virtual_memory().used,
            "free": psutil.virtual_memory().free,
        },
        "disk_usage": psutil.disk_usage('/')._asdict(),
        "uptime": time.time() - psutil.boot_time(),
    }

def collect_user_activity():
    """
    Collect active sessions and command history.
    """
    try:
        active_sessions = os.popen("who").read().strip()
        command_history = os.popen("cat ~/.bash_history").read().strip()
        return {
            "active_sessions": active_sessions,
            "command_history": command_history,
        }
    except Exception as e:
        return {"error": str(e)}

def collect_network_activity():
    """
    Collect IP addresses, open connections, and bandwidth usage.
    """
    try:
        connected_ips = os.popen("hostname -I").read().strip()
        open_connections = os.popen("netstat -tunapl").read().strip()
        bandwidth = psutil.net_io_counters()._asdict()
        return {
            "connected_ips": connected_ips,
            "open_connections": open_connections,
            "bandwidth_usage": bandwidth,
        }
    except Exception as e:
        return {"error": str(e)}

def collect_file_system_details():
    """
    Find largest files and directories, count photos/videos.
    """
    largest_files = []
    try:
        for root, dirs, files in os.walk("/"):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    size = os.path.getsize(file_path)
                    largest_files.append({"file": file_path, "size": size})
                except:
                    continue
        largest_files = sorted(largest_files, key=lambda x: x["size"], reverse=True)[:10]

        photo_count = os.popen(r"find / -type f \( -iname '*.jpg' -o -iname '*.png' \) | wc -l").read().strip()
        video_count = os.popen(r"find / -type f \( -iname '*.mp4' -o -iname '*.mov' \) | wc -l").read().strip()

        return {
            "largest_files": largest_files,
            "photo_count": photo_count,
            "video_count": video_count,
        }
    except Exception as e:
        return {"error": str(e)}

def save_data(data, output_file="/tmp/data_capture.json"):
    """
    Append collected data to a JSON file. If the file does not exist, create it.
    """
    try:
        # Load existing data if the file exists
        if os.path.exists(output_file):
            with open(output_file, "r") as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        # Append new data
        existing_data.append(data)

        # Save updated data
        with open(output_file, "w") as f:
            json.dump(existing_data, f, indent=4)

        print(f"Data appended to {output_file}")
    except Exception as e:
        print(f"Error saving data: {e}")

if __name__ == "__main__":
    # Interval between data captures (in seconds)
    INTERVAL = 300  # 5 minutes

    while True:
        print(f"[{datetime.now()}] Capturing data...")

        # Collect all data
        system_usage = collect_system_usage()
        user_activity = collect_user_activity()
        network_activity = collect_network_activity()
        file_system_details = collect_file_system_details()

        # Combine data into a single object
        data = {
            "timestamp": str(datetime.now()),
            "system_usage": system_usage,
            "user_activity": user_activity,
            "network_activity": network_activity,
            "file_system_details": file_system_details,
        }

        # Save data locally
        save_data(data)

        # Wait before next collection
        time.sleep(INTERVAL)
