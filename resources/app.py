# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext.nemo import Nemo
from capitains_nautilus.flask_ext import FlaskNautilus, WerkzeugCacheWrapper
from werkzeug.contrib.cache import FileSystemCache
from flask_cache import Cache
from lxml import etree
import os
from config import nemo_config

from nemo_oauth_plugin import NemoOauthPlugin
from nemo_plokamos_plugin import PlokamosPlugin
from pkg_resources import resource_filename

perseids_api_key=os.environ.get('PERSEIDS_API_KEY')
perseids_api_secret=os.environ.get('PERSEIDS_API_SECRET')
base_url='https://sosol.perseids.org/sosol/api/v1/'
access_token_url='https://sosol.perseids.org/sosol/oauth/token'
authorize_url='https://sosol.perseids.org/sosol/oauth/authorize'
sparql_select=os.environ.get('SPARQL_SELECT_ENDPOINT')
sparql_update=os.environ.get('SPARQL_UPDATE_ENDPOINT')

d = "/opt/data"
app = Flask("Nautilus")
nautilus_cache = FileSystemCache("/opt/cache")
nautilus = FlaskNautilus(
    app=app,
    prefix="/api/cts",
    name="nautilus",
    resources=[os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))],
    parser_cache=WerkzeugCacheWrapper(nautilus_cache),
    http_cache=Cache(config={'CACHE_TYPE': "simple"})
)

# We set up Nemo
nemo = Nemo(
    app=app,
    name="nemo",
    base_url="",
    api_url="/api/cts",
    retriever=nautilus.retriever,
    plugins=[NemoOauthPlugin(app,name='perseids',oauth_access_token_url=access_token_url,oauth_authorize_url=authorize_url,
                oauth_base_api_url=base_url,oauth_callback_url='https://localhost/apps/oauth/authorized',
                oauth_key=perseids_api_key,oauth_scope='read',oauth_secret=perseids_api_secret),
                PlokamosPlugin(sparql_update,sparql_select,app)],
    **nemo_config
)
# We register its routes
#nemo.register_routes()
# We register its filters
#nemo.register_filters()

app.debug = True
app.secret_key = os.environ.get('APP_SECRET_KEY')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
