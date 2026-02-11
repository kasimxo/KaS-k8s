# Utilizar la versión oficial de Python como imagen base
FROM python:3.13  
 
# Crear un directorio para la aplicación dentro del contenedor
RUN mkdir /app
 
# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app
 
# Configurar variables de entorno 
# PYTHONDONTWRITEBYTECODE evita que Python cree archivos .pyc, 
# lo que puede ahorrar espacio y evitar problemas de permisos en algunos entornos.
ENV PYTHONDONTWRITEBYTECODE=1
# PYTHONUNBUFFERED asegura que la salida de Python se muestre en tiempo real, 
# lo que es útil para el registro y la depuración.
ENV PYTHONUNBUFFERED=1 
 
# Actualizar pip a la última versión 
RUN pip install --upgrade pip 
 
# Copiar el archivo requirements.txt al contenedor para instalar las dependencias
COPY requirements.txt  /app/
 
# Instalar todas las dependencias de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
 
# Copiar el resto de los archivos de la aplicación al contenedor
COPY . /app/
 
# Exponer el puerto 8080 para acceder al servidor Django
EXPOSE 8080
 
# Levantar el servidor Django en el puerto 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]