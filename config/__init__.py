from flask_nemo import Nemo
from flask_nemo.chunker import level_grouper

nemo_config = {
    "chunker": {
        "default": level_grouper
    },
    "css": [
        "/code/static/assets/nemo.secondary/css/theme-ext.css"
    ],
    "transform": {
        "default": "/code/static/assets/xslt/epidocShort.xsl"
    }
}
