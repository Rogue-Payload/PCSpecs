# **System Intel Pro**

![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellowgreen?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge)

> **Developed by: Dr. Aubrey W. Love II (AKA Rogue Payload)**  
> **A Product of Global Bug Hunters**

---

## 🚀 **Project Overview**

_System Intel Pro_ is a comprehensive tool that gathers in-depth information about your computer's hardware and software specifications, and then compares these specs against popular game requirements to assess gaming compatibility. This project is perfect for:

- **Nerds and Tech Enthusiasts** who want quick access to detailed system specifications.
- **Gamers** who wish to check if their systems can handle popular games like **Call of Duty**, **Fortnite**, **Roblox**, and **Minecraft**.
- **Developers** who want an example project on system hardware detection and flashy Python scripting.

---

## 🎨 **Features**

- 💻 **Detailed System Specs**: Collects information about CPU, RAM, GPU, motherboard, and OS.
- 🌐 **Internet Speed Detection**: Measures ping rate, download, and upload speeds.
- 🎮 **Game Compatibility Checker**: Compares your system's specs with popular games' requirements and provides colorful feedback.
- 🎉 **Flashy and Engaging Output**: Uses colored text for a user-friendly, visually appealing terminal output.
- 🔍 **Cross-Platform Support**: Works on Windows, macOS, and Linux.

---

## 🛠️ **Installation**

To set up _System Intel Pro_, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/System-Intel-Pro.git
   cd System-Intel-Pro
   ```
2. **Install the required dependencies:**
    ```bash 
    pip install -r requirements.txt
    ```
3. **Run the Script:**
    ```bash
    python3 PCSpecs.py
    ```
_Note: Make sure you have Python 3.8 or above installed._

## 📋 Usage

### Running the Script
_Simply execute the script using the command:_
```bash
python3 PCSpecs.py
```
### Sample Output
_The script outputs a summary of your system specifications and checks them against the requirements of popular games. Here is an example:_
```bash
System Intel Pro
Developed by: Dr. Aubrey W. Love II (AKA Rogue Payload)
A product of Global Bug Hunters

Hardware Specs:
CPU: Intel Core i7-9700K (8 cores)
RAM: 16 GB (45% free)
GPU: NVIDIA GeForce RTX 2080 SUPER
Motherboard: ASUSTeK COMPUTER INC. X99-A

Internet Specs:
Ping Rate: 25 ms
Upload Speeds: 10 Mbps
Download Speeds: 50 Mbps

