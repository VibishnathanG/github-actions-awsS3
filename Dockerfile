FROM python:3

COPY requirements.txt /requirements.txt

COPY deployment.py /deployment.py

RUN pip install -r /requirements.txt

CMD ["python3", "/deployment.py"]