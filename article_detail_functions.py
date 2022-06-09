# Modules
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re

def getDateMetadataForLink(link):
    year = int(link.split(".com/",1)[1].split("/",1)[0])
    month = int(link.split(".com/",1)[1].split("/",1)[1].split("/",1)[0])
    day = int(link.split(".com/",1)[1].split("/",1)[1].split("/",1)[1].split("/",1)[0])
    date = datetime(year, month, day)
    
    return date

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
        if soup.title.string != "Page not found – Guido Fawkes":
            links = soup.find_all("a", {"class": "link--title"})
            # original_size = len(page_links)
            for i in range(0, len(links)):
                if links[i]['href'] not in page_links:
                    page_links.append(links[i]['href'])
            # print("In page: " + str(current_page) + ", we found: " + str(len(page_links)-original_size) + " articles.")
            current_page += 1
        else:
            valid_url = True
            
    print("Overall, we found " + str(len(page_links)) + " articles")
    return page_links


link = "https://order-order.com/2015/12/12/saturday-seven-up-313/"

def getContentFromLink(link, current, total):
    print(current)
    if ((current % int(total*0.1)) == 0):
        print("We are on article " + str(current) + " out of " + str(total))
        print("Currently extracting: " + str(link)) 
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    
    current_title = soup.find("v-card-title", {"class": "red accent-4 white--text d-block"}).text.lstrip().rstrip()
    
    article_details = ""
    find_by_p1_class = soup.find("p", {"class": "p1"})
    if find_by_p1_class is not None:
        article_details = find_by_p1_class.text
    else:
        p_locator = soup.find_all("p")
        for i in range(0, len(p_locator)):
            if p_locator[i].text == "The top stories last week in order of popularity were:":
                article_details = p_locator[i-1].text
            elif "The top stories" in p_locator[i].text:
                article_details = p_locator[i].text
            elif "most popular stories" in p_locator[i].text:
                article_details = p_locator[i].text
    
    post_time = soup.find("span", {"class": "posted-on blue-grey--text text--darken-4"}).text.split("@", 1)[1].lstrip().rstrip()
        
    list_links_raw = soup.find_all("li")
    list_links = []
    for i in range(0, len(list_links_raw)):
        list_links.append(re.sub('\s+', ' ', list_links_raw[i].text.replace(u'\xa0', u' ')))
     
    return [current_title, article_details, post_time, list_links]
    
getContentFromLink(link, 1, 11)
    