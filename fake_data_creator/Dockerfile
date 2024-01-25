FROM python:3.12

WORKDIR /script
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY fake_sql_creator.py .

CMD ["sh", "-c", "python fake_sql_creator.py"]