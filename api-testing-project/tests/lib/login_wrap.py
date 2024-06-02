import requests
from tests.lib.utils_wrap import default_header
from config import SESSION
class Login:

    login_url ="/users/login"

    @classmethod
    def user_login(self, app_url, payload):
        request_headers= default_header()
        response = SESSION.post(f"{app_url}{self.login_url}", data=payload)
        return response
    
 