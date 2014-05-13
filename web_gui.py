from bottle import route, install, run, get, post, request, template, static_file
from bottle_sqlite import SQLitePlugin
from file_reader import InputFileReader
from ShortestPath import ShortestPath
from my_exceptions import * 

install(SQLitePlugin(dbfile='db/biicode.sqlite'))

@route('/about')
def about():
    return "BiiCode Assessment App"

@get('/test')
def test(db):
    cities = db.execute('SELECT Name,x,y from City').fetchall()
    roads = db.execute('SELECT source,dest from Road').fetchall()
    return template('templates/search.tpl', cities = cities, roads = roads)

@get('/boot-strap')
def boot_strap(db):
    cities = db.execute('SELECT Name,x,y from City').fetchall()
    roads = db.execute('SELECT source,dest from Road').fetchall()
    return template('templates/search-bootstrap.tpl', cities=cities, roads=roads)

@post('/test')
def parse_test(db):
    orig = request.forms.get('orig')
    dest = request.forms.get('dest')

    finput, cities = InputFileReader().read()
    cities = db.execute('SELECT Name,x,y from City').fetchall()
    roads = db.execute('SELECT source,dest from Road').fetchall()
    try:
        path, distance = ShortestPath().find(finput, s=orig, t=dest)
    except PathNotFoundException:
        return template('templates/results_notfound.tpl', orig = orig, dest = dest)

    #return "<p>Orig: %s, Dest: %s, Path: %s " % (orig, dest, path)
    return template('templates/results.tpl', orig = orig, dest = dest, dist = distance, path = path, cities = cities, roads = roads)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/home/nacho/git/biicode/templates')

run(host='localhost', port=8000, debug=True)