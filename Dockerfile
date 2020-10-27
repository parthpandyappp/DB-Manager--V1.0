FROM ubuntu

RUN apt-get update
RUN apt-get install python -y

RUN apt-get install python3-pip -y
RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip

WORKDIR /app
COPY . /app

RUN pip3 install flask
RUN pip3 install Flask_SQLAlchemy

EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["app.py"]