# Proyecto Redes DevOps

Aplicación web hecha con Flask para el proyecto de Redes.

## Ejecutar localmente

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Ejecutar con Docker

Construir la imagen (desde la raíz del proyecto):

```bash
docker build -t flaskk_app .
```

Ejecutar el contenedor y mapear el puerto 5000:

```bash
docker run --name flask_app -p 5000:5000 flask_app
```

Nota: asegúrate de usar el mismo nombre de imagen/etiqueta al construir y ejecutar (por ejemplo, usa `flask_app` en ambos si prefieres).
