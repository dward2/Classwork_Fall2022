def create_patient_entry(patient_first_name,
                         patient_last_name, patient_id,
                         patient_age):

    new_patient = {"First Name": patient_first_name,
                   "Last Name": patient_last_name,
                   "Id": patient_id,
                   "Age": patient_age,
                   "Tests": []}
    return new_patient


def print_database(db):
    # Method one that iterates over the keys in the dictionary "db"
    print("print_database Method #1")
    for patient_key in db:
        print(patient_key)
        print("Name: {}, id: {}, age: {}"
              .format(get_full_name(db[patient_key]),
                      db[patient_key]["Id"],
                      db[patient_key]["Age"]))

    # Method two that iterates over the specific values in the dictionary "db"
    print("print_database Method #2")
    for patient in db.values():
        print("Name: {}, id: {}, age: {}".format(get_full_name(patient),
                                                 patient["Id"],
                                                 patient["Age"]))


def get_full_name(patient):
    full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name


def find_patient(db, id_no):
    patient = db[id_no]
    return patient


def add_test_to_patient(db, id_no, test_name, test_value):
    patient = find_patient(db, id_no)
    patient["Tests"].append((test_name, test_value))


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"


def main():
    # database will be a dictionary where the keys are the patient_ids
    #   and the values will dictionaries containing patient info
    db = {}
    db[11] = create_patient_entry("Ann", "Ables", 11, 30)
    db[22] = create_patient_entry("Bob", "Boyles", 22, 34)
    db[3] = create_patient_entry("Chris", "Chou", 3, 25)
    print_database(db)
    add_test_to_patient(db, 3, "HDL", 100)
    print(db[3]["Tests"])
    print("Patient {} is a {}".format(get_full_name(db[3]),
                                      adult_or_minor(db[3])))


if __name__ == "__main__":
    main()
