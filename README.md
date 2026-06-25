# 🔒 SecM: Windows 11 Privacy Terminal (JX Terminal)

> **A zero-trace Python terminal interface that spawns applications securely under isolated Windows 11 secondary accounts.**

**SecM** is a lightweight, privacy-focused terminal emulator written in Python. It acts as a secure control gateway on your desktop, letting you instantly trigger secondary user accounts (`runas`) and launch everyday tools like Chrome, Notepad, or CMD without fully logging out of your primary environment. 

---

## ✨ Features Built Into SecM

* **Stealth Activation (`shadow`)**: The primary automation menu is hidden behind a secret password/command (`shadow`).
* **Isolated App Spawning**: Instantly execute apps (`Chrome`, `Notepad`, `CMD`) under a designated secure Windows account using native `runas` escalation.
* **Instant Lock (Workstation Switch)**: Quick routine to immediately lock the local Windows workstation (`LockWorkStation`) when leaving the terminal.
* **Hardware Emergency Exit**: A global low-level keyboard hook (`Ctrl + Alt + Win + 1 + Tab`) that immediately kills the terminal process in case of an emergency inspection.

---

## 📺 Demo Video

Check out **SecM (JX Terminal)** in action! Click the preview below to watch the quick setup and feature walkthrough on YouTube:

[![SecM Video Demo]https://www.youtube.com/watch?v=flSphWbGuhY)]

> 💡 *Note: Replace `[YOUR_YOUTUBE_VIDEO_ID]` in the code above with your actual YouTube video string (e.g., if your link is `://youtube.com`, use `dQw4w9WgXcQ`).*

---

## 🛠 Tech Stack

- ![Python] — Main language used
- **keyboard** — For intercepting system-wide emergency hotkeys.
- **subprocess** — Leverages native Win32 `runas.exe` and `rundll32.exe` bindings.

---

## 🚀 Getting Started

### ⚠️ Prerequisites
* **OS**: Windows 11 (Pro/Enterprise required for multi-account `runas` functionality).
* **Target Account**: A secondary Windows user account configured on your local machine.

### 📦 Installation

#### Option 1: Download the Pre-compiled Executable (Recommended)
You do not need Python installed to run SecM. You can download the standalone executable directly from our releases.

1. Go to the [📂 GitHub Releases]((https://github.com/coder1529/SecM/releases/tag/SecM_%2BV1.0)) page.
2. Download the latest `SecM.exe` from the assets list.
3. Move `SecM.exe` to your preferred directory.
4. Double-click `SecM.exe`

## 💡 How to Use It

### 1. Fire up the Interface
Run the script or executable from an administrative command line. You will see the entry terminal interface:
```
===============================================
                  JX TERMINAL                  
===============================================
> 
```

### 2. Standard Commands
* `help` : Lists basic profile details.
* `status` : Verification check of terminal health.
* `vault` : Triggers automated private access.
* `exit` : Gracefully winds down the instance.

### 3. Triggering Hidden Sub-modes
Type your custom phrase (`shadow` by default) into the prompt to reveal the privilege escalation matrix:
```text
> shadow

        1. Launch app as your_windows_account
        2. Switch account
        
> 
```
* Selecting **`1`** will prompt you to type `chrome`, `cmd`, or `notepad` to instantly pass application processes to your clean secondary runtime.
* Selecting **`2`** calls the native `user32.dll` library to locks your workstation layout instantly.

### 🚨 Emergency Overrides
If at any moment you need to instantly clear the terminal context from sight, press the global macro shortcut:
`Ctrl` + `Alt` + `Win` + `1` + `Tab`

---
