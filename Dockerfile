FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /to_do_list_app

ADD . /to_do_list_app

COPY ./requirements.txt /to_do_list_app/requirements.txt

RUN pip install  -r requirements.txt

COPY . /to_do_list_app