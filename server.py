from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_stats():
    return "The server is on."


if __name__ == "__main__":
    app.run()
