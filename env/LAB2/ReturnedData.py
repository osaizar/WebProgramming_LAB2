import json

class ReturnedData(object):

    def __init__(self, success, message, data):
        self.success = success
        self.message = message
        self.data = data

    def createJSON(self):
        data = {}
        data["success"] = self.success
        data["message"] = self.message
        data["data"] = self.data

        return json.dumps(data)
