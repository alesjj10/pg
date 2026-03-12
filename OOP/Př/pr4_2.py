import json


if __name__ == "__main__":
    data = {"aaa": 1, "bbb": [1,2,3,4]}
    print(data)
    print(type(data))

    json_data = json.dumps(data)
    print(json_data)
    print(type(json_data))

    data2 = json.loads(json_data)
    print(data2)
    print(type(data2))