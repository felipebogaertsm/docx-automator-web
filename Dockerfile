FROM python:3.9
LABEL maintainer="Felipe Bogaerts de Mattos"

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip setuptools wheel
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

WORKDIR /usr/app
COPY ./web ./
RUN mkdir scripts
COPY ./scripts ./scripts

RUN chmod +x ./scripts/*

EXPOSE 8000

ENTRYPOINT ["sh", "./scripts/entrypoint.sh"]