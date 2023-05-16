#Import necessary modules
from flask import Flask, render_template, request, send_file
from scaletool import *
import base64
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    
    string6 = request.form.get('string6')
    string5 = request.form.get('string5')
    string4 = request.form.get('string4')
    string3 = request.form.get('string3')
    string2 = request.form.get('string2')
    string1 = request.form.get('string1')
    key_center = request.form.get('key-center')
    scale_name = request.form.get('scale-name')

    tuning = [string6, string5, string4, string3, string2, string1]
    
    # Generate the image based on the selected options
    output = generate_scale_image(tuning, key_center, scale_name)


    # image_path = f'Images/{tuning}_{key}maj.png'
    buffer = io.BytesIO()
    output.save(buffer, format='PNG')

    # Convert the image to a base64-encoded string
    image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    # Render the index.html template with the image data
    return render_template('index.html', image_data=image_data)


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
