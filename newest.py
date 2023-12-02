from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import re
from datetime import datetime
import csv

# Initialize WebDriver
service = Service(executable_path='C:/chromedriver-win64/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

# Initialize lists to store data
titles = []
prices = []
authors = []
descriptions = []
dates = []
samples = []
words = []
languages = []
booktype = []



def scrapping(url):
    driver.get(url)
    sleep(5)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    for b in soup.findAll('div', attrs={'class': 'library-book row p-2'}):
        title = b.find("a", class_="library-title").text.strip()
        author_element = b.find("span", class_="library-by-line")
        author = author_element.find("a").text.strip()

        priceis = b.find('div', attrs={"class": "text col-md-10"})
        allspan = priceis.findAll('span')
        price = 0

        for x in allspan:
            if '$' in str(x.text):
                price = x.text.replace("$", "").split()[0]
                price = price.strip().replace(" ", "")
                print(price)
                break

        word = 0
        for x in allspan:
            if 'Words: ' in str(x.text):
                word = x.text.replace("Words: ", "")
                word = word.strip().replace(" ", "")
                break

        original_published_year = 0
        date = 0
        for x in allspan:
            if 'Originally Published:' in str(x.text):
                date = x.text.replace("Originally Published:", "")
                date = date.strip().replace(" ", "")
                date_object = datetime.strptime(date, "%B%d,%Y")
                original_published_year = date_object.year
                print(original_published_year)
                break
            elif 'Published:' in str(x.text):
                date = x.text.replace("Published:", "")
                date = date.strip().replace(" ", "")
                date_object = datetime.strptime(date, "%B%d,%Y")
                original_published_year = date_object.year
                print(original_published_year)
                break

        for x in allspan:
            if 'Language:' in str(x.text):
                language = x.text.replace('Language:', '')
                language = language.strip().replace(" ", "")
                print(language)
                break

        samples.append(0)
        fiction = b.find_all(style="white-space: nowrap;")
        last_element = fiction[-1].text.strip() if len(fiction) else None
        print(last_element)
        booktype.append(last_element) if last_element else booktype.append('nothing')
        languages.append(language) if language else languages.append('nothing')
        words.append(word) if word else words.append('0')
        dates.append(original_published_year) if isinstance(original_published_year, int) else dates.append('nothing')
        prices.append(price) if price is not None else prices.append('0')
        description = b.find("div", class_="card bg-light border-light p-2").text.strip()
        descriptions.append(description) if description else descriptions.append('nothing')
        authors.append(author) if author else authors.append('nothing')
        titles.append(title) if title else titles.append('nothing')


def main(run, resume, url, baseurl):
    urlofsubpage=url
    if  resume :
        
        if run :
            if urlofsubpage is  not None:
             with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsortedurl.txt', 'w', encoding='utf-8') as file:
                file.write(urlofsubpage)
                
            scrapping(url)

            sleep(1)
            try:
                next = driver.find_element(By.CLASS_NAME, 'page-link')
                print(len(titles), len(authors), len(prices), len(words), len(descriptions), len(samples), len(languages),
                      len(booktype), len(dates))

                for i in range(95020, 95120, 20):
                    print(resume)
                    urlofsubpage = baseurl + str(i)
                    if urlofsubpage is  not None:
                     with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsortedurl.txt', 'w', encoding='utf-8') as file:
                        file.write(urlofsubpage)
                
                    scrapping(urlofsubpage)
                    sleep(5)
                    print(urlofsubpage)

            except:
                savetofile()
                driver.quit()

        else:
            savetofile()

            driver.quit()
            

    else:
        
        savetofile()
        
        if urlofsubpage is  not None:
            with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsortedurl.txt', 'w', encoding='utf-8') as file:
                file.write(urlofsubpage)
                print('sdfhj')
            driver.quit()



def savetofile():
    df = pd.DataFrame({
        "name": titles,
        'Author': authors,
        'Price': prices,
        'Words': words,
        "Description": descriptions,
        'date': dates,
        "Language": languages,
        'category': booktype
    })

    # Save to CSV
    df.to_csv('C:\\Users\\hp\OneDrive\\Desktop\\resources\\smashwordsorted1.csv', index=False, encoding='utf-8',
              header=False, mode='a')



