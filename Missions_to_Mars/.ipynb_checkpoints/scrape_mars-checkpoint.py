#!/usr/bin/env python
# coding: utf-8

# # Module 12 Homework - Mission to Mars

# In[1]:


# Scott Whigham
# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import pymongo
import json;

# In[2]:

def scrape():
    # Store responses here:
    return_dict = {}
    
    # Initialize PyMongo to work with MongoDB (for later)
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)


    # ------------------------------------
    # # NASA Mars News
    # ------------------------------------
    # | Step  | √ | Requirement |
    # | :---: | :---: | :--- 
    # | 01 | √ | Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
    # | 02 | √ | Create a Jupyter Notebook file called `mission_to_mars.ipynb`
    # | 03 | √ | Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later

    # In[3]:


    # Turn off launching of Chrome by setting headless=True
    browser = Browser('chrome', headless=True)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)  # let the page load
    html = browser.html # Get the HTML
    # browser.quit() # Be kind and release the browser - started causing hanged sessions


    # In[4]:


    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html, 'html.parser')

    #| 03 | √ | Assign the text to variables that you can reference later
    news = soup.find_all('div', class_='list_text')
    mars_news = []
    for article in news:
        title = article.find('div', class_='content_title').text
        pg = article.find('div', class_='article_teaser_body').text
        mars_news.append({'title' : title, 'paragraph' : pg})
        
    return_dict['headline'] = mars_news[0]['title']
    return_dict['headline_paragraph'] = mars_news[0]['paragraph']
    # Make it pretty!
    ######################################
    # BONUS MATERIAL????
    ######################################
    json_object = json.dumps(mars_news, indent=2)
    # print(json_object)


    # ------------------------------------
    # # JPL Mars Space Images - Featured Image
    # ------------------------------------
    # | Step | √ | Requirement |
    # | :---: | :---: | :--- 
    # | 01 | √ | Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
    # | 02 | √ | Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`
    # | 03 | √ | Make sure to find the image url to the full size `.jpg` image.
    # | 04 | √ | Make sure to save a complete url string for this image.

    # In[5]:


    # Same pattern as before: little different 

    # 1 - browse base URL to get the "Full Image" link:
    source_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser = Browser('chrome', headless = True)
    browser.visit(source_url)
    time.sleep(2) # let the ajax load
    html = browser.html
    soup = bs(html, 'html.parser')


    # | 03 | √ | Make sure to find the image url to the full size `.jpg` image.\
    # | 04 | √ | Make sure to save a complete url string for this image.

    # In[6]:


    # 2 - Get the relative link to the image from the button
    full_image_button = soup.find('a', id='full_image')
    picture = full_image_button.get('data-fancybox-href')

    # 3 - Put it all together:
    base_url = 'https://www.jpl.nasa.gov'
    featured_image_url = base_url + picture
    # browser.quit()
    # featured_image_url    

    # Add to return_dict
    return_dict['featured_image_url'] = featured_image_url


    # # Mars Weather
    # | Step | √ | Requirement |
    # | :---: | :---: | :--- 
    # | 01 | √ | Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.
    # | 02 | √ | **Note: Be sure you are not signed in to twitter, or scraping may become more difficult.**
    # | 03 | √ | **Note: Twitter frequently changes how information is presented on their website. If you are having difficulty getting the correct html tag data, consider researching Regular Expression Patterns and how they can be used in combination with the .find() method.**

    # In[7]:


    # Repeat design pattern
    twitter = 'https://twitter.com/marswxreport?lang=en'
    browser = Browser('chrome', headless=True)
    browser.visit(twitter)
    time.sleep(2)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Save the tweet text for the weather report as a variable called mars_weather.
    # No good - finds too many 
    # mars_weather = soup.find_all('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')[0].text

    # Loop:
    all_matches = soup.find_all('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')

    # Twitter was very laky - run this 10 times and it runs successfully 5, fails. Think I was being blocked due to too many requests maybe
    mars_weather = "Error!"
    for match in all_matches:
        if "InSight sol" in match.text:
            mars_weather = match.text
            break;

    # print(mars_weather)
    
    # Add to return_dict
    return_dict['current_weather'] = mars_weather

    # # Mars Facts
    # | Step | √ | Requirement |
    # | :---: | :---: | :--- 
    # | 01 | √ | Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # | 02 | √ | Use Pandas to convert the data to a HTML table string.

    # In[8]:


    mars_facts_url = 'https://space-facts.com/mars/'
    response = requests.get(mars_facts_url)
    html = response.content

    df = pd.read_html(html)
    facts_html = df[0].to_html()
    # print(facts_html)
    return_dict['facts'] = facts_html


    # # Mars Hemispheres
    # | Step | √ | Requirement |
    # | :---: | :---: | :--- 
    # | 01 | √ | Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
    # | 02 | √ | You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # | 03 | √ | Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
    # | 04 | √ | Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

    # In[9]:


    # Keep doing same design pattern
    hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser = Browser ('chrome', headless=True)
    browser.visit(hemispheres)
    time.sleep(2)


    # In[10]:


    links = browser.find_by_css('.description .itemLink')

    # 1. Collect the links
    hrefs = []
    titles = []
    for link in links:
        hrefs.append(link['href'])
        titles.append(link.text)

    current_index = 0
    hemisphere_pics = [] # store the json
    for href in hrefs:
        # "Click" the link
        browser.visit(href)
        time.sleep(5) # wait for it to load - slow down too. I was getting "server refused" at 2 secs

        css_image = '.downloads ul li a'
        image_link = browser.find_by_css(css_image)[0]
        hemisphere_pics.append({"title" : titles[current_index], "img_url" : image_link['href']})
        current_index += 1
        
    
    # Add to return_dict
    return_dict['hemispheres'] = hemisphere_pics

    browser.quit()
    
    # Return results
    return return_dict
