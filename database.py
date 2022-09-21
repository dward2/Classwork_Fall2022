def create_patient_entry(patient_name, patient_id,
                         patient_age):

    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient


def print_database(db):
    for patient in db:
        print(patient)
        print("Name: {}, id: {}, age: {}".format(patient[0],
                                                 patient[1],
                                                 patient[2]))


def find_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient
    return False


def add_test_to_patient(db, id_no, test_name, test_value):
    patient = find_patient(db, id_no)
    patient[3].append((test_name, test_value))


def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 11, 30))
    db.append(create_patient_entry("Bob Boyles", 22, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    add_test_to_patient(db, 3, "HDL", 100)
    print("Output for finding patient:")
    print(find_patient(db, 3))

    room_list = ["Room 1", "Room 2", "Room 3"]

    print("Output of normal for loop")
    for patient in db:
        print(patient)

    print("Output for enumerate")
    for i, patient in enumerate(db):
        print(i)
        print("Name = {}, Room = {}".format(patient[0], room_list[i]))

    print("Output for zip")
    for patient, room in zip(db, room_list):
        print("Name = {}, Room = {}".format(patient, room))


if __name__ == "__main__":
    main()
