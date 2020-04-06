import os
import datetime
from notion.client import NotionClient
client = NotionClient(token_v2="755b8383ea1fd5f49c33e819c614ae05049052d07fd98932f48d84b5128ae07bdf3b5beed6d367185e7c9610e6321aa7388ad25544c3bb1fd521b8db69fd96672ea6a4e2a5d030cf38164265071c")
blog_home = client.get_block("https://www.notion.so/Test-Notion-as-CMS-f669259591b742ebba11e2f7c9c07a37")
# Main Loop
for post in blog_home.children:
    print(post)