import PIL.Image
from glitch_this import ImageGlitcher
import random

def apply_glitch(path):
    try:
        # Abrimos la imagen utilizando la biblioteca PIL
        image = PIL.Image.open(path)
    except:
        print("Ruta no válida")
        return img

    # Aplicamos el filtro de ruido a la imagen
    img = noise(image)
    # Aplicamos el efecto de glitch a la imagen
    img = glitch(image)
    return img

def noise(img):
    # Generamos píxeles de ruido en la imagen
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
    booleanRand = random.randint(0, 1)
    colorOffsetVal = True
    if booleanRand == 0:
        colorOffsetVal = False

    # Inicializamos el objeto ImageGlitcher
    glitcher = ImageGlitcher()

    # Aplicamos el efecto de glitch a la imagen con parámetros aleatorios
    glitchImage = glitcher.glitch_image(
        img, random.uniform(0.1, 10.0), color_offset=colorOffsetVal
    )
    return glitchImage

def generate_filename():
    # Generamos un nombre único para la imagen
    return f"glitch_{random.randint(1000, 9999)}.jpg"