CapiTainS suite docker image
============================

[![Docker Stars](https://img.shields.io/docker/stars/capitains/nemo-nautilus.svg?maxAge=86400)](https://hub.docker.com/r/capitains/nemo-nautilus/tags/) 
[![Docker Pulls](https://img.shields.io/docker/pulls/capitains/nemo-nautilus.svg?maxAge=86400)](https://hub.docker.com/r/capitains/nemo-nautilus/tags/)


This repository contains resource to run CapiTainS web services and frontend using docker, which means you'll only need to perform few commands to install these resources. Good bye Python issues, Gunicorn and Apache headache, welcome Docker !

## Docker basics

- **Build the image**

	- User `docker build .` in this directory

- **Creating a container**
	
	If you used a local build, *save the hash* given at the end of the build (such as `475d347abade`). Of course, replace /path/to/ by your own absolute path to given directory.
	
	- If you do not have any resources, we advice to run locally the following commands :
		- `sh download-perseus-csel.sh` will download zipped repositories of Perseus Greek and Latin litterature and the CSEL repository of the Open Greek and Latin project
		- `sh unzip-corpora-local-volume` will unzip downloaded repositories in the repository folder.
	- `docker run -i -p 8080:80 --name capitains -v /path/to/volumes/repositories:/opt/data -v /path/to/volumes/cache:/opt/cache capitains/nemo-nautilus:latest` will run and pull the docker instance
		- Replacing `-i` by `-d` will run docker as a daemon. Instead of seeing the log as an interactive application, the docker instance will be run locally
		- `-p 8080:80` tunnels the host machine `8080` port to `80` port on the docker container.
		- `-v /first/path:/second/path` creates a data volumes and forwards `/first/path` (on your machine) to `/second/path` (on the docker container). We used it for cache and repositories so that maintenance and evolution is easily done outside containers. It also enables data volume sharing for multiple containers.
		- `--name capitains` names your container capitains. If you want to have multiple containers, change the name.