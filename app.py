from flask import Flask, render_template, jsonify
from pathlib import Path
from datetime import datetime, timezone
import json
import os

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
CONTENT_FILE = BASE_DIR / "content" / "site.json"

DEFAULT_CONTENT = {
    "app_name": "Proyecto de Redes 2026",
    "headline": "Aplicación web sencilla, lista para contenerizar",
    "subtitle": "Hecha con Flask para que puedas cambiar texto o imagen sin tocar la lógica del servidor.",
    "hero_image": "images/hero.svg",
    "hero_alt": "Ilustración del proyecto",
    "tagline": "Ideal para pruebas de Git, Docker, ACR y Kubernetes.",
    "features": [],
    "footer": "EIF-208 - Comunicaciones y Redes"
}

def load_content():
    try:
        if CONTENT_FILE.exists():
            with CONTENT_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)

                merged = DEFAULT_CONTENT.copy()
                merged.update(data)

                return merged

    except Exception:
        pass

    return DEFAULT_CONTENT

@app.route("/")
def index():
    site = load_content()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template(
        "index.html",
        site=site,
        now=now
    )

@app.route("/healthz")
def healthz():
    return jsonify(
        status="ok",
        service="proyecto-redes-devops",
        utc_time=datetime.now(timezone.utc).isoformat()
    ), 200

@app.errorhandler(404)
def not_found(error):
    return render_template(
        "index.html",
        site=load_content(),
        now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"

    app.run(
        host="0.0.0.0",
        port=port,
        debug=debug_mode
    )