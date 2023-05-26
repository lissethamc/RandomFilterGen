import PIL.Image

# Arreglo de caracteres que reemplazarán los píxeles de la imagen
# Cambia estos caracteres para obtener diferentes resultados
AsciiChars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Función que redimensiona la imagen
def resizeImage(image, newWidth=100):
    width, height = image.size
    ratio = height / width
    newHeight = int((newWidth * ratio) / 2)
    resizedImage = image.resize((newWidth, newHeight))
    return resizedImage

# Función que convierte la imagen a escala de grises
def grayfy(image):
    grayScaleImage = image.convert("L")
    return grayScaleImage

# Función que reemplaza los píxeles por caracteres del arreglo declarado anteriormente
def pixelsToAscii(image):
    pixels = image.getdata()
    characters = "".join([AsciiChars[pixel // 25] for pixel in pixels])
    return characters

def imageToAscii(path, newWidth=100):
    try:
        # Abrimos la imagen utilizando la biblioteca PIL
        image = PIL.Image.open(path)
    except:
        print("Ruta no válida")
        return

    # Convertimos la imagen a una representación ASCII
    newImageData = pixelsToAscii(grayfy(resizeImage(image, newWidth)))
    pixel_count = len(newImageData)
    
    # Generamos la representación de la imagen ASCII con saltos de línea
    asciiImage = "\n".join(newImageData[i : (i + newWidth)] for i in range(0, pixel_count, newWidth))

    return asciiImage
