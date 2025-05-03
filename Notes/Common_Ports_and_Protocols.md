## Introduction

In networking and offensive security, knowing which ports correspond to which services is crucial. It helps in identifying open services during scans, understanding potential attack vectors, and prioritizing targets.

Below is a list of commonly used ports and their associated services/protocols.

<br>

---
## Common Ports Table

| Port | Protocol | Service             | Description                              |
|------|----------|---------------------|------------------------------------------|
| 20   | TCP      | FTP (Data)          | File transfer (data channel)             |
| 21   | TCP      | FTP (Control)       | File Transfer Protocol (control channel) |
| 22   | TCP      | SSH                 | Secure Shell for remote access           |
| 23   | TCP      | Telnet              | Unencrypted remote login                 |
| 25   | TCP      | SMTP                | Email sending                            |
| 53   | TCP/UDP  | DNS                 | Domain Name System                       |
| 67   | UDP      | DHCP (Server)       | IP assignment to clients                 |
| 68   | UDP      | DHCP (Client)       | IP request from server                   |
| 69   | UDP      | TFTP                | Trivial File Transfer Protocol           |
| 80   | TCP      | HTTP                | Web traffic (unencrypted)                |
| 110  | TCP      | POP3                | Receiving email                          |
| 123  | UDP      | NTP                 | Time synchronization                     |
| 135  | TCP      | RPC                 | Remote Procedure Call (Windows)          |
| 139  | TCP      | NetBIOS             | Windows file/printer sharing             |
| 143  | TCP      | IMAP                | Email retrieval                          |
| 161  | UDP      | SNMP                | Network management                       |
| 162  | UDP      | SNMP Trap           | Alerts from SNMP                         |
| 443  | TCP      | HTTPS               | Secure web traffic                       |
| 445  | TCP      | SMB                 | File sharing (Windows)                   |
| 465  | TCP      | SMTPS               | Secure SMTP                              |
| 514  | UDP      | Syslog              | System logging                           |
| 587  | TCP      | SMTP (Submission)   | Authenticated email sending              |
| 993  | TCP      | IMAPS               | Secure IMAP                              |
| 995  | TCP      | POP3S               | Secure POP3                              |
| 1433 | TCP      | MSSQL               | Microsoft SQL Server                     |
| 1521 | TCP      | Oracle DB           | Oracle database service                  |
| 3306 | TCP      | MySQL               | MySQL database                           |
| 3389 | TCP      | RDP                 | Remote Desktop Protocol                  |
| 5432 | TCP      | PostgreSQL          | PostgreSQL database                      |
| 5900 | TCP      | VNC                 | Remote desktop via VNC                   |
| 6379 | TCP      | Redis               | In-memory data structure store           |
| 8080 | TCP      | HTTP-Alt            | Alternative HTTP port                    |

<br>

---
## Notes

- Always correlate open ports with potential vulnerabilities.
- Some services like SMB (445) and RDP (3389) are frequent targets in attacks.
- Ports alone don’t confirm the service – use banner grabbing or deeper inspection
