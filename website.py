from flask import Flask, request, send_file
from ImageToAscii import create_ascii_image
import io
import os

app = Flask(__name__)

@app.route("/create/<font_size>/<spacing>", methods=['POST'])
def create(font_size, spacing):
    file = request.files['file']   
    return_file = create_ascii_image(io.BytesIO(file.read()), int(font_size), int(spacing))
    data = io.BytesIO(open(return_file, "rb").read())
    os.remove(return_file)
    return send_file(data, as_attachment=True, download_name=file.filename)

if __name__ == '__main__':
    app.run(debug=True)