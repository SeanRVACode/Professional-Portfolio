from flask import Flask,render_template,url_for,jsonify,request,flash,redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os




# Ini flask app
app = Flask(__name__)
app.config['SECRET_KEY'] ='secretkeything'
app.config['UPLOAD_FOLDER'] = 'Files'
Bootstrap5(app)


# Approved Upload file types
approved_extensions = set(('jpg','png','jpeg'))

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")
    

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in approved_extensions
    

# Homepage
@app.route("/",methods=['GET','POST'])
@app.route("/home",methods=['GET','POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # Grabs the file
        if allowed_file(file.filename):
            # Save the file to our upload folder.
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
            return "File has Been Uploaded"
        else:
            return "Invalid file type upload."
    return render_template("index.html",form=form)


