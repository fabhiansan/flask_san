import os

from flask import Flask, flash, request, render_template,redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

upload_folder = 'Z:\htdocs\qhse\uploads'
allowed_extensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'php', 'py'])


app.config['upload_folder'] = upload_folder

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in allowed_extensions

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files :
            flash('no file part')
            return redirect(request.url)

        if file.filename == '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config[upload_folder], filename))
            return redirect(url_for('uploaded_file', filename=filename))



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['upload_folder'], filename)



@app.route('/')
def index():
    return render_template