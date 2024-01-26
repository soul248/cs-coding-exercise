FROM python:3.12
WORKDIR /app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5108
RUN apt-get update
RUN apt-get install -y default-mysql-client
RUN apt-get clean autoclean
RUN apt-get autoremove --yes
RUN rm -rf /var/lib/apt/lists/*

# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app ./app
COPY config.py ./config.py

CMD ["sh", "-c", "/wait ; flask run"]