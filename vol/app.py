from flask import Flask
from flask.templating import render_template
import scraping as scrap
import os
import json
app = Flask(__name__)
@app.route('/')
def index():
    #スクレイピングサンプル
    s = scrap.Scraping()
    data =s.collectData()

    #cronサンプル
    f = open('sample.text')
    x =f.read()
    f.close()
    x = x + "a"
    f = open('sample.text','w')
    f.writelines(x)
    f.close()
    f = open('sample.text')
    text =f.read()
    f.close()
    html = render_template('index.html',a=data,b=text)
    return html


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)


    