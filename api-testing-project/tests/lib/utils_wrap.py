from config import LOG
from config import HideSensitiveData

def build_request_header(access_token, content_type="application/json", **kwargs):
    headers = {
       "Authorization": f"Bearer {access_token}",
       "Accept": "application/json",
       "Content-Type":content_type
    }
    LOG.debug(f"Request Headers: {headers} ")
  
    return headers

def default_header():
    headers ={
        "Content-Type": "application/json"
    }
    LOG.debug(f"Request Headers: {headers} ")
    return headers