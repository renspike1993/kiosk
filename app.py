from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('admin/home.html')


@app.route("/kiosk")
def kiosk():
    return render_template('client.html')

if __name__ == "__main__":
    # Debug=True auto-reloads when you change code
    app.run(host="0.0.0.0", port=5000, debug=True)
