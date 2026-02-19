FROM python:3

COPY requirements.txt /requirements.txt

COPY deployment.py /deployment.py

pip install -r /requirements.txt

CMD ["python3", "/deployment.py"]