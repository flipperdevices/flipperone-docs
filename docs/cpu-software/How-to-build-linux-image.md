---
title: How to build a Linux image
slug: cpu-software/how-to-build-linux-image
---

This page describes how to build an OS image locally on your computer. This is useful for testing your changes in the OS components on Flipper One or any of the [supported boards](Supported-boards.md) before submitting pull request to the repository.

When building an image locally, the same workflow is used as on the Build Server. This workflow is described in the [Build system](Build-system.md) page.

***

## Step 1: Install required tools

:::hint{type="info"}
The operating system image is built inside a Docker container, ensuring cross-platform compatibility of the build process.
:::

Before starting the image build, install the required components to ensure that the container runs properly.

### :inlineImage[]{src="/files/icons/apple-logo.png"} macOS 

:::::WorkflowBlock

:::WorkflowBlockItem
Install [Docker Desktop](https://www.docker.com/).
:::

:::WorkflowBlockItem
Install [git](https://git-scm.com/install/mac).
:::

:::::

‎ 

### :inlineImage[]{src="/files/icons/linux-logo.png"} Linux (Debian)

:::::WorkflowBlock
:::WorkflowBlockItem
Install the required packages:

`sudo apt install -y docker.io docker-cli git qemu-user-binfmt`
:::

:::WorkflowBlockItem
Add the current user to the **docker** group and apply it in the current session:

`sudo usermod -aG docker $USER && newgrp docker`
:::

:::::

‎ 

### :inlineImage[]{src="/files/icons/windows-logo.png"} Windows 10/11

:::::WorkflowBlock
:::WorkflowBlockItem
Open a terminal and start the installation of **WSL 2** (Windows Subsystem for Linux v2) with Debian distribution:

`wsl --install -d Debian`
:::

:::WorkflowBlockItem
Restart your computer. After rebooting, the installation of the Debian distribution will continue automatically.
:::

:::WorkflowBlockItem
You’ll be prompted to create a Unix **username** and **password** during installation.
:::

:::WorkflowBlockItem
Install the required packages:
`sudo apt install -y docker.io docker-cli git qemu-user-binfmt`
:::

:::WorkflowBlockItem
Add the current user to the **docker** group and apply it in the current session:

`sudo usermod -aG docker $USER && newgrp docker`
:::

:::WorkflowBlockItem
Close the terminal.
:::

:::::

***

## Step 2: Build an OS Image

:::hint{type="info"}
Building an OS image is a long-running process that **takes from several tens of minutes to over an hour**.
:::

To build an OS image:

:::::WorkflowBlock
:::WorkflowBlockItem
Open the terminal in the folder where you plan to save image build system.
:::

:::WorkflowBlockItem
**On Linux/macOS:** Skip this step.

**On Windows:** 
Enter the Debian terminal:

`wsl -d Debian`

Go to the Debian user’s home directory:

`cd ˜`
:::

:::WorkflowBlockItem
Clone the OS image build scripts repository:

`git clone https://github.com/flipperdevices/flipperone-linux-build-scripts && cd flipperone-linux-build-scripts`
:::

:::WorkflowBlockItem
Build the Docker image: 

`docker build -t flipperone-linux-build-scripts .`
:::

:::WorkflowBlockItem
Run the container

`docker run --privileged --rm -v $(pwd)/out:/artifacts flipperone-linux-build-scripts`
:::

:::WorkflowBlockItem
Wait for the build to complete. 
:::
:::::

:::hint{type="success"}
The full-disk OS images are stored in:

* **Linux and macOS:** `flipperone-linux-build-scripts/out/images`. 
* **Windows 10/11:** `Linux/Debian/home/[wsl user]/flipperone-linux-build-scripts/out/images`.

You can now [install the image to your board](./How-to-install-linux-image.md).
:::
