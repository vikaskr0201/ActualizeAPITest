import pytest
import requests
from tests.lib.register_wrap import Register
from config import APP_URL,LOG, SESSION

@pytest.mark.description("New user registration with valid credentials")
def test_user_valid_register(valid_user_payload):
    LOG.info("**** SUCCESSFUL NEW USER REGISTRATION ****")
    payload=eval(valid_user_payload)
    LOG.debug(payload)
    response = Register.user_register(APP_URL, payload)
    LOG.debug(response.json())
    assert response.ok
    assert response.json()["message"] == "User is registered successfully."


@pytest.mark.description("Wrong credentials leading to user registration fail")
def test_user_invalid_register(invalid_user_payload):
    LOG.info("**** REGISTRATION DECLINED WRONG CREDENTIALS ****")
    payload= eval(invalid_user_payload)
    LOG.debug(payload)
    response = Register.user_register(APP_URL, payload)
    LOG.debug(response.json())
    assert response.status_code == 400
    assert response.json()["message"] == "User fail to register"

@pytest.mark.description("Already existing user trying to register again")
def test_user_forbidden_register(forbidden_register_user_payload):
    LOG.info("**** ALREADY REGISTERED USER TRYING TO REGISTER AGAIN ****")
    payload= eval(forbidden_register_user_payload)
    LOG.debug(payload)
    response = Register.user_register(APP_URL, payload)
    LOG.debug(response.json())
    assert response.status_code == 403
    assert response.json()["message"] == "User is already registered, re-registration with same email forbidden. Please use new email address."


    