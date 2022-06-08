BASE_URL = "https://order-order.com/2022/06/04/saturday-7-up-183/"
BASE_YEAR = int(BASE_URL.split(".com/",1)[1].split("/",1)[0])
BASE_MONTH = int(BASE_URL.split(".com/",1)[1].split("/",1)[1].split("/",1)[0])
BASE_DAY = int(BASE_URL.split(".com/",1)[1].split("/",1)[1].split("/",1)[1].split("/",1)[0])
BASE_INDEX = int(BASE_URL[BASE_URL.rindex('-')+1:].split("/",1)[0])

# Make new sample URL
#from dateutil.relativedelta import relativedelta
from dateutil import relativedelta
from datetime import datetime

#print(str(datetime(BASE_YEAR, BASE_MONTH, BASE_DAY)))
#newdate = datetime(BASE_YEAR, BASE_MONTH, BASE_DAY) + relativedelta.relativedelta(weekday=relativedelta.SA(-2))
#print(newdate)
#print(newdate.year)

def getNewLink(amount_down):
    newdate = datetime(BASE_YEAR, BASE_MONTH, BASE_DAY) + relativedelta.relativedelta(weekday=relativedelta.SA(-1-amount_down))
    return ("https://order-order.com/"+str(newdate.year)+"/"+str(newdate.month).zfill(2)+"/"+str(newdate.day).zfill(2)+"/saturday-7-up-"+str(BASE_INDEX-1)+"/")
    
getNewLink(1)

#for i in range(BASE_INDEX, )


# page 79 -6
# page 80 -5
# Total Estimated Saturday 7 up's: (79 * 6) + 5 = 479

# Code Plan
    # Iterate through pages of the 'Saturday 7-up' tag
        # e.g: 'https://order-order.com/tag/saturday-seven-up/page/80/'
    # For each page,
        # first check if title != "Page not found - Guido Fawkes"
            # if so stop
        # else, get all the "a" tags that have the class "link--title"
        # Store all links in an array, ready for parsing into the dataframe. 
