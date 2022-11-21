FROM python:3.8y

ADD main.py .

RUN pip install requests beautifulsoup4

CMD ["python", "./main.py"]