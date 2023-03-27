from flask import Flask, render_template, request, send_file
from scaletool import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    tuning = request.form.get('option1')
    key = request.form.get('option2')
    
    # Generate the image based on the selected options
    # Replace this with your own image generation code
    output = generate_scale(list(tuning), key)


    image_path = f'Images/{tuning}_{key}maj.png'
    output.save(image_path)
    
    # Return the image file
    return send_file(image_path, mimetype='image/png')


# @app.route('/?tuning=<tuning>?key=<key>', methods=['POST'])
# def generate_image_HTTP(tuning, key):    
#     # Generate the image based on the selected options
#     # Replace this with your own image generation code
#     output = generate_scale(list(tuning), key)


#     image_path = f'Images/{tuning}_{key}maj.png'
#     output.save(image_path)
    
#     # Return the image file
#     return send_file(image_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
