Tested in Ubuntu 18.04, Python 3.7.4, scrapy 1.8.0

Configuration: Left the default configuration from genspider
Code: See fully commented code in craigslist/craigslist/spiders/parts.py
Usage: Obtain list of mustang parts and prices in my area

Must install:
Python3
Scrapy (I used anaconda, could probably just pip)


To run:
1. cd to craiglist (e.g. cd ~/Projects/craigslist/)
2. Issue a crawl specifying desired output file name and type (e.g. scrapy crawl parts -o output-file.json)


Editing source code:
1. Change name to a relevant name
2. Change starting url(s) to desired location(s) aka the place you would issue your craiglist search
3. Change keywords to the words you would use to search
4. Title and URL should be given for any ad. Price may not be. Use them as a template and update per the meta-data you're looking for
5. Change the for loop yield based on changes in step 4
