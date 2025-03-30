from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' not in request.files:
        return redirect('/')
    file = request.files['photo']
    if file.filename == '':
        return redirect('/')
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
