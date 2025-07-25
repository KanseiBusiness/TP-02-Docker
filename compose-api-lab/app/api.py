from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

@app.route("/utilisateurs")
def get_utilisateurs():
    try:
        connection = mysql.connector.connect(
            host="mysql",
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 'Hello from MySQL!' AS message;")
        result = cursor.fetchone()
        return jsonify({"message": result[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
