from flask import Flask, render_template, send_from_directory
import os

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Route for the PCB model page
@app.route('/pcb_model')
def pcb_model():
    return render_template('pcb_model.html')

# Route to serve static files (images, CSS, JavaScript, etc.)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run
