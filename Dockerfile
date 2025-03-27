# Usar una imagen base de Python 3.11 (más estable con las dependencias actuales)
FROM python:3.11-slim

WORKDIR /app

# Copiar los archivos de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt .

# Actualizar pip y setuptools primero
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Asegurar que los scripts sean ejecutables
RUN chmod +x startup.sh check_environment.py

# Exponer el puerto donde corre la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["./startup.sh"]