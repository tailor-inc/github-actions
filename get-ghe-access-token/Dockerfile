FROM python:3.9 AS deps

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]

