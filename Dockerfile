FROM frolvlad/alpine-python3
MAINTAINER ponteineptique <thibault.clerice[@]uni-leipzig.de>

# Install required packages
RUN apk add --no-cache \
        python3-dev python py-pip nginx supervisor \
        gcc linux-headers libxml2 libxml2-dev libxslt libxslt-dev musl musl-dev

# Sets up locales to avoid decode issue in python
ENV LANG C.UTF-8

WORKDIR /code/

# Required by supervisor which runs on python 2.7 apparently
RUN pip2.7 install supervisor-stdout

# Install our apps dependencies
ADD ./requirements-py3.txt requirements-py3.txt
RUN pip3 install -r requirements-py3.txt

# Get the main app and configuration files
# File management (everything after an ADD is uncached) so we do it as late as possible in the process.
ADD ./supervisord.conf /etc/supervisord.conf
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./app.py ./app.py
ADD ./assets /code/static/assets

# Expose right ports
EXPOSE 80

# start supervisor to run our wsgi server
CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]