# Introduction

The 4-Way Handshake is a process used in WPA/WPA2 Wi-Fi security to establish a secure connection between a client (supplicant) and an Access Point (authenticator). It's part of the authentication process after a successful PSK (pre-shared key) match.

Understanding this process is essential for Wi-Fi attacks like handshake capture and password cracking.

<br>

---
## Why It Matters

- It’s where the **Pairwise Transient Key (PTK)** is created.
- Capturing this exchange allows you to perform **offline dictionary/brute-force attacks**.
- Tools like `aircrack-ng`, `hcxdumptool`, and `hashcat` rely on it.

<br>

---
## Overview of the Steps

| Step | Direction | Description                                                  |
|------|-----------|--------------------------------------------------------------|
| 1    | AP → Client | AP sends ANonce (a random number) to the client            |
| 2    | Client → AP | Client responds with SNonce + MIC (Message Integrity Code) |
| 3    | AP → Client | AP sends GTK (Group Temporal Key) + MIC                    |
| 4    | Client → AP | Client confirms receipt with a final ACK                   |

<br>

---
## Step-by-Step Breakdown

### Step 1 – AP → Client
- AP sends a **random nonce** (`ANonce`)
- Also includes SSID and replay counter

### Step 2 – Client → AP
- Client creates its own **SNonce**
- Derives PTK from:
  - PMK (from PSK)
  - ANonce
  - SNonce
  - MAC addresses
- Sends SNonce + **MIC** back

### Step 3 – AP → Client
- AP confirms the PTK is correct
- Sends the **Group Temporal Key (GTK)** encrypted
- Includes another MIC

### Step 4 – Client → AP
- Client sends ACK to confirm
- Secure session begins

<br>

---
## Attack Scenario

- Capture handshake using tools like:
  - `airodump-ng` + `aireplay-ng` (to deauth)
  - `hcxdumptool`
- Crack with:
  - `aircrack-ng -w wordlist.txt capture.cap`
  - `hashcat -m 22000 capture.hc22000 wordlist.txt`

<br>

---
## Key Terms

| Term  | Meaning                                       |
|-------|-----------------------------------------------|
| **PMK**   | Pairwise Master Key (from passphrase + SSID) |
| **PTK**   | Pairwise Transient Key (session key)         |
| **ANonce/SNonce** | Nonces exchanged to derive PTK        |
| **MIC**   | Message Integrity Code (verifies messages)   |
| **GTK**   | Group Temporal Key (used for broadcast)      |

<br>

---
## Notes

- The actual **password is never sent** — only proofs derived from it.
- A valid capture needs **all 4 packets**, ideally Steps 2 & 3.
- Without client traffic, try a **deauth attack** to force a handshake.

