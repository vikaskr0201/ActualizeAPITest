import pytest
import requests
from tests.lib.login_wrap import Login
from config import SESSION, APP_URL, VALID_USER, VALID_PASSWORD,LOG

@pytest.mark.description("Successful login and we are receiving access token")
def test_valid_login(valid_user_payload):
    LOG.info("**** SUCCESSFUL LOGIN ****")
    payload=eval(valid_user_payload)
    LOG.debug(payload)
    response = Login.user_login(APP_URL, payload)
    LOG.debug(response.json())
    access_token= response.json()["access_token"]
    assert response.ok
    assert access_token is not None, "access token is null"

@pytest.mark.description("Invalid login bad request test")
def test_user_invalid_login(invalid_user_payload):
    LOG.info("**** LOGIN FAILED WRONG EMAIL ****")
    payload= eval(invalid_user_payload)
    LOG.debug(payload)
    response = Login.user_login(APP_URL, payload)
    LOG.debug(response.json())
    assert response.status_code == 400

@pytest.mark.description("Unregistered user trying to login -404")
def test_user_not_found_login(user_not_found_payload):
    LOG.info("**** UNREGISTERED USER TRYING TO LOGIN ****")
    payload= eval(user_not_found_payload)
    LOG.debug(payload)
    response = Login.user_login(APP_URL, payload)
    LOG.debug(response.json())
    assert response.status_code == 404
    assert response.json()["message"] == "User not found. Please check the credentials."