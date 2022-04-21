FROM python:3.8-slim-buster

run mkdir -p /webApp/
WORKDIR /webApp

COPY web.py web.py
COPY index index
COPY index/index.html index/index.html

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install flask

CMD [ "python3", "web.py" ]
