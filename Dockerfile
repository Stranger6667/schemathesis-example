FROM python:3.8

EXPOSE 5000

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .
COPY app/ /app

CMD [ "python", "main.py" ]
