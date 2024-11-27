---
layout: page
title: URL Shortener
description: Developed a scalable URL shortener using Python, MongoDB, and Kubernetes.
importance: 1
category: fun
img: assets/img/project_preview/urls.png
---

This project involved designing and implementing a **URL shortener** as part of a database systems lab. The system was built using **Python** for backend logic, **MongoDB** as the database, and tested for scalability with **Docker** and **Kubernetes** under various stress conditions. A **dashboard** was also created to monitor API calls and system performance, providing insights into usage patterns.

### Technical Details

The URL shortening logic relied on a custom **hashing function** to generate unique identifiers for input URLs. The hash function mapped each URL to a fixed-length string using a combination of:
1. **Base62 Encoding:** Encoded hash outputs into a mix of alphanumeric characters to keep shortened URLs compact.
2. **Hash Collisions:** Managed potential hash collisions by appending incremental counters to conflicting hashes.
3. **Database Integration:** Stored mappings between original URLs and their shortened counterparts in **MongoDB**, ensuring fast retrieval and scalability for high-volume traffic.

### Stress Testing

To evaluate system performance, I used **Docker** containers and **Kubernetes clusters** to simulate high traffic scenarios. Tests were designed to measure response times, database query performance, and overall API throughput. The system proved robust under load, maintaining low latency and high reliability.

[GitHub Repository](https://github.com/Computer-Engineering-Department-Archive/CE-231-DB-Lab/tree/main/HWs-2023/Prj)
