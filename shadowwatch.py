import sqlite3
import hashlib

# ---------- Step 1: Initialize Database ----------
def initialize_database():
    conn = sqlite3.connect("shadowwatch.db")
    cursor = conn.cursor()
    with open("schema.sql") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()
    print("✅ Database initialized.")

# ---------- Step 2: Hash Password ----------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- Step 3: Insert Sample Breach Data ----------
def insert_sample_breach(email, password, source):
    hashed_pw = hash_password(password)
    conn = sqlite3.connect("shadowwatch.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO breaches (email, password_hash, breach_source)
        VALUES (?, ?, ?)
    """, (email, hashed_pw, source))
    conn.commit()
    conn.close()
    print(f"✅ Breach data inserted for {email}")

# ---------- Step 4: Display All Breach Records ----------
def display_breaches():
    conn = sqlite3.connect("shadowwatch.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM breaches")
    rows = cursor.fetchall()
    print("\n📄 Stored Breaches:")
    for row in rows:
        print(row)
    conn.close()

# ---------- Step 5: Search for a Breached Email ----------
def check_if_breached(email):
    conn = sqlite3.connect("shadowwatch.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM breaches WHERE email = ?", (email,))
    results = cursor.fetchall()
    conn.close()

    if results:
        print(f"\n🚨 ALERT: {email} found in {len(results)} breach(s):")
        for row in results:
            print(row)
    else:
        print(f"\n✅ {email} not found in breach records.")

# ---------- MAIN EXECUTION ----------
initialize_database()
insert_sample_breach("testuser@example.com", "Test@1234", "MockBreach2025")
display_breaches()
check_if_breached("testuser@example.com")
check_if_breached("newuser@drexel.edu")
