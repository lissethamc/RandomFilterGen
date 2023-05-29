FROM python:3.10

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todo el contenido del directorio de trabajo al contenedor
COPY . /app/

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar tu aplicación
CMD [ "python", "webApp.py" ]
