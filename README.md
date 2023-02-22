# DFRACS Research Scraper # 

Hi there! I will be using this README as the main way of Documenting my progress on this research

CURRENTLY PLANNED:

|      Project Name      |        Current Feature Planned            | Progress| is Working|
|:----------------------:|:------------------------------------:|:-------:|:-------:|
|Twarc (Twitter Scraper) | Make a better query for scraping     |   30%   |  Yes |
|        MongoDB         | Feed scraped data straight to MONGODB|   10%   | Yes
|      Django Site       | Find out whether to connect to MongoDB or MySQL| 0% | No |


## Twarc / Twitter Scaper

Currently using this from Twitter's API tutorial to scrape data from Twitter, I am only able to scrape about 7 day old tweets at the
moment, but I am able to get data from specific users.
 
 **Things that are being worked on:**
 * The search query being used to scrape data
 * How and where that data is going to be stored
 * How I am going to run it
    * This one might take a bit to figure out, I can either run it off of my macbook or off of my computer at home.

## MongoDB

According to several people who use Twarc as their means of getting tweet data from twitter, using MongoDB to store scraped data is
the easiest way. after using it, I would have to say I agree. the easiest way to recieve twitter data from Twarc is in the form of 
a JSON file. MongoDB takes BSON Files, which is similar enough to JSON that MongoDB can just take the JSON files and turn it into
their file format. 

**Things that are being worked on:**
* How to recieve data straight from Twarc.
* How to map the data received to a readable table
* If and how to connect MongoDB to Django
   * Will work on this once I get Django to work better.

## Django

This is still mostly a Work-In-Progress, and I'm still learning how to use this part of the project anyway. Will probably end up being
the biggest part if I manage to get it to work.

**Things that are being worked on:**
* Get it up and running
* attach the site to GitHub (Or some other service)
* create a UI design that can be navigated.
* connect the database to the site
* allow for access to the database from the site
