from helpers.api_helper import Api
from helpers.general_helpers import generate_string


def test_api_scenario():
    username = generate_string(6)
    password = generate_string(6)
    api = Api()
    api.create_user(username, password)
    api.login(username, password)
    api.get_user_info(username)
    api.logout()
    api.delete_user(username)
