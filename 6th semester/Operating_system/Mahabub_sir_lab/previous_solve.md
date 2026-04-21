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


### Compiling Environment: Running a C/C++ Program in Linux. [02]

```bash
ping -c 5 sharafat.xyz > file.txt
g++ input.cpp
./a.out
```

---

### Linux Shell Commands: Use commands to perform the following: [06]

**(i) Show home directory of your user.**
```bash
echo $HOME
```

**(ii) List files in the current directory.**
```bash
ls
```

**(iii) Change directory.**
```bash
cd
```

**(iv) Create a folder/directory.**
```bash
mkdir name
```

**(v) Delete files and directories.**
```bash
rm filename
```

**(vi) Create a file.**
```bash
touch file.txt
```

**(vii) Access manual pages (help) for a command.**
```bash
ls --help
man ls
```

**(viii) Change file permissions (make a file executable).**
```bash
chmod +x filename
```

**(ix) Move files via command line.**
```bash
mv source/ destination/
```

**(x) Locate a file in the system.**
```bash
ls -R | grep input.jpg
```

**(xi) Check server connectivity (ping).**
```bash
ping 9.9.9.9
ping -c 5 sharafat.xyz
```

**(xii) Redirect data/text into a file.**
```bash
echo "text content" > file.txt
```
"""

write_file("midterm_exam_cit322.md", content)

---

## 📝 Mid Term Examination: July–December 2021

### 1. List home directory, navigate folders, and create/delete files/directories.
```bash
# List home directory
ls ~

# Navigate folders
cd /path/to/directory

# Create file
touch filename.txt

# Create directory
mkdir dirname

# Delete file
rm filename.txt

# Delete directory
rm -r dirname
```

### 2. Check disk space in partitions.
```bash
df -h
```

### 3. Check network connection (ping).
```bash
ping sharafat.xyz
```

### 4. Installation of Linux with Virtual Machine. [01]
* Download ISO file (e.g., Ubuntu).
* Create a New Virtual Machine in VirtualBox/VMware.
* Allocate RAM and Virtual Hard Disk.
* Mount the ISO image and boot the virtual machine.
* Follow the on-screen installation prompts.

### 5. Running a C/C++ Program in Linux. [02]
```bash
g++ input.cpp -o a.out
./a.out
```

### 6. Running a Java Code in Linux. [02]
```bash
javac Main.java
java Main
```

### 7. Check block devices (disk partitions).
```bash
lsblk
```

### 8. Run commands with administrative/root privileges (sudo).
```bash
sudo command
```

### 9. Compress files into a .zip archive.
```bash
zip compressed.zip file_1 file_2
```

### 10. Check disk usage of a specific file.
```bash
du -h compressed.zip
```

### 11. Check network connection (additional).
```bash
ping -c 4 google.com
```
"""
---

## 📝 Mid Term Examination: July–December 2020


content = """# Linux Customization & Management [05]

### 1. Change wallpaper and screensaver via Linux command line.
```bash
# Change wallpaper (GNOME)
gsettings set org.gnome.desktop.background picture-uri file:///path/to/image.jpg

# Change screensaver
gsettings set org.gnome.desktop.screensaver picture-uri file:///path/to/image.jpg
```

### 2. Create a directory (student name), create a file within, and copy it to a new directory in the home folder.
```bash
# Create directory
mkdir student_name

# Create a file within the directory
touch student_name/test.txt

# Create the target directory in home
mkdir ~/test

# Copy the file to the new directory
cp student_name/test.txt ~/test/
```

### 3. Create disk partitions.
```bash
# View current block devices to identify the disk
lsblk

# Use fdisk to manage partitions (requires root privileges)
sudo fdisk /dev/sdX

# Inside fdisk:
# n - create a new partition
# p - primary partition
# w - write changes and exit
```
"""

write_file("linux_customization_management.md", content)

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


