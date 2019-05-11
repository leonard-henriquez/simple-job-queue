# Simple Job Queue ![language](https://img.shields.io/badge/language-Python-blue.svg)

> A simple system to run jobs in Python in containers

Technologies:

- Python 3.7
- Celery 3.1.1
- RabbitMQ
- Flower
- Docker & docker compose

## :books: Table of Contents

- [Installation](#package-installation)
- [Usage](#rocket-usage)
- [Support](#hammer_and_wrench-support)
- [Contributing](#memo-contributing)

## :package: Installation

Clone repo

```sh
git clone https://github.com/leonard-henriquez/simple-job-queue
```

Make sure you have [Docker Compose](https://docs.docker.com/compose/) installed on your computer

## :rocket: Usage

Start the job queue system (RabbitMQ) with:

```sh
docker-compose up
```

Then [open the web UI](http://localhost:5555/) (Flower) to monitor the system

Finally add new jobs to the queue:

```sh
# First tell indicate where is the broker
export CELERY_BROKER_URL=amqp://admin:mypass@127.0.0.1:5672
export CELERY_RESULT_BACKEND=amqp://admin:mypass@127.0.0.1:5672
# Then launch tasks
python launch_tasks.py
```

## :hammer_and_wrench: Support

Please [open an issue](https://github.com/leonard-henriquez/simple-job-queue/issues/new) for support.

## :memo: Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/leonard-henriquez/simple-job-queue/compare/).
