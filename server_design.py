from flask import Flask, request, jsonify
import logging
from pymodm import connect
from patient_class import Patient
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

db_test = list()


# @app.route("/", methods=["GET"])
# def server_stats():
#     return "The server is active."

def add_patient_to_db(name, id_info, blood_type):
    new_patient = Patient(name = name,
                          id_no = id_info,
                          blood_type = blood_type)
    saved_patient = new_patient.save()
    logging.info("Added new patient id {} to database").format(svaed_patient.id_no)
    return saved_patient


def add_test_to_db(id_info, test_name, test_result):
    new_test = {"id_info": id_info,
                "test_name": test_name,
                "test_result": test_result,
                "test": list()}
    db_test.append(new_test)
    logging.info(new_test)
    return True


def init_server():
    print("Connecting to MongoDB")
    connect("mongodb+srv://cyrusc008:PnX5fWFgyc9S0KLo@bme547.idiaq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    print("Connected to MongoDB")


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # get input data from requests
    in_data = request.get_json()
    # validate input
    answer, server_status = process_new_patient(in_data)

    return answer, server_status


def validate_new_patient_info(in_dict):
    expected_keys = ("name", "id", "blood_type")
    expected_types = (str, int, str)
    for key, ty in zip(expected_keys, expected_types):
        if key not in in_dict.keys():
            return "key not found: {}".format(key), 400
        if type(in_dict[key]) != ty:
            return "{} key has the wrong value type".format(key), 400
    return True, 200


def process_new_patient(in_data):
    validate_input, server_status = validate_new_patient_info(in_data)
    if validate_input is not True:
        return validate_input, server_status
    # define new patient dictionary
    add_patient_to_db(in_data["name"],
                      in_data["id"],
                      in_data["blood_type"])
    return "Patient successfully loaded", 200


@app.route("/new_test", methods=["POST"])
def post_add_test():
    # get input data from requests
    in_data = request.get_json()
    # validate input
    answer, server_status = process_new_test(in_data)

    return answer, server_status


def validate_new_test(in_dict):
    expected_keys = ("id", "test_name", "test_result")
    expected_types = (int, str, int)
    for key, ty in zip(expected_keys, expected_types):
        if key not in in_dict.keys():
            return "key not found: {}".format(key), 400
        if type(in_dict[key]) != ty:
            return "{} key has the wrong value type".format(key), 400
    return True, 200


def process_new_test(in_data):
    validate_input, server_status = validate_new_test(in_data)
    if validate_input is not True:
        return validate_input, server_status
    # define new patient dictionary
    add_test_to_db(in_data["id"],
                   in_data["test_name"],
                   in_data["test_result"])
    return "Test successfully loaded", 200

# @app.route("/HDL", methods=["POST"])
# def HDL_request():
#     """
#         input info: {"HDL": 60}
#     """
#     from blood_tests import analyzeHDL
#     in_data = request.get_json()
#     print(in_data)
#     HDL = in_data["HDL"]
#     result = analyzeHDL(HDL)
#     answer = {"HDL": HDL, "Analysis": result}
#     if answer != "normal":
#         return "Bad HDL", 400
#     return jsonify(answer)


if __name__ == "__main__":
    init_server()
    app.run()
