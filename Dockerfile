FROM python:3.6.5-alpine

WORKDIR /take-home-test

ADD . /take-home-test

RUN pip install -r requirements.txt

CMD [ "python", "src/app.py"]
