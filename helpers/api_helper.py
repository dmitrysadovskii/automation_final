import requests
import json
from helpers.general_helpers import generate_int


class Api:

    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2/user/'
        self.headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        
    def _assert_request(self, method, url, data=None, params=None, status_code=200):
        response = requests(method, url)
        assert response.status_code = status_code
        return response.json()
        

    def create_user(self, username: str, password: str):
        ids = generate_int(3)
        data = [{
            "id": ids,
            "username": username,
            "firstName": 'firstname',
            "lastName": 'lastname',
            "email": 'email',
            "password": password,
            "phone": "string",
            "userStatus": '0'
        }]
        url =
        self._assert_request('POST', url, data=json.dump(data))
#         r = requests.post(self.base_url + 'createWithArray', data=json.dumps(data),
#                           headers=self.headers)
#         assert r.status_code == 200

    def get_user_info(self, username: str):
        r = requests.get(self.base_url + username)
        r_json = r.json()
        assert r_json['username'] == username
        assert r.status_code == 200

    def login(self, username, password):
        params = f'login?username={username}&password={password}'
        r = requests.get(self.base_url + params)
        r_json = r.json()
        assert 'logged in user session' in r_json['message']
        assert r.status_code == 200

    def logout(self):
        r = requests.get(self.base_url + 'logout')
        assert r.status_code == 200

    def delete_user(self, username):
        r = requests.delete(self.base_url + username)
        assert r.status_code == 200
