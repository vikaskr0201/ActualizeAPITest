import requests
from tests.lib.utils_wrap import build_request_header
from config import SESSION,LOG
import re
class Cart:

    cart_url ="/users/{userid}/cart"
   
    @classmethod
    def add_to_cart_successful(self, app_url, access_token, payload, useridParam):
        new_cart_url= re.sub(r'{userid}',str(useridParam), self.cart_url)
        LOG.info(new_cart_url)
        request_headers = build_request_header(access_token)
        LOG.debug(request_headers)
        response = SESSION.post(f"{app_url}{new_cart_url}", headers=request_headers, data=payload)
        return response
     
    @classmethod
    def add_to_cart_failure(self, app_url, access_token, payload, useridParam):
        new_cart_url= re.sub(r'{userid}',str(useridParam), self.cart_url)
        LOG.info(new_cart_url)
        request_headers = build_request_header(access_token)
        LOG.debug(request_headers)
        response = SESSION.post(f"{app_url}{new_cart_url}", headers=request_headers, data=payload)
        return response

    @classmethod
    def add_to_cart_failure_qty(self, app_url, access_token, payload, useridParam):
        new_cart_url= re.sub(r'{userid}',str(useridParam), self.cart_url)
        LOG.info(new_cart_url)
        request_headers = build_request_header(access_token)
        LOG.debug(request_headers)
        response = SESSION.post(f"{app_url}{new_cart_url}", headers=request_headers, data=payload)
        return response
    @classmethod
    def add_to_cart_unauthorized(self, app_url, access_token, payload, useridParam):
        new_cart_url= re.sub(r'{userid}',str(useridParam), self.cart_url)
        LOG.info(new_cart_url)
        request_headers = build_request_header(access_token)
        LOG.debug(request_headers)
        response = SESSION.post(f"{app_url}{new_cart_url}", data=payload) 
        return response