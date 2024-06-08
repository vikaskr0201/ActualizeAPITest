import requests
import logging
import re
import os

SESSION = requests.Session()

APP_URL= os.getenv("APP_URL", "http://localhost:3001")
VALID_USER = os.getenv("VALID_USER", "apitester@example.com")
VALID_PASSWORD= os.getenv("VALID_PASSWORD", "Password@1234")

LOG = logging.getLogger()

logging.getLogger('faker').setLevel(logging.ERROR)
class HideSensitiveData(logging.Filter):

    def filter(self, record):
        record.msg = str(record.msg).replace(VALID_PASSWORD, "*******")
        record.msg = re.sub(r'password.*?}',
                            'password\': \'*******\' ',str(record.msg))
        record.msg = re.sub(r'access_token.*?}',
                            'access_token\': \'*******\' ', str(record.msg))
        record.msg = re.sub(r'Authorization.*?,',
                          'Authorization\': \'*******\', ', str(record.msg))
        return True


LOG.addFilter(HideSensitiveData())
