## 📝 Mid Term Examination: July–December 2023

### SET-A (Synchronization)
* Implement Peterson’s solution for ensuring synchronization. **[07]**
* Implement mutex locks to ensure synchronization.
* Semaphore implementation to solve busy waiting problem.

### SET-B (Threading & Linux)
**[✓] 4. Multithreading Basics [04]** Write a code to demonstrate how to create and start Python’s or Java’s threads using the `threading` module (or `Thread` class).
* It should run a function `print_name` that prints a name along with provided arguments.
* Create two threads, start them using `start()`, and wait for completion using `join()`.

**5. Concurrent Calculation [04]** Write code to calculate the square and cube of a number concurrently.
* Create two threads (`t1` and `t2`).
* Print results in parallel and print “Done!” only when both threads finish.

```
python?code_reference&code_event_index=1
markdown_content = """# Linux Command Operations Guide

This document provides explanations and examples for various essential Linux terminal operations.
```
---

## 6. File Information and Content Analysis
These commands help you understand the contents and properties of files.

- `ls`: Lists files and directories in the current directory.
- `ls -lah`: Lists all files (`-a`), including hidden ones, in a long format (`-l`) with human-readable file sizes (`-h`).

- `wc filename`: Counts the lines, words, and characters in a file.
- `wc -l filename`: Counts only the **lines** in the file.
- `wc -c filename`: Counts only the **bytes/characters** in the file.
- `wc --help`: Displays the manual/help page for the `wc` (word count) command.

---

## 2. Directory and File Management
Steps to create directories, files, and copy them:

1. **Create directory and file:**
   ```bash
   mkdir <student_name>
   cd <student_name>
   touch example.txt
   ```
2. **Copy file to home directory:**
   ```bash
   # Copy the file to a new folder in home
   mkdir ~/backup_dir
   cp example.txt ~/backup_dir/
   ```

---

## 3. Navigation
- `cd`: Change Directory.
  - `cd ..`: Move up one level.
  - `cd ~`: Return to the home directory.
  - `cd /path/to/folder`: Navigate to a specific path.

---

## 4. Removing Directories
- `find . -type d -empty -delete`: This command finds all empty directories (`-type d -empty`) in the current location and deletes them (`-delete`).

---

## 5. File Copy/Cut/Move
- **Copy:** `cp source destination` (e.g., `cp file.txt /tmp/`)
- **Cut/Move:** `mv source destination` (e.g., `mv file.txt /tmp/`) - Note that `mv` is used for both moving files and renaming them.

---

## 6. Downloading Files
- `wget URL`: Downloads files from the web directly to your terminal.
- `aria2c URL`: A multi-protocol download utility that is often faster than `wget` for large files.

---

## 7. User Identification
- `whoami`: Displays the username of the current logged-in user.
- `echo $USER`: Prints the value of the environment variable `USER`.

---

## 8. Calendar
- `cal`: Displays the calendar for the current month.
- `cal 8 2002`: Displays the calendar for August 2002 (Note: `cal` uses `month year` format).

---

## 9. System Details
- `neofetch` / `fastfetch`: Displays system information and OS branding.
- `lscpu`: Shows detailed information about the CPU architecture.
- `lsblk`: Lists information about all available block devices (disks, partitions, USB drives).
"""

with open("Linux_Command_Operations.md", "w") as f:
    f.write(markdown_content)


## 📝 Mid Term Examination: July–December 2022 (PART-B)
**Course Code:** CIT 322 | **Session:** 2019-20  

* **Compiling Environment:** Running a C/C++ Program in Linux. **[02]**
* **Connectivity & Redirection:**
    ```bash
    ping -c 5 mim.xyz > file.txt
    ```

---

## 📝 Mid Term Examination: July–December 2021
**Course Code:** CIT 322 | **Session:** 2018-19  
**Total Marks:** 15

1.  Installation of Linux with Virtual Machine. **[01]**
2.  Running a C/C++ Program in Linux. **[02]**
3.  **Running Java Code in Linux:**
    ```bash
    javac Main.java
    java Main
    ```

**[✓] 4. System Administration & Navigation Commands [10]**
* List home directory, navigate folders, and create/delete files/directories.
* Check disk space in partitions: `df -h`
* Network test: `ping mim.xyz`

---

## 📝 Mid Term Examination: July–December 2020

### 1. FCFS Scheduling Analysis [10]
| Process | Arrival Time | Duration (Burst) |
| :--- | :--- | :--- |
| P1 | 0 | 3 |
| P2 | 1 | 12 |
| P3 | 5 | 1 |

* **Tasks:** Draw Gantt Chart and compute Average Waiting Time (AWT).
* **Analysis:** Define the **"Convoy Effect."** Provide an alternative arrival order to improve AWT and another to demonstrate the convoy effect.

### 2. Comparative Scheduling [10]
Compare AWT for **FCFS, SJF, and SRTF** for the following:
| Process | Arrival Time | Burst Time |
| :--- | :--- | :--- |
| P1 | 0 | 8 |
| P2 | 3 | 3 |
| P3 | 5 | 4 |
| P4 | 6 | 6 |

### 3. Algorithm Simulation
* **[✓]** Simulate **Round-Robin** Scheduling. **[10]**
* Simulate **Priority Scheduling** (Random).
* Simulate **FCFS** and **SJF** (Preemptive and Non-Preemptive).

---

## 🛠️ Linux Customization & Management Tasks

**[✓] System Customization**
* Change wallpaper via CLI: 
    ```bash
    gsettings set org.gnome.desktop.background picture-uri 'file:///path/to/mim_wallpaper.jpg'
    ```

**[✓] File & Directory Management**
* **Create and Copy:**
    ```bash
    mkdir mim
    touch text.txt
    cp /home/mim/mim/text.txt /home/mim/test
    cp text.txt ~/test
    ```
* **Cleanup:** Remove empty directories:
    ```bash
    find . -type d -empty -delete
    ```
* **Transfer:**
    ```bash
    cp source/ destination/    # Copy
    mv source/ destination/    # Cut/Move
    ```

**[✓] Information & Utilities**
* **Identity:** `whoami` or `echo $USER`
* **Calendar:** `cal` or `cal 8 11 2002`
* **System Hardware:** ```bash
    neofetch
    lscpu
    lsblk      # List block devices/partitions
    ```
* **Downloads:** `wget URL` or `aria2c URL`

**[✓] Permissions & Root Access**
* Make file executable: `chmod +x filename`
* Run as admin: `sudo command`

**[✓] Compression & Storage**
* **Archive:** `zip compressed.zip file1 file2`
* **Disk Usage:** `du -h compressed.zip`

**[✓] Search & Help**
* Locate file: `ls -R | grep input.jpg`
* Manual pages: `man ls` or `ls --help`


