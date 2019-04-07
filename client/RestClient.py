import requests


class MyDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class RESTClient:
    def __init__(self, url):
        self.url = url

    def get_type_all(self):
        return list(map(MyDict, requests.get(url=self.url + "/type").json()))

    def get_type(self, pk):
        return MyDict(requests.get(url=self.url + "/type" + f"/{pk}").json())

    def set_type(self, *args):
        pass

    def reset_type(self, pk, *args):
        pass

    def delete_type(self, pk):
        pass

    def get_math_operations_all(self):
        return list(map(MyDict, requests.get(url=self.url + "/mathoperation").json()))

    def get_math_operation(self, pk):
        return MyDict(requests.get(url=self.url + "/mathoperation" + f"/{pk}").json())

    def set_math_operation(self, *args):
        pass

    def reset_math_operation(self, pk, *args):
        pass

    def delete_math_operation(self, pk):
        pass

    def get_class_all(self):
        return list(map(MyDict, requests.get(url=self.url + "/class").json()))

    def get_class(self, pk):
        print(pk)
        return MyDict(requests.get(url=self.url + "/class" + f"/{pk}").json())

    def set_class(self, *args):
        pass

    def reset_class(self, pk, *args):
        pass

    def delete_class(self, pk):
        pass
