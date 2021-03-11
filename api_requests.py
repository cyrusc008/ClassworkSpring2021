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


if __name__ == "__main__":
    students()
