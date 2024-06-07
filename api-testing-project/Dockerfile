FROM python:3.12.3

WORKDIR /opt/restapi_testactualize
COPY requirements.txt .
RUN pip install --upgrade pip; \
    pip install -r requirements.txt
COPY . /opt/restapi_testactualize