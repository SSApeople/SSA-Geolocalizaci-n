# Usa una imagen base con Python 3.13.1
FROM python:3.11-slim

# Instalar dependencias necesarias
RUN apt update && apt install -y curl gnupg apt-transport-https ca-certificates

# Agregar la clave GPG de Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Agregar el repositorio de Microsoft para ODBC Driver 17
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Instalar el ODBC Driver 17 para SQL Server
RUN apt update && ACCEPT_EULA=Y apt install -y msodbcsql17 unixodbc unixodbc-dev

# Limpiar caché de paquetes
RUN apt clean && rm -rf /var/lib/apt/lists/*


# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . /app/

# Expone el puerto 5002, que es el puerto donde Flask escuchará
EXPOSE 5015

# Comando para ejecutar la aplicación Flask cuando el contenedor se inicie
CMD ["python", "app.py"]
