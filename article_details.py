# Modules
from article_detail_functions import *
import pandas as pd

# Get list of links to all episodes
article_list = []
articleDetails = []

article_list = getLinksForArticles()
for i in range(0, len(article_list)):
    individual_article_date = getDateMetadataForLink(article_list[i])
    articleDetails.append(
        {
            'Date': individual_article_date,
            'Link': article_list[i]
            #'Title': individual_article_date[1],
            #'Release Date': individual_article_date[2],
            #'Body Text': individual_article_date[3]
        }
    )

articleDetails = pd.DataFrame(articleDetails)
articleDetails.to_pickle('article_details.pkl')