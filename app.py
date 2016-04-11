# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext.nemo import Nemo
from capitains_nautilus.flask_ext import FlaskNautilus
from werkzeug.contrib.cache import FileSystemCache
from flask_cache import Cache

app = Flask("Nautilus")
nautilus_cache = FileSystemCache("/code/cache")
nautilus = FlaskNautilus(
    app=app,
    prefix="/api/cts",
    name="nautilus",
    resources=["/code/data/canonical-latinLit-master"],
    parser_cache=nautilus_cache,
    http_cache=Cache(config={'CACHE_TYPE': "simple"})
)
# We set up Nemo
nemo = Nemo(
    app=app,
    name="nemo",
	base_url="",
	api_url="/api/cts",
    endpoint=nautilus.endpoint
)
# We register its routes
nemo.register_routes()
# We register its filters
nemo.register_filters()

app.debug = True
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')