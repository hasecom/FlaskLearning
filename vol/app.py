from flask import Flask
from flask.templating import render_template
import scraping as scrap
import cron
import os
import json
app = Flask(__name__)
@app.route('/')
def index():
    #スクレイピングサンプル
    s = scrap.Scraping()
    data =s.collectData()

    #cronサンプル
    c = cron.cron()
    text = c.limp()
    html = render_template('index.html',a=data,b=text)
    return html


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)


    