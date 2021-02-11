def create_database_entry(name, id_no, age):
    new_patient = [name, id_no, age, []]
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
        if id_no == patient[1]:
            patient[3].append((test_name, test_result))

    print(db)


def main():
    db = []
    db.append(create_database_entry("Ann Ables", 1, 30))
    db.append(create_database_entry("Bob Boyles", 2, 31))
    db.append(create_database_entry("Chris Chou", 3, 32))
    db.append(create_database_entry("David Dinkins", 4, 33))
    add_test_result(3, db, "HDL", 65)
    add_test_result(3, db, "LDL", 80)


if __name__ == "__main__":
    main()
