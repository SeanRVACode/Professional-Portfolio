from flask import Flask,render_template,url_for,jsonify,request,flash,redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from PIL import Image
import os
import numpy as np
from sklearn.cluster import KMeans





# Ini flask app
app = Flask(__name__)
app.config['SECRET_KEY'] ='secretkeything'
app.config['UPLOAD_FOLDER'] = './static/Files'
Bootstrap5(app)


# Approved Upload file types
approved_extensions = set(('jpg','png','jpeg'))

class UploadFileForm(FlaskForm):
    file = FileField("File Upload",render_kw={"class":"form-control custom-file-input","style":"font-family: roboto; justify-content:center;"})
    submit = SubmitField("Upload File")
    

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in approved_extensions

def top_10_colors(img):
    width_limit = 600
    width = img.size[0]
    height = img.size[1]
    
    # Resize Image
    width_per = width_limit/width
    updated_height = int(height*width_per)
    
    img = img.resize((width_limit,updated_height))
    
    img_array = np.asarray(img)
    # 3 columns for RGB -1 indicates unknown rows
    img_array = img_array.reshape(-1,3)
    # w,h,d = tuple(img.shape)
    # Reshape the image into a 2D array, where each row represents a pixel
    # pixel = np.reshape(img,(w*h,d))
    
    # Desired number of colors for an image
    n_colors = 18
    
    # Kmeans cluster model
    model = KMeans(n_clusters=n_colors).fit(img_array)
    
    color_palette = model.cluster_centers_.tolist()
    
    return color_palette

def convert_colors_to_rgb(colors):
    rgb_colors = [f'rgb({r},{g},{b})' for r,g,b in colors]
    return rgb_colors



    

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
            print(file.filename)
            img = Image.open(fr'./static/Files/{file.filename}')
            img_loc = url_for('static',filename=f'Files/{secure_filename(file.filename)}')
            print(img_loc)
            colors = top_10_colors(img=img)
            
            return render_template('index.html',colors=colors,image=img_loc,form=form)
        else:
            return redirect(url_for('home',form=form))
    return render_template("index.html",form=form)

# @app.route('/images/<img>')
# def background(img):
#     return redirect(f'./static/images/{img}')


