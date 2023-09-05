import flask from Flask

app = Flask("__name__")


@app.r
def Homepage ():
    return "Página inicial Garai"


if __name__ == "__main__":
    app.run(debug = True)