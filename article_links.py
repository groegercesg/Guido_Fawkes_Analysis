# Modules
from bs4 import BeautifulSoup
import requests
from dateutil import relativedelta
from datetime import datetime

def getDateMetadataForLink(link):
    year = int(BASE_URL.split(".com/",1)[1].split("/",1)[0])
    month = int(BASE_URL.split(".com/",1)[1].split("/",1)[1].split("/",1)[0])
    day = int(BASE_URL.split(".com/",1)[1].split("/",1)[1].split("/",1)[1].split("/",1)[0])
    date = datetime(year, month, day)
    index = int(BASE_URL[BASE_URL.rindex('-')+1:].split("/",1)[0])
    
    return [date, year, month, day, index]

# Code Plan
    # Iterate through pages of the 'Saturday 7-up' tag
        # e.g: 'https://order-order.com/tag/saturday-seven-up/page/80/'
    # For each page,
        # first check if title != "Page not found - Guido Fawkes"
            # if so stop
        # else, get all the "a" tags that have the class "link--title"
        # Store all links in an array, ready for parsing into the dataframe. 
   
def getLinksForArticles():
    # Website for episodes     
    TAG_URL = "https://order-order.com/tag/saturday-seven-up/page/"
    valid_url = False
    current_page = 1
    page_links= []
    
    while valid_url is not True:
        page = requests.get(TAG_URL+str(current_page)+"/")
        soup = BeautifulSoup(page.content, "html.parser")
        print(soup.title.string)
        if soup.title.string != "Page not found – Guido Fawkes":
            links = soup.find_all("a", {"class": "link--title"})
            original_size = len(page_links)
            for i in range(0, len(links)):
                if links[i]['href'] not in page_links:
                    page_links.append(links[i]['href'])
            print("In page: " + str(current_page) + ", we found: " + str(len(page_links)-original_size) + " articles.")
            current_page += 1
        else:
            valid_url = True
            
    print("Overall, we found " + str(len(page_links)) + " articles")
    return page_links
    
links = getLinksForArticles()
print(links)