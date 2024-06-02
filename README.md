
:star: Star us on GitHub — it motivates us a lot to code !!
### Author : _Vikas Kumar_

##  :beginner: Project Description 
Design and implement mock APIs for a hypothetical online bookstore, then develop a comprehensive automated testing suite for these APIs.
## Project Objectives 
Demonstrate proficiency in API design, mocking services, and automated testing through the development of a functional mock API environment and corresponding test automation scripts. This repo will depicts the details on the below:\
 **API Design and Implementation**\
 **API Automation Testing**
 
### API Endpoints to be implemented: 

 ⁠*User Registration:* ⁠ POST /users/register
 ##
 ⁠*User Login:* ⁠ POST /users/login 
 ##
 ⁠*Search Books:* ⁠ GET /books?search=query
 ##
 ⁠*Add to Cart:* ⁠ POST /users/{userId}/cart
 ##
 ⁠*Checkout:* ⁠ POST /users/{userId}/checkout
 ##

### :notebook: Prerequistes:

Python - Version 3.12.3 is used [click here](https://www.python.org/downloads/)<br/>
Docker [click here](https://docs.docker.com/get-docker/)<br/>
Mockoon [click here](https://mockoon.com/download/#download-section) or Mockoon CLI [click here](https://hub.docker.com/r/mockoon/cli)<br/>
Postman for API functional test and API Documentation [click here](https://www.postman.com/downloads/)<br/>

###  :beginner: Approach: 

Mockoon is used to mock the required services. All the required API routes are created defining proper status, error handling and the rules.<br/>

Python testing framework pytest is used and pytest-html is used to generate the test reports.<br/>

### :electric_plug: Environment Set Up: 
Install the Docker as link in the prerequisites<br/>
Install Postman as per link in the prerequisites<br/>
Install Python as per the link in the prerequisites, Mac users can using homebrew and ensure pip3 is installed<br/>
Download the mockoon and install [click here]<br/>

###  :file_folder: Project Structure
The API test framework project structure as below 

```
.
└── api-testing-project
    ├── mock-apis/
    │   ├── config/
    │   │   ├── api_env.postman_environment.json --> postman environment file
    │   │   ├── Api_Tests.postman_collection.json --> API collections depicts the API documentation also
    │   │   └── mock_api.json --> Mockoon environment file, open as local env using this json once Mockoon installed
    │   └── reports/
    │       ├── API_Report.html --> Test report generated using pytest html
    │       └── api_test_actualize.log --> Test log generated for execution
    ├── tests/
    │   ├── integrations/ -- Tests added under this directory
    │   │   ├── test1_user_register.py --> user registration test
    │   │   ├── test2_user_login.py --> user login test
    │   │   ├── test3_search_book.py --> search book test
    │   │   ├── test4_add_to_cart.py --> add to cart test
    │   │   └── test5_checkout.py --> checkout test
    │   ├── lib/ -- wrapper and utilities under lib
    │   │   ├── utils_wrap.py --> building default header and header with Authorization access token 
    │   │   ├── books_wrap.py --> utilities class having methods for search test
    │   │   ├── cart_wrap.py --> utilities for add to cart tests 
    │   │   ├── checkout_wrap.py -->wrapper for checkout tests
    │   │   ├── login_wrap.py --> utilities method for login 
    │   │   └── register_wrap.py --> utilities method for user registration
    │   ├── conftest.py --> test data creation using pytest fixtures
    │   └── pytest.ini --> pytest initialization configs like logger, reports
    ├── config.py --> Details of App URL, method for masking sensitive data in logs like access token
    ├── requirements.txt --> to be installed in python vitual environment using pip3
    └── README.md --> Details of the project
```
###  :nut_and_bolt: Development Environment Readiness 

Download the code using git command as below or Download as zip from repositories<br/>
```git clone git@github.com:vikaskr0201/ActualizeAPITest.git
```
















