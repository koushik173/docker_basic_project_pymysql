FROM python:3.11-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","python_msql.py"]

