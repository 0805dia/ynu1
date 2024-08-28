import requests
from bs4 import BeautifulSoup

def search_incruit(keyword,page):
    jobs = []
    for i in range(page):
        page = i * 30
        response= requests.get(
            f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}")

        soup = BeautifulSoup(response.text, "html.parser")

        lis = soup.find_all("li", class_="c_col")


        for li in lis:
            company = li.find("a",class_="cpname").text
            
            title = li.find("div", class_="cell_mid").find("a").text
            location = li.find("div" ,class_="cell_mid").find_all("span")[3].text
            link = li.find("div", class_="cell_mid").find("a").get("href")

            job_data = {

                "title":title,
                "company":company,
                "location":location,
                "link" : link
                }

            jobs.append(job_data)
        print(f"{i+1}번째 페이지를 스크롤링 완료하였습니다.")
    return jobs




def search_jobkorea(keyword,page):
    jobs =[]
    for i in range(page):
        page = i+1
        response = requests.get(
            f"https://www.jobkorea.co.kr/Search/?stext={keyword}&tabType=recruit&Page_No={page}")
        soup = BeautifulSoup(response.text, "html.parser")

        lis = soup.find_all("article", class_="list-item")


        for li in lis:
            try:
                title = li.find("div", class_="information-title").find("a").text.strip()
                company = li.find("div", class_ ="list-section-corp").find("a").text.strip()
                location = li.find_all("li",class_="chip-information-item")[3].text
                if location[0] == "D":
                    location = li.find_all("li",class_="chip-information-item")[2].text

                link = li.find("div", class_="information-title").find("a").get("href")
            

                job_data ={
                    "title" : title,
                    "company" : company,
                    "location" : location,
                    "link" : f"https://www.jobkorea.co.kr{link}"
                }
            
                jobs.append(job_data)
            except:
                pass
        
        print(f"{i+1}번째 페이지를 스크래핑 완료했습니다")
    return jobs








#git init    #처음할때
#git add .
#git commit -m "" 
#git remote add origin https://github.com/0805dia/ynu_scrapper.git    #처음할때
#git push origin master




                       

