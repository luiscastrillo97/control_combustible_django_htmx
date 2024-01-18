# Imagen base
FROM python:3.10.13-slim-bullseye
# FROM --platform=linux/amd64 python:3.10.13-slim-bullseye # Para no tener problemas con la instalación

# Establecer variables de entorno

# Evitar comprobaciones de version de pip
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# Evitar que python genere archivos con extensiones .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Desactivar el almacenamiento en buffer
ENV PYTHONUNBUFFERED 1

# Establecer el directorio de trabajo
WORKDIR /code

# Instalar las dependencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copiar el proyecto
COPY . .