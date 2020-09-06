from flask import Flask, send_file, request
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
import glob
from io import BytesIO

app = Flask(__name__)

DIRECTORY = "images/"

# Send a zipped file with the last N images (in reverse alphabetic order)
@app.route('/byCount', methods=['GET'])
def by_count():
    count = int(request.args.get('count'))
    # location = request.args.get('location')
    if not count:
        count = 1
    file_list = []
    for name in glob.glob(DIRECTORY + '*.jpg'):
        file_list.append(name)
    file_list.sort()
    files_to_zip = file_list[-count:]
    if not len(files_to_zip):
        return "NO IMAGES"
    memory_file = BytesIO()
    with ZipFile(memory_file, 'w') as zip:
        for file in files_to_zip:
            with open(file, 'rb') as f:
                data = ZipInfo(file)
                data.compress_type = ZIP_DEFLATED
                zip.writestr(data, f.read())
    memory_file.seek(0)
    return send_file(memory_file, attachment_filename='images.zip', as_attachment=True)

# Send a zipped file with images following the given last filename
@app.route('/byLast', methods=['GET'])
def by_last():
    last = request.args.get('last')
    # location = request.args.get('location')
    if not last:
        last = ''
    file_list = []
    for name in glob.glob(DIRECTORY + '*.jpg'):
        if name.split('.') > last:
            file_list.append(name)
    if not len(file_list):
        return "NO IMAGES"
    memory_file = BytesIO()
    with ZipFile(memory_file, 'w') as zip:
        for file in file_list:
            with open(file, 'rb') as f:
                data = ZipInfo(file)
                data.compress_type = ZIP_DEFLATED
                zip.writestr(data, f.read())
    memory_file.seek(0)
    return send_file(memory_file, attachment_filename='images.zip', as_attachment=True)

# Send an image by id/name
@app.route('/byId', methods=['GET'])
def by_id():
    id = request.args.get('id')
    if not id:
        return 'ERROR'
    return send_file(DIRECTORY + id + ".jpg", mimetype='image/jpeg')
