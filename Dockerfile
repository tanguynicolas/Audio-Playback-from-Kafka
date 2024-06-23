FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Install package dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        alsa-base \
        alsa-utils \
        libsndfile1-dev && \
    apt-get clean

WORKDIR /code
COPY . .
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["python3", "main.py"]