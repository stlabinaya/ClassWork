import json


def create_person():
    bob = {"First Name": "Robert",
           "Last Name": "Smith",
           "Age": 35,
           "Visits": ["1/1/2020", "1/10/2020",
                      "3/15/2020"]}
    return bob


def output_json(my_dict):
    filename = "patient.json"
    out_file = open(filename, 'w')
    json.dump(my_dict, out_file)
    out_file.close()


def alternate_output(my_dict):
    filename = "patient.json"
    with open(filename, 'w') as out_file: # using this means you don't need close
        json.dump(my_dict,out_file)
    print("Here")


if __name__ == "__main__":
    x = create_person()
    output_json(x)
