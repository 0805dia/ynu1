from flask import Flask, render_template , request , redirect , send_file    #파이썬 플라스크 공식 홈페이지 공식 그대로 복붙
from scrapper import search_incruit , search_jobkorea
from file import save_to_csv

app = Flask(__name__)
page =1
db = {}

@app.route('/')  
def home():
    return render_template("home.html")     #바꾸면 새롭게 들어가야함 터미널에서 ctrl +c 하고 다시


#search 페이지 만들기
@app.route('/search')        # ㄴ반드시 templates 폴더 안에 있어야 작동 
def search():
    keyword = request.args.get("keyword")  #주소창에 있는 키워드 값만 뺴오는것

    # db = {
    # "회계" : [1,2,3,4]
    # "파이썬":[1,2,3,4]
    # }
    
    if keyword in db:
        jobs = db[keyword]                   #키워드가 회계라면 db 에 있기에 그냥 나옴
    else:
        jobs_incruit = search_incruit(keyword,page)
        jobs_jobkorea = search_jobkorea(keyword,page)
        jobs = jobs_incruit + jobs_jobkorea      #키워드가 의사라면 db에 없기에 크롤링
        db[keyword] = jobs                    
        #db["의사"] = [1,2,3,...100]   

    return render_template(
        "search.html",
         keyword=keyword, 
        jobs=enumerate(jobs),
        counts=len(jobs))
# db = {
#     "파이썬": [1, 2, 3, 4, .... 500], 
#     "간호사" : [1, 2, 3, ... 500] 
# }
# db["파이썬"]

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    print(keyword)
    
    if keyword == "":
        return redirect("/")    #redirect는 강제적으로 이동시키는 것
    
    if keyword not in db:
        return redirect("/")
    
    save_to_csv(db[keyword])
    
    return send_file("./to_save.csv", as_attachment=True)


if __name__ == '__main__':
    app.run()   #debug=True 개발자 모드 => 자동으로 서버가 저장