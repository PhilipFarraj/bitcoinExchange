FROM python:3.6
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
COPY . /usr/src/app
RUN pip install -r requirements.txt