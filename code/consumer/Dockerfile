FROM python:3.8

#RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /home/invest_bot

COPY code/consumer/* consumer/

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD python consumer/run.py