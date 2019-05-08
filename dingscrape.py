# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import codecs
#with open("report.html") as fp:
#	soup = BeautifulSoup(fp,"lxml")
#	print(soup.prettify())

f=codecs.open("report.html", 'r', 'utf-8')
#document= BeautifulSoup(f.read(),"lxml").get_text()
document = BeautifulSoup(f.read(),"lxml")

feed_list = document.find_all("div", class_='feedDetailCard')
#old version: feed_list = document.find_all("div", {"class": "feedDetailCard"})
#print(feed_list)

feed_author_list = []
feed_date_list = []
feed_comment_list = []
feeds_text = ""
feed_id = 1
#pull html from all instance of div class="date"
for feed in feed_list:
	feed_author = feed.find("div", class_="username")
	
	if feed_author.text != "target_username".decode('utf-8'):
		continue
	
	feed_date = feed.find("div", class_="date")
	feed_bd = feed.find("div", class_="bd")
	feed_content_list = feed_bd.find_all("div", class_="content")
	lastIndex = len(feed_content_list) - 1
	feed_comment = feed_content_list[lastIndex].find("span", class_="value")	

	feed_author_list.append(feed_author)
        feed_date_list.append(feed_date)
	feed_comment_list.append(feed_comment)

	#for feeds in 2019, year needed to be added to the date
	if "2018" not in feed_date.text and \
	   "2017" not in feed_date.text:
		year_added_date = "2019." + feed_date.text

	else:
		year_added_date = feed_date.text
	
	feed_combined = str(feed_id) + "\n" + year_added_date + "\n" + feed_comment.text
	feeds_text = feeds_text + feed_combined + "\n\n"
	feed_id += 1

print(feed_id)
print(len(feed_author_list))

if len(feed_author_list) != len(feed_date_list) and \
   len(feed_date_list) != len(feed_comment_list):
   	print(len(feed_author_list) + "," + len(feed_date_list) + "," + len(feed_comment_list))

file = open("target_username_feeds.txt", "a+")
file.write(feeds_text.encode('utf-8') + "\n")
file.close()
