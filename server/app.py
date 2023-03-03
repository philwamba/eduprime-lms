from flask import Flask, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="../client/dist/assets", template_folder="../client/dist")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/static/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('../client/dist/images', path)

if __name__ == "__main__":
    app.run(debug=True)