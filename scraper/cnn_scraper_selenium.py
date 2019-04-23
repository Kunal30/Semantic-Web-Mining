from selenium import webdriver
from bs4 import BeautifulSoup
import json, requests, pickle

def scrape_section(source, type_of_article):    
    if type_of_article == '/style/':
        target = source.find('div', class_='BasicArticle__main')
        if target is None:
            target = source.find('div', class_='SpecialArticle__body')
        targets = list(target)
    elif type_of_article == '/travel/':
        targets = list(source.find('div', class_='Article__body'))
    else:
        targets = source.find_all('section', id="body-text")

    for target in targets:
        ## delete scripts and ads
        while True:
            try:
                target.find('script').decompose()
            except:
                break
        
        while True:
            try:
                target.find('style').decompose()
            except:
                break
        
        while True:
            try:
                target.find('div', class_="ad").decompose()
            except:
                break
        
        text = target.text
        text = text.replace('"', "").replace("'", "")
    
    return text
    

def scrape_cnn():
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

    skiplist = ['/videos/', 'bleacherreport.com', '/interactive/']
    typelist = ['/style/', '/travel/']

    dataset = []
    datasetText = []
    for each in headlines_list:
        try:
            title = each.select_one("span").text
            obj = {
                'title': title,
                'link': each.select_one("a").get('href')
            }

            ## get link
            news_link = each.select_one("a").get('href')
            if any(skipItem in news_link for skipItem in skiplist):
                continue
            
            type_of_article = 'normal'
            for typeItem in typelist:
                if typeItem in news_link:
                    type_of_article = typeItem

            if (news_link.startswith('/')):
                news_link = url + news_link

            page = requests.get(news_link)
            page_source = page.text

            ## parse inner page
            article_page = BeautifulSoup(page_source, 'lxml')            
            text = scrape_section(article_page, type_of_article)

            ## save data
            obj['text'] = text
            datasetText.append(title + ' ' + text)
            dataset.append(obj)
        except Exception as ex: 
            print ("Error parsing:", ex, '||', title, news_link)
            continue

        print ("({}) Parsed news with headline:- [{}]".format(len(dataset), each.select_one("span").text))


    ## write to file
    with open("cnn_out.json", 'w') as outfile:  
        json.dump(dataset, outfile)

    with open('cnn_text.pickle', 'wb') as outfile:
        pickle.dump(datasetText, outfile, protocol=2)

## import cnn_scraper_selenium and/or uncomment the below code to run the scraper
#scrape_cnn()