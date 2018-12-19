from flask import Flask, render_template
import requests
import time 
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    print("nice")
    return "hello world"
    
@app.route('/naver_toon')
def naver_toon():
    today = time.strftime("%a").lower()
    url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' + today
    response = requests.get(url).text
    soup = bs(response, 'html.parser')

    toons = []
    li = soup.select('.img_list li')
    for item in li:
      toon = {
        "title" : item.select_one('dt a').text, 
        "url" : 'https://comic.naver.com' + item.select('dt a')[0]["href"],
        "img_url" : item.select('.thumb img')[0]["src"]
      }
      toons.append(toon)
      
    return render_template('naver_toon.html', t = toons)

@app.route('/daum_toon')
def daum_toon():
    return render_template('naver_toon.html')