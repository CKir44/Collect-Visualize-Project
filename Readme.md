# Data Collection and Visualization Project

## Overview
This project demonstrates the end-to-end process of collecting, processing, and visualizing system data. It is designed as a practical exercise in Python programming, data analytics, and visualization using Power BI.
Only steps 2 and 3 of this project are demonstrated, focusing on the collection and visualization aspects. The remote penetration test utilizing Hydra is not included for ethical purposes. 

## Features
### Data Collection
- **Script:** `data_collector.py`
- **Purpose:** Collects key system metrics, including:
  - CPU and memory usage
  - Disk usage details
  - User activity (e.g., active sessions and command history)
  - Network activity (e.g., bandwidth usage and connected IPs)
  - File system details (e.g., largest files, photo, and video counts)
- **Output:** Saves the collected data as a JSON file (`data_capture.json`).

### Data Visualization
- **Script:** `visualizer.py`
- **Purpose:** Processes the JSON data and converts it into CSV files for Power BI visualization. Key features include:
  - Parsing and cleaning data
  - Generating insights on system usage, user activity, and network activity
  - Preparing data for visual representation in Power BI
- **Output:** CSV files for visualizations.

## Tools and Technologies
- **Python**:
  - Libraries: `json`, `pandas`, `os`
  - Data collection and processing
- **Power BI**:
  - Visualization of trends and insights
- **GitHub**:
  - Repository management and code sharing

## Installation
### Prerequisites
- Python 3.8+
- Required Python libraries:
  ```bash
  pip install pandas
  ```
- Power BI Desktop (optional, for visualizing the output)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/data-collection-visualization.git
   cd data-collection-visualization
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Step 1: Run Data Collection
1. Execute the `data_collector.py` script to collect system data:
   ```bash
   python data_collector.py
   ```
2. The collected data will be saved in `data_capture.json`.

### Step 2: Prepare Data for Visualization
1. Run the `data_visualization.py` script:
   ```bash
   python data_visualization.py
   ```
2. The script generates CSV files for Power BI in the current directory.

### Step 3: Visualize Data
1. Open Power BI Desktop.
2. Import the generated CSV files.
3. Create visualizations to gain insights into system usage, user activity, and more.

## Sample Visualizations
Below are some examples of visualizations created using the project data:
- **System Usage Trends**: Line chart showing CPU and memory usage over time.
- **Largest Files**: Bar chart displaying the largest files on the system.
- **Network Activity**: Time-series plots for bandwidth usage.
