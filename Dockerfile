FROM python:3.7-alpine
LABEL maintainer="docker@mcxiaoke.com"

ADD . /opt/wechat-robot
WORKDIR /opt/wechat-robot

RUN pip install -r requirements.txt

# Start the application with gunicorn
CMD gunicorn -w 4 -b 0.0.0.0:8000 app:app