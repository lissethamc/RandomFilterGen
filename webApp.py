from flask import Flask, render_template, request
from PIL import Image
import socket
import os
import PIL.Image
from glitch_this import ImageGlitcher
import random
import io
from randomizer import *

app = Flask(__name__)

@app.route('/')
def index():
    # Renderizamos la plantilla 'index.html' y pasamos la dirección IP como variable
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        # Obtenemos el archivo de imagen del formulario
        image = request.files['image']
        image_rgba = Image.open(image)
        image_rgb=image_rgba.convert("RGB")
        filename = image.filename
        # Guardamos el archivo en la carpeta 'uploads' con el nombre original
        image_rgb.save('static/uploads/' + filename)
        # Aplicamos el efecto de glitch a la imagen
        glitched_image = apply_glitch('static/uploads/' + filename)
        
        # Generamos un nombre para la imagen glitcheada
        glitched_filename = generate_filename()
        # Guardamos la imagen glitcheada en la carpeta 'uploads' con el nuevo nombre
        glitched_image.save('static/generated_images/' + glitched_filename)
        # Renderizamos la plantilla 'index.html' y pasamos el nombre de la imagen glitcheada como variable
        return render_template('index.html', filename=glitched_filename)
    #Si no se seleccionó ninguna imagen, mostramos un mensaje de error
    return 'No se seleccionó ninguna imagen'


if __name__ == '__main__':
    # Ejecutamos la aplicación Flask en el host 0.0.0.0 y el puerto 5000 localhost,80 contenedores
    app.run(host='0.0.0.0', port=80)
