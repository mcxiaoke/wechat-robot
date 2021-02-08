FROM python:3.9-slim-buster
ADD ./ /app
WORKDIR /app
#RUN pip install -U pip
#RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
#RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
# CMD ["python3", "app.py"]
CMD ["gunicorn", "-b", "0.0.0.0:8001", "app"]
