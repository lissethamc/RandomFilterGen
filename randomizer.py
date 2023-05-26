import PIL.Image
from glitch_this import ImageGlitcher
import random

def applyFilter(path):
    try:
        # Abrimos la imagen utilizando la biblioteca PIL
        image = PIL.Image.open(path)
    except:
        print("Ruta no válida")
        return

    # Aplicamos el filtro de ruido a la imagen
    img = noise(image)

    # Aplicamos el efecto de glitch a la imagen
    img = glitch(image)

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

    # Guardamos la imagen glitcheada en un archivo
    glitchImage.save("test_images/glitch.jpg")
