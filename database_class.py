class Patient:

    def __init__(self, first_name, last_name, age=None, state="NC"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)

    
    def output_full_name(self):
        return self.first_name + " " + self.last_name


def main():
    patient_1 = Patient("Ann", "Ables")
    patient_2 = Patient("Bob", "Boyles", 45)

    print(patient_1)
    print(patient_1.output_full_name())


if __name__ == "__main__":
    main()
