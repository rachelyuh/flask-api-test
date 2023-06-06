from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    apikey = "randomapikey"
    response = requests.get("https://pokeapi.co/api/v2/pokemon/eevee")
    response = requests.get("https://pokeapi.co/api/v2/pokemon/eevee" + "?apikey=" + apikey)
    data = response.json()  
    name = data["species"]["name"]
    img = data["sprites"]["front_default"]
    return render_template("index.html", poke_src = img, poke_name = name)

if __name__ == "__main__":
    app.run()
