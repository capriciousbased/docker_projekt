FROM python:3.11.0a6-alpine3.15
WORKDIR /app
COPY requirments.txt /app
RUN pip install -r requirments.txt --no-cache-dir
COPY . /app

CMD ["python", "./main.py"]