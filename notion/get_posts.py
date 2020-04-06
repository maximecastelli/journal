import os
import datetime
from notion.client import NotionClient
from config import NOTION_TOKEN, NOTION_COLLECTION_URL
from slugify import slugify

client = NotionClient(token_v2=NOTION_TOKEN)
cv = client.get_collection_view(NOTION_COLLECTION_URL)

#filter by tag
rows = cv.collection.get_rows()

# function that filters posts by tag 
def filterByTag(input):

    tag = 'Post'
    if(tag in input.tags):
        return True
    else:
        return False

result = filter(filterByTag, rows)

for post in list(result):
    #print("This row is {}".format(post.title))
    #Handle Frontmatter
    text = """---
path: "/journal/%s"
title: %s
date: "%s"
description: ""
---""" % (slugify(post.title),post.title, datetime.datetime.now())
    # Handle Title
    #text = text + '\n\n' + '# ' + post.title + '\n\n'
    for content in post.children:
        # Handles H1
        if (content.type == 'header'):
            text = text + '# ' + content.title + '\n\n'
        # Handles H2
        if (content.type == 'sub_header'):
            text = text + '## ' + content.title + '\n\n'
        # Handles H3
        if (content.type == 'sub_sub_header'):
            text = text + '### ' + content.title + '\n\n'
        # Handles Code Blocks
        if (content.type == 'code'):
            text = text + '```\n' + content.title + '\n```\n'
        # Handles Images
        if (content.type == 'image'):
            text = text + '![' + content.id + '](' + content.source + ')\n\n'
        # Handles Bullets
        if (content.type == 'bulleted_list'):
            text = text + '* ' + content.title + '\n'
        # Handles Dividers
        if (content.type == 'divider'):
            text = text + '---' + '\n'
        # Handles Basic Text, Links, Single Line Code
        if (content.type == 'text'):
            text = text + content.title + '\n'
    title = post.title.replace(' ', '-')
    title = title.replace(',', '')
    title = title.replace(':', '')
    title = title.replace(';', '')
    title = title.lower()
    if post.title != "":
        try:
            os.touch('../content/journal/' + title + 'md')
        except:
            pass
        file = open('../content/journal/' + title + '.md', 'w')
        print('Wrote A New Page:' + title)
        file.write(text)