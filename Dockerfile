FROM python:3.11-slim
WORKDIR /code
COPY . /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["main.py"]