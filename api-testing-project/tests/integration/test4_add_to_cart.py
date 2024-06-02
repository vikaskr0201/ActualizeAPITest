import pytest
import requests
from tests.lib.cart_wrap import Cart
from tests.lib.utils_wrap import build_request_header
import os
from config import APP_URL,LOG

@pytest.mark.description("Successful adding to the cart")
def test_success_add_to_cart(login_as_user, add_to_cart_payload, userid_param):
    LOG.info("**** SUCCESSFUL ADDING TO THE CART ****")
    response = Cart.add_to_cart_successful(APP_URL,login_as_user, add_to_cart_payload, userid_param)
    data=response.json()
    LOG.debug(data)
    cartid= response.json()["cartid"]
    bookid= response.json()["bookid"]
    quantity= response.json()["quantity"]
    price= response.json()["price"]
    assert response.ok
    assert cartid is not None, "cartid is null"
    assert bookid is not None, "bookid is null"
    assert quantity is not None, "quantity is null"
    assert price is not None, "price is null"

@pytest.mark.description("Fail to add to the cart as books not found")
def test_fail_add_to_cart(login_as_user, fail_add_to_cart_payload, userid_param):
    LOG.info("*** FAILED TO ADD TO THE CART ***")
    response = Cart.add_to_cart_failure(APP_URL,login_as_user, fail_add_to_cart_payload, userid_param)
    data=response.json()
    LOG.debug(data)
    message= response.json()["message"]
    assert response.status_code == 404
    assert message == "Book is out of stock."


@pytest.mark.description("Bad Request with quantity range more than permissible value")
def test_bad_add_to_cart(login_as_user, bad_req_add_to_cart_payload, userid_param):
    LOG.info("**** BAD REQUEST ORDERED QUANTITY MORE THAN PERMISSIBLE VALUE ****")
    response = Cart.add_to_cart_failure_qty(APP_URL,login_as_user, bad_req_add_to_cart_payload, userid_param)
    data=response.json()

    LOG.debug(data)
    message= response.json()["message"]
    assert response.status_code == 400
    assert message == "Bad request. Please check the ordered quantity."



@pytest.mark.description("Unauthorized due to access token issue")
def test_unauthorized_add_to_cart(login_as_user, add_to_cart_payload, userid_param):
    LOG.info("**** UNAUTHORIZED ERROR - WHILE ADDING TO CART ****")
    response = Cart.add_to_cart_unauthorized(APP_URL,login_as_user, add_to_cart_payload, userid_param)
    data=response.json()
    message = data["message"]
    LOG.debug(data)
    assert response.status_code == 401
    assert message == "User is unauthorized. Please check the credentials."