# ShadowWatch

**A SQL-based credential breach detection system** built to monitor and flag leaked or insecure login data, empowering early detection of suspicious activity.

##  Features
- Simulates credential breaches using test datasets
- Detects duplicate or weak passwords (e.g., "123456", "admin")
- Analyzes login attempts for anomalies
- Uses SQL queries for efficient scanning
- [Optional] Integrates with Wireshark or packet logs

##  Tech Stack
- SQL (SQLite or MySQL)
- Python (for automation or scripting)
- Wireshark (for packet analysis simulation)
- Git/GitHub for version control

##  File Structure
- `/data`: Sample breached credentials
- `/src`: SQL scripts and logic
- `/logs`: Output of scans or reports

##  How to Use
1. Clone the repo  
2. Import sample data into your SQL tool  
3. Run `scan.sql` to detect weak/reused credentials  
4. (Optional) Add new `.csv` files to `/data` and re-run the query

##  Inspiration
Built as part of my cybersecurity studies at Drexel University to practice database skills, security logic, and breach simulation.

##  License
MIT License
