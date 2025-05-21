from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# Define absolute paths to your folders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates_DoC')
STATIC_DIR = os.path.join(BASE_DIR, 'static_DoC')
IMAGES_DIR = os.path.join(BASE_DIR, 'images_DoC')

# Override default Flask folders
app.template_folder = TEMPLATES_DIR
app.static_folder = STATIC_DIR

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')  # Serves from templates_DoC/

# Serve CSS from /static_DoC/
@app.route('/static_DoC/<path:filename>')
def serve_css(filename):
    return send_from_directory(STATIC_DIR, filename)

@app.route("/duty-of-care.html")
def duty_of_care():
    return render_template("duty-of-care.html")

@app.route("/effective-efforts.html")
def effective_efforts():
    return render_template("effective_efforts.html")

@app.route("/toolbox.html")
def toolbox():
    return render_template("toolbox.html")

@app.route("/Our_Community.html")
def our_community():
    return render_template("our_community.html")

@app.route("/story1")
def story1():
    return render_template("story1.html")

@app.route("/dt_index")
def dt_index():
    return render_template("dt_index.html")

@app.route("/companies.html")
def companies():
    return render_template("companies.html")

@app.route("/substance")
def substance():
    cas_number = request.args.get("cas")
    return render_template("substance.html", cas=cas_number)

# Serve images from /images_DoC/
@app.route('/images_DoC/<path:filename>')
def serve_images(filename):
    return send_from_directory(IMAGES_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)