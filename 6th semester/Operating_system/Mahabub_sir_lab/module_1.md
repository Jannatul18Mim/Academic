# OS Lab 1 - Basics & Linux


## 💻 Windows Basic Commands

| Command | Description |
| :--- | :--- |
| `dir` | Lists files and directories in the current directory. |
| `cd` | Changes the current directory. |
| `md` | Creates a new directory. |
| `rd` | Removes (deletes) a directory. |
| `copy` | Copy files. |
| `move` | Move files. |
| `del` | Delete files. |
| `ren` | Rename files. |
| `type` | Displays the content of a text file. |
| `tree` | Displays a graphical representation of the directory structure. |
| `edit` | Opens a simple text editor (or use `notepad`). |
| `chkdsk` | Checks a disk for errors. |
| `systeminfo` | Shows your PC’s details. |
| `powercfg /batteryreport` | Generates a battery report. |
| `ping` | Sends ICMP Echo Request packets to test network connectivity. |
| `ipconfig` | Displays IP configuration information. |
| `date` | Displays or sets the system date. |
| `time` | Displays or sets the system time. |
| `set` | Displays, sets, or removes environment variables. |
| `tasklist` | Displays a list of currently running tasks. |
| `taskkill` | Terminates one or more running tasks. |
| `fc` | Compares two files or sets of files. |
| `help` | Displays help information for commands. |
| `exit` | Exits the Command Prompt. |

---

## 🚀 Running Programs in Windows

### 1. C/C++ Codes
To compile and run C++ on Windows:
```bash
g++ input.cpp
.\a.exe
```

### 2. Assembly Codes (x64)
**Prerequisite:** Install the NASM compiler.
```bash
winget install nasm
```

**Example Code (`hello.asm`):**
```nasm
; hello.asm (Windows x64, NASM)
 
default rel
extern printf
global main
 
section .data
    msg db "Hello, World!", 10, 0
 
section .text
main:
    sub rsp, 40        ; shadow space + stack alignment
    lea rcx, [msg]    ; first argument (Windows x64)
    call printf
    add rsp, 40
 
    xor eax, eax
    ret
```

**Compile and Run:**
```bash
nasm -f win64 hello.asm -o hello.obj	
gcc hello.obj -o hello.exe
.\hello.exe
```

### 3. Python Codes
```bash
python source.py
```

---

## 📱 Running Programs in Android (Termux)

1. **Install Termux:** Search for "Termux" on the [F-Droid Store](https://f-droid.org/).
2. **Install Packages:**
   ```bash
   pkg install clang
   ```
3. **Edit Files:** Use a CLI-based text editor.
   ```bash
   nano input.cpp
   ```
4. **Compile and Run:**
   ```bash
   g++ input.cpp
   ./a.out
   ```

---

## 🐧 Running Programs in Linux

### 1. C/C++ Code
```bash
g++ input.c
./a.out
```

### 2. Java Code
**Example Code (`Main.java`):**
```java
public class Main {
    public static void main(String args[]) {
        System.out.println("Hello, World!");
    }
}
```
**Compile and Run:**
```bash
javac Main.java
java Main
```

### 3. Python Code
```bash
python main.py

