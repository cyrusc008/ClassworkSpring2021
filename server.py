from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_stats():
    return "The server is on again."


@app.route("/info", methods=["GET"])
def information():
    return "This server will allow the user to request blood analyses."


@app.route("/HDL", methods=["POST"])
def HDL_request():
    """
        input info: {"HDL": 60}
    """
    from blood_tests import analyzeHDL
    in_data = request.get_json()
    print(in_data)
    HDL = in_data["HDL"]
    result = analyzeHDL(HDL)
    answer = {"HDL": HDL, "Analysis": result}
    if answer != "normal":
        return "Bad HDL", 400
    return jsonify(answer)


@app.route("/say_hello/<name>/<age>", methods=["GET"])
def say_hello_function(name, age):
    next_year = int(age) + 1
    output = "Hello there, {}! You will be {} old next year".format(
        name, next_year)
    return output


if __name__ == "__main__":
    app.run()
