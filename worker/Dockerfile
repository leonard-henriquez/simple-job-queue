FROM python:3.7-alpine3.9

WORKDIR /
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

ADD . /worker
CMD ["celery", "-A", "worker.worker", "worker", "--queues=worker_queue", "--loglevel=info"]
