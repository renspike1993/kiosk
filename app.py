from flask import Flask, render_template,request,jsonify
from model.student import Record
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('admin/home.html')


@app.route("/kiosk")
def kiosk():
    return render_template('student/step1.html')



@app.route("/step2", methods=["POST"])
def step2():
    data = request.get_json()
    student_name = data.get("student_name", "").strip()

    # Split by whitespace
    parts = student_name.split()

    if len(parts) < 2:
        return jsonify({"error": "Please provide at least first and last name"}), 400

    # If valid, continue with search
    result = Record.search_by_name(student_name)
    print(result)

    return jsonify({"student": result})

if __name__ == "__main__":
    # Debug=True auto-reloads when you change code
    app.run(host="0.0.0.0", port=5000, debug=True)
