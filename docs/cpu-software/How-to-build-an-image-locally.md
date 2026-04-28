---
title: How to build an image locally
slug: cpu-software/build-image
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:19:24 GMT+0000 (Coordinated Universal Time)
---

This page describes how to build the OS image locally on your computer. This is useful for testing your changes in the OS components on Flipper One or any of the [supported boards](Supported-boards.md) before submitting a pull request to the repository.

When building the image locally, the same workflow is used as on the Build Server. This workflow is described in the [Build system](Build-system.md) page.

:::hint{type="warning"}
Now image building is supported **only on Linux** (on EXT4 or XFS file system) due to limitations related to sparse images handling.
:::

To build Flipper OS images locally:

1. Install [docker](https://www.docker.com/) and [git](https://git-scm.com/).
2. Clone the build scripts repository:

`git clone https://github.com/flipperdevices/rk3576-linux-build && cd rk3576-linux-build`

3. Build the Docker image:

`docker build -t rk3576-linux-build .`

4. Run the container:

`docker run --privileged --rm -v $(pwd)/out:/artifacts rk3576-linux-build`

5. Wait for the build to complete. This is a long-running process that may take from several tens of minutes to over an hour.

The full-disk OS images will be saved in the `rk3576-linux-build/out/images` directory. You can now [install the image to your board](How-to-install-an-image.md).
