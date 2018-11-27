import os
from flask import Flask, render_template, request
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)


def mdrendered(form):
    return [{
        "left": "AAA side 1",
        "right": "gabbeligab",
        "longtext":"<h1>This is a heading</h1>"
        }]

@app.route('/', methods=["GET","POST"])
def index():
    template = jinja_env.get_template('index.html')
    form = dict((k.strip(), v.strip()) for k,v in request.form.items())
    return template.render(
        rendered = mdrendered(form),
        **form
    )    
