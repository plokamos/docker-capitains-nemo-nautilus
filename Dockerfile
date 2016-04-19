FROM debian:jessie
MAINTAINER ponteineptique <thibault.clerice[@]uni-leipzig.de>

RUN DEBIAN_FRONTEND=noninteractive apt-get update --fix-missing

# Install required packages
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
        git-core \
        zlib1g-dev \
        libxslt1-dev \
        libxml2-dev \
        python3 \
        python3-dev \
        python3-pip \
        build-essential \
        nginx \
        supervisor \
        unzip \
        nano \
        python-setuptools

# Sets up locales to avoid decode issue in python
ENV LANG C.UTF-8

# Clone required resources
run mkdir /var/log/gunicorn

WORKDIR /code/

# Required by supervisor which runs on python 2.7 apparently
RUN easy_install pip && pip2.7 install supervisor-stdout

# Stop supervisor service as we'll run it manually
RUN service supervisor stop
RUN service nginx stop

# Install our apps dependencies
RUN easy_install3 --upgrade pip
ADD ./requirements-py3.txt requirements-py3.txt
RUN pip3 install -r requirements-py3.txt

# Get the main app and configuration files
# File management (everything after an ADD is uncached) so we do it as late as possible in the process.
ADD ./supervisord.conf /etc/supervisord.conf
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./app.py ./app.py
ADD ./repositories /opt/data
ADD ./assets /code/static/assets

RUN cd /opt/data && unzip -q "*.zip"

# Expose right ports
EXPOSE 80

# start supervisor to run our wsgi server
CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]