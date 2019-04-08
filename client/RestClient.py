import requests


class MyDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class RESTClient:
    def __init__(self, url):
        self.url = url

    def get_type_all(self):
        return list(map(MyDict, requests.get(url=self.url + "/type/").json()))

    def get_type(self, pk):
        return MyDict(requests.get(url=self.url + "/type" + f"/{pk}/").json())

    def set_type(self, *args):
        data = {
            "name": args[0],
            "min_value": args[1],
            "max_value": args[2],
            "format_of_value": args[3],
            "size": args[4],
            "description": args[5],
        }
        return MyDict(requests.post(url=self.url + "/type/", data=data).json())

    def reset_type(self, pk, *args):
        data = {
            "name": args[0],
            "min_value": args[1],
            "max_value": args[2],
            "format_of_value": args[3],
            "size": args[4],
            "description": args[5],
        }
        return MyDict(
            requests.put(url=self.url + "/type" + f"/{pk}/", data=data).json()
        )

    def delete_type(self, pk):
        requests.delete(url=self.url + "/type" + f"/{pk}/")

    def get_math_operations_all(self):
        return list(map(MyDict, requests.get(url=self.url + "/mathoperation/").json()))

    def get_math_operation(self, pk):
        return MyDict(requests.get(url=self.url + "/mathoperation" + f"/{pk}/").json())

    def set_math_operation(self, *args):
        data = {
            "name": args[0],
            "type_of_argument": args[1],
            "type_of_value": args[2],
            "description": args[3],
        }
        return MyDict(requests.post(url=self.url + "/mathoperation/", data=data).json())

    def reset_math_operation(self, pk, *args):
        data = {
            "name": args[0],
            "type_of_argument": args[1],
            "type_of_value": args[2],
            "description": args[3],
        }
        return MyDict(
            requests.put(url=self.url + "/mathoperation" + f"/{pk}/", data=data).json()
        )

    def delete_math_operation(self, pk):
        requests.delete(url=self.url + "/mathoperation" + f"/{pk}/")

    def get_class_all(self):
        return list(map(MyDict, requests.get(url=self.url + "/class/").json()))

    def get_class(self, pk):
        return MyDict(requests.get(url=self.url + "/class" + f"/{pk}/").json())

    def set_class(self, *args):
        data = {"name": args[0], "num_of_methods": args[1], "num_of_fields": args[2]}
        return MyDict(requests.post(url=self.url + "/class/", data=data).json())

    def reset_class(self, pk, *args):
        data = {"name": args[0], "num_of_methods": args[1], "num_of_fields": args[2]}
        return MyDict(
            requests.put(url=self.url + "/class" + f"/{pk}/", data=data).json()
        )

    def delete_class(self, pk):
        requests.delete(url=self.url + "/class" + f"/{pk}/")
