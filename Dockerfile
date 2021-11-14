FROM python:3.9
LABEL maintainer = "kevinha298"

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
COPY ./djangoapp /djangoapp

WORKDIR /djangoapp
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home appuser

ENV PATH="/py/bin:$PATH"

USER appuser


