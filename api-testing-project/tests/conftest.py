import pytest
import requests
import json
from faker import Faker
import random
from config import SESSION
from config import SESSION, APP_URL, VALID_USER, VALID_PASSWORD, LOG

##Fixture for api that requires access token
@pytest.fixture(scope='session')
def login_as_user():
    LOG.info("login_as_user")
    payload={"email":VALID_USER,"password": VALID_PASSWORD}
    LOG.debug(f"Login payload: {payload}")
    response = SESSION.post(f"{APP_URL}/users/login", data=payload)
    access_token= response.json()["access_token"]
    yield access_token

##Fixture for registration & login
@pytest.fixture(scope='session')
def valid_user_payload():
    fake= Faker()
    email_data= fake.email()
    password_data = fake.password(length=10)
    valid_json={"email": email_data,"password": password_data}
    return json.dumps(valid_json)

@pytest.fixture(scope='session')
def invalid_user_payload():
    fake= Faker()
    invalid_email_data= fake.email().split('@')[1] ## making invalid email by trimming @
    password_data = fake.password(length=10)
    valid_json={"email": invalid_email_data,"password": password_data}
    return json.dumps(valid_json)

@pytest.fixture(scope='session')
def forbidden_register_user_payload():
    fake= Faker()
    forbidden_email_data= "admin@actualize.com" ## considering this is already registered email address
    password_data = fake.password(length=10)
    valid_json={"email": forbidden_email_data,"password": password_data}
    return json.dumps(valid_json)

@pytest.fixture(scope='session')
def user_not_found_payload():
    fake= Faker()
    user_not_found_email_data= "test@actualize.com" ## considering this user is not registered and trying to login
    password_data = fake.password(length=10)
    valid_json={"email": user_not_found_email_data,"password": password_data}
    return json.dumps(valid_json)

@pytest.fixture(scope='session')
def add_to_cart_payload():
    fake= Faker()
    quantity = fake.pyint(min_value=1, max_value=99)
    LOG.debug(quantity)
    bookid = fake.pyint(min_value=1, max_value=99)
    while bookid == 50: ##bookid 50 is considered not found in the store as per mock design
        bookid = fake.pyint(min_value=1, max_value=99)
    valid_json={"bookid": bookid,"quantity": quantity}
    LOG.debug(valid_json)
    return json.dumps(valid_json)

@pytest.fixture(scope='session')
def userid_param():
    fake= Faker()
    userid = fake.pyint(min_value=1, max_value=99)
    LOG.info(userid)
    yield userid
   
@pytest.fixture(scope='session')
def fail_add_to_cart_payload():
    fake= Faker()
    quantity = fake.pyint(min_value=1, max_value=99)
    LOG.debug(quantity)
    bookid = 50 ## mock bookid 50 is considered not found in the store as per design
    valid_json={"bookid": bookid,"quantity": quantity}
    LOG.debug(valid_json)
    return json.dumps(valid_json)

@pytest.fixture(scope='session')
def bad_req_add_to_cart_payload():
    fake= Faker()
    quantity = 101 ## Mock designed to support quantity maximum as 99
    bookid = fake.pyint(min_value=1, max_value=99)
    while bookid == 50: ##bookid 50 is considered not found in the store as per mock design
        bookid = fake.pyint(min_value=1, max_value=99)
    valid_json={"bookid": bookid,"quantity": quantity}
    LOG.debug(valid_json)
    return json.dumps(valid_json)

@pytest.fixture(scope='session')
def checkout_payload():
    fake= Faker()
    paymentToken = fake.hexify('^^^^^^^^^^^^^^^^') #generating string of 16 hexadecimal digits

    #paymentToken1 = random.choice(["0123456789abcdef","abcdefabcdefabcd","1234567890abcdef","FFFFFFFFFFFFFFFF"])
    LOG.debug(paymentToken)
    cartid = fake.pyint(min_value=1, max_value=99)
    payment_method_1 = "credit_card"
    payment_method_2 = "debit_card" 
    paymentMethod= random.choice([payment_method_1, payment_method_2])
    valid_json={"cartid": cartid,"paymentMethod": paymentMethod,"paymentToken":paymentToken}
    LOG.debug(valid_json)
    return json.dumps(valid_json)

@pytest.fixture(scope='session')
def payment_failed_checkout_payload():
    fake= Faker()
    paymentToken = fake.hexify('^^^^^^^^^^^^^^^^^^') #generating string of 18 hexadecimal digits
    #paymentToken1 = random.choice(["0123456789abcdef12","abcdefabcdefabcd12","1234567890abcdef12","FFFFFFFFFFFFFFFF12"])
    LOG.debug(paymentToken)
    cartid = fake.pyint(min_value=1, max_value=99)
    payment_method_1 = "credit_card"
    payment_method_2 = "debit_card" 
    paymentMethod= random.choice([payment_method_1, payment_method_2])
    valid_json={"cartid": cartid,"paymentMethod": paymentMethod,"paymentToken":paymentToken}
    LOG.debug(valid_json)
    return json.dumps(valid_json)