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


# Read from file
def readFile(namafile):
    pass


# Distance between coordinate
def getDistance(lng1, lat1, lng2, lat2):
    distLon = (lng2 - lng1) * math.pi / 180.0
    distLat = (lat2 - lat1) * math.pi / 180.0
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    a = ((((math.sin(distLon/2))**2) *
         math.cos(lat1) * math.cos(lat2)) + (math.sin(distLat/2)**2))
    c = 2 * math.asin(math.sqrt(a))
    dist = c * 6371
    return dist


if __name__ == "__main__":
    app.run(debug=True)
