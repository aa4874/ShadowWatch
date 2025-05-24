from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        email = request.form.get("email")
        conn = sqlite3.connect("shadowwatch.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM breaches WHERE email = ?", (email,))
        result = cursor.fetchall()
        conn.close()
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

