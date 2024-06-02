import pytest
import requests
from tests.lib.checkout_wrap import Checkout
from tests.lib.utils_wrap import build_request_header
import os
from config import APP_URL,LOG



@pytest.mark.description("Successful Checkout")
def test_successful_add_to_cart(login_as_user, checkout_payload, userid_param):
    LOG.info("*** Successful Checkout ***")
    response = Checkout.final_checkout(APP_URL,login_as_user, checkout_payload, userid_param)
    data=response.json()
    LOG.debug(data)
    message= response.json()["message"]
    assert response.ok
    assert message == "Checkout Successful"

@pytest.mark.description("Payment Failed")
def test_failure_add_to_cart(login_as_user, payment_failed_checkout_payload, userid_param):
    LOG.info("*** Payment Declined ***")
    response = Checkout.final_checkout(APP_URL,login_as_user, payment_failed_checkout_payload, userid_param)
    data=response.json()
    LOG.debug(data)
    message= response.json()["message"]
    assert response.status_code == 402
    assert message == "Please provide the valid card information."