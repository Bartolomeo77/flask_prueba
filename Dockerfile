# Usa la imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor (incluyendo app.py y requirements.txt)
COPY . .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Expone el puerto 5000 para que Flask pueda escuchar las solicitudes
EXPOSE 5000

# Comando para ejecutar la aplicación Flask cuando se inicie el contenedor
CMD ["python", "app.py"]
