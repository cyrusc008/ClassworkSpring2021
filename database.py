def create_database_entry(name, id_no, age):
    new_patient = {"name": name, "id": id_no, "age": age, "test": list()}
    return new_patient


def print_directory(db):
    other_data = ["Room 2", "Room 3", "Room 4", "Room 5"]
    for i, patient in enumerate(db):
        print(i)
        print("Name: {}, id: {}, age: {}".format(patient[0],
                                                 patient[1],
                                                 patient[2]))
        print("Patient is in {}".format(other_data[i]))


def find_patient(id_no, db):
    for patient in db:
        if id_no == patient[1]:
            return patient[0]


def add_test_result(id_no, db, test_name, test_result):
    for patient in db:
        if patient["id"] == patient[1]:
            patient["test"].append((test_name, test_result))


def print_db(db):
    for patient in db:
        print_patient(patient)


def print_patient(patient):
    for key in patient:
        print("  {} = {}".format(key, patient[key]))


def demo(patient):
    if "name" in patient:
        print("Name is {}".format(patient["name"]))
    if "DOB" in patient:
        print("DOB is {}".format(patient["DOB"]))


def find_minor(patient):
    if patient["age"] <= 18:
        return "Minor"
    else:
        return "Adult"


def main():
    db = []
    db.append(create_database_entry("Ann Ables", 1, 15))
    db.append(create_database_entry("Bob Boyles", 2, 31))
    db.append(create_database_entry("Chris Chou", 3, 32))
    db.append(create_database_entry("David Dinkins", 4, 33))
    #print_db(db)
    #demo(db[0])
    print(find_minor(db[0]))
    #add_test_result(3, db, "HDL", 65)
    #add_test_result(3, db, "LDL", 80)


if __name__ == "__main__":
    main()
