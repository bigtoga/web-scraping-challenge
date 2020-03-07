## Homework Requirements/Deliverables

## Hints
| Step | √ | Requirement |
| :---: | :---: | :--- 
| 01 |  | Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
| 02 | | Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.
| 03 | | Use Bootstrap to structure your HTML template.

### NASA Mars News
| Step  | √ | Requirement |
| :---: | :---: | :--- 
| 01 | √ | Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
| 02 | √ | Create a Jupyter Notebook file called `mission_to_mars.ipynb`
| 03 | √ | Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later
 
~~~
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
~~~

### JPL Mars Space Images - Featured Image
| Step | √ | Requirement |
| :---: | :---: | :--- 
| 01 | √ | Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
| 02 | √ | Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`
| 03 | √ | Make sure to find the image url to the full size `.jpg` image.
| 04 | √ | Make sure to save a complete url string for this image.
~~~
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
~~~

### Mars Weather
| Step | √ | Requirement |
| :---: | :---: | :--- 
| 01 | √ | Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.
| 02 | √ | **Note: Be sure you are not signed in to twitter, or scraping may become more difficult.**
| 03 | √ | **Note: Twitter frequently changes how information is presented on their website. If you are having difficulty getting the correct html tag data, consider researching Regular Expression Patterns and how they can be used in combination with the .find() method.**

~~~
# Example:
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
~~~

### Mars Facts
| Step | √ | Requirement |
| :---: | :---: | :--- 
| 01 | √ | Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
| 02 | √ | Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres
| Step | √ | Requirement |
| :---: | :---: | :--- 
| 01 | √ | Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
| 02 | √ | You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
| 03 | √ | Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
| 04 | √ | Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

~~~
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
~~~

## Step 2 - MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

| Step | √ | Requirement |
| :---: | :---: | :--- 
| 01 | √ | Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
| 02 | | Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.
| 03 | | Store the return value in Mongo as a Python dictionary.
| 04 | | Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
| 05 | | Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.
| 06 | | [final_app_part1.png](Images/final_app_part1.png)
| 07 | | [final_app_part2.png](Images/final_app_part2.png)

## Step 3 - Submission
| Step | √ | Requirement |
| :---: | :---: | :--- 
| 01 | √ | upload the  Jupyter Notebook containing the scraping code used
| 02 | | upload Screenshots of your final application

### From the grading rubric pdf:
| Step | √ | Requirement |
| :---: | :---: | :--- 
| 01 | | Jupyter: Scrapes the most recent NASA news
| 02 | | Jupyter: Scrapes the URL for the featured image
| 03 | | Jupyter: Scrapes the latest weather from twitter
| 04 | | Jupyter: Scrapes all 4 hemisphere image urls
| 05 | | Jupyter: Scrapes the Mars facts HTML table
| 06 | | Flask: Has Routes for loading the webpage and scraping the content
| 07 | | Flask: Connects, fetches, and inserts data to and from a mongoDB without error
| 08 | | Flask: Correctly returns a rendered template and passes it a variable of the scraped data
| 09 | | Flask: Calls scrape method from an external python module
| 10 | | Web app: Landing page loads even before scraping index.html includes a button to the scrape routes
| 11 | | Web app: Uses jinja to load data from the variable passed by flask
| 13 | | Web app: Uses bootstrap to style the webpage
| 14 | | Web app: Facts table renders correctly
