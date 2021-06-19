import requests
from requests import exceptions


class Bears:
    # class to communicate with server
    def __init__(self):
        self.bears_type = ("POLAR", "BROWN", "BLACK", "GUMMY")

    def get_info(self):
        """
        Make GET request to /info adress 

        :return: code, headers, text
        """
        r = requests.get('http://localhost:8091/info')

        return {"code": r.status_code, "headers": r.headers, "text": r.text}

    def post_bear_create(self, bear_type: str, bear_name: str, bear_age: float):
        """
        Make POST request to /bear adress to add new bear

        :bear_type:  str from "POLAR", "BROWN", "BLACK", "GUMMY"
        :bear_name:  str
        :bear_age:   float
        :return:     code, headers, text, json
        """

        js_data = {"bear_type": bear_type,
                   "bear_name": bear_name,
                   "bear_age": bear_age}
        r = requests.post('http://localhost:8091/bear', json=js_data)
        return {"code": r.status_code, "headers": r.headers, "text": r.text, "json": r.json()}

    def get_all_bears(self):
        """
        Make GET request to /bear adress and get all bears
        :return:     code, headers, text, json
        """
        r = requests.get('http://localhost:8091/bear')

        return {"code": r.status_code, "headers": r.headers, "text": r.text, "json": r.json()}

    def get_bear(self, id: int):
        """
        Make GET request to /bear adress and get specific bear by id
        :id:         int bear id
        :return:     code, headers, text, json
        """
        r = requests.get('http://localhost:8091/bear/'+str(id))

        return {"code": r.status_code, "headers": r.headers, "text": r.text, "json": r.json()}

    def put_bear(self, bear_type: str, bear_name: str, bear_age: float, id: int):
        """
        Make PUT request to /bear/id adress and nodify bear by id
        :bear_type:  str from "POLAR", "BROWN", "BLACK", "GUMMY"
        :bear_name:  str
        :bear_age:   float
        :id:         int bear id
        :return:     code, headers
        """
        js_data = {"bear_type": bear_type,
                   "bear_name": bear_name,
                   "bear_age": bear_age}

        r = requests.put('http://localhost:8091/bear/'+str(id), json=js_data)

        return {"code": r.status_code, "headers": r.headers}

    def delete_all_bears(self):
        """
        Make DELETE request to /bear and delete all bears 

        :return:     code, headers
        """
        r = requests.delete('http://localhost:8091/bear')

        return {"code": r.status_code, "headers": r.headers}

    def delete_bear(self, id: int):
        """
        Make DELETE request to /bear adress and delete specific bear by id
        :id:         int bear id
        :return:     code, headers
        """
        r = requests.delete('http://localhost:8091/bear/'+str(id))

        return {"code": r.status_code, "headers": r.headers}
