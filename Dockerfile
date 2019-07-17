FROM python:3.7.3-alpine

EXPOSE 5000
WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE=1 

ADD requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

RUN addgroup -g 1001 app && \
    adduser -D -u 1001 -G app app

USER app
