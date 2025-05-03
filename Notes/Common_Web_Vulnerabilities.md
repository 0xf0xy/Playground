## Introduction

Web applications often expose sensitive behaviors through their HTTP requests and responses. By analyzing and manipulating them, attackers can discover vulnerabilities and exploit them for unauthorized access, data leaks, and more. Below are some of the most common web vulnerabilities, how to spot them, and what to look for in HTTP traffic.

<br>

---
## Vulnerability Table

| Vulnerability       | Where to Look                 | Signs / Symptoms                          | Example Payload                        |
|---------------------|-------------------------------|-------------------------------------------|----------------------------------------|
| **SQL Injection**   | URL params, POST body         | SQL errors, login bypass, time delays     | `admin'--`                             |
| **XSS**             | Query params, forms, headers  | Script reflected in response              | `<script>alert(1)</script>`            |
| **Command Injection** | POST data, hidden fields     | Command output in response                | `127.0.0.1; cat /etc/passwd`           |
| **Directory Traversal** | File parameters            | Access to system files                    | `../../../../etc/passwd`               |
| **CSRF**            | Missing CSRF tokens in forms  | Sensitive actions triggered externally    | Image tag POSTing to action URL        |
| **Open Redirect**   | URL parameters                | Redirects to user-controlled location     | `?redirect=http://evil.com`            |
| **Host Header Injection** | Host header              | Response manipulation or SSRF             | `Host: evil.com`                       |
| **Insecure Cookies** | Set-Cookie headers            | No `HttpOnly`, `Secure`, `SameSite` flags| `Set-Cookie: session=abc123`           |

<br>

---
## 1. SQL Injection (SQLi)

**Description:** Injection of raw SQL queries via user input.

**Tip:** Try `' OR '1'='1`, time-based payloads (`SLEEP(5)`), or logic testing (`1=1` vs `1=2`).

**Tools:** sqlmap, Burp, manual testing

<br>

---
## 2. Cross-Site Scripting (XSS)

**Description:** Injection of JavaScript into pages viewed by others.

**Types:**
- Reflected: in URL/query
- Stored: saved in database
- DOM-based: in JS logic

**Tools:** Burp, XSStrike, browser console

<br>

---
## 3. Command Injection

**Description:** Input is passed directly to system commands.

**Tip:** Chain with `;`, `&&`, or backticks. Look for responses containing system file data.

**Tools:** Burp, curl, manual payloads

<br>

---
## 4. Directory Traversal

**Description:** Bypass file access control by navigating directories.

**Tip:** Try various encodings: `../`, `..%2f`, `%2e%2e/`

<br>

---
## 5. CSRF

**Description:** Tricks the user’s browser into submitting a request using their credentials.

**Tip:** Check for lack of CSRF tokens and state-changing actions via GET.

**Mitigation Check:** Look for presence of `csrf_token` or `SameSite` flags.

<br>

---
## 6. Open Redirect

**Description:** Redirects that can be manipulated to point to malicious domains.

**Danger:** Used in phishing and token theft.

**Tip:** Try `redirect=https://evil.com`

<br>

---
## 7. Host Header Injection

**Description:** If the server trusts the `Host` header, you can modify it to:
- Poison cache
- Forge password reset links
- Exploit SSRF in internal APIs

<br>

---
## 8. Insecure Cookie Settings

**What to look for:**
- Missing `HttpOnly` (can be stolen via XSS)
- Missing `Secure` (sent over HTTP)
- Missing `SameSite` (vulnerable to CSRF)

<br>

---
## Final Notes

- Always test using tools like Burp Suite, curl, or browser DevTools.
- Chain multiple bugs (e.g., XSS + CSRF) for deeper impact.
- Don't rely on status codes alone — inspect headers, responses, cookies, and behaviors.

