from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Site 1
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('div', class_='list_text')[0]
    news_title = results.find('div', class_='content_title').text
    news_p = results.find('div', class_='article_teaser_body').text

    # Site 2
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    browser.links.find_by_partial_text('FULL IMAGE').click()
    html = browser.html
    soup = bs(html, 'html.parser')

    fancy_image = soup.find('img', class_='fancybox-image')['src']
    fancy_image = url + fancy_image

    # Site 3
    url = 'https://galaxyfacts-mars.com/'

    mfv = pd.read_html(url)[0]
    mars_facts = mfv.to_html()

    # Site 4
    url = 'https://marshemispheres.com/'

    hemisphere_image_urls = []

    # Image 1
    browser.visit(url)
    browser.links.find_by_partial_text('Enhanced')[0].click()
    html = browser.html
    soup = bs(html, 'html.parser')

    down = soup.find('div', class_='downloads')
    hemi = down.find('a')['href']
    hemi = url + hemi
    title = soup.find('h2', class_='title').text
    dict = {
        'title': title,
        'img_url': hemi
    }
    hemisphere_image_urls.append(dict)

    browser.back()

    # Image 2
    browser.links.find_by_partial_text('Enhanced')[1].click()
    html = browser.html
    soup = bs(html, 'html.parser')

    down = soup.find('div', class_='downloads')
    hemi = down.find('a')['href']
    hemi = url + hemi
    title = soup.find('h2', class_='title').text
    dict = {
        'title': title,
        'img_url': hemi
    }
    hemisphere_image_urls.append(dict)

    browser.back()

    # Image 3
    browser.links.find_by_partial_text('Enhanced')[2].click()
    html = browser.html
    soup = bs(html, 'html.parser')

    down = soup.find('div', class_='downloads')
    hemi = down.find('a')['href']
    hemi = url + hemi
    title = soup.find('h2', class_='title').text
    dict = {
        'title': title,
        'img_url': hemi
    }
    hemisphere_image_urls.append(dict)

    browser.back()

    # Image 4
    browser.links.find_by_partial_text('Enhanced')[3].click()
    html = browser.html
    soup = bs(html, 'html.parser')

    down = soup.find('div', class_='downloads')
    hemi = down.find('a')['href']
    hemi = url + hemi
    title = soup.find('h2', class_='title').text
    dict = {
        'title': title,
        'img_url': hemi
    }
    hemisphere_image_urls.append(dict)

    browser.back()


    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "fancy_image": fancy_image,
        "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data