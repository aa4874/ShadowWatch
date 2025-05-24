#  ShadowWatch – Credential Breach Detection System

ShadowWatch is a security-focused tool that allows users to detect and analyze compromised credentials using a local breach database. Built with **Python, SQLite, and Flask**, it provides both a command-line interface and a lightweight web dashboard for email breach checking.

---

##  Features

-  Store breached emails + SHA-256 hashed passwords
-  Check if a specific email exists in known breaches
-  SQL injection-safe lookups with parameterized queries
-  Flask web interface for simple UI-based checks
-  Timestamped logs for each breach entry

---

##  Technologies Used

- Python 3.13  
- SQLite3  
- Flask (Jinja2 templates)  
- SHA-256 via `hashlib`  

---

##  Local Web Interface

Run the Flask app to check breaches via browser:

```bash
python app.py
