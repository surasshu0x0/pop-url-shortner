from bottle import (
        run, template, get, route,
        request, response, redirect,
        )
import sqlite3
from shortid import ShortId

sid = ShortId()

@get('/')
def index():
    'show all shortened urls and shortner form'
    
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * from url')
    results = c.fetchall()
    c.close()
    
    return template('index', rows=results)

@route('/new-url', method=['GET', 'POST'])
def new_url():
    'create new url'
    
    if request.POST:    
        url = request.forms.get('url')
        shortId = sid.generate()

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('INSERT INTO url (url, shortId) VALUES (?, ?)', (url, shortId))
        conn.commit()
        c.close()

        return redirect('/')
    else:
        return template('new_url')


@route('/<shortid>', method=['GET'])
def redirect_link(shortid):
    'redirect to actual link'
    
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT url  FROM url WHERE shortId='%s'" % shortid)
    url = c.fetchone()
    c.close()
    if url:
        return redirect(url[0])
    else:
        return '<p>Invalid link</p>'

run(debug=True, reloader=True)
