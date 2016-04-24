from flask_nemo import Nemo

nemo_config = {
    "chunker": {
        "default": Nemo.level_grouper
    },
    "css": [
        "/code/static/assets/nemo.secondary/css/theme-ext.css"
    ],
    "transform": {
        "default": "/code/static/assets/xslt/epidocShort.xsl"
    }
}