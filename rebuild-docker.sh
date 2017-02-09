#!/bin/sh
if [[ -d nemo_plokamos_plugin || -L nemo_plokamos_plugin ]]; then
	if [[  -f plokamos_keys.sh ]]; then
		source ./plokamos_keys.sh
		docker rm capitains
		docker rmi nemo:latest
		docker build . -t nemo:latest
		docker run -i -p 8443:443 --name capitains \
		-v $NEMO_DATA:/opt/data \
		-v $NEMO_CACHE:/opt/cache \
		-v $NEMO_ASSETS:/code/nemo_plokamos_plugin/nemo_plokamos_plugin/data/assets \
		-e PERSEIDS_API_KEY=$PERSEIDS_API_KEY \
		-e PERSEIDS_API_SECRET=$PERSEIDS_API_SECRET \
		-e APP_SECRET_KEY=$APP_SECRET_KEY \
		 -e SPARQL_UPDATE_ENDPOINT=$SPARQL_UPDATE_ENDPOINT \
		 -e SPARQL_SELECT_ENDPOINT=$SPARQL_SELECT_ENDPOINT \
		nemo:latest
	else
		echo "Plokamos API keys missing [plokamos_keys.sh]."
	fi
else
	echo "nemo_plokamos_plugin is missing, clone from Github and build."
fi
