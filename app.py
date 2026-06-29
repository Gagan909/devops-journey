from flask import Flask, render_template, request, redirect
import socket
from datetime import datetime

app = Flask(__name__)

employees = [
    {"id": 101, "name": "Mukesh", "department": "AWS"},
    {"id": 102, "name": "Rahul", "department": "DevOps"},
    {"id": 103, "name": "Priya", "department": "Testing"}
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        employees=employees,
        hostname=socket.gethostname(),
        current_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

@app.route("/add", methods=["POST"])
def add_employee():

    name = request.form["name"]
    department = request.form["department"]

    employees.append({
        "id": len(employees) + 101,
        "name": name,
        "department": department
    })

    return redirect("/")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)