# temporary update to trigger redeploy


from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    photo = request.files['photo']
    upload_path = os.path.join('static', 'uploads', photo.filename)
    photo.save(upload_path)
    return f"<h2>Uploaded!</h2><img src='/{upload_path}'_
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
