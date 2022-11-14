import requests

def upload_patient_info(patient_name, patient_id, patient_blood_type):
    """Uploads patient information to the server.

    This function recevies patient information from the GUI code, creates
    the needed JSON dictionary with this data, and issues a POST request
    to the server to upload this data.  The response information is returned.

    Args:
        patient_name (str): patient name
        patient_id (int): patient medical record number
        patient_blood_type (str): patient blood type (ex, "A+")

    Returns:
        str, int: the response text and status code

    """
    out_data = {"name": patient_name, "id": patient_id,
                "blood_type": patient_blood_type}
    r = requests.post("http://127.0.0.1:5000/new_patient", json=out_data)
    return r.text, r.status_code


# Commented-out code below is remnants of when this file was used as a
#   test client for server.  It is commented out so that the function above
#   can be successfully imported into GUI code.
# Other functions could be made from the code below.

# test_data = {"id": 3, "test_name": "LDL", "test_result": 200}
# r = requests.post("http://127.0.0.1:5000/add_test", json=test_data)
# print(r.status_code)
# print(r.text)
#
# r = requests.get("http://127.0.0.1:5000/get_results/3")
# print(r.status_code)
# if r.status_code == 200:
#     print(r.json())
# else:
#     print(r.text)
#
# Invalid request to see what happens
# r = requests.get("http://127.0.0.1:5000/get_results/43")
# print(r.status_code)
# print(r.text)
