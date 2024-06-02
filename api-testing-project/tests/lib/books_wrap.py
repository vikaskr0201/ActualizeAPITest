import requests
from tests.lib.utils_wrap import build_request_header
from config import SESSION
class Books:

    book_url ="/books"


    @classmethod
    def search_available_book(self, app_url, access_token):
        params={"title": "Catalyst"}
        request_headers = build_request_header(access_token)
        response = SESSION.get(f"{app_url}{self.book_url}", headers=request_headers, params=params)
        return response
    

    @classmethod
    def search_unavailable_book(self, app_url, access_token):
        params={"title": "Working backwards"}
        request_headers = build_request_header(access_token)
        response = SESSION.get(f"{app_url}{self.book_url}", headers=request_headers, params=params)
        return response
    
    @classmethod
    def search_unauthorized_user_book(self, app_url, access_token):
        params={"title": "Catalyst"}
        request_headers = build_request_header(access_token)
        response = SESSION.get(f"{app_url}{self.book_url}", params=params)
        return response

