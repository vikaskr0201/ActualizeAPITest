import pytest
import requests
from tests.lib.books_wrap import Books
from tests.lib.utils_wrap import build_request_header
import os
from config import APP_URL,LOG


@pytest.mark.description("Search for the book available in bookstore")
def test_search_available_book(login_as_user):
    LOG.info("**** SEARCHING BOOK AVAILABLE IN BOOKSTORE ****")
    response = Books.search_available_book(APP_URL,login_as_user)
    LOG.debug(response.json())
    assert response.ok


@pytest.mark.description("Search for the book unavailable in bookstore")
def test_search_unavailable_book(login_as_user):
    LOG.info("**** SEARCHING BOOK UNAVAILABLE IN BOOKSTORE ****")
    response = Books.search_unavailable_book(APP_URL,login_as_user)
    LOG.debug(response.json())
    assert response.status_code == 404
    assert response.json()["message"] == "Book is not available in bookstore."

@pytest.mark.description("Unauthorized while searching the book")
def test_search_unauthorized_user_book(login_as_user):
    LOG.info("**** SEARCHING BOOK WITH UNAUTHORIZED USER ****")
    response = Books.search_unauthorized_user_book(APP_URL,login_as_user)
    LOG.debug(response.json())
    assert response.status_code == 401
    assert response.json()["message"] == "User unauthorized.Please login again."