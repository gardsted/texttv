"""
# This is a texttv application

It can just do one thing - write monospace text with a few colors in the tables below.

It will split the text at seemingly random places, unless You decide to force it, in which case You can insert 
  @NEWLINE at on the blank line You want to be converted to a newline.

@NEWLINE

## This is the first heading after one of these

It will be converted to html, but all pre-eisting html-tags will be stripped



"""
from html.parser import HTMLParser
import os
from flask import Flask, request, send_from_directory
import jinja2
import markdown

NUMCHARS = 800
WIDTH=800
FONTSIZE=115


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)


class MLStripper(HTMLParser):
    def __init__(self, html):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []
        self.feed(html)

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def mustchange(lines, index, charcount):
    if lines[index + 1].startswith("@NEWLINE"):
        return True

    if lines[index + 1].startswith("#"):
        if charcount > NUMCHARS*.8:
            return True
        return False
    else:
        if charcount > NUMCHARS*1.2:
            return True
        return False


def mdrendered(left="", right="", longtext="", **other):
    longtext += "\n\n\n\n\n\n\n"
    results = []
    lines = longtext.splitlines()
    charcount = 0
    result = {"lines": []}
    for index, line in enumerate(lines[:-6]):
        if not line.startswith("@NEWLINE"):
            result["lines"].append(line)
        charcount += len(line)
        if mustchange(lines, index, charcount):
            charcount = 0
            results.append(result)
            result = {"lines": []}

    if result["lines"]:
        results.append(result)

    for index, result in enumerate(results):
        result["left"] = left.replace("#/#", "%d/%d" % (index+1, len(results)))
        result["right"] = right
        result["html"] = markdown.markdown(
            "\n".join(result.pop("lines")).strip()
        )
    return results


@app.route('/', methods=["GET", "POST"])
def index():
    template = jinja_env.get_template('index.html')
    form = dict(
        (k.strip(), MLStripper(v.strip()).get_data())
        for k, v in request.args.items()
        if k in ["left", "right", "longtext"])
    form["left"] = form.get("left", "")[:25]
    form["right"] = form.get("right", "")[-25:]
    form["width"] = WIDTH
    form["fontsize"] = FONTSIZE
    return template.render(
        rendered=mdrendered(**form),
        **form
    )

@app.route('/meme/', methods=["GET", "POST"])
def meme():
    template = jinja_env.get_template('meme.html')
    form = dict(
        (k.strip(), v.strip())
        for k, v in request.args.items()
        if k in ["img"])
    return template.render(
        rendered=mdrendered(**form),
        **form
    )


if __name__ == '__main__':
    import pprint
    pprint.pprint(mdrendered(
        left="side #/#",
        right="",
        longtext=__doc__
    ))
