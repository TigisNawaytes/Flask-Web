from flask import Flask, render_template

app = Flask(__name__)

DataAlumni = [
    {
        'id': 1,
        'Nama': 'Rakhmad Adi S',
        'Angkatan': '1999',
        'Jabatan': 'Safety Manager',
        'Perusahaan': 'PT. Pertamina Persero'
    },
    {
        'id': 2,
        'Nama': 'Sigit Setyawan',
        'Angkatan': '2003',
        'Jabatan': 'Chemist Engineer',
        'Perusahaan': 'Cirebon Power -1'
    },
    {
        'id': 3,
        'Nama': 'Guntur Widyatama',
        'Angkatan': '2003',
        'Jabatan': 'Technical Manager',
        'Perusahaan': 'PT. Laiutan Luas Indonesia'
    },
    {
        'id': 4,
        'Nama': 'Mohammad Sidik',
        'Angkatan': '2003',
        'Jabatan': 'Chemist Engineer',
        'Perusahaan': 'PT. Bhumi Jepara Services'
    },
]


@app.route('/')
def hello_world():
  print(DataAlumni)
  return render_template("home.html", DataAlumni=DataAlumni)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
