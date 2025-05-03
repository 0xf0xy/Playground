## Introduction

The OSI (Open Systems Interconnection) model and the TCP/IP model are conceptual frameworks that help us understand how data travels across a network. They break down communication into layers, making it easier to design, implement, and troubleshoot network systems.

The OSI model has 7 layers, while the TCP/IP model is more practical and has 4 or 5 layers, depending on interpretation. Despite the differences, the two models complement each other.

<br>

---
## OSI Model - Layers and Functions

| Layer Name        | Number | Basic Function                                                |
|-------------------|--------|---------------------------------------------------------------|
| Application        | 7      | Interface for applications and end-user processes (HTTP, FTP) |
| Presentation       | 6      | Data formatting, encryption, compression                      |
| Session            | 5      | Manages sessions between applications                        |
| Transport          | 4      | Reliable data delivery (TCP, UDP)                            |
| Network            | 3      | Routing and logical addressing (IP)                          |
| Data Link          | 2      | Physical addressing, error detection (MAC, switches)         |
| Physical           | 1      | Transmission of raw bits over physical medium (cables, radio)|

<br>

---
## TCP/IP Model - Layers and OSI Mapping

| TCP/IP Layer           | Equivalent OSI Layers        | Basic Function                                        |
|------------------------|------------------------------|-------------------------------------------------------|
| Application            | 5, 6, 7                       | Software-level communication with the user           |
| Transport              | 4                            | End-to-end communication (TCP, UDP)                  |
| Internet               | 3                            | Logical addressing and routing (IP)                  |
| Network Access / Link  | 1, 2                         | Physical and data link communication                 |

<br>

---
## Notes

- The OSI model is more theoretical, while TCP/IP is widely used in real-world networking.
- Protocols like HTTP, FTP, and DNS operate at the Application layer.
- TCP is reliable and connection-oriented; UDP is faster but connectionless.
