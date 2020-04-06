import os
import re
from notion.client import NotionClient
from config import NOTION_TOKEN, NOTION_COLLECTION_URL
from slugify import slugify

client = NotionClient(token_v2=NOTION_TOKEN)
cv = client.get_collection_view(NOTION_COLLECTION_URL)

#First we get the data we want from Notion
#print(cv.collection.name)
#print()

siteName = cv.collection.name
siteDesc = cv.collection.description

with open('../gatsby-config.js','r+') as f:
    #convert to string:
    data = f.read()
    f.seek(0)
    #overwrite the file
    f.write(re.sub(r"siteMetadata: {\n      title: `(.*)`,\n      description: `(.*)`,",r"siteMetadata: {\n      title: `" + siteName + "`,\n      description: `" + siteDesc + "`,",data))
    f.truncate()
    print('Title updated to: ' + '\033[1m' + siteName + '\033[0m' + '\n'+'Description updated to: ' + '\033[1m' + siteDesc +'\033[0m')