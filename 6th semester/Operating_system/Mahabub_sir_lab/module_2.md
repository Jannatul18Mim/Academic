
# OS Lab 2 - Process Management

## ⚙️ Process Controlling

### 1. `fork()`
Used to create a new process by duplicating the calling process.
```cpp
#include<bits/stdc++.h>
using namespace std;
 
int main() {
    int pid = fork();
    if (pid == 0)
        cout << "Child process  -> " << pid << endl;
    else
        cout << "Parent process -> " << pid << endl;
}
```

### 2. `exec()`
Replaces the current process image with a new process image.
```cpp
#include <bits/stdc++.h>
#include <unistd.h>

int main() {
    execlp("ls", "", "-la", NULL);
    return 0;
}
```

### 3. `wait()`
Makes the parent process wait until its child process terminates.
```cpp
#include<bits/stdc++.h>
#include<sys/wait.h>
#include<unistd.h>
 
using namespace std;
 
int main() {
    int pid = fork();
    if (pid == 0) {
        sleep(5);
        cout << "Child process  -> " << pid << endl;
    } else {
        cout << "Parent process -> " << pid << endl;
        wait(NULL);
    }
}
```

---

## 🚦 Signal Controlling

### 1. `SIGINT`
Handles the interrupt signal (typically sent via `Ctrl+C`).
```cpp
#include<bits/stdc++.h>
#include<csignal>
using namespace std;
 
void sig_int(int sig_num) {
    cout << "Received signal, " << sig_num << endl;
    exit(sig_num);
}
 
int main() {
    signal(SIGINT, sig_int);
    while (true);
}
```

### 2. `SIGKILL`
Used to force a process to terminate immediately.
```cpp
#include<bits/stdc++.h>
#include<csignal>
using namespace std;
 
int main() {
    int target_pid = 1234;
    if (kill(target_pid, SIGKILL) == 0)
        cout << "Killed " << target_pid << endl;
    else
        cout << "Not found!" << endl;
}
```

---

## 🛠️ Mini Shell
A basic implementation of a shell using `fork`, `exec`, and `signal` handling.
```cpp
#include<bits/stdc++.h>
#include<sys/wait.h>
#include<unistd.h>
 
using namespace std;
 
void sig_handle(int sig_num) {
    cout << "\nCtrl + c pressed! Exiting..." << endl;
    exit(sig_num);
}
 
int main() {
    signal(SIGINT, sig_handle);
 
    string s;
    while (true) {
        cout << "mini-shell:";
        cin >> s;
        if (s == "exit") break;
 
        if (fork() == 0) {
            execlp(s.c_str(), "", NULL);
            exit(1);
        } else {
            wait(NULL);
        }
    }
}
```

---

## 🧵 Threading

### 1. C++ Implementation
```cpp
#include<bits/stdc++.h>
#include<thread>
using namespace std;
 
void func() {
    cout << "hello from a thread..." << endl;
}
 
int main() {
    thread t1(func);
    t1.join();
 
    cout << "Thread finished!" << endl;
}
```

### 2. Python Implementation
```python
import threading
 
def func():
    print("Hello from a thread!")
 
t1 = threading.Thread(target=func)
 
t1.start()
t1.join()
 
print("Thread finished!")

