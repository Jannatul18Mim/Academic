```
section .data
    msg db 'Hello, World!', 0xa
    len equ $ - msg

section .text
    global _start

_start:
    ; syscall: write(1, msg, len)
    mov rax, 1          ; sys_write
    mov rdi, 1          ; stdout
    mov rsi, msg
    mov rdx, len
    syscall

    ; syscall: exit(0)
    mov rax, 60         ; sys_exit
    xor rdi, rdi        ; return 0
    syscall

```
---

```# 1. Assemble the code into an object file (ELF64 format)
nasm -f elf64 hello.asm -o hello.o

# 2. Link the object file to create an executable
ld hello.o -o hello

# 3. Run the executable
./hello
```

The ./ literally means "look in this current directory"

apt -> three main parts of the process: the Manager (APT), the Catalog, and the Warehouse (Repositories).

APT is the logic that connects your terminal to the warehouse using the catalog.

---

### C++ Development Cheat Sheet (Kali Linux)

| Action | Command | Description |
| :--- | :--- | :--- |
| **Open/Edit File** | `nano filename.cpp` | Opens a simple text editor inside the terminal to write your code. |
| **View File Content** | `cat filename.cpp` | Displays the code in the terminal without opening an editor. |
| **Compile** | `g++ filename.cpp -o output_name` | Translates your code into a machine-readable executable named `output_name`. |
| **Execute** | `./output_name` | Runs the compiled program from the current directory. |

---

### Step-by-Step Example

If you want to create a program called "hello", follow these steps in your terminal:

1.  **Create the source file:**
    ```bash
    nano main.cpp
    ```
    *(Type your code, then press `Ctrl+O`, `Enter`, and `Ctrl+X` to save and exit.)*

2.  **Compile the code:**
    ```bash
    g++ main.cpp -o hello
    ```

3.  **Run the program:**
    ```bash
    ./hello
    ```



### Pro Tips:
* **The `-o` flag:** This stands for "output". Whatever word follows `-o` will be the name of your final clickable program.
* **Errors:** If `g++` shows a list of errors, the compilation failed. You must fix the code in `nano` and run the `g++` command again.
* **Permissions:** If you get a "Permission denied" error when running `./output_name`, run `chmod +x output_name` to make it executable.
