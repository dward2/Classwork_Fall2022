import pytest
from database_definition import Patient


@pytest.mark.parametrize("in_data, expected_keys, expected_types, expected", [
    ({"a": 1, "b": "string"}, ["a", "b"], [int, str], True),
    ({"a": 1, "b": 2}, ["a", "b"], [int, str],
     "Key b's value has the wrong data type"),
    ({"c": 1, "b": "string"}, ["a", "b"], [int, str],
     "Key a is missing from POST data"),
    (["a", "b", 1, 2], ["a", "b"], [int, str],
     "POST data was not a dictionary"),
    ({"a": "1", "b": "string"}, ["a", "b"], [int, str],
     "Key a's value has the wrong data type"),
    ({"a": 1, "b": "string", "c": True}, ["a", "b"], [int, str], True),
])
def test_dictionary_validation(in_data, expected_keys, expected_types,
                               expected):
    from db_server import dictionary_validation
    answer = dictionary_validation(in_data, expected_keys, expected_types)
    assert answer == expected


def test_add_patient():
    # import function to test as well as function to connect to MongoDB
    #   database
    from db_server import add_patient, init_server
    # initiate connection to database
    init_server()
    # Create data for the patient
    patient_name = "David"
    patient_id = 222
    blood_type = "A+"

    # Option 1: function being tested returns a Patient instance with copy of
    #           what was saved to MongoDB.  So, call function and receive
    #           the result.  Use that result to call the ".delete()" method of
    #           the MongoModel-type class to remove the entry from the MongoDB
    #           database, then assert that the saved name matches the name
    #           sent in this test.
    answer = add_patient(patient_name, patient_id, blood_type)
    answer.delete()
    assert answer.name == patient_name

    # Option 2: function being tested does not return a Patient instance.  So,
    #           call function.  Then, separately query database for the
    #           record which should have been added.  Delete that record in
    #           the MongoDB database, then assert that the found record name
    #           matched the name sent in this test.
    # add_patient(patient_name, patient_id, blood_type)
    # find_patient = Patient.objects.raw({"_id": patient_id}).first()
    # find_patient.delete()
    # assert answer.name == patient_name

    # Overall approach to writing a test of database functions:
    # 1. Set up the data base with the needed data
    # 2. Run code that you want to test
    # 3. Clean up database
    # 4. Assert
