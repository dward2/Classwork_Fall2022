class Patient:

    def __init__(self, first_name, last_name, patient_id, age):
        self.first_name = first_name
        self.last_name = last_name
        self.patient_id = patient_id
        self.age = age
        self.tests = []

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def adult_or_minor(self):
        if self.age >= 18:
            return "adult"
        else:
            return "minor"


def create_patient_entry(patient_first_name,
                         patient_last_name, patient_id,
                         patient_age):
    new_patient = Patient(patient_first_name, patient_last_name,
                          patient_id, patient_age)
    return new_patient


def print_database(db):
    # Method one that iterates over the keys in the dictionary "db"
    print("print_database Method #1")
    for patient_key in db:
        print(patient_key)
        print("Name: {}, id: {}, age: {}".format(db[patient_key].full_name(),
                                                 db[patient_key].patient_id,
                                                 db[patient_key].age))

    # Method two that iterates over the specific values in the dictionary "db"
    print("print_database Method #2")
    for patient in db.values():
        print("Name: {}, id: {}, age: {}".format(patient.full_name(),
                                                 patient.patient_id,
                                                 patient.age))


def find_patient(db, id_no):
    patient = db[id_no]
    return patient


def add_test_to_patient(db, id_no, test_name, test_value):
    patient = find_patient(db, id_no)
    patient.tests.append((test_name, test_value))


def main():
    # database will be a dictionary where the keys are the patient_ids
    #   and the values will be instances of the "Patient" class
    db = {}
    db[11] = create_patient_entry("Ann", "Ables", 11, 30)
    db[22] = create_patient_entry("Bob", "Boyles", 22, 34)
    db[3] = create_patient_entry("Chris", "Chou", 3, 25)
    print_database(db)
    add_test_to_patient(db, 3, "HDL", 100)
    print(db[3].tests)
    patient_to_check = db[3]
    print("Patient {} is a {}".format(patient_to_check.full_name(),
                                      patient_to_check.adult_or_minor()))


if __name__ == "__main__":
    main()