Game Compatibility:
Call of Duty: 🟢 Exceeds Optimized Requirements
Fortnite: 🟢 Meets Recommended Settings
Roblox: 🟢 Meets Minimum Requirements
Minecraft: 🟢 Meets Recommended Requirements
```

## 🧩 Features Breakdown

### 1. System Information Collection

- **CPU Specs:** Detects the make, model, and number of cores.
- **RAM Details:** Reports total memory and current usage.
- **GPU Specs:** Identifies the GPU model and manufacturer.
- **Motherboard Info:** Gathers details about the motherboard manufacturer and model.
- **OS Detection:** Determines the operating system and version.

### 2. Internet Speed Testing
- Measures ping rate, upload speed, and download speed.
- Uses the `speedtest-cli` package to gather accurate data.

### 3. Game Compatibility Checker
- Compares gathered system specs with popular game requirements:
  - **Call of Duty**
  - **Fortnite**
  - **Roblox**
  - **Minecraft**
- Outputs colorful status indicators:
  - 🟢 **Exceeds Optimized Requirements**
  - 🟡 **Meets Recommended Requirements**
  - 🔴 **Does NOT Meet Requirements**

### 📂 Directory Structure
```bash
PC_Specs/
├── PCSpecs.py
├── README.md
└── requirements.txt
```
### 4. **Dependencies**

_The project uses the following libraries:_

| Package         | Description                                                                       |
|-----------------|-----------------------------------------------------------------------------------|
| `psutil`        | Provides system and hardware information (CPU, RAM, disk usage, etc.).            |
| `GPUtil`        | Retrieves GPU details such as make, model, and memory usage.                      |
| `colorama`      | Enables colored output for the terminal (cross-platform support for colored text).|
| `speedtest-cli` | Allows internet speed testing with Speedtest.net servers.                         |

_To install all dependencies, run:_
```bash
pip install -r requirements.txt
```

# 🖥️ PC Specs Checker

Welcome to the **PC Specs Checker** project! This script helps you gather your system's hardware specs and checks if your computer meets the requirements for popular games. It's an essential tool for gamers, system enthusiasts, and nerds who want to know their system capabilities at a glance.

## 🔗 [PC Specs GitHub Repository](https://github.com/Rogue-Payload/PCSpecs)

---

## 📋 **Features**
- Collects detailed hardware specs:
  - **CPU, RAM, GPU, Motherboard**
  - **Operating System detection**
  - **Internet speed (Ping, Upload, Download)**
- Compares gathered system specs with popular game requirements:
  - **Call of Duty**
  - **Fortnite**
  - **Roblox**
  - **Minecraft**
- Outputs colorful status indicators:
  - 🟢 **Exceeds Optimized Requirements**
  - 🟡 **Meets Recommended Requirements**
  - 🔴 **Does NOT Meet Requirements**
  - 🔵 **General Information**

---

## 🕹️ **Game Compatibility Requirements**

Below are the general requirements for popular games considered in the script:

### **Call of Duty**

| Requirement | Minimum                          | Recommended                     | High/Competitive               | Ultra                           |
|-------------|----------------------------------|---------------------------------|--------------------------------|---------------------------------|
| **CPU**     | i3-4340 / FX-6300                | i5-2500K / R5 1600X             | i7-8700K / R7 1800X            | i7-9700K / R7 2700X             |
| **RAM**     | 8GB                              | 12GB                            | 16GB                           | 16GB                            |
| **GPU**     | GTX 670 / GTX 1650               | GTX 970 / GTX 1660              | GTX 1080 / RTX 2070            | RTX 2080 SUPER                  |

### **Fortnite**

| Requirement | Minimum                          | Recommended                     | Epic Quality                   |
|-------------|----------------------------------|---------------------------------|--------------------------------|
| **CPU**     | i3-3225                          | i5-7300U / R3 3300U             | i7-8700 / R7 3700x             |
| **RAM**     | 8GB                              | 16GB                            | 16GB                           |
| **GPU**     | Intel HD 4000 / Vega 8           | GTX 960 / R9 280                | RTX 3070 / RX 6700 XT          |

### **Roblox**

| Requirement | Minimum                          | Recommended                     |
|-------------|----------------------------------|---------------------------------|
| **CPU**     | 1.6 GHz (2005+)                  | Dual-core, higher clock         |
| **RAM**     | 1GB                              | 4GB                             |
| **GPU**     | DX10-compatible                  | Dedicated GPU recommended       |

### **Minecraft**

| Requirement | Minimum                          | Recommended                     |
|-------------|----------------------------------|---------------------------------|
| **CPU**     | i3-4150 / N4100                  | i7-6500U / FX-4100              |
| **RAM**     | 2GB                              | 8GB                             |
| **GPU**     | HD 4400 / R5 series              | GeForce 940M / HD 7750          |

---

## 🎨 **Color Legend for Output**

- 🟢 **Green:** Exceeds Requirements
- 🟡 **Yellow:** Meets Recommended Requirements
- 🔴 **Red:** Does NOT Meet Requirements
- 🔵 **Blue:** General Information

---

## 🚀 **Future Enhancements**

- **Additional Game Support:** Expand the script to check for more games.
- **GUI Version:** Develop a graphical interface for non-tech users.
- **Automated Updates:** Add functionality to automatically update game requirements.
- **Benchmark Integration:** Add real-time benchmarking for further accuracy.

---

## 👥 **Contributing**

We welcome contributions! If you have suggestions, enhancements, or want to add new features, feel free to:

1. **Fork** the repository.
2. **Create a new branch.**
3. **Submit a pull request.**

---

## 📜 **License**

This project is licensed under the [MIT License](LICENSE.md). You are free to use, modify, and distribute this software as you see fit.

---

## ❤️ **Support**

If you find this project helpful, please give it a ⭐ on GitHub.


