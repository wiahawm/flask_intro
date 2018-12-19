from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>서버가 html도 보내주나??</h1>"
    
@app.route("/html_tag")
def html_tag():
    return """
    <h1>첫번째 줄</h1>
    <h2>두번째 줄</h2>
    """
    
@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html", people=name)
    
@app.route("/cube/<int:num>")
def cube(num):
    return render_template("cube.html", result=num**3, num=num)
    
@app.route('/lunch')
def lunch():
    #요부분에 점심메뉴를 추천해주는 코드를 작성!
    menu = ["김치찌개","계란말이","피자","떡볶이","볶음밥","알탕"]
    pick = random.choice(menu)
    return render_template("lunch.html", menu=pick)
    
@app.route('/lotto')
def lotto():
    numbers=list(range(1,51))
    number=random.sample(numbers,6)
    number.sort()
    return render_template("lotto.html",number=number)
    
@app.route('/naver')
def naver():
    return render_template("naver.html")