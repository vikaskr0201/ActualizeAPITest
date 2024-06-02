import requests
from tests.lib.utils_wrap import default_header
from config import SESSION
class Register:

    register_url ="/users/register"

    @classmethod
    def user_register(self, app_url, payload):
        request_headers= default_header()
        response = SESSION.post(f"{app_url}{self.register_url}", data=payload)
        return response
    
 

