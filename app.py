from flask import Flask, render_template, url_for, request
import os

# Cari file root
uploadDir=(str(os.getcwd())+"/upload/")


app = Flask(__name__)

data=[
    {
        'name':'Audrin',
        'place': 'kaka',
        'mob': '7736'
    },
    {
        'name': 'Stuvard',
        'place': 'Goa',
        'mob' : '546464'
    }
]


@app.route('/', methods=['POST','GET'])



def index():
    if request.method == 'POST':
        koordinatAwal = request.form['posisi-awal']
        koordinatTujuan = request.form['posisi-tujuan']
        fileInput = request.files['file-graf']
        fileInput.save(os.path.join(uploadDir, fileInput.filename))
        # return koordinatTujuan
        return render_template('index.html', data=data)
    else:
        return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)

