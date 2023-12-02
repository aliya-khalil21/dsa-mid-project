# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import re

# Initialize WebDriver
service = Service(executable_path='C:/chromedriver-win64/chromedriver.exe')
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)


def scrapping(url):
    driver.get(url)
    sleep(5)
    page_source = driver.page_source
    
    soup = BeautifulSoup(page_source, 'html.parser')
    descriptionbutton = driver.find_element(By.CLASS_NAME, 'icon-th-list')
    descriptionbutton.click()
    sleep(5)
    page_source_after_clickis = driver.page_source
    soup_after_clickis = BeautifulSoup(page_source_after_clickis, 'html.parser')

    # Iterate through each book entry
    for b in soup_after_clickis.findAll('div', attrs={'class': 'row library-book'}):
        
        author = b.find("span", class_="library-by-line").text.strip().replace("by", "")
        title = b.find("span", class_="library-title").text.strip()

        priceis = b.find('div', attrs={"class": "col-sm-10"})
        allspan = priceis.findAll('span')
        price = 0
        for x in allspan:
            if str(x.text).__contains__('$'):
                price = x.text.replace("$", "")
                print(price)
                break
        for x in allspan:
            if str(x.text).__contains__('Words: '):
                word = x.text.replace("Words: ", "")
                break
        for x in allspan:
            if str(x.text).__contains__('Published on '):
                date = x.text.replace("Published on ", "")
                break
        for x in allspan:
            if str(x.text).__contains__('Language:'):
                language = x.text.replace('Language:', '')
                print(x.text.replace('Language:', ''))
                break

        sample = b.find('div', attrs={"class": "p-2 border-light"})
        spanofsample = sample.findAll('span')

        for x in spanofsample[:1]:
            if '% Sample:' in str(x.text):
                print(x.text)
                numeric_value = re.search(r'\d+', x.text)

                if numeric_value:
                    samples.append(numeric_value.group())
                    print(numeric_value.group())
                else:
                    samples.append('nothing')
            else:
                samples.append('nothing')

            break

        fiction = b.find_all(class_='text-nowrap')
        last_element = fiction[-1].text.strip()
        booktype.append(last_element) if last_element else booktype.append('nothing')

        languages.append(language) if language else languages.append('nothing')
        words.append(word) if word else words.append('nothing')
        dates.append(date) if date else dates.append('nothing')
        prices.append(price) if price is not None else prices.append('nothing')
        description = b.find("div", class_="card bg-light border-light p-2").text.strip()
        descriptions.append(description) if description else descriptions.append('nothing')
        authors.append(author) if author else authors.append('nothing')
        titles.append(title) if title else titles.append('nothing')
        print(len(titles), len(authors), len(prices), len(words), len(descriptions), len(samples), len(languages),
              len(booktype), len(dates))

# Initialize a list to store the URLs
urls = []

titles = []
prices = []
authors = []
descriptions = []
dates = []
samples = []
words = []
languages = []
booktype = []


def scraping_pages_having_subpage(urlofpage):
    driver.get(urlofpage)
    sleep(5)
    buttons = driver.find_elements(By.CSS_SELECTOR, 'span.icon.icon-plus')
    for button in buttons:
        url = button.find_element(By.XPATH, '..').get_attribute('href')
        urls.append(url)

    for url in urls:
        baseurl = url
        scrapping(url)
        sleep(1)
        # Create a DataFrame

        try:
            next = driver.find_element(By.CLASS_NAME, 'page-link')
            print(len(titles), len(authors), len(prices), len(words), len(descriptions), len(samples), len(languages),
                  len(booktype), len(dates))

            for i in range(1, 50):
                try:
                    urlofsubpage = baseurl + '/' + str(i)
                    print(baseurl)
                    print(urlofsubpage)

                    scrapping(urlofsubpage)
                    sleep(5)
                    print(len(titles), len(authors), len(prices), len(words), len(descriptions), len(samples),
                          len(languages),
                          len(booktype), len(dates))

                except:
                    continue
        except:
            continue


urlhhavingsubpage = [
    'https://www.smashwords.com/',
    'https://www.smashwords.com/shelves/home/892/any/any',

    'https://www.smashwords.com/shelves/home/896/any/any',
    'https://www.smashwords.com/shelves/home/1248/any/any',
    'https://www.smashwords.com/shelves/home/1106/any/any',
    'https://www.smashwords.com/shelves/home/62/any/any',
    'https://www.smashwords.com/shelves/home/1105/any/any',
    'https://www.smashwords.com/shelves/home/895/any/any',
    'https://www.smashwords.com/shelves/home/61/any/any',
    'https://www.smashwords.com/shelves/home/1223/any/any',
    'https://www.smashwords.com/shelves/home/1348/any/any',
    'https://www.smashwords.com/shelves/home/1095/any/any',

    'https://www.smashwords.com/shelves/home/1332/any/any',
    'https://www.smashwords.com/shelves/home/896/any/any',
    'https://www.smashwords.com/shelves/home/887/any/any',
    'https://www.smashwords.com/shelves/home/1206/any/any',
    'https://www.smashwords.com/shelves/home/5306/any/any',
    'https://www.smashwords.com/shelves/home/58/any/any',
    'https://www.smashwords.com/shelves/home/884/any/any',
    'https://www.smashwords.com/shelves/home/1067/any/any',
    'https://www.smashwords.com/shelves/home/883/any/any',
    'https://www.smashwords.com/shelves/home/882/any/any'
]


def main():
    for url in urlhhavingsubpage:
        scraping_pages_having_subpage(url)

        df = pd.DataFrame({
            "Title": titles,
            'Author': authors,
            'Price': prices,
            'Words': words,
            "Description": descriptions,
            "Sample": samples,
            "Language": languages,
            'Book Type': booktype,
            
        })

        # Save to CSV
        df.to_csv('smashwords.csv', index=False, encoding='utf-8', mode='a', header=False)

        # Clear the lists for the next URL
        titles.clear()
        prices.clear()
        authors.clear()
        descriptions.clear()
        dates.clear()
        samples.clear()
        words.clear()
        languages.clear()
        booktype.clear()

    
    driver.quit()

# Call the main function if you're running this script directly
if __name__ == '__main__':
    main()









# Call the main function if you're running this script directly
if __name__ == '__main__':
    main()
