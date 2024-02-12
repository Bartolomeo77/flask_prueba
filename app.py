from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_URL = "http://ip172-18-0-9-cn518v4nupig00cjngdg-5000.direct.labs.play-with-docker.com//recommendations"


@app.route("/recommendations", methods=["GET", "POST"])
def mostrar_recomendaciones():
    if request.method == "POST":
        # Obtener el nuevo user_id del formulario
        user_id = request.form.get("user_id")
        # Crear la URL con el nuevo user_id
        new_url = f"{API_URL}?user_id={user_id}"
        # Hacer una solicitud GET al API con el nuevo user_id
        response = requests.get(new_url)
    else:
        # Hacer una solicitud GET al API con el user_id predeterminado (1)
        response = requests.get(API_URL)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        message = data.get("message", "No hay mensaje disponible.")
        recommendations = data.get("recommendations", [])
    else:
        message = "Error al obtener recomendaciones del API."
        recommendations = []

    # Renderizar el template HTML con los datos
    return render_template(
        "recomendaciones.html", message=message, recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)
