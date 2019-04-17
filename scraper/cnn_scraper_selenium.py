from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os, json

## start url
url = "https://cnn.com"

## create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

## get page
soup_level1=BeautifulSoup(driver.page_source, 'lxml')

## get all headlines
headlines_class = soup_level1.find_all('h3', class_="cd__headline")
print ('Total headlines found:', len(headlines_class))

dataset = []
for each in headlines_class:
    try:
        obj = {
            'title': each.select_one("span").text,
            'link': each.select_one("a").get('href')
        }

        ## click on link
        # link = each.select_one("a").getAttribute('href')
        # link = each.find_element_by_tag_name('a')
        # link.click()
        driver.get(url + each.select_one("a").get('href'))

        ## parse inner page
        soup_level2=BeautifulSoup(driver.page_source, 'lxml')
        
        targets = soup_level2.find_all('section', id="body-text")
        for target in targets:
            text = target.text
            text = text.replace('"', "").replace("'", "")
            obj['text'] = text
        
        
        ## go back to homepage
        #driver.execute_script("window.history.go(-1)") 
        driver.get(url)

        ## save data
        dataset.append(obj)
    except Exception as ex: 
        print ("Error parsing:", ex)
        continue

    print ("({}) Parsed news with headline:- [{}]".format(len(dataset), each.select_one("span").text))


driver.quit()

#write to file
with open("cnn_out.json", 'w') as outfile:  
    json.dump(dataset, outfile)
