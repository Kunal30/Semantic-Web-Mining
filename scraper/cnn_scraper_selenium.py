from selenium import webdriver
from bs4 import BeautifulSoup
import json, requests

## start url
url = "https://cnn.com"

## create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

## get page
home_page = BeautifulSoup(driver.page_source, 'lxml')

## get all headlines
headlines_list = home_page.find_all('h3', class_="cd__headline")
print ('Total headlines found:', len(headlines_list))

driver.quit()

dataset = []
for each in headlines_list:
    try:
        obj = {
            'title': each.select_one("span").text,
            'link': each.select_one("a").get('href')
        }

        ## get each link
        news_link = each.select_one("a").get('href')
        if (news_link.startswith('/')):
            news_link = url + news_link
        page = requests.get(news_link)
        page_source = page.text

        ## parse inner page
        article_page = BeautifulSoup(page_source, 'lxml')
        
        targets = article_page.find_all('section', id="body-text")
        for target in targets:
            ## delete scripts and ads
            while True:
                try:
                    target.find('script').decompose()
                except:
                    break
            
            while True:
                try:
                    target.find('div', class_="ad").decompose()
                except:
                    break
            
            text = target.text
            text = text.replace('"', "").replace("'", "")
            obj['text'] = text

        ## save data
        dataset.append(obj)
    except Exception as ex: 
        print ("Error parsing:", ex)
        continue

    print ("({}) Parsed news with headline:- [{}]".format(len(dataset), each.select_one("span").text))


#write to file
with open("cnn_out.json", 'w') as outfile:  
    json.dump(dataset, outfile)
