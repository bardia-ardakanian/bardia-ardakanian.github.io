---
layout: page
title: Extended xv6 Kernel
description: Extended the xv6 kernel by adding system calls, scheduling algorithms, and kernel-level threads.
importance: 1
category: fun
img: assets/img/project_preview/xv6.png
---

**xv6** is a modern reimplementation of the **Sixth Edition Unix** operating system, designed as an educational tool for understanding operating system concepts. This project involved modifying and extending the xv6 kernel, focusing on enhancing its functionality and exploring advanced operating system design principles.

### Technical Enhancements

I added a **dozen new system calls** to the xv6 kernel, enabling additional functionalities and improving interaction between user programs and the operating system. Furthermore, I implemented **custom scheduling algorithms** to experiment with task prioritization and efficiency. These included algorithms like **Round Robin** and **Priority Scheduling**, which optimized CPU usage across different workloads. 

To improve kernel concurrency, I integrated **ticket locks** for mutual exclusion and introduced **kernel-level threads**, enabling parallelism within the operating system. Additionally, I developed a **basic graphical interface**, providing a visual layer to interact with system processes and improve usability. This hands-on project offered valuable insights into how operating systems manage resources, handle concurrency, and execute user programs.

[GitHub Repository](https://github.com/Computer-Engineering-Department-Archive/OS-XV6)
