import requests

# Making a GET request to GitHub to get list of branches in a repository
r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
print(r)
print(type(r))
print(r.text)
if r.status_code == 200:
    answer = r.json()
    print(type(answer))
    for branch in answer:
        print(branch["name"])
else:
    print("Bad request: {}".format(r.text))

# Making a POST request to the name server
output_info = {"name": "David Ward",
               "net_id": "daw74",
               "e-mail": "david.a.ward@duke.edu"}

r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
                  json=output_info)
print(r)
print(r.text)

# Making a GET request to the name server
r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)

# POSTing and GETing to/from the message server
msg = {"user": "daw74", "message": "hello daw"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=msg)

r1 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/daw74")
print(r1.text)
