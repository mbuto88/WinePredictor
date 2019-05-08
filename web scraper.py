### web scraper for a single website. This is a playground for figuring out
### how to use a the Beautiful soup scraper as well as calling in the import
### function already in excel

#importing libraries
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

###set up parse requests 
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text,'html.parser')

###remove bottom links

last_links = soup.find(class_="AlphaNav")
last_links.decompose()

###pull text from bodytext <div>
artist_name_list = soup.find(class_= 'BodyText')
artist_name_list_items = artist_name_list.find_all('a')

### loop funciton to iterate over each string pulled in

for artist_name in artist_name_list_items:
    print(artist_name.prettify())



