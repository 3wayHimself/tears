import os
import json
from functools import partial
from bottle import Bottle
from bottle import jinja2_template
from bottle import TEMPLATE_PATH
from bottle import route, get, redirect, post, request, static_file, error, response
from bottle.ext.mongo import MongoPlugin
from bson.json_util import dumps
import pymongo
import markdown2

app = Bottle()


# Basedir
basedir = os.path.abspath(os.path.dirname(__file__))

# Template location
TEMPLATE_PATH.append(basedir + "/templates")

###############################################################################
# filters ######################################################################
###############################################################################


def datetime_to_date(datetime):
    return str(datetime)[:10]


def markdown(string):
    return markdown2.markdown(string, extras=["fenced-code-blocks"])


def generate_post_url():
    return

# Template filter and setting
template_settings = dict(filters={"datetime_to_date": datetime_to_date,
                                  "markdown": markdown})
template = partial(jinja2_template, template_settings=template_settings)

# Database
plugin = MongoPlugin(uri='mongodb://127.0.0.1', db='tears', json_mongo=True)
app.install(plugin)

client = pymongo.MongoClient("localhost", 27017)
db = client.tears


###############################################################################
# core #########################################################################
###############################################################################

@app.route('/static/<file_type>/<filename>')
def serve_static(file_type, filename):
    return static_file(filename, root=basedir + '/static/' + file_type)


@app.error(404)
def error404(error):
    return 'Nothing here, sorry'


@app.route('/')
@app.route('/index')
@app.route('/posts/<page_num:int>')
def index(page_num=1):
    post_list = []
    for p in db.posts.find().sort("date", -1):
        post_list.append(p)
    page_size = 5
    if len(post_list) % page_size == 0 and post_list:
        total = len(post_list) // page_size
    else:
        total = len(post_list) // page_size + 1
    print(total)
    final_list = post_list[(page_num - 1) * page_size: page_num * page_size]
    return template('index.html',
                    posts=final_list,
                    page_num=page_num,
                    total=total,
                    earlier=page_num + 1,
                    later=page_num - 1)


@app.route('/post/<year>/<month>/<day>/<name>')
def posts(year, month, day, name):
    pass


@app.route('/achieve')
def achieve():
    pass


@app.route('/tag/<tag_name>')
def tag(tag_name):
    pass


@app.route('/category/<category_name>')
def category(category_name):
    pass


if __name__ == '__main__':
    from bottle import run, debug

    # Active debug
    DEBUG = True
    debug(DEBUG)

    # Run WSGI web-server
    run(app, host='localhost', port=8080, reloader=DEBUG)
