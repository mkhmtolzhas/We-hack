import requests 
from bs4 import BeautifulSoup 
import json 
HOST = "https://egov.kz/" 
URL = "https://egov.kz/cms/ru" 
HEADERS = { 
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", 
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" 
} 
def get_html(url): 
    request = requests.get(url, headers=HEADERS) 
    return request 
 
def get_content(html): 
    soup = BeautifulSoup(html, 'html.parser') 
    items = soup.find_all("li", class_='') 
    articles = [] 
    count = 0
    for item in items:
        try:
            count+=1
            if count > 17:
                articles.append( 
                    { 
                        #"title" : item.find("span", class_="content_main_item_title").find('a').get_text(strip = True), 
                        "link" : item.find("a").get("href"), 
                        "servise" : item.find("a").get_text(strip=True) 
                        #"image" : item.find("a").find("picture").find("img").get("src") 
                    } 
                ) 
        except: 
            pass 
    return articles 
 
 
def parser(): 
    html = get_html(url=URL) 
    articles = get_content(html.text) 
    with open("./any-article.json", "w") as file: 
        json.dump(articles, file, indent=4, ensure_ascii=False) 
 
if __name__ == "__main__": 
    parser()
