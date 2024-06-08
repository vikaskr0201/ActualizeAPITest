
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

###  :zap: Approach: 

Mockoon is used to mock the required services. All the required API routes are created defining proper status, error handling and the rules.<br/>
POSTMAN for functional validation that mock API's are working and used to derive API documentation.
Python testing framework pytest is used and pytest-html is used to generate the test reports.<br/>

### :electric_plug: Environment Set Up: 
Install the Docker refer Prerequisites <br/>
Install Postman refer Prerequisites<br/>
Install Python as per the link in the Prerequisites, Mac users can use homebrew and ensure pip3 is installed<br/>
Download the Mockoon and Mockoon ClI<br/>
Links are provided under Prerequisites<br/>

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
    │       └── api_test_actualize.log --> Test log generated for execution (sensitive information masked)
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
```
git clone git@github.com:vikaskr0201/ActualizeAPITest.git
```
From the downloaded path navigate to api-testing-project<br/>
```
cd ActualizeAPITest/api-testing-project
```
Set up the python virtual environment [click here](https://docs.python.org/3/library/venv.html)
Mac Users can perform below steps under api-testing-project<br/>

```
python3 -m venv venv
source venv/bin/activate
```
Once virtual environment is set or activated we need to install the required package listed in requirements.txt<br/>
Run the below command<br/>
```
pip3 install -r requirements.txt
```
**Get Backend Mockserver Up (Mockoon)**<br/>

**Approach 1:**<br/>
1. Start the Mockoon<br/>
2. Click on File -> Open Local Environment-> Select the mock_api.json and click open<br/>
3. The file mock_api.json can be found under api-testing-project/mock-apis/config<br/>
4. Click on start server(green button)<br/>
5. Once started go to setting on the mockoon to confirm API URL and port.<br/>
6. Under Settings -> API url value should be :<br/>
```
localhost and port as 3001
```
If port is not 3001 then we need to check and update the code config.py APP_URL= "http://localhost:3001" accordingly as the port backend mock mockoon is running.<br/>

**Approach 2:**<br/>
**Note** : If by anychance facing challenge to start then mockoon can be started using command line.<br/>

If docker is installed use mockoon cli [click here](https://hub.docker.com/r/mockoon/cli)<br/>
1. Run from commandline: <br/>
```
docker run -d --mount type=bind,source=/Users/vikaskumar/workspace/TestActualize/api-testing-project/mock-apis/config/mock_api.json,target=/data,readonly -p 3001:3001 mockoon/cli:latest -d data -p 3001
```
2. After start you will see a container id im command line 
For instance like<br/>
```
9bd05d002b4b3b4cfc2ba0e3c56ce118b2e2ed1c542bd2e64b82e9790dee1177
```
**Note**: in above command source points to your mock_api.json path <br/>

There are two ways to start the backend mock server either of the way can be applied. In case approach 2: Mockoon CLI is used then user should know basic docker commands and can watch container logs when developed mock API's are exercised<br/>

```
docker ps -a  
docker logs <containerid> --> to see container logs while hitting the API
docker kill <containerid> --> to stop server

```

**Postman Set Up**<br/>
1. Import the API collections and environment varialbles from from mock-apis/config directory in the POSTMAN<br/>
2. Files to be imported<br/>
```
api_env.postman_environment.json
API_Tests.postman_collection.json

```
3. Manually hit any API ensure backend Mockoon is running should return success. If required change the port in environment file currently its 3001<br/>
4. Click on ... three dots and click "View Documentation" to visualize detail API documentation. 

###  :rocket: Running Automated Test

**Note** : Before running the test ensure your virtual environment venv is ready with python3 and pip3<br/>
Install packages
```
pip3 install -r requirements.txt

```

Once all the requirements installed and module able to import, if face any change install or create __init__.py file in the folder<br/>

Run the below command to run the required tests:<br/>
```
python3 -m pytest tests/integration/test1_user_register.py
python3 -m pytest tests/integration/test2_user_login.py
python3 -m pytest tests/integration/test3_search_book.py 
python3 -m pytest tests/integration/test4_add_to_cart.py 
python3 -m pytest tests/integration/test5_checkout.py 
```
Report and Logs will be generated under reports/ directory. Sample reports and logs attached.<br/>

Masking password and access token feature is added in config.py.<br/>

**Note** : Mocks are designed considering preconditions mentioned in postman API documentation.<br/> 

## :camera: Demo Video
[!Watch here](https://drive.google.com/file/d/1ofhjzP1uYaHLAzeyvj8pnbiLABUiWK6Q/view?usp=sharing)

 ###  :fire: Improvements
 1. Automation Code can be dokerized and can be used together with Mockoon CLI. Refer `develop` branch<br/>
 2. Jenkins integration <br/>
 3. Enhancement in reporting like adding reportportal which which give us trends.<br/>

  ### :cactus: Branches

 Agile continuous integration methodology, so the version is frequently updated and development is really fast.<br/>

1. **`develop`** is the development branch, currently dockerized code is in the develop branch

2. **`main`** is the roduction ready code without dockerized.

##  :lock: License
Add a license here, or a link to it.






