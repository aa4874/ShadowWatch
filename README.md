#  ShadowWatch – Credential Breach Detection Tool

**ShadowWatch** is a lightweight security intelligence tool built using Python and SQL. It allows users or analysts to track and query breached email-password combinations, simulating real-world breach monitoring systems used in SOC teams.

##  Features

-  Insert breached credentials (email + hashed password + breach source)
-  Query if a specific email is compromised
-  SHA-256 hashing to protect stored passwords
-  Timestamped logs of all stored breach data
-  SQL-injection safe queries using parameterized inputs

##  Technologies Used

- **Python 3**
- **SQLite3 (SQL)**
- `hashlib` for SHA-256 password hashing
- Terminal-based interface (CLI)

##  Project Structure

