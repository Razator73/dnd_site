FROM python:3.9

RUN pip install --upgrade pip
RUN pip install pipenv
COPY . .
RUN pipenv install --deploy

EXPOSE 5000
