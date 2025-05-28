from flask import Flask, g, render_template, send_from_directory, session, redirect, url_for, request, jsonify
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = "replace-this-with-a-secret-key"

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

@app.route("/certification.html")
def certification():
    return render_template("certifications.html")

@app.route("/aboutus.html")
def aboutus():
    return render_template("aboutus.html")

@app.route("/story1")
def story1():
    return render_template("story1.html")

@app.route("/dt_index")
def dt_index():
    return render_template("dt_index.html")

@app.route("/guide")
def guide():
    return render_template("guide.html")

# Serve images from /images_DoC/
@app.route('/images_DoC/<path:filename>')
def serve_images(filename):
    return send_from_directory(IMAGES_DIR, filename)

############################################################################################################################################
# ToolBox
############################################################################################################################################

@app.route("/toolbox.html", endpoint='toolbox')
def toolbox():
    session.pop("x_clicked", None)
    return render_template("toolbox.html")

@app.route("/substance", endpoint='substance')
def substance():
    cas_number = request.args.get("cas")
    session["x_clicked"] = True
    return render_template("substance.html", cas=cas_number)


def load_data():
    filepath = os.path.join(BASE_DIR, 'static_DoC', 'data', 'companies.csv')
    df = pd.read_csv(filepath, sep=',', engine='python')
    df['TechList'] = df['Technologies'].astype(str).str.split(';')
    columns = [col for col in df.columns if col != 'TechList']
    return df.to_dict(orient='records')

FILTERS = {
    'Anaerobic Technology': ['Anaerobic water treatment', 'Downflow Anaerobic Carrier System'],
    'Ion Exchange': ['Ion Exchange', 'Inorganic filtermedia for ionexchange and adsorption', 'Delta water softeners'],
    'Filters': [
        'HFNF (Hollow fiber nanofiltration membranes)', 'NORIT (Granular activated Carbons)', 'Hydrodarco',
        'Granular Activated Carbon filtration', 'Fluized Activated Carbon', 'Bag Filter', 'Candel Filters',
        'Bag filters and Strainers', 'High Flow', 'Stainless steel filter housings', 'Carbon Filters',
        'Inert Filtermedia for filtration of suspended solids', 'Filtermedia for catalyc iron-and manganese removal',
        'Unspecified Filters'
    ],
    'Membrane / Advanced Filtration': [
        'Membrane solutions', 'Reverse Osmosis', 'Electrodialysis cells', 'Hollow fiber spinlines', 'Filtration Systems'
    ],
    'Oxidation / Chemical Treatment': [
        'Electrochemical Destruction', 'Supercritical water oxidation', 'Ferrate (VI)', 'Ozonation',
        'Advanced oxidation', 'Thermal Oxidizers', 'Chemical Scrubbers'
    ],
    'Physical / Chemical Processes': [
        'Dissolved air flotation (DAF)', 'Vacuum foam fractionation', 'Testing ACF', 'Discontinue filtration',
        'Settling tank dortmund tank', 'Physical chemical containers', 'Static mixers', 'Dynamic mixers',
        'Flocculator', 'Dosing Systems', 'Polymer preparation units', 'Dissolved air flotation units',
        'Lamella Settlers', 'De-Acidification, remineralisation and PH increase of Water',
        'Seeding material for crystallisation softening proces', 'Fluor-Mop'
    ],
    'Biological Treatment': [
        'Aerobic Biological Treatment', 'BODAC', 'Effluent polishing equipment',
        'Sludge discharge and dewatering equipment', 'Nitrogen removal', 'P-recovery with struvite'
    ],
    'Instrumentation / Measurement': [
        'Inductively coupled plasma mass spectrometry', 'Electronic sensors', 'Atomic absorption spectroscopy',
        'Electrical control equipment'
    ],
    'Others': [
        'Oxyle own technology', 'Specials', 'Flow makers'
    ]
}

@app.route("/companies.html", endpoint='companies')
def companies():
    filepath = os.path.join(BASE_DIR, 'static_DoC', 'data', 'companies.csv')
    df = pd.read_csv(filepath, sep=None, engine='python')
    if 'Technologies' in df.columns:
        tech_index = df.columns.get_loc("Technologies")
        df = df.iloc[:, :tech_index + 1]  # Slice columns
    columns = df.columns.tolist()
    data = df.to_dict(orient='records')
    return render_template("companies.html", data=data, columns=columns, filters=FILTERS)


if __name__ == '__main__':
    app.run(debug=True)