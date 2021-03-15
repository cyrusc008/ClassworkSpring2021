import requests


def get_branches():
    r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
    print(r)
    print(type(r))
    print(r.status_code)
    print(r.text)
    branches = r.json()
    for branch in branches:
        print(branch["name"])


def students():
    my_info = {"name": "Cyrus Tanade", "net_id": "ctt14",
               "e-mail": "cyrus.tanade@duke.edu"}
    r = requests.post("http://vcm-6764.vm.duke.edu:5000/student", json=my_info)
    print(r.status_code)
    print(r.text)
    data = r.json()
    print(data["message"])


def blood_match():
    r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/ctt14")
    data = r.json()
    ids = [data["Donor"], data["Recipient"]]
    for index, idx in enumerate(ids):
        g = requests.get(
            "http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(idx))
        print(g.text)
    my_info = {"Name": "ctt14", "Match": "Yes"}
    a = requests.post(
        "http://vcm-7631.vm.duke.edu:5002/match_check", json=my_info)
    print(a.status_code)
    print(a.text)


if __name__ == "__main__":
    blood_match()
