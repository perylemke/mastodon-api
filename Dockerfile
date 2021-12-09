FROM python:3.8-slim

EXPOSE 8080

COPY ./mastodon_api mastodon_api/
COPY requirements.txt mastodon_api/

RUN pip install -r mastodon_api/requirements.txt

CMD ["uvicorn", "mastodon_api.app:app", "--host", "0.0.0.0", "--port", "8080"]