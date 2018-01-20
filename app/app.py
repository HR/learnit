from flask import Flask
app = Flask(__name__)


@app.route("/teacher")
def main():
    return render_template('teacher.html')
