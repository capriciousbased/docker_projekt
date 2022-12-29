FROM python:3.11
WORKDIR /app
COPY requirments.txt /app
RUN pip install -r requests.txt
COPY . /app

CMD ["python", "./main.py"]