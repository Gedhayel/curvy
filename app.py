from flask import Flask, render_template

app = Flask(__name__)

# Datos de tus redes sociales (fácil de editar)
redes_sociales = {
    "instagram": {
        "url": "https://www.instagram.com/curvy.perfec5?igsh=MXJtNDVxenNqZGJtZw==",
        "icono": "fab fa-instagram",
        "nombre": "Instagram",
        "clase": "instagram"
    },
    "facebook": {
        "url": "https://facebook.com/TU_USUARIO",
        "icono": "fab fa-facebook-f",
        "nombre": "Facebook",
        "clase": "facebook"
    },
    "tiktok": {
        "url": "https://www.tiktok.com/@curvyperfect5?_r=1&_t=ZS-94KabDKiW8N",
        "icono": "fab fa-tiktok",
        "nombre": "TikTok",
        "clase": "tiktok"
    },
    "whatsapp": {
        "url": "https://wa.link/0v9wj0",
        "icono": "fab fa-whatsapp",
        "nombre": "WhatsApp",
        "clase": "whatsapp"
    }
}

@app.route("/")
def home():
    return render_template("index.html", redes=redes_sociales)
if __name__ == "__main__":
    app.run(debug=True)