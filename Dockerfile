FROM python:3.12

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN addgroup --system app && adduser --system --group app

COPY ./src/app /code/app
