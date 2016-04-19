# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext.nemo import Nemo
from capitains_nautilus.flask_ext import FlaskNautilus, WerkzeugCacheWrapper
from werkzeug.contrib.cache import FileSystemCache
from flask_cache import Cache
from lxml import etree
import os
     
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
    chunker={
        "default": Nemo.level_grouper
    },
    css=[
        "/code/static/assets/nemo.secondary/css/theme-ext.css"
    ],
    transform={
        "default": "/code/static/assets/xslt/epidocShort.xsl"
    }
)
# We register its routes
nemo.register_routes()
# We register its filters
nemo.register_filters()

app.debug = True
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

