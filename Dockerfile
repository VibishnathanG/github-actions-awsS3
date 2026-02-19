FROM python:3

COPY requirements.txt /requirements.txt

COPY Deployment.py /Deployment.py

RUN pip install -r /requirements.txt

CMD ["python3", "/Deployment.py"]