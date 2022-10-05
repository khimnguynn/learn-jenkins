FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN pip3 install flask

EXPOSE 8080

ENTRYPOINT ["python3", "app.py"]