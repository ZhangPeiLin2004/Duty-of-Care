from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Define absolute paths to your folders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates_DoC')  # Path to your HTML
STATIC_DIR = os.path.join(BASE_DIR, 'static_DoC')       # Path to CSS
IMAGES_DIR = os.path.join(BASE_DIR, 'images_DoC')       # Path to images

# Override default Flask folders
app.template_folder = TEMPLATES_DIR
app.static_folder = STATIC_DIR

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Serves from templates_DoC/

# Serve CSS from /static_DoC/
@app.route('/static_DoC/<path:filename>')
def serve_css(filename):
    return send_from_directory(STATIC_DIR, filename)

app.secret_key = "replace_this_with_a_random_secret"
@app.route("/toolbox.html")
def test_page():
    return render_template("/toolbox.html")

@app.route("/alternatives")
def alternatives():
    return render_template("alternatives.html")

@app.route("/companies")
def companies():
    return render_template("companies.html")

# Serve images from /images_DoC/
@app.route('/images_DoC/<path:filename>')
def serve_images(filename):
    return send_from_directory(IMAGES_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
