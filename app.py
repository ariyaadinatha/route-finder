from flask import Flask, render_template, url_for, request
import os

# Cari file root
uploadDir = (str(os.getcwd())+"/upload/")


app = Flask(__name__)

data = [
    {
        'name': 'Audrin',
        'place': 'kaka',
        'mob': '7736'
    },
    {
        'name': 'Stuvard',
        'place': 'Goa',
        'mob': '546464'
    }
]


@app.route('/', methods=['POST', 'GET'])
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


# Distance between coordinate
def getDistance(coor1, coor2):
    distLon = (coor2[0] - coor1[0]) * math.pi / 180.0
    distLat = (coor2[1] - coor1[1]) * math.pi / 180.0
    coor1[1] = (coor1[1]) * math.pi / 180.0
    coor2[1] = (coor2[1]) * math.pi / 180.0

    a = ((((math.sin(distLon/2))**2) *
         math.cos(coor1[1]) * math.cos(coor2[1])) + (math.sin(distLat/2)**2))
    c = 2 * math.asin(math.sqrt(a))
    dist = c * 6371
    return dist


if __name__ == "__main__":
    app.run(debug=True)
