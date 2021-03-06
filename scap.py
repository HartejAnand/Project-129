from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time;  import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

headers = ["Name","Distance","Mass","Radius"]
star_data=[]
new_star_data=[]

def scrap():
    for i in range(1,489):
        time.sleep(2)
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","browndrawf"}):
            li_tags = ul_tag.find_all("li")
            temp_list=[]
            for index, li_tag in enumerate (li_tags): 
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try: 
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag=li_tags[0]
            temp_list.append("https://en.wikipedia.org/"+hyperlink_li_tag.find_all("a", href=True)[0]["href"])
            
            star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        
        with open("scrapper.csv", "w") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(star_data)

def scrap_more_data(hyperlink):
    try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,"html.parser")
        for tr_tag in soup.find_all("tr", attrs={"class":"fact_row"}):
            td_tags=tr_tag.find_all("td")
            temp_list=[]
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_star_data.append(temp_list)
    except:
        time.sleep(1)
        scrap_more_data(hyperlink)

scrap()

for data in star_data:
    scrap_more_data(data[5])


final_star_data=[]
for index,data in enumerate(star_data):
    final_star_data.append(data+final_star_data[index])

with open("data.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final_star_data)