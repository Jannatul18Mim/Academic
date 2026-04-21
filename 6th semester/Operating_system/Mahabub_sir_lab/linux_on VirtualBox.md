# Guide: Installing Kali Linux on VirtualBox (Windows Host)



## Step 1: Download Required Software
1.  **VirtualBox**: Go to [virtualbox.org](https://www.virtualbox.org/) and download the "Windows hosts" installer. Run the `.exe` and follow the prompts to install it.
2.  **Kali Linux ISO**: Go to [kali.org/get-kali](https://www.kali.org/get-kali/).
    * Select **Installer Images**.
    * Choose the **64-bit** version and click the Download button (usually a `.iso` file).

## Step 2: Create a New Virtual Machine
1.  Open **VirtualBox Manager**.
2.  Click the **New** (blue star) button.
3.  **Name and Operating System**:
    * **Name**: `Kali Linux`
    * **Folder**: Leave as default.
    * **ISO Image**: Click the dropdown -> **Other...** -> Select the Kali ISO you downloaded in Step 1.
    * **Type**: Linux.
    * **Version**: Debian (64-bit) — *Kali is based on Debian.*
4.  Check **Skip Unattended Installation** (recommended for beginners to see the full setup process). Click **Next**.

## Step 3: Hardware Allocation
1.  **Base Memory (RAM)**: Assign at least **2048 MB** (4096 MB is recommended for better performance).
2.  **Processors**: Assign at least **2 CPUs** (stay within the green bar area).
3.  Click **Next**.

## Step 4: Virtual Hard Disk
1.  Select **Create a Virtual Hard Disk Now**.
2.  **Disk Size**: Set it to at least **80 GB** (Kali's tools take up significant space over time).
3.  Click **Next**, then click **Finish**.

## Step 5: Final Settings Adjustments
1.  With "Kali Linux" selected in the left pane, click **Settings** (orange gear).
2.  Go to **Display**:
    * Increase **Video Memory** to **128 MB**.
    * Enable **3D Acceleration** (optional, but helps with UI smoothness).
3.  Go to **System** -> **Processor**:
    * Ensure "Enable PAE/NX" is checked.
4.  Click **OK**.

## Step 6: Installing Kali Linux
1.  Click the green **Start** arrow in VirtualBox Manager.
2.  A new window will open. Use your arrow keys to select **Graphical Install** and press **Enter**.
3.  **Language/Region**: Select your preferred language (e.g., English), Location, and Keyboard layout.
4.  **Network Configuration**:
    * **Hostname**: Leave as `kali` or choose a nickname.
    * **Domain name**: Leave blank.
5.  **Users and Passwords**:
    * **Full name**: Enter your name.
    * **Username**: Choose a login name (e.g., `kaliuser`).
    * **Password**: Set a strong password and confirm it.
6.  **Partition Disks**:
    * Select **Guided - use entire disk**.
    * Select the virtual disk (SCSI1).
    * Select **All files in one partition** (Recommended for new users).
    * Select **Finish partitioning and write changes to disk**.
    * When asked "Write the changes to disks?", select **Yes**.

## Step 7: Software Selection
1.  The installer will run for a few minutes. Eventually, you will see a list of "Desktop Environments" and "Collection of tools."
2.  Keep the defaults checked (**Xfce** and **default desktop environment**).
3.  Click **Continue**. This part may take 10-20 minutes depending on your internet speed and hardware.

## Step 8: Finishing Up
1.  **GRUB Boot Loader**: When asked to install the GRUB boot loader to your primary drive, select **Yes**.
2.  Select the device path (usually `/dev/sda`).
3.  Once the "Installation Complete" message appears, click **Continue**. The VM will automatically reboot.

## Step 9: Login and Update
1.  Enter the username and password you created in Step 6.
2.  Open the **Terminal** (the black square icon in the top bar).
3.  It is best practice to update your system immediately. Type the following command:
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
4.  Enter your password when prompted.

**Congratulations! Your Kali Linux Virtual Machine is ready to use.**
"""

file_path = "install-kali-vbox.md"
with open(file_path, "w") as f:
    f.write(markdown_content)
