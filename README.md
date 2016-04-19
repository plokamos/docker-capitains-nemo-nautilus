# docker-debian-capitains

CapiTainS suite docker image
============================

This repository contains resource to run CapiTainS web services and frontend using docker, which means you'll only need to perform few commands to install these resources. Good bye Python issues, Gunicorn and Apache headache, welcome Docker !

## Docker basics

- **Build the image**

	- User `docker build .` in this directory. Do not forget to put your github zip download in repositories folder (You can modify and run `download-perseus-csel.sh`)

- **Useful links**

	- Use a shared folder for repositories [ https://docs.docker.com/engine/userguide/containers/dockervolumes/#mount-a-host-directory-as-a-data-volume ]