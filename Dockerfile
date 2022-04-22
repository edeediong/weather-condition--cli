FROM python:3.7.13-slim

WORKDIR /src/app

COPY main.py main.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV WEATHER_API_KEY WEATHER_API_KEY

ENTRYPOINT ["python", "main.py"]
