FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install package dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        alsa-utils \
        libsndfile1-dev && \
    apt-get clean

WORKDIR /code
COPY . .
RUN ln -s /usr/local/bin/python3 /usr/bin/python3 && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["python3", "main.py"]