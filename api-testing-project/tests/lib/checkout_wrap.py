import requests
from tests.lib.utils_wrap import build_request_header
from config import SESSION,LOG
import re
class Checkout:

    checkout_url ="/users/{userid}/checkout"
   
    @classmethod
    def final_checkout(self, app_url, access_token, payload, useridParam):
        new_checkout_url= re.sub(r'{userid}',str(useridParam), self.checkout_url)
        LOG.info(new_checkout_url)
        request_headers = build_request_header(access_token)
        LOG.debug(request_headers)
        response = SESSION.post(f"{app_url}{new_checkout_url}", headers=request_headers, data=payload)
        return response
     