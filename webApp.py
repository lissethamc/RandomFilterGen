from flask import Flask, render_template, request

from PIL import Image
import socket
import os
import PIL.Image
from glitch_this import ImageGlitcher
import random
import io

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
        glitched_filename = 'glitched_' + filename
        # Guardamos la imagen glitcheada en la carpeta 'uploads' con el nuevo nombre
        glitched_image.save('static/generated_images/' + glitched_filename)
        # Renderizamos la plantilla 'index.html' y pasamos el nombre de la imagen glitcheada como variable
        return render_template('index.html', filename=glitched_filename)
    #Si no se seleccionó ninguna imagen, mostramos un mensaje de error
    return 'No se seleccionó ninguna imagen'

def apply_glitch(path):
    try:
        # Abrimos la imagen utilizando la biblioteca PIL
        image = PIL.Image.open(path)
    except:
        print("Ruta no válida")
        return

    # Aplicamos el efecto de ruido a la imagen
    img = noise(image)
    # Aplicamos el efecto de glitch a la imagen
    img = glitch(img)

    # Generamos un nombre único para la imagen glitcheada
    glitched_filename = generate_filename()
    # Ruta de la carpeta 'uploads' en la ruta 'RandomFilterGen/uploads/'
    uploads_folder = os.path.join('static', 'generated_images')
    # Comprobamos si la carpeta 'uploads' existe, si no, la creamos
    if not os.path.exists(uploads_folder):
        os.makedirs(uploads_folder)
    # Guardamos la imagen glitcheada en la carpeta 'uploads' con el nuevo nombre y en la ruta correcta
    glitched_save_path = os.path.join(uploads_folder, glitched_filename)
    img.save(glitched_save_path)

    # Retornamos la imagen glitcheada en lugar del nombre de archivo
    return img

def noise(img):
    # Aplicamos el efecto de ruido a la imagen
    for i in range(round(img.size[0] * img.size[1] / random.randint(1, 10))):
        img.putpixel(
            (
                random.randint(0, img.size[0] - 1),
                random.randint(0, img.size[1] - 1),
            ),
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ),
        )
    return img

def glitch(img):
    # Aplicamos el efecto de glitch a la imagen
    booleanRand = random.randint(0, 1)
    colorOffsetVal = True
    if booleanRand == 0:
        colorOffsetVal = False

    glitcher = ImageGlitcher()
    glitchImage = glitcher.glitch_image(
        img, random.uniform(0.1, 10.0), color_offset=colorOffsetVal
    )
    return glitchImage

def generate_filename():
    # Generamos un nombre único para la imagen
    return f"glitch_{random.randint(1000, 9999)}.jpg"

if __name__ == '__main__':
    # Ejecutamos la aplicación Flask en el host 0.0.0.0 y el puerto 5000
    app.run(host='0.0.0.0', port=5000)
