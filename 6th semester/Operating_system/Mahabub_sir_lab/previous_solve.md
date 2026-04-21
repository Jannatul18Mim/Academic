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

**6. Linux Command Operations [04]** Perform/Explain the following terminal operations:
* Display information about files in the current directory: `ls`
* Word/Line count operations:
    ```bash
    wc filename          # General count
    wc -l filename       # Line count
    wc -c filename       # Character count
    wc --help            # Help menu
    ```

---

## 📝 Mid Term Examination: July–December 2022 (PART-B)
**Course Code:** CIT 322 | **Session:** 2019-20  
**Total Marks:** 08

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
**Course Code:** CIT 322 | **Session:** 2017-18  
**Total Marks:** 15

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

---
