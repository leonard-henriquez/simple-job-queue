FROM python:3.7

WORKDIR /
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

ADD ./app /app
CMD ["celery", "-A", "app.worker", "worker", "--loglevel=info"]
