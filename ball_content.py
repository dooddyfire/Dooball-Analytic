import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#from linkedin_scraper import Person, actions
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


output_filename = input("ชื่อไฟล์ : ")
#search_scroll = int(input("ช่วงการเลื่อนเมาส์ : "))
main_url = "https://www.goal.co/%E0%B8%A7%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B2%E0%B8%B0%E0%B8%AB%E0%B9%8C%E0%B8%9A%E0%B8%AD%E0%B8%A5%E0%B8%84%E0%B8%B7%E0%B8%99%E0%B8%99%E0%B8%B5%E0%B9%89/"
print(main_url)

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(main_url)

soup = BeautifulSoup(driver.page_source,'html.parser')


content_lis = []

post_lis =  [url.find('a')['href'] for url in soup.find_all('div',{'class':'topicboard'})]
title_lis =  [url.find('a').text for url in soup.find_all('div',{'class':'topicboard'})]

print(post_lis)
for url in post_lis: 
    try:
        driver.get(url)
        content = driver.find_element(By.CSS_SELECTOR,'div.topic-content').get_attribute('innerHTML')
        content_lis.append(content)


        print("---------------------------------")
    except: 
        continue


df = pd.DataFrame()
df['ชื่อบทความ'] = title_lis[:len(content_lis)]
df['ข้อมูล'] = content_lis
df['ลิงค์'] = post_lis[:len(content_lis)]


df.to_excel("{}.xlsx".format(output_filename))
df.to_csv("{}.csv".format(output_filename))

print("Done")