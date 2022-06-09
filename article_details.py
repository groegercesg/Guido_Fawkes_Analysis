# Modules
from article_detail_functions import *
import pandas as pd

# Get list of links to all episodes
article_list = []
articleDetails = []

article_list = getLinksForArticles()
for i in range(0, len(article_list)):
    individual_article_date = getDateMetadataForLink(article_list[i])
    current_title, article_details, post_time, list_links = getContentFromLink(article_list[i], i, len(article_list))
    if current_title != "Most Read Stories of 2020":
        articleDetails.append(
            {
                'Date': individual_article_date,
                'Link': article_list[i],
                'Title': current_title,
                'Article Details': article_details, 
                'Post Time': post_time,
                'List Links': list_links,
                'Number of Links': len(list_links)
            }
        )

articleDetails = pd.DataFrame(articleDetails)
articleDetails.to_pickle('article_details.pkl')