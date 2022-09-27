from flask import Flask, render_template, request, redirect, url_for

import garage_door
import sprinklers

app = Flask(__name__, template_folder="templates", static_folder="static")

# CONSTANTS
HOST = "0.0.0.0"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("action") == "toggle_door":
            print("Button pressed to toggle door")
            garage_door.toggle_garage_door()
        elif request.form.get("action") == "run_sprinklers":
            print("Button pressed to run sprinkler system")
            sprinklers.run_system()

        return redirect(url_for("index"))

    elif request.method == "GET":
        return render_template("index.html")

    else:
        render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host=HOST)

